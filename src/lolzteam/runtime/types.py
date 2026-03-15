from __future__ import annotations

from collections.abc import Awaitable, Callable
from dataclasses import dataclass, field
from typing import Literal

JsonValue = dict[str, "JsonValue"] | list["JsonValue"] | str | int | float | bool | None


@dataclass(frozen=True, slots=True)
class ProxyConfig:
    url: str


@dataclass(frozen=True, slots=True)
class RetryInfo:
    """Information passed to the on_retry callback before each retry attempt."""

    attempt: int
    """Retry attempt number (0-based: 0 = first retry, 1 = second, etc.)."""
    delay: float
    """Delay in seconds before the retry."""
    error: Exception
    """The exception that triggered the retry."""
    method: str
    """HTTP method (GET, POST, etc.)."""
    path: str
    """Request path."""


OnRetryCallback = Callable[[RetryInfo], None]
OnRetryCallbackAsync = Callable[[RetryInfo], Awaitable[None]]


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
    search_rate_limit: RateLimitConfig | None = None
    on_retry: OnRetryCallback | None = None
    on_retry_async: OnRetryCallbackAsync | None = None


HttpMethod = Literal["GET", "POST", "PUT", "DELETE", "PATCH"]
ContentType = Literal["form", "json", "multipart"]


@dataclass(frozen=True, slots=True)
class RequestOptions:
    method: HttpMethod
    path: str
    query: dict[str, object] | None = None
    body: dict[str, object] | None = None
    headers: dict[str, str] | None = None
    content_type: ContentType = "form"
    is_search: bool = False
