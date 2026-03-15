"""Convert OpenAPI schema objects to Python type strings."""

from __future__ import annotations

import keyword

from codegen.utils.deref import deref_shallow

Spec = dict[str, object]
SchemaObject = dict[str, object]


def _primitive_type(t: str, fmt: str | None = None) -> str:
    match t:
        case "string":
            if fmt == "binary":
                return "bytes"
            return "str"
        case "integer":
            return "int"
        case "number":
            return "int | float"
        case "boolean":
            return "bool"
        case "null":
            return "None"
        case _:
            return "object"


def schema_to_type_string(schema: SchemaObject | None, spec: Spec) -> str:
    """Convert an OpenAPI schema to a Python type string."""
    if not schema or len(schema) == 0:
        return "object"

    # $ref -> component schema refs emit named type, others resolve and convert
    if "$ref" in schema and isinstance(schema["$ref"], str):
        ref = schema["$ref"]
        if ref.startswith("#/components/schemas/"):
            return ref.rsplit("/", 1)[-1]
        resolved = deref_shallow(schema, spec)
        if isinstance(resolved, dict):
            return schema_to_type_string(resolved, spec)
        return "object"

    # enum -> Literal union (skip huge enums, use base type instead)
    enum_vals = schema.get("enum")
    if isinstance(enum_vals, list) and len(enum_vals) > 0:
        if len(enum_vals) > 50:
            # Too many values for Literal, fall through to base type
            pass
        else:
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
            return schema_to_type_string(merged, spec)
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
            item_type = schema_to_type_string(items, spec) if isinstance(items, dict) else "object"
            return f"list[{item_type}]"

        if schema_type == "object" or schema.get("properties"):
            return _object_type(schema, spec)

        fmt = schema.get("format")
        return _primitive_type(schema_type, fmt if isinstance(fmt, str) else None)

    # Has properties but no explicit type
    if schema.get("properties"):
        return _object_type(schema, spec)

    return "object"


def _object_type(schema: SchemaObject, spec: Spec) -> str:
    props = schema.get("properties")
    if not isinstance(props, dict) or len(props) == 0:
        additional = schema.get("additionalProperties")
        if isinstance(additional, dict):
            val_type = schema_to_type_string(additional, spec)
            return f"dict[str, {val_type}]"
        return "dict[str, object]"
    return "dict[str, object]"


def schema_to_type(schema: SchemaObject | None) -> str:
    """Convert schema to type string without spec (no ref resolution)."""
    return schema_to_type_string(schema, {})


def _is_valid_identifier(name: str) -> bool:
    return name.isidentifier() and not keyword.iskeyword(name)


def _needs_functional_form(fields: list[tuple[str, str]]) -> bool:
    return any(not _is_valid_identifier(name) for name, _ in fields)


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
        prop_type = schema_to_type_string(prop_schema, spec)
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


def _emit_functional_typed_dict(
    name: str,
    required_fields: list[tuple[str, str]],
    optional_fields: list[tuple[str, str]],
) -> str:
    """Emit TypedDict using functional form (for field names with special chars)."""
    lines: list[str] = []
    required_names = {fname for fname, _ in required_fields}
    all_fields = required_fields + optional_fields

    if required_fields and optional_fields:
        # Use total=False + Required[] for required fields
        lines.append(f'{name} = TypedDict("{name}", {{')
        for fname, ftype in all_fields:
            if fname in required_names:
                lines.append(f'    "{fname}": Required[{ftype}],')
            else:
                lines.append(f'    "{fname}": {ftype},')
        lines.append("}, total=False)")
    elif required_fields:
        lines.append(f'{name} = TypedDict("{name}", {{')
        for fname, ftype in required_fields:
            lines.append(f'    "{fname}": {ftype},')
        lines.append("})")
    else:
        lines.append(f'{name} = TypedDict("{name}", {{')
        for fname, ftype in optional_fields:
            lines.append(f'    "{fname}": {ftype},')
        lines.append("}, total=False)")

    return "\n".join(lines)


def emit_typed_dict_fields(
    type_name: str,
    required_fields: list[tuple[str, str]],
    optional_fields: list[tuple[str, str]],
) -> str:
    """Emit TypedDict for params/body, choosing class or functional form."""
    all_fields = required_fields + optional_fields
    if _needs_functional_form(all_fields):
        return _emit_functional_typed_dict(type_name, required_fields, optional_fields)

    lines: list[str] = []
    if required_fields and optional_fields:
        base_name = f"_{type_name}Required"
        lines.append(f"class {base_name}(TypedDict):")
        for fname, ftype in required_fields:
            lines.append(f"    {fname}: {ftype}")
        lines.append("")
        lines.append("")
        lines.append(f"class {type_name}({base_name}, total=False):")
        for fname, ftype in optional_fields:
            lines.append(f"    {fname}: {ftype}")
    elif required_fields:
        lines.append(f"class {type_name}(TypedDict):")
        for fname, ftype in required_fields:
            lines.append(f"    {fname}: {ftype}")
    else:
        lines.append(f"class {type_name}(TypedDict, total=False):")
        for fname, ftype in optional_fields:
            lines.append(f"    {fname}: {ftype}")

    return "\n".join(lines)
