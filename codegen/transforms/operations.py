"""Extract structured operation definitions from an OpenAPI spec."""

from __future__ import annotations

from dataclasses import dataclass, field

from codegen.transforms.parameters import OperationParameters, extract_parameters
from codegen.transforms.responses import extract_response_info
from codegen.transforms.types import SchemaObject, schema_to_type_string
from codegen.utils.deref import deref_shallow

Spec = dict[str, object]


@dataclass
class BodyProperty:
    name: str
    type: str
    required: bool
    default: object | None = None


@dataclass
class BodyVariant:
    """A single variant in a discriminated oneOf body."""

    title: str
    discriminator_field: str
    discriminator_value: str | int
    properties: list[BodyProperty]


@dataclass
class MethodDefinition:
    operation_id: str
    method_name: str
    http_method: str
    path: str
    params: OperationParameters
    body_properties: list[BodyProperty] = field(default_factory=list)
    has_body: bool = False
    body_required: bool = False
    response_type: str = "object"
    response_schema: SchemaObject | None = None
    content_type: str = "form"  # "form", "json", or "multipart"
    body_is_array: bool = False
    body_array_item_type: str = "object"
    body_variants: list[BodyVariant] = field(default_factory=list)
    response_is_html: bool = False


def _detect_discriminator(variants: list[object]) -> str | None:
    """Find a field that acts as discriminator across all oneOf variants.

    A field is a discriminator if every variant has it as a property with a
    single-value enum.
    """
    if len(variants) < 2:
        return None

    # Collect candidate fields from first variant
    first = variants[0]
    if not isinstance(first, dict):
        return None
    first_props = first.get("properties")
    if not isinstance(first_props, dict):
        return None

    candidates: list[str] = []
    for name, prop_schema in first_props.items():
        if isinstance(prop_schema, dict):
            enum = prop_schema.get("enum")
            if isinstance(enum, list) and len(enum) == 1:
                candidates.append(name)

    # Check each candidate against all variants
    for candidate in candidates:
        all_match = True
        for variant in variants:
            if not isinstance(variant, dict):
                all_match = False
                break
            v_props = variant.get("properties")
            if not isinstance(v_props, dict):
                all_match = False
                break
            prop = v_props.get(candidate)
            if not isinstance(prop, dict):
                all_match = False
                break
            enum = prop.get("enum")
            if not isinstance(enum, list) or len(enum) != 1:
                all_match = False
                break
        if all_match:
            return candidate

    return None


def _extract_discriminated_variants(
    variants: list[object],
    discriminator: str,
    spec: Spec,
) -> BodyExtractionResult:
    """Extract body variants for a discriminated oneOf schema."""
    result_variants: list[BodyVariant] = []

    for variant in variants:
        if not isinstance(variant, dict):
            continue
        title = variant.get("title")
        if not isinstance(title, str):
            title = "Unknown"
        v_props = variant.get("properties")
        if not isinstance(v_props, dict):
            continue

        disc_prop = v_props.get(discriminator)
        if not isinstance(disc_prop, dict):
            continue
        disc_enum = disc_prop.get("enum")
        if not isinstance(disc_enum, list) or len(disc_enum) != 1:
            continue
        disc_value = disc_enum[0]

        raw_required = variant.get("required")
        required_set: set[str] = set()
        if isinstance(raw_required, list):
            required_set = {r for r in raw_required if isinstance(r, str)}

        props: list[BodyProperty] = []
        for name, prop_schema in v_props.items():
            if not isinstance(prop_schema, dict):
                continue
            props.append(
                BodyProperty(
                    name=name,
                    type=schema_to_type_string(prop_schema, spec),
                    required=name in required_set,
                    default=prop_schema.get("default"),
                )
            )

        result_variants.append(
            BodyVariant(
                title=title,
                discriminator_field=discriminator,
                discriminator_value=disc_value,
                properties=props,
            )
        )

    return BodyExtractionResult(variants=result_variants)


def _detect_content_type(operation: dict[str, object], spec: Spec) -> str:
    """Detect whether the operation uses multipart, json, or form-urlencoded."""
    request_body = operation.get("requestBody")
    if request_body is None:
        return "form"
    resolved = deref_shallow(request_body, spec)
    if not isinstance(resolved, dict):
        return "form"
    content = resolved.get("content")
    if not isinstance(content, dict):
        return "form"
    has_form = "application/x-www-form-urlencoded" in content
    if "multipart/form-data" in content and not has_form:
        return "multipart"
    if "application/json" in content and not has_form:
        return "json"
    return "form"


@dataclass
class BodyExtractionResult:
    properties: list[BodyProperty] = field(default_factory=list)
    is_array: bool = False
    array_item_type: str = "object"
    variants: list[BodyVariant] = field(default_factory=list)


def _extract_body(
    operation: dict[str, object],
    spec: Spec,
) -> BodyExtractionResult:
    """Extract body properties from a request body, resolving $ref as needed."""
    empty = BodyExtractionResult()

    request_body = operation.get("requestBody")
    if request_body is None:
        return empty

    resolved_body = deref_shallow(request_body, spec)
    if not isinstance(resolved_body, dict):
        return empty

    content = resolved_body.get("content")
    if not isinstance(content, dict):
        return empty

    # Prefer form-urlencoded (matches _detect_content_type priority), then json, then multipart
    media_type = (
        content.get("application/x-www-form-urlencoded")
        or content.get("application/json")
        or content.get("multipart/form-data")
    )
    if not isinstance(media_type, dict):
        return empty

    schema = media_type.get("schema")
    if not isinstance(schema, dict):
        return empty

    body_properties: list[BodyProperty] = []

    # Handle oneOf -- detect discriminated union or merge flat
    one_of = schema.get("oneOf")
    if isinstance(one_of, list):
        discriminator = _detect_discriminator(one_of)
        if discriminator is not None:
            return _extract_discriminated_variants(one_of, discriminator, spec)

        all_props: dict[str, dict[str, object]] = {}
        variant_required_sets: list[set[str]] = []
        for variant in one_of:
            if not isinstance(variant, dict):
                continue
            variant_props = variant.get("properties")
            if isinstance(variant_props, dict):
                for name, prop_schema in variant_props.items():
                    if isinstance(prop_schema, dict):
                        if name in all_props:
                            # Merge enum values when both have enum
                            existing = all_props[name]
                            existing_enum = existing.get("enum")
                            new_enum = prop_schema.get("enum")
                            if isinstance(existing_enum, list) and isinstance(new_enum, list):
                                merged = dict(existing)
                                merged["enum"] = existing_enum + [
                                    v for v in new_enum if v not in existing_enum
                                ]
                                all_props[name] = merged
                            # Otherwise keep existing (first-wins for non-enum conflicts)
                        else:
                            all_props[name] = prop_schema
            variant_required = variant.get("required")
            if isinstance(variant_required, list):
                variant_required_sets.append({r for r in variant_required if isinstance(r, str)})
        # Intersect: only required if ALL variants require it
        if variant_required_sets:
            all_required: set[str] = variant_required_sets[0]
            for s in variant_required_sets[1:]:
                all_required = all_required & s
        else:
            all_required: set[str] = set()
        for name, prop_schema in all_props.items():
            body_properties.append(
                BodyProperty(
                    name=name,
                    type=schema_to_type_string(prop_schema, spec),
                    required=name in all_required,
                    default=prop_schema.get("default"),
                )
            )
    # Handle array body (e.g. POST /batch)
    elif schema.get("type") == "array" and not schema.get("properties"):
        items = schema.get("items")
        item_type = schema_to_type_string(items, spec) if isinstance(items, dict) else "object"
        return BodyExtractionResult(is_array=True, array_item_type=item_type)

    else:
        properties = schema.get("properties")
        if isinstance(properties, dict):
            raw_required = schema.get("required")
            required_set: set[str] = set()
            if isinstance(raw_required, list):
                required_set = {r for r in raw_required if isinstance(r, str)}
            for name, prop_schema in properties.items():
                if not isinstance(prop_schema, dict):
                    continue
                body_properties.append(
                    BodyProperty(
                        name=name,
                        type=schema_to_type_string(prop_schema, spec),
                        required=name in required_set,
                        default=prop_schema.get("default"),
                    )
                )

    return BodyExtractionResult(properties=body_properties)


def extract_method_definition(
    operation_id: str,
    method_name: str,
    http_method: str,
    path: str,
    operation: dict[str, object],
    spec: Spec,
) -> MethodDefinition:
    """Build a MethodDefinition from a resolved operation object."""
    params = extract_parameters(operation, spec)
    body = _extract_body(operation, spec)
    response_info = extract_response_info(operation, spec)

    request_body = operation.get("requestBody")
    has_body = request_body is not None
    body_required = False
    if has_body:
        resolved = deref_shallow(request_body, spec)
        if isinstance(resolved, dict):
            body_required = bool(resolved.get("required", False))

    content_type = _detect_content_type(operation, spec)

    return MethodDefinition(
        operation_id=operation_id,
        method_name=method_name,
        http_method=http_method.upper(),
        path=path,
        params=params,
        body_properties=body.properties,
        has_body=has_body,
        body_required=body_required,
        response_type=response_info.type_string,
        response_schema=response_info.schema,
        content_type=content_type,
        body_is_array=body.is_array,
        body_array_item_type=body.array_item_type,
        body_variants=body.variants,
        response_is_html=response_info.is_html,
    )
