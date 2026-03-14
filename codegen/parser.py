"""Parse an OpenAPI spec into grouped operation definitions."""

from __future__ import annotations

from dataclasses import dataclass, field

from codegen.transforms.operations import MethodDefinition, extract_method_definition
from codegen.utils.deref import deref
from codegen.utils.naming import operation_id_to_group, operation_id_to_method

Spec = dict[str, object]

HTTP_METHODS = ("get", "post", "put", "delete", "patch")


@dataclass
class ParsedGroup:
    group_name: str
    methods: list[MethodDefinition] = field(default_factory=list)


@dataclass
class ParseResult:
    groups: list[ParsedGroup]
    component_schemas: dict[str, dict[str, object]]
    base_url: str


def parse_spec(raw_spec: dict[str, object]) -> ParseResult:
    """Load and resolve all $refs, iterate paths, extract grouped method definitions."""
    spec = deref(raw_spec, raw_spec)
    if not isinstance(spec, dict):
        return ParseResult(groups=[], component_schemas={}, base_url="https://localhost")

    paths = spec.get("paths")
    if not isinstance(paths, dict):
        return ParseResult(groups=[], component_schemas={}, base_url="https://localhost")

    group_map: dict[str, list[MethodDefinition]] = {}

    for path, path_item in paths.items():
        if not isinstance(path, str) or not isinstance(path_item, dict):
            continue

        for method in HTTP_METHODS:
            operation = path_item.get(method)
            if not isinstance(operation, dict):
                continue

            operation_id = operation.get("operationId")
            if not isinstance(operation_id, str):
                continue

            group = operation_id_to_group(operation_id)
            # Normalize known typos in group names
            if group == "manging":
                group = "managing"
            method_name = operation_id_to_method(operation_id)

            method_def = extract_method_definition(
                operation_id=operation_id,
                method_name=method_name,
                http_method=method,
                path=path,
                operation=operation,
                spec=spec,
            )

            if group in group_map:
                group_map[group].append(method_def)
            else:
                group_map[group] = [method_def]

    groups = [ParsedGroup(group_name=name, methods=methods) for name, methods in group_map.items()]

    component_schemas: dict[str, dict[str, object]] = {}
    components = spec.get("components")
    if isinstance(components, dict):
        schemas = components.get("schemas")
        if isinstance(schemas, dict):
            for name, schema in schemas.items():
                if isinstance(name, str) and isinstance(schema, dict):
                    component_schemas[name] = schema

    servers = spec.get("servers")
    base_url = "https://localhost"
    if isinstance(servers, list) and len(servers) > 0:
        first = servers[0]
        if isinstance(first, dict):
            url = first.get("url")
            if isinstance(url, str):
                base_url = url

    return ParseResult(groups=groups, component_schemas=component_schemas, base_url=base_url)
