"""Recursive $ref resolver for OpenAPI schemas."""

from __future__ import annotations

from typing import TypeVar

T = TypeVar("T")

Spec = dict[str, object]


def resolve_ref(ref: str, spec: Spec) -> object:
    """Follow a JSON pointer path like `#/components/schemas/Foo` through a spec object."""
    parts = ref.removeprefix("#/").split("/")
    current: object = spec
    for part in parts:
        if not isinstance(current, dict):
            return None
        current = current.get(part)
        if current is None:
            return None
    return current


def _is_ref_object(value: object) -> bool:
    return isinstance(value, dict) and isinstance(value.get("$ref"), str)


def deref(value: object, spec: Spec, visited: set[str] | None = None) -> object:
    """Recursively resolve all `$ref` pointers in an object.

    Tracks visited refs to avoid infinite loops on circular references.
    """
    seen = visited if visited is not None else set()

    if _is_ref_object(value):
        assert isinstance(value, dict)
        ref = value["$ref"]
        assert isinstance(ref, str)
        # Preserve component schema refs — they map to named types
        if ref.startswith("#/components/schemas/"):
            return value
        if ref in seen:
            return {}
        seen.add(ref)
        resolved = resolve_ref(ref, spec)
        return deref(resolved, spec, seen)

    if isinstance(value, list):
        return [deref(item, spec, set(seen)) for item in value]

    if isinstance(value, dict):
        return {k: deref(v, spec, set(seen)) for k, v in value.items()}

    return value


def deref_shallow(
    value: object,
    spec: Spec,
    *,
    _visited: set[str] | None = None,
) -> object:
    """Shallow $ref resolution -- only resolves the top-level ref, does not recurse."""
    if _is_ref_object(value):
        assert isinstance(value, dict)
        ref = value["$ref"]
        assert isinstance(ref, str)
        seen = _visited if _visited is not None else set()
        if ref in seen:
            return value
        seen.add(ref)
        resolved = resolve_ref(ref, spec)
        if _is_ref_object(resolved):
            return deref_shallow(resolved, spec, _visited=seen)
        return resolved
    return value
