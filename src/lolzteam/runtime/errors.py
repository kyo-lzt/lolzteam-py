from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import httpx


class LolzteamError(Exception):
    pass


class HttpError(LolzteamError):
    def __init__(
        self,
        status: int,
        body: object,
        headers: httpx.Headers,
        parse_error: Exception | None = None,
    ) -> None:
        super().__init__(f"HTTP {status}")
        self.status = status
        self.body = body
        self.headers = headers
        self.parse_error = parse_error


class RateLimitError(HttpError):
    def __init__(
        self, body: object, headers: httpx.Headers, parse_error: Exception | None = None
    ) -> None:
        super().__init__(429, body, headers, parse_error=parse_error)
        raw = headers.get("retry-after")
        self.retry_after: float | None = float(raw) if raw is not None else None


class AuthError(HttpError):
    def __init__(
        self,
        status: int,
        body: object,
        headers: httpx.Headers,
        parse_error: Exception | None = None,
    ) -> None:
        super().__init__(status, body, headers, parse_error=parse_error)


class NotFoundError(HttpError):
    def __init__(
        self, body: object, headers: httpx.Headers, parse_error: Exception | None = None
    ) -> None:
        super().__init__(404, body, headers, parse_error=parse_error)


class ServerError(HttpError):
    def __init__(
        self,
        status: int,
        body: object,
        headers: httpx.Headers,
        parse_error: Exception | None = None,
    ) -> None:
        super().__init__(status, body, headers, parse_error=parse_error)


class NetworkError(LolzteamError):
    def __init__(self, cause: Exception) -> None:
        message = str(cause) if str(cause) else "Network error"
        super().__init__(message)
        self.__cause__ = cause

    @property
    def is_transient(self) -> bool:
        import httpx

        return isinstance(self.__cause__, (httpx.TimeoutException, httpx.ConnectError))


class RetryExhaustedError(LolzteamError):
    def __init__(self, last_error: Exception, attempts: int) -> None:
        self.last_error = last_error
        self.attempts = attempts
        super().__init__(f"Request failed after {attempts} attempts: {last_error}")


class ConfigError(LolzteamError):
    pass


def create_http_error(
    status: int,
    body: object,
    headers: httpx.Headers,
    parse_error: Exception | None = None,
) -> HttpError:
    if status == 429:
        return RateLimitError(body, headers, parse_error=parse_error)
    if status in (401, 403):
        return AuthError(status, body, headers, parse_error=parse_error)
    if status == 404:
        return NotFoundError(body, headers, parse_error=parse_error)
    if status in (500, 502, 503, 504):
        return ServerError(status, body, headers, parse_error=parse_error)
    return HttpError(status, body, headers, parse_error=parse_error)
