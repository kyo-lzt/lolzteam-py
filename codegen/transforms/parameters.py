"""Extract and classify parameters from an OpenAPI operation."""

from __future__ import annotations

from dataclasses import dataclass

from codegen.transforms.types import schema_to_type_string
from codegen.utils.deref import deref_shallow

Spec = dict[str, object]


@dataclass
class ParsedParameter:
    name: str
    type: str
    required: bool
    default: object | None = None


@dataclass
class OperationParameters:
    path_params: list[ParsedParameter]
    query_params: list[ParsedParameter]


def extract_parameters(operation: dict[str, object], spec: Spec) -> OperationParameters:
    """Extract and classify parameters into path vs query (skip header/cookie)."""
    path_params: list[ParsedParameter] = []
    query_params: list[ParsedParameter] = []

    raw_params = operation.get("parameters")
    if not isinstance(raw_params, list):
        return OperationParameters(path_params=path_params, query_params=query_params)

    for raw_param in raw_params:
        param = deref_shallow(raw_param, spec)
        if not isinstance(param, dict):
            continue

        param_in = param.get("in")
        if param_in in ("header", "cookie"):
            continue

        name = param.get("name")
        if not isinstance(name, str):
            continue

        schema = param.get("schema")
        type_str = schema_to_type_string(schema, spec) if isinstance(schema, dict) else "object"
        required = bool(param.get("required", False))
        default = schema.get("default") if isinstance(schema, dict) else None

        parsed = ParsedParameter(name=name, type=type_str, required=required, default=default)

        if param_in == "path":
            parsed.required = True  # path params are always required
            path_params.append(parsed)
        elif param_in == "query":
            query_params.append(parsed)

    return OperationParameters(path_params=path_params, query_params=query_params)
