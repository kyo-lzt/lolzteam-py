from __future__ import annotations


def apply_auth(headers: dict[str, str], token: str) -> dict[str, str]:
    return {**headers, "Authorization": f"Bearer {token}"}
