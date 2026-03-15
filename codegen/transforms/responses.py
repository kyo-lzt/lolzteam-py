"""Extract response type from an OpenAPI operation's responses."""

from __future__ import annotations

from dataclasses import dataclass

from codegen.transforms.types import SchemaObject, schema_to_type_string
from codegen.utils.deref import deref_shallow

Spec = dict[str, object]


@dataclass
class ResponseInfo:
    type_string: str
    schema: SchemaObject | None


def extract_response_info(operation: dict[str, object], spec: Spec) -> ResponseInfo:
    """Pick 200/201 response, extract application/json schema and type string."""
    responses = operation.get("responses")
    if not isinstance(responses, dict):
        return ResponseInfo(type_string="object", schema=None)

    raw_success = responses.get("200") or responses.get("201")
    if raw_success is None:
        return ResponseInfo(type_string="object", schema=None)

    success = deref_shallow(raw_success, spec)
    if not isinstance(success, dict):
        return ResponseInfo(type_string="object", schema=None)

    content = success.get("content")
    if not isinstance(content, dict):
        return ResponseInfo(type_string="object", schema=None)

    json_content = content.get("application/json")
    if not isinstance(json_content, dict):
        return ResponseInfo(type_string="object", schema=None)

    raw_schema = json_content.get("schema")
    if raw_schema is None:
        return ResponseInfo(type_string="object", schema=None)

    # If raw schema is a $ref to a component schema, return the name directly
    if isinstance(raw_schema, dict):
        ref = raw_schema.get("$ref")
        if isinstance(ref, str) and ref.startswith("#/components/schemas/"):
            schema_name = ref.rsplit("/", 1)[-1]
            resolved = deref_shallow(raw_schema, spec)
            schema = resolved if isinstance(resolved, dict) else None
            return ResponseInfo(type_string=schema_name, schema=schema)

    schema = deref_shallow(raw_schema, spec)
    if not isinstance(schema, dict):
        return ResponseInfo(type_string="object", schema=None)

    return ResponseInfo(
        type_string=schema_to_type_string(schema, spec),
        schema=schema,
    )
