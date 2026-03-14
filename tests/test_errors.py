from __future__ import annotations

import httpx
import pytest

from lolzteam.runtime.errors import (
    AuthError,
    HttpError,
    LolzteamError,
    NetworkError,
    NotFoundError,
    RateLimitError,
    ServerError,
    create_http_error,
)

EMPTY_HEADERS = httpx.Headers()


class TestCreateHttpError:
    def test_429_returns_rate_limit_error(self) -> None:
        err = create_http_error(429, {}, EMPTY_HEADERS)
        assert isinstance(err, RateLimitError)
        assert err.status == 429

    def test_401_returns_auth_error(self) -> None:
        err = create_http_error(401, {}, EMPTY_HEADERS)
        assert isinstance(err, AuthError)
        assert err.status == 401

    def test_403_returns_auth_error(self) -> None:
        err = create_http_error(403, {}, EMPTY_HEADERS)
        assert isinstance(err, AuthError)
        assert err.status == 403

    def test_404_returns_not_found_error(self) -> None:
        err = create_http_error(404, {}, EMPTY_HEADERS)
        assert isinstance(err, NotFoundError)
        assert err.status == 404

    @pytest.mark.parametrize("status", [500, 502, 503])
    def test_5xx_returns_server_error(self, status: int) -> None:
        err = create_http_error(status, {}, EMPTY_HEADERS)
        assert isinstance(err, ServerError)
        assert err.status == status

    def test_other_status_returns_base_http_error(self) -> None:
        err = create_http_error(418, {"detail": "teapot"}, EMPTY_HEADERS)
        assert type(err) is HttpError
        assert err.status == 418
        assert err.body == {"detail": "teapot"}


class TestRateLimitError:
    def test_parses_retry_after_header(self) -> None:
        headers = httpx.Headers({"retry-after": "2.5"})
        err = RateLimitError(body={}, headers=headers)
        assert err.retry_after == 2.5

    def test_retry_after_none_when_missing(self) -> None:
        err = RateLimitError(body={}, headers=EMPTY_HEADERS)
        assert err.retry_after is None


class TestNetworkError:
    def test_wraps_cause(self) -> None:
        cause = ConnectionError("connection refused")
        err = NetworkError(cause)
        assert err.__cause__ is cause
        assert "connection refused" in str(err)

    def test_fallback_message_for_empty_cause(self) -> None:
        cause = OSError()
        err = NetworkError(cause)
        assert str(err) == "Network error"


class TestErrorHierarchy:
    def test_http_error_is_lolzteam_error(self) -> None:
        assert issubclass(HttpError, LolzteamError)

    def test_network_error_is_lolzteam_error(self) -> None:
        assert issubclass(NetworkError, LolzteamError)

    def test_rate_limit_error_is_http_error(self) -> None:
        assert issubclass(RateLimitError, HttpError)

    def test_server_error_is_http_error(self) -> None:
        assert issubclass(ServerError, HttpError)
