"""Convert OpenAPI schema objects to Python type strings."""

from __future__ import annotations

import keyword
import re

from codegen.utils.deref import deref_shallow

Spec = dict[str, object]
SchemaObject = dict[str, object]

# Module-level collector for inline TypedDicts generated during type resolution.
# The emitter should call `reset_inline_types()` before and `drain_inline_types()`
# after processing each schema group.
_inline_typed_dicts: list[str] = []


def reset_inline_types() -> None:
    """Clear the inline TypedDict collector."""
    _inline_typed_dicts.clear()


def drain_inline_types() -> list[str]:
    """Return and clear all collected inline TypedDicts."""
    result = list(_inline_typed_dicts)
    _inline_typed_dicts.clear()
    return result


def _primitive_type(t: str, fmt: str | None = None) -> str:
    match t:
        case "string":
            if fmt == "binary":
                return "bytes"
            return "str"
        case "integer":
            return "int"
        case "number":
            return "float"
        case "boolean":
            return "bool"
        case "null":
            return "None"
        case _:
            return "object"


def schema_to_type_string(
    schema: SchemaObject | None,
    spec: Spec,
    parent_name: str = "",
) -> str:
    """Convert an OpenAPI schema to a Python type string.

    When ``parent_name`` is provided and the schema is an object with properties,
    an inline TypedDict is generated and collected via ``_inline_typed_dicts``.
    """
    if not schema or len(schema) == 0:
        return "object"

    # $ref -> component schema refs emit named type, others resolve and convert
    if "$ref" in schema and isinstance(schema["$ref"], str):
        ref = schema["$ref"]
        if ref.startswith("#/components/schemas/"):
            return ref.rsplit("/", 1)[-1]
        resolved = deref_shallow(schema, spec)
        if isinstance(resolved, dict):
            return schema_to_type_string(resolved, spec, parent_name)
        return "object"

    # enum -> Literal union (skip huge enums, use base type instead)
    enum_vals = schema.get("enum")
    if isinstance(enum_vals, list) and len(enum_vals) > 0:
        literals: list[str] = []
        for v in enum_vals:
            if isinstance(v, str):
                escaped = v.replace("\\", "\\\\").replace('"', '\\"')
                literals.append(f'"{escaped}"')
            elif isinstance(v, (int, float)):
                literals.append(str(v))
        if literals:
            return "Literal[" + ", ".join(literals) + "]"

    # oneOf / anyOf -> union
    one_of = schema.get("oneOf")
    if isinstance(one_of, list) and len(one_of) > 0:
        types = [schema_to_type_string(s, spec) for s in one_of if isinstance(s, dict)]
        return " | ".join(types) if types else "object"

    any_of = schema.get("anyOf")
    if isinstance(any_of, list) and len(any_of) > 0:
        types = [schema_to_type_string(s, spec) for s in any_of if isinstance(s, dict)]
        return " | ".join(types) if types else "object"

    # allOf -> merge all schemas' properties into a single dict type
    all_of = schema.get("allOf")
    if isinstance(all_of, list) and len(all_of) > 0:
        merged_props: dict[str, object] = {}
        merged_required: list[str] = []
        for s in all_of:
            if not isinstance(s, dict):
                continue
            props = s.get("properties")
            if isinstance(props, dict):
                merged_props.update(props)
            req = s.get("required")
            if isinstance(req, list):
                merged_required.extend(r for r in req if isinstance(r, str))
        if merged_props:
            merged: dict[str, object] = {"properties": merged_props}
            if merged_required:
                merged["required"] = merged_required
            return schema_to_type_string(merged, spec, parent_name)
        # No properties found — use first non-trivial type
        for s in all_of:
            if isinstance(s, dict) and len(s) > 0:
                t = schema_to_type_string(s, spec)
                if t != "object":
                    return t
        return "object"

    # Multi-type array: type: ["string", "integer"]
    schema_type = schema.get("type")
    if isinstance(schema_type, list):
        has_null = "null" in schema_type
        non_null = [_primitive_type(t) for t in schema_type if isinstance(t, str) and t != "null"]
        result = " | ".join(non_null) if non_null else "object"
        return f"{result} | None" if has_null else result

    if isinstance(schema_type, str):
        if schema_type == "array":
            items = schema.get("items")
            item_type = (
                schema_to_type_string(items, spec, parent_name)
                if isinstance(items, dict)
                else "object"
            )
            return f"list[{item_type}]"

        if schema_type == "object" or schema.get("properties"):
            return _object_type(schema, spec, parent_name)

        fmt = schema.get("format")
        return _primitive_type(schema_type, fmt if isinstance(fmt, str) else None)

    # Has properties but no explicit type
    if schema.get("properties"):
        return _object_type(schema, spec, parent_name)

    return "object"


def _object_type(
    schema: SchemaObject,
    spec: Spec,
    parent_name: str = "",
) -> str:
    props = schema.get("properties")
    if not isinstance(props, dict) or len(props) == 0:
        additional = schema.get("additionalProperties")
        if isinstance(additional, dict):
            val_type = schema_to_type_string(additional, spec)
            return f"dict[str, {val_type}]"
        return "dict[str, object]"

    # Has properties — generate inline TypedDict
    if parent_name:
        td_name = parent_name
        _collect_inline_typed_dict(td_name, schema, spec)
        return td_name

    return "dict[str, object]"


def _capitalize_first(s: str) -> str:
    if not s:
        return s
    return s[0].upper() + s[1:]


def _sanitize_identifier(name: str) -> str:
    """Turn an arbitrary string into a valid Python identifier fragment.

    Splits on non-alphanumeric characters and PascalCases the parts.
    """
    parts = re.split(r"[^0-9a-zA-Z_]+", name)
    return "".join(_capitalize_first(p) for p in parts if p)


def _prop_to_inline_name(parent: str, prop_name: str) -> str:
    """Build an inline TypedDict name from parent and property name."""
    return parent + _sanitize_identifier(prop_name)


def _collect_inline_typed_dict(
    name: str,
    schema: SchemaObject,
    spec: Spec,
) -> None:
    """Generate a TypedDict for an inline object and add it to the collector."""
    code = generate_typed_dict(name, schema, spec)
    _inline_typed_dicts.append(code)


def schema_to_type(schema: SchemaObject | None) -> str:
    """Convert schema to type string without spec (no ref resolution)."""
    return schema_to_type_string(schema, {})


def _is_valid_identifier(name: str) -> bool:
    return name.isidentifier() and not keyword.iskeyword(name)


def _needs_functional_form(fields: list[FieldTuple]) -> bool:
    return any(not _is_valid_identifier(f[0]) for f in fields)


def generate_typed_dict(
    name: str,
    schema: SchemaObject,
    spec: Spec,
) -> str:
    """Generate a TypedDict class string from a schema with properties."""
    props = schema.get("properties")
    if not isinstance(props, dict) or len(props) == 0:
        # No properties -> type alias
        type_str = schema_to_type_string(schema, spec)
        return f"{name} = {type_str}"

    required_set: set[str] = set()
    raw_required = schema.get("required")
    if isinstance(raw_required, list):
        required_set = {r for r in raw_required if isinstance(r, str)}

    required_fields: list[tuple[str, str]] = []
    optional_fields: list[tuple[str, str]] = []

    for prop_name, prop_schema in props.items():
        if not isinstance(prop_schema, dict):
            continue
        inline_name = _prop_to_inline_name(name, prop_name)
        prop_type = schema_to_type_string(prop_schema, spec, inline_name)
        if prop_name in required_set:
            required_fields.append((prop_name, prop_type))
        else:
            optional_fields.append((prop_name, prop_type))

    all_fields = required_fields + optional_fields
    if _needs_functional_form(all_fields):
        return _emit_functional_typed_dict(name, required_fields, optional_fields)

    lines: list[str] = []

    if required_fields and optional_fields:
        # Mixed: base class for required, subclass with total=False for optional
        base_name = f"_{name}Required"
        lines.append(f"class {base_name}(TypedDict):")
        for fname, ftype in required_fields:
            lines.append(f"    {fname}: {ftype}")
        lines.append("")
        lines.append("")
        lines.append(f"class {name}({base_name}, total=False):")
        for fname, ftype in optional_fields:
            lines.append(f"    {fname}: {ftype}")
    elif required_fields:
        # All required
        lines.append(f"class {name}(TypedDict):")
        for fname, ftype in required_fields:
            lines.append(f"    {fname}: {ftype}")
    else:
        # All optional
        lines.append(f"class {name}(TypedDict, total=False):")
        if optional_fields:
            for fname, ftype in optional_fields:
                lines.append(f"    {fname}: {ftype}")
        else:
            lines.append("    pass")

    return "\n".join(lines)


def _format_default(value: object) -> str:
    """Format a schema default value as a Python-style comment suffix."""
    if isinstance(value, bool):
        return f"  # default: {value}"
    if isinstance(value, str):
        return f'  # default: "{value}"'
    if isinstance(value, (int, float)):
        return f"  # default: {value}"
    return ""


def _format_default_value(value: object) -> str | None:
    """Format a schema default value as a Python literal. Returns None if not representable."""
    if isinstance(value, bool):
        return "True" if value else "False"
    if isinstance(value, str):
        escaped = value.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'
    if isinstance(value, int):
        return str(value)
    if isinstance(value, float):
        return str(value)
    return None


def emit_defaults_dict(
    type_name: str,
    fields: list[FieldTuple],
) -> str | None:
    """Emit a DEFAULTS dict for a TypedDict with fields that have default values.

    Returns None if no fields have defaults.
    """
    entries: list[tuple[str, str]] = []
    for f in fields:
        default = _field_default(f)
        if default is None:
            continue
        formatted = _format_default_value(default)
        if formatted is None:
            continue
        entries.append((f[0], formatted))

    if not entries:
        return None

    lines: list[str] = [f"{type_name}_DEFAULTS: dict[str, object] = {{"]
    for name, val in entries:
        lines.append(f'    "{name}": {val},')
    lines.append("}")
    return "\n".join(lines)


FieldTuple = tuple[str, str] | tuple[str, str, object | None]


def _field_default(field: FieldTuple) -> object | None:
    """Extract default from a field tuple (2 or 3 elements)."""
    return field[2] if len(field) >= 3 else None


def _emit_functional_typed_dict(
    name: str,
    required_fields: list[FieldTuple],
    optional_fields: list[FieldTuple],
) -> str:
    """Emit TypedDict using functional form (for field names with special chars)."""
    lines: list[str] = []
    required_names = {f[0] for f in required_fields}
    all_fields = required_fields + optional_fields

    if required_fields and optional_fields:
        # Use total=False + Required[] for required fields
        lines.append(f'{name} = TypedDict("{name}", {{')
        for f in all_fields:
            comment = _format_default(_field_default(f))
            if f[0] in required_names:
                lines.append(f'    "{f[0]}": Required[{f[1]}],{comment}')
            else:
                lines.append(f'    "{f[0]}": {f[1]},{comment}')
        lines.append("}, total=False)")
    elif required_fields:
        lines.append(f'{name} = TypedDict("{name}", {{')
        for f in required_fields:
            comment = _format_default(_field_default(f))
            lines.append(f'    "{f[0]}": {f[1]},{comment}')
        lines.append("})")
    else:
        lines.append(f'{name} = TypedDict("{name}", {{')
        for f in optional_fields:
            comment = _format_default(_field_default(f))
            lines.append(f'    "{f[0]}": {f[1]},{comment}')
        lines.append("}, total=False)")

    return "\n".join(lines)


def emit_typed_dict_fields(
    type_name: str,
    required_fields: list[FieldTuple],
    optional_fields: list[FieldTuple],
) -> str:
    """Emit TypedDict for params/body, choosing class or functional form."""
    all_fields = required_fields + optional_fields
    if _needs_functional_form(all_fields):
        return _emit_functional_typed_dict(type_name, required_fields, optional_fields)

    lines: list[str] = []
    if required_fields and optional_fields:
        base_name = f"_{type_name}Required"
        lines.append(f"class {base_name}(TypedDict):")
        for f in required_fields:
            comment = _format_default(_field_default(f))
            lines.append(f"    {f[0]}: {f[1]}{comment}")
        lines.append("")
        lines.append("")
        lines.append(f"class {type_name}({base_name}, total=False):")
        for f in optional_fields:
            comment = _format_default(_field_default(f))
            lines.append(f"    {f[0]}: {f[1]}{comment}")
    elif required_fields:
        lines.append(f"class {type_name}(TypedDict):")
        for f in required_fields:
            comment = _format_default(_field_default(f))
            lines.append(f"    {f[0]}: {f[1]}{comment}")
    else:
        lines.append(f"class {type_name}(TypedDict, total=False):")
        for f in optional_fields:
            comment = _format_default(_field_default(f))
            lines.append(f"    {f[0]}: {f[1]}{comment}")

    return "\n".join(lines)
