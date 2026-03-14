from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

JsonValue = dict[str, "JsonValue"] | list["JsonValue"] | str | int | float | bool | None


@dataclass(frozen=True, slots=True)
class ProxyConfig:
    url: str


@dataclass(frozen=True, slots=True)
class RetryConfig:
    max_retries: int = 3
    base_delay: float = 1.0  # seconds
    max_delay: float = 30.0  # seconds


@dataclass(frozen=True, slots=True)
class RateLimitConfig:
    requests_per_minute: int


@dataclass(frozen=True, slots=True)
class ClientConfig:
    token: str
    base_url: str = ""
    proxy: ProxyConfig | None = None
    retry: RetryConfig = field(default_factory=RetryConfig)
    rate_limit: RateLimitConfig | None = None


HttpMethod = Literal["GET", "POST", "PUT", "DELETE", "PATCH"]
ContentType = Literal["form", "multipart"]


@dataclass(frozen=True, slots=True)
class RequestOptions:
    method: HttpMethod
    path: str
    query: dict[str, object] | None = None
    body: dict[str, object] | None = None
    headers: dict[str, str] | None = None
    content_type: ContentType = "form"
