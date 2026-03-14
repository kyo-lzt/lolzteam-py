"""Emit Python source files from parsed OpenAPI data."""

from __future__ import annotations

from typing import TYPE_CHECKING

from codegen.transforms.types import (
    emit_typed_dict_fields,
    generate_typed_dict,
)
from codegen.utils.naming import (
    build_type_name,
    group_to_class_name,
    group_to_file_name,
    group_to_property_name,
)

if TYPE_CHECKING:
    from codegen.parser import ParsedGroup
    from codegen.transforms.operations import MethodDefinition

Spec = dict[str, object]


# ─── Type Emission ───────────────────────────────────────────────────────────


def _emit_query_params_typed_dict(
    group: str,
    method: MethodDefinition,
) -> tuple[str, str] | None:
    """Emit a TypedDict for query params. Returns (type_name, code) or None."""
    if not method.params.query_params:
        return None

    type_name = f"{build_type_name(group, method.method_name)}Params"
    required_fields: list[tuple[str, str]] = []
    optional_fields: list[tuple[str, str]] = []

    for param in method.params.query_params:
        if param.required:
            required_fields.append((param.name, param.type))
        else:
            optional_fields.append((param.name, param.type))

    return type_name, emit_typed_dict_fields(type_name, required_fields, optional_fields)


def _emit_body_typed_dict(
    group: str,
    method: MethodDefinition,
) -> tuple[str, str] | None:
    """Emit a TypedDict for request body. Returns (type_name, code) or None."""
    if not method.has_body:
        return None

    type_name = f"{build_type_name(group, method.method_name)}Body"

    # Array body — emit a type alias instead of a TypedDict
    if method.body_is_array:
        return type_name, f"{type_name} = list[{method.body_array_item_type}]"

    if not method.body_properties:
        return None

    required_fields: list[tuple[str, str]] = []
    optional_fields: list[tuple[str, str]] = []

    for prop in method.body_properties:
        if prop.required:
            required_fields.append((prop.name, prop.type))
        else:
            optional_fields.append((prop.name, prop.type))

    return type_name, emit_typed_dict_fields(type_name, required_fields, optional_fields)


def _emit_response_type(group: str, method: MethodDefinition) -> tuple[str, str]:
    """Emit a TypedDict or type alias for the response. Returns (type_name, code)."""
    type_name = f"{build_type_name(group, method.method_name)}Response"

    # If we have a schema with properties, generate a TypedDict
    schema = method.response_schema
    if isinstance(schema, dict):
        props = schema.get("properties")
        if isinstance(props, dict) and len(props) > 0:
            # Spec is {} because all $refs are already resolved by the parser
            code = generate_typed_dict(type_name, schema, {})
            return type_name, code

    return type_name, f"{type_name} = {method.response_type}"


def _py_type_to_python(ts_type: str) -> str:
    """Convert TS-style types that leaked through to Python equivalents."""
    replacements = {
        "unknown": "object",
        "Record<string, unknown>": "dict[str, object]",
        "Array<": "list[",
    }
    result = ts_type
    for old, new in replacements.items():
        result = result.replace(old, new)
    return result


def emit_types_file(
    groups: list[ParsedGroup],
    component_schemas: dict[str, dict[str, object]],
) -> str:
    """Generate types.py content with TypedDict classes."""
    sections: list[str] = []

    sections.append("# Auto-generated. Do not edit manually.")
    sections.append("from __future__ import annotations")
    sections.append("")
    sections.append("from typing import Literal, TypedDict")

    # Component schemas
    if component_schemas:
        sections.append("")
        sections.append("")
        sections.append("# ─── Component Schemas ────────────────────────────────────────")

        for name, schema in component_schemas.items():
            sections.append("")
            sections.append("")
            code = generate_typed_dict(name, schema, {})
            sections.append(code)

    # Operation types per group
    for group in groups:
        group_types: list[str] = []

        for method in group.methods:
            query_result = _emit_query_params_typed_dict(group.group_name, method)
            if query_result is not None:
                group_types.append(query_result[1])

            body_result = _emit_body_typed_dict(group.group_name, method)
            if body_result is not None:
                group_types.append(body_result[1])

            _, response_code = _emit_response_type(group.group_name, method)
            group_types.append(response_code)

        if group_types:
            class_name = group_to_class_name(group.group_name)
            sections.append("")
            sections.append("")
            sections.append(f"# ─── {class_name} Types ────────────────────────────────────────")

            for code in group_types:
                sections.append("")
                sections.append("")
                sections.append(code)

    sections.append("")
    return "\n".join(sections)


# ─── Group Class Emission ────────────────────────────────────────────────────


def _build_path_expression(path: str) -> str:
    """Convert /threads/{thread_id} to f-string or plain string."""
    if "{" not in path:
        return f'"{path}"'
    return 'f"' + path + '"'


def _emit_sync_method(group: str, method: MethodDefinition) -> str:
    """Emit a single sync method."""
    lines: list[str] = []
    response_name = f"{build_type_name(group, method.method_name)}Response"

    # Build argument list
    args: list[str] = ["self"]

    # Path params (positional)
    for param in method.params.path_params:
        args.append(f"{param.name}: {param.type}")

    # Keyword-only marker
    body_type_name = f"{build_type_name(group, method.method_name)}Body"
    has_body_type = method.has_body and (len(method.body_properties) > 0 or method.body_is_array)
    query_type_name = f"{build_type_name(group, method.method_name)}Params"
    has_query_type = len(method.params.query_params) > 0

    if has_body_type or has_query_type:
        args.append("*")

    body_effectively_required = method.body_required or any(
        p.required for p in method.body_properties
    )
    if has_body_type:
        if body_effectively_required:
            args.append(f"body: {body_type_name}")
        else:
            args.append(f"body: {body_type_name} | None = None")

    has_required_query = any(p.required for p in method.params.query_params)
    if has_query_type:
        if has_required_query:
            args.append(f"params: {query_type_name}")
        else:
            args.append(f"params: {query_type_name} | None = None")

    arg_str = ", ".join(args)
    path_expr = _build_path_expression(method.path)

    lines.append(f"    def {method.method_name}({arg_str}) -> {response_name}:")
    lines.append("        return self._http.request(RequestOptions(")
    lines.append(f'            method="{method.http_method}",')
    lines.append(f"            path={path_expr},")

    if has_query_type:
        lines.append("            query=params,")
    if has_body_type:
        lines.append("            body=body,")
    if method.content_type != "form":
        lines.append(f'            content_type="{method.content_type}",')

    lines.append("        ))")

    return "\n".join(lines)


def _emit_async_method(group: str, method: MethodDefinition) -> str:
    """Emit a single async method."""
    lines: list[str] = []
    response_name = f"{build_type_name(group, method.method_name)}Response"

    args: list[str] = ["self"]

    for param in method.params.path_params:
        args.append(f"{param.name}: {param.type}")

    body_type_name = f"{build_type_name(group, method.method_name)}Body"
    has_body_type = method.has_body and (len(method.body_properties) > 0 or method.body_is_array)
    query_type_name = f"{build_type_name(group, method.method_name)}Params"
    has_query_type = len(method.params.query_params) > 0

    if has_body_type or has_query_type:
        args.append("*")

    body_effectively_required = method.body_required or any(
        p.required for p in method.body_properties
    )
    if has_body_type:
        if body_effectively_required:
            args.append(f"body: {body_type_name}")
        else:
            args.append(f"body: {body_type_name} | None = None")

    has_required_query = any(p.required for p in method.params.query_params)
    if has_query_type:
        if has_required_query:
            args.append(f"params: {query_type_name}")
        else:
            args.append(f"params: {query_type_name} | None = None")

    arg_str = ", ".join(args)
    path_expr = _build_path_expression(method.path)

    lines.append(f"    async def {method.method_name}({arg_str}) -> {response_name}:")
    lines.append("        return await self._http.request(RequestOptions(")
    lines.append(f'            method="{method.http_method}",')
    lines.append(f"            path={path_expr},")

    if has_query_type:
        lines.append("            query=params,")
    if has_body_type:
        lines.append("            body=body,")
    if method.content_type != "form":
        lines.append(f'            content_type="{method.content_type}",')

    lines.append("        ))")

    return "\n".join(lines)


def emit_group_file(group: ParsedGroup) -> str:
    """Generate one file per tag with both sync and async classes."""
    class_name = group_to_class_name(group.group_name)
    async_class_name = f"Async{class_name}"
    lines: list[str] = []

    lines.append("# Auto-generated. Do not edit manually.")
    lines.append("from __future__ import annotations")
    lines.append("")

    # Collect type imports first to check if Literal is needed
    type_imports: list[str] = []
    needs_literal = False
    for method in group.methods:
        base = build_type_name(group.group_name, method.method_name)
        type_imports.append(f"{base}Response")
        if method.params.query_params:
            type_imports.append(f"{base}Params")
        if method.has_body and (method.body_properties or method.body_is_array):
            type_imports.append(f"{base}Body")
        # Only path params appear inline in method signatures;
        # query/body types are referenced via TypedDict names
        for param in method.params.path_params:
            if "Literal[" in param.type:
                needs_literal = True

    # Standard library imports
    if needs_literal:
        lines.append("from typing import TYPE_CHECKING, Literal")
    else:
        lines.append("from typing import TYPE_CHECKING")
    lines.append("")

    # Runtime import (needed at runtime for RequestOptions construction)
    lines.append("from lolzteam.runtime.types import RequestOptions")
    lines.append("")

    # Type-only imports
    lines.append("if TYPE_CHECKING:")
    lines.append("    from lolzteam.runtime.async_http_client import AsyncHttpClient")
    lines.append("    from lolzteam.runtime.http_client import HttpClient")

    sorted_type_imports = sorted(type_imports)
    if sorted_type_imports:
        lines.append("")  # blank line separating third-party from local imports
        import_line = f"    from .types import {', '.join(sorted_type_imports)}"
        if len(import_line) > 80:
            lines.append("    from .types import (")
            for name in sorted_type_imports:
                lines.append(f"        {name},")
            lines.append("    )")
        else:
            lines.append(import_line)

    # Sync class
    lines.append("")
    lines.append("")
    lines.append(f"class {class_name}:")
    lines.append("    def __init__(self, http: HttpClient) -> None:")
    lines.append("        self._http = http")

    for method in group.methods:
        lines.append("")
        lines.append(_emit_sync_method(group.group_name, method))

    # Async class
    lines.append("")
    lines.append("")
    lines.append(f"class {async_class_name}:")
    lines.append("    def __init__(self, http: AsyncHttpClient) -> None:")
    lines.append("        self._http = http")

    for method in group.methods:
        lines.append("")
        lines.append(_emit_async_method(group.group_name, method))

    lines.append("")
    return "\n".join(lines)


# ─── Index File Emission ─────────────────────────────────────────────────────


def emit_index_file(
    groups: list[ParsedGroup],
    client_name: str,
    default_base_url: str,
    default_rate_limit: int,
) -> str:
    """Generate __init__.py with sync and async client classes."""
    async_client_name = f"Async{client_name}"
    lines: list[str] = []

    lines.append("# Auto-generated. Do not edit manually.")
    lines.append("from __future__ import annotations")
    lines.append("")
    lines.append("from lolzteam.runtime.async_http_client import AsyncHttpClient")
    lines.append("from lolzteam.runtime.http_client import HttpClient")
    lines.append(
        "from lolzteam.runtime.types import ClientConfig, ProxyConfig, RateLimitConfig, RetryConfig"
    )

    # Sort group imports by file name (blank line separating absolute from relative)
    lines.append("")
    group_imports: list[str] = []
    for group in groups:
        class_name = group_to_class_name(group.group_name)
        async_class = f"Async{class_name}"
        file_name = group_to_file_name(group.group_name)
        group_imports.append(f"from .{file_name} import {async_class}, {class_name}")
    group_imports.sort()
    for imp in group_imports:
        lines.append(imp)

    # Sync client
    lines.append("")
    lines.append("")
    lines.append(f"class {client_name}:")
    lines.append("    def __init__(")
    lines.append("        self,")
    lines.append("        token: str,")
    lines.append("        *,")
    lines.append(f'        base_url: str = "{default_base_url}",')
    lines.append("        proxy: str | None = None,")
    lines.append("        max_retries: int = 3,")
    lines.append("        base_delay: float = 1.0,")
    lines.append("        max_delay: float = 30.0,")
    lines.append(f"        requests_per_minute: int = {default_rate_limit},")
    lines.append("    ) -> None:")
    lines.append("        config = ClientConfig(")
    lines.append("            token=token,")
    lines.append("            base_url=base_url,")
    lines.append("            proxy=ProxyConfig(url=proxy) if proxy else None,")
    lines.append(
        "            retry=RetryConfig("
        "max_retries=max_retries, base_delay=base_delay, max_delay=max_delay),"
    )
    lines.append("            rate_limit=RateLimitConfig(requests_per_minute=requests_per_minute),")
    lines.append("        )")
    lines.append("        self._http = HttpClient(config)")

    for group in groups:
        class_name = group_to_class_name(group.group_name)
        prop_name = group_to_property_name(group.group_name)
        lines.append(f"        self.{prop_name} = {class_name}(self._http)")

    lines.append("")
    lines.append("    def close(self) -> None:")
    lines.append("        self._http.close()")
    lines.append("")
    lines.append(f"    def __enter__(self) -> {client_name}:")
    lines.append("        return self")
    lines.append("")
    lines.append("    def __exit__(self, *args: object) -> None:")
    lines.append("        self.close()")

    # Async client
    lines.append("")
    lines.append("")
    lines.append(f"class {async_client_name}:")
    lines.append("    def __init__(")
    lines.append("        self,")
    lines.append("        token: str,")
    lines.append("        *,")
    lines.append(f'        base_url: str = "{default_base_url}",')
    lines.append("        proxy: str | None = None,")
    lines.append("        max_retries: int = 3,")
    lines.append("        base_delay: float = 1.0,")
    lines.append("        max_delay: float = 30.0,")
    lines.append(f"        requests_per_minute: int = {default_rate_limit},")
    lines.append("    ) -> None:")
    lines.append("        config = ClientConfig(")
    lines.append("            token=token,")
    lines.append("            base_url=base_url,")
    lines.append("            proxy=ProxyConfig(url=proxy) if proxy else None,")
    lines.append(
        "            retry=RetryConfig("
        "max_retries=max_retries, base_delay=base_delay, max_delay=max_delay),"
    )
    lines.append("            rate_limit=RateLimitConfig(requests_per_minute=requests_per_minute),")
    lines.append("        )")
    lines.append("        self._http = AsyncHttpClient(config)")

    for group in groups:
        async_class = f"Async{group_to_class_name(group.group_name)}"
        prop_name = group_to_property_name(group.group_name)
        lines.append(f"        self.{prop_name} = {async_class}(self._http)")

    lines.append("")
    lines.append("    async def close(self) -> None:")
    lines.append("        await self._http.close()")
    lines.append("")
    lines.append(f"    async def __aenter__(self) -> {async_client_name}:")
    lines.append("        return self")
    lines.append("")
    lines.append("    async def __aexit__(self, *args: object) -> None:")
    lines.append("        await self.close()")
    lines.append("")
    return "\n".join(lines)
