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
    content_type: str = "form"  # "form" or "multipart"


def _detect_content_type(operation: dict[str, object], spec: Spec) -> str:
    """Detect whether the operation uses multipart or form-urlencoded."""
    request_body = operation.get("requestBody")
    if request_body is None:
        return "form"
    resolved = deref_shallow(request_body, spec)
    if not isinstance(resolved, dict):
        return "form"
    content = resolved.get("content")
    if isinstance(content, dict) and "multipart/form-data" in content:
        return "multipart"
    return "form"


def _extract_body_properties(
    operation: dict[str, object],
    spec: Spec,
) -> list[BodyProperty]:
    """Extract body properties from a request body, resolving $ref as needed."""
    body_properties: list[BodyProperty] = []

    request_body = operation.get("requestBody")
    if request_body is None:
        return body_properties

    resolved_body = deref_shallow(request_body, spec)
    if not isinstance(resolved_body, dict):
        return body_properties

    content = resolved_body.get("content")
    if not isinstance(content, dict):
        return body_properties

    # Try application/json first, then multipart/form-data
    media_type = content.get("application/json") or content.get("multipart/form-data")
    if not isinstance(media_type, dict):
        return body_properties

    schema = media_type.get("schema")
    if not isinstance(schema, dict):
        return body_properties

    # Handle oneOf -- merge all properties from all variants
    one_of = schema.get("oneOf")
    if isinstance(one_of, list):
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
                )
            )
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
                    )
                )

    return body_properties


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
    body_properties = _extract_body_properties(operation, spec)
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
        body_properties=body_properties,
        has_body=has_body,
        body_required=body_required,
        response_type=response_info.type_string,
        response_schema=response_info.schema,
        content_type=content_type,
    )
