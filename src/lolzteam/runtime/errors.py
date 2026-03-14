from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import httpx


class LolzteamError(Exception):
    pass


class HttpError(LolzteamError):
    def __init__(self, status: int, body: object, headers: httpx.Headers) -> None:
        super().__init__(f"HTTP {status}")
        self.status = status
        self.body = body
        self.headers = headers


class RateLimitError(HttpError):
    def __init__(self, body: object, headers: httpx.Headers) -> None:
        super().__init__(429, body, headers)
        raw = headers.get("retry-after")
        self.retry_after: float | None = float(raw) if raw is not None else None


class AuthError(HttpError):
    def __init__(self, status: int, body: object, headers: httpx.Headers) -> None:
        super().__init__(status, body, headers)


class NotFoundError(HttpError):
    def __init__(self, body: object, headers: httpx.Headers) -> None:
        super().__init__(404, body, headers)


class ServerError(HttpError):
    def __init__(self, status: int, body: object, headers: httpx.Headers) -> None:
        super().__init__(status, body, headers)


class NetworkError(LolzteamError):
    def __init__(self, cause: Exception) -> None:
        message = str(cause) if str(cause) else "Network error"
        super().__init__(message)
        self.__cause__ = cause


def create_http_error(status: int, body: object, headers: httpx.Headers) -> HttpError:
    if status == 429:
        return RateLimitError(body, headers)
    if status in (401, 403):
        return AuthError(status, body, headers)
    if status == 404:
        return NotFoundError(body, headers)
    if status in (500, 502, 503):
        return ServerError(status, body, headers)
    return HttpError(status, body, headers)
