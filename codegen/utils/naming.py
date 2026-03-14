"""Naming utilities for converting OpenAPI identifiers to Python names."""

from __future__ import annotations

import re


def _lowercase_first(s: str) -> str:
    if not s:
        return s
    return s[0].lower() + s[1:]


def _capitalize_first(s: str) -> str:
    if not s:
        return s
    return s[0].upper() + s[1:]


def _camel_to_snake(s: str) -> str:
    """Convert camelCase or PascalCase to snake_case."""
    # Insert underscore between lowercase/digit and uppercase
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)
    # Insert underscore between consecutive uppercase followed by lowercase
    s = re.sub(r"([A-Z])([A-Z][a-z])", r"\1_\2", s)
    return s.lower()


def operation_id_to_method(operation_id: str) -> str:
    """Extract method name from operationId: everything after the first dot, snake_cased.

    Examples:
        "Threads.List" -> "list"
        "Users.SA.Reset" -> "sa_reset"
        "Category.All" -> "all"
    """
    parts = operation_id.split(".")
    if len(parts) < 2:
        return _camel_to_snake(operation_id)
    rest = parts[1:]
    # In TS: join with camelCase. In Python: join with underscore, lowercase.
    return "_".join(part.lower() for part in rest)


def operation_id_to_group(operation_id: str) -> str:
    """Extract group name from operationId: first segment, lowercased first char."""
    first = operation_id.split(".")[0]
    return _lowercase_first(first) if first else operation_id


def group_to_file_name(group: str) -> str:
    """Convert PascalCase group name to snake_case file name (Python convention)."""
    return _camel_to_snake(group)


def group_to_class_name(group: str) -> str:
    """Convert group name to class name: PascalCase + 'Api'."""
    return _capitalize_first(group) + "Api"


def group_to_property_name(group: str) -> str:
    """Convert group name to snake_case property name (Python convention)."""
    return _camel_to_snake(group)


def build_type_name(group: str, method: str) -> str:
    """Build a type name prefix from group + method.

    The method name comes in as snake_case, so we PascalCase each segment.
    E.g. group "threads", method "list" -> "ThreadsList"
         group "users", method "sa_reset" -> "UsersSaReset"
    """
    group_part = _capitalize_first(group)
    method_parts = method.split("_")
    method_part = "".join(_capitalize_first(p) for p in method_parts)
    return group_part + method_part
