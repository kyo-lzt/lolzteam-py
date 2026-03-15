"""Emit Python source files from parsed OpenAPI data."""

from __future__ import annotations

from typing import TYPE_CHECKING

from codegen.transforms.types import (
    drain_inline_types,
    emit_defaults_dict,
    emit_typed_dict_fields,
    generate_typed_dict,
    reset_inline_types,
)
from codegen.utils.naming import (
    build_type_name,
    group_to_class_name,
    group_to_property_name,
    variant_title_to_suffix,
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
    required_fields: list[tuple[str, str, object | None]] = []
    optional_fields: list[tuple[str, str, object | None]] = []

    for param in method.params.query_params:
        if param.required:
            required_fields.append((param.name, param.type, param.default))
        else:
            optional_fields.append((param.name, param.type, param.default))

    code = emit_typed_dict_fields(type_name, required_fields, optional_fields)
    defaults_code = emit_defaults_dict(type_name, required_fields + optional_fields)
    if defaults_code:
        code = f"{code}\n\n\n{defaults_code}"
    return type_name, code


def _emit_body_typed_dict(
    group: str,
    method: MethodDefinition,
) -> tuple[str, str] | None:
    """Emit a TypedDict for request body. Returns (type_name, code) or None."""
    if not method.has_body:
        return None

    type_name = f"{build_type_name(group, method.method_name)}Body"

    # Discriminated union — emit separate TypedDicts per variant + union alias
    if method.body_variants:
        return _emit_discriminated_body(type_name, group, method)

    # Array body — emit a type alias instead of a TypedDict
    if method.body_is_array:
        return type_name, f"{type_name} = list[{method.body_array_item_type}]"

    if not method.body_properties:
        return None

    required_fields: list[tuple[str, str, object | None]] = []
    optional_fields: list[tuple[str, str, object | None]] = []

    for prop in method.body_properties:
        if prop.required:
            required_fields.append((prop.name, prop.type, prop.default))
        else:
            optional_fields.append((prop.name, prop.type, prop.default))

    code = emit_typed_dict_fields(type_name, required_fields, optional_fields)
    defaults_code = emit_defaults_dict(type_name, required_fields + optional_fields)
    if defaults_code:
        code = f"{code}\n\n\n{defaults_code}"
    return type_name, code


def _emit_discriminated_body(
    union_name: str,
    group: str,
    method: MethodDefinition,
) -> tuple[str, str]:
    """Emit TypedDicts for each discriminated variant + a union type alias."""
    parts: list[str] = []
    variant_names: list[str] = []

    for variant in method.body_variants:
        suffix = variant_title_to_suffix(variant.title)
        variant_name = f"{build_type_name(group, method.method_name)}{suffix}Body"
        variant_names.append(variant_name)

        required_fields: list[tuple[str, str, object | None]] = []
        optional_fields: list[tuple[str, str, object | None]] = []

        for prop in variant.properties:
            if prop.required:
                required_fields.append((prop.name, prop.type, prop.default))
            else:
                optional_fields.append((prop.name, prop.type, prop.default))

        parts.append(emit_typed_dict_fields(variant_name, required_fields, optional_fields))

    # Union alias
    union_members = " | ".join(variant_names)
    parts.append(f"{union_name} = {union_members}")

    return union_name, "\n\n\n".join(parts)


def _emit_response_type(group: str, method: MethodDefinition) -> tuple[str, str]:
    """Emit a TypedDict or type alias for the response. Returns (type_name, code)."""
    type_name = f"{build_type_name(group, method.method_name)}Response"

    # If we have a schema with properties, generate a TypedDict
    schema = method.response_schema
    if isinstance(schema, dict):
        props = schema.get("properties")
        if isinstance(props, dict) and len(props) > 0:
            # Spec is {} because all $refs are already resolved by the parser
            reset_inline_types()
            code = generate_typed_dict(type_name, schema, {})
            inline_parts = drain_inline_types()
            if inline_parts:
                code = "\n\n\n".join(inline_parts) + "\n\n\n" + code
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
            reset_inline_types()
            code = generate_typed_dict(name, schema, {})
            for inline_code in drain_inline_types():
                sections.append("")
                sections.append("")
                sections.append(inline_code)
            sections.append("")
            sections.append("")
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
    result = "\n".join(sections)

    # Patch import to include Required if functional-form TypedDicts use it
    if "Required[" in result:
        result = result.replace(
            "from typing import Literal, TypedDict",
            "from typing import Literal, Required, TypedDict",
        )

    return result


# ─── Group Class Emission ────────────────────────────────────────────────────


def _build_path_expression(path: str) -> str:
    """Convert /threads/{thread_id} to f-string or plain string."""
    if "{" not in path:
        return f'"{path}"'
    return 'f"' + path + '"'


def _emit_sync_method(group: str, method: MethodDefinition, *, is_search: bool = False) -> str:
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
    has_body_type = method.has_body and (
        len(method.body_properties) > 0 or method.body_is_array or len(method.body_variants) > 0
    )
    query_type_name = f"{build_type_name(group, method.method_name)}Params"
    has_query_type = len(method.params.query_params) > 0

    # GET requests can't have a body — promote body fields to query params
    get_body_as_query = method.http_method == "GET" and has_body_type
    if get_body_as_query:
        has_body_type = False
        has_query_type = True
        query_type_name = body_type_name

    if has_body_type or has_query_type:
        args.append("*")

    body_effectively_required = (
        method.body_required
        or any(p.required for p in method.body_properties)
        or len(method.body_variants) > 0
    )
    if has_body_type:
        if body_effectively_required:
            args.append(f"body: {body_type_name}")
        else:
            args.append(f"body: {body_type_name} | None = None")

    has_required_query = any(p.required for p in method.params.query_params)
    if has_query_type:
        query_required = has_required_query or (get_body_as_query and body_effectively_required)
        if query_required:
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
    if method.content_type != "form" and not get_body_as_query:
        lines.append(f'            content_type="{method.content_type}",')
    if is_search:
        lines.append("            is_search=True,")
    if method.response_is_html:
        lines.append("            is_html=True,")

    lines.append("        ))  # type: ignore[return-value]")

    return "\n".join(lines)


def _emit_async_method(group: str, method: MethodDefinition, *, is_search: bool = False) -> str:
    """Emit a single async method."""
    lines: list[str] = []
    response_name = f"{build_type_name(group, method.method_name)}Response"

    args: list[str] = ["self"]

    for param in method.params.path_params:
        args.append(f"{param.name}: {param.type}")

    body_type_name = f"{build_type_name(group, method.method_name)}Body"
    has_body_type = method.has_body and (
        len(method.body_properties) > 0 or method.body_is_array or len(method.body_variants) > 0
    )
    query_type_name = f"{build_type_name(group, method.method_name)}Params"
    has_query_type = len(method.params.query_params) > 0

    # GET requests can't have a body — promote body fields to query params
    get_body_as_query = method.http_method == "GET" and has_body_type
    if get_body_as_query:
        has_body_type = False
        has_query_type = True
        query_type_name = body_type_name

    if has_body_type or has_query_type:
        args.append("*")

    body_effectively_required = (
        method.body_required
        or any(p.required for p in method.body_properties)
        or len(method.body_variants) > 0
    )
    if has_body_type:
        if body_effectively_required:
            args.append(f"body: {body_type_name}")
        else:
            args.append(f"body: {body_type_name} | None = None")

    has_required_query = any(p.required for p in method.params.query_params)
    if has_query_type:
        query_required = has_required_query or (get_body_as_query and body_effectively_required)
        if query_required:
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
    if method.content_type != "form" and not get_body_as_query:
        lines.append(f'            content_type="{method.content_type}",')
    if is_search:
        lines.append("            is_search=True,")
    if method.response_is_html:
        lines.append("            is_html=True,")

    lines.append("        ))  # type: ignore[return-value]")

    return "\n".join(lines)


def _emit_group_classes(group: ParsedGroup, *, is_search: bool = False) -> str:
    """Emit sync + async classes for a single group (no file header/imports)."""
    class_name = group_to_class_name(group.group_name)
    async_class_name = f"Async{class_name}"
    lines: list[str] = []

    # Sync class
    lines.append(f"class {class_name}:")
    lines.append("    def __init__(self, http: HttpClient) -> None:")
    lines.append("        self._http = http")

    for method in group.methods:
        lines.append("")
        lines.append(_emit_sync_method(group.group_name, method, is_search=is_search))

    # Async class
    lines.append("")
    lines.append("")
    lines.append(f"class {async_class_name}:")
    lines.append("    def __init__(self, http: AsyncHttpClient) -> None:")
    lines.append("        self._http = http")

    for method in group.methods:
        lines.append("")
        lines.append(_emit_async_method(group.group_name, method, is_search=is_search))

    return "\n".join(lines)


# ─── Combined File Emission ──────────────────────────────────────────────────


def _collect_referenced_schema_names(
    groups: list[ParsedGroup],
    component_schema_names: frozenset[str],
) -> list[str]:
    """Find component schema type names used directly in __init__.py method signatures.

    Only path params appear as bare types in method signatures. Query params and body
    properties are wrapped in TypedDicts (defined in types.py), so their schema
    references are resolved there, not in __init__.py.
    """
    import re

    found: set[str] = set()
    for group in groups:
        for method in group.methods:
            for param in method.params.path_params:
                for name in component_schema_names:
                    if re.search(r"(?<!\w)" + re.escape(name) + r"(?!\w)", param.type):
                        found.add(name)
    return sorted(found)


def emit_combined_file(
    groups: list[ParsedGroup],
    client_name: str,
    default_base_url: str,
    default_rate_limit: int,
    *,
    search_groups: frozenset[str] = frozenset(),
    default_search_rate_limit: int | None = None,
    component_schema_names: frozenset[str] = frozenset(),
) -> str:
    """Generate __init__.py with all group classes + sync/async client classes."""
    async_client_name = f"Async{client_name}"
    lines: list[str] = []

    lines.append("# Auto-generated. Do not edit manually.")
    lines.append("from __future__ import annotations")
    lines.append("")

    # Check if any group needs Literal
    needs_literal = False
    type_imports: list[str] = []
    for group in groups:
        for method in group.methods:
            base = build_type_name(group.group_name, method.method_name)
            type_imports.append(f"{base}Response")
            if method.params.query_params:
                type_imports.append(f"{base}Params")
            if method.has_body and (
                method.body_properties or method.body_is_array or method.body_variants
            ):
                type_imports.append(f"{base}Body")
            for param in method.params.path_params:
                if "Literal[" in param.type:
                    needs_literal = True

    # Add component schema types referenced in method signatures
    referenced_schemas = _collect_referenced_schema_names(groups, component_schema_names)
    type_imports.extend(referenced_schemas)

    # Standard library imports
    if needs_literal:
        lines.append("from typing import TYPE_CHECKING, Literal")
    else:
        lines.append("from typing import TYPE_CHECKING")
    lines.append("")

    # Runtime imports (needed at runtime)
    lines.append("from lolzteam.runtime.async_http_client import AsyncHttpClient")
    lines.append("from lolzteam.runtime.errors import ConfigError")
    lines.append("from lolzteam.runtime.http_client import HttpClient")
    lines.append("from lolzteam.runtime.types import (")
    lines.append("    ClientConfig,")
    lines.append("    OnRetryCallback,")
    lines.append("    ProxyConfig,")
    lines.append("    RateLimitConfig,")
    lines.append("    RequestOptions,")
    lines.append("    RetryConfig,")
    lines.append(")")
    lines.append("")

    # Type-only imports from types.py
    sorted_type_imports = sorted(type_imports)
    if sorted_type_imports:
        lines.append("if TYPE_CHECKING:")
        lines.append("    from .types import (")
        for name in sorted_type_imports:
            lines.append(f"        {name},")
        lines.append("    )")

    # Emit all group classes
    for group in groups:
        lines.append("")
        lines.append("")
        lines.append(
            _emit_group_classes(
                group,
                is_search=group.group_name in search_groups,
            )
        )

    # Sync client
    lines.append("")
    lines.append("")
    lines.append(f"class {client_name}:")
    lines.append("    def __init__(")
    lines.append("        self,")
    lines.append("        config: ClientConfig | None = None,")
    lines.append("        *,")
    lines.append("        token: str | None = None,")
    lines.append(f'        base_url: str = "{default_base_url}",')
    lines.append("        proxy: str | None = None,")
    lines.append("        max_retries: int = 3,")
    lines.append("        base_delay: float = 1.0,")
    lines.append("        max_delay: float = 30.0,")
    lines.append(f"        requests_per_minute: int = {default_rate_limit},")
    if default_search_rate_limit is not None:
        lines.append(f"        search_requests_per_minute: int = {default_search_rate_limit},")
    lines.append("        on_retry: OnRetryCallback | None = None,")
    lines.append("    ) -> None:")
    lines.append("        if config is None:")
    lines.append("            if token is None:")
    lines.append('                raise ConfigError("either config or token must be provided")')
    lines.append("            import warnings")
    lines.append("            warnings.warn(")
    lines.append(
        f'                "{client_name}(token=...) is deprecated, "',
    )
    lines.append(f'                "use {client_name}(ClientConfig(token=..., ...)) instead",')
    lines.append("                DeprecationWarning,")
    lines.append("                stacklevel=2,")
    lines.append("            )")
    lines.append("            config = ClientConfig(")
    lines.append("                token=token,")
    lines.append("                base_url=base_url,")
    lines.append("                proxy=ProxyConfig(url=proxy) if proxy else None,")
    lines.append(
        "                retry=RetryConfig("
        "max_retries=max_retries, base_delay=base_delay, max_delay=max_delay),"
    )
    lines.append(
        "                rate_limit=RateLimitConfig(requests_per_minute=requests_per_minute),"
    )
    if default_search_rate_limit is not None:
        lines.append(
            "                search_rate_limit=RateLimitConfig("
            "requests_per_minute=search_requests_per_minute),"
        )
    lines.append("                on_retry=on_retry,")
    lines.append("            )")
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
    lines.append("        config: ClientConfig | None = None,")
    lines.append("        *,")
    lines.append("        token: str | None = None,")
    lines.append(f'        base_url: str = "{default_base_url}",')
    lines.append("        proxy: str | None = None,")
    lines.append("        max_retries: int = 3,")
    lines.append("        base_delay: float = 1.0,")
    lines.append("        max_delay: float = 30.0,")
    lines.append(f"        requests_per_minute: int = {default_rate_limit},")
    if default_search_rate_limit is not None:
        lines.append(f"        search_requests_per_minute: int = {default_search_rate_limit},")
    lines.append("        on_retry: OnRetryCallback | None = None,")
    lines.append("    ) -> None:")
    lines.append("        if config is None:")
    lines.append("            if token is None:")
    lines.append('                raise ConfigError("either config or token must be provided")')
    lines.append("            import warnings")
    lines.append("            warnings.warn(")
    lines.append(
        f'                "{async_client_name}(token=...) is deprecated, "',
    )
    lines.append(
        f'                "use {async_client_name}(ClientConfig(token=..., ...)) instead",'
    )
    lines.append("                DeprecationWarning,")
    lines.append("                stacklevel=2,")
    lines.append("            )")
    lines.append("            config = ClientConfig(")
    lines.append("                token=token,")
    lines.append("                base_url=base_url,")
    lines.append("                proxy=ProxyConfig(url=proxy) if proxy else None,")
    lines.append(
        "                retry=RetryConfig("
        "max_retries=max_retries, base_delay=base_delay, max_delay=max_delay),"
    )
    lines.append(
        "                rate_limit=RateLimitConfig(requests_per_minute=requests_per_minute),"
    )
    if default_search_rate_limit is not None:
        lines.append(
            "                search_rate_limit=RateLimitConfig("
            "requests_per_minute=search_requests_per_minute),"
        )
    lines.append("                on_retry=on_retry,")
    lines.append("            )")
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
