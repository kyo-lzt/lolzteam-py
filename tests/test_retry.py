from __future__ import annotations

from unittest.mock import patch

import httpx
import pytest

from lolzteam.runtime.errors import (
    AuthError,
    HttpError,
    NetworkError,
    RateLimitError,
    ServerError,
)
from lolzteam.runtime.retry import (
    async_with_retry,
    compute_delay,
    is_retryable,
    with_retry,
)
from lolzteam.runtime.types import RetryConfig

EMPTY_HEADERS = httpx.Headers()
CONFIG = RetryConfig(max_retries=3, base_delay=1.0, max_delay=30.0)


class TestIsRetryable:
    def test_rate_limit_error_is_retryable(self) -> None:
        err = RateLimitError(body={}, headers=EMPTY_HEADERS)
        assert is_retryable(err) is True

    def test_server_error_502_is_retryable(self) -> None:
        err = ServerError(502, body={}, headers=EMPTY_HEADERS)
        assert is_retryable(err) is True

    def test_server_error_503_is_retryable(self) -> None:
        err = ServerError(503, body={}, headers=EMPTY_HEADERS)
        assert is_retryable(err) is True

    def test_server_error_500_is_not_retryable(self) -> None:
        err = ServerError(500, body={}, headers=EMPTY_HEADERS)
        assert is_retryable(err) is False

    def test_auth_error_is_not_retryable(self) -> None:
        err = AuthError(401, body={}, headers=EMPTY_HEADERS)
        assert is_retryable(err) is False

    def test_generic_http_error_is_not_retryable(self) -> None:
        err = HttpError(418, body={}, headers=EMPTY_HEADERS)
        assert is_retryable(err) is False

    def test_network_error_is_not_retryable(self) -> None:
        err = NetworkError(ConnectionError())
        assert is_retryable(err) is False


class TestComputeDelay:
    def test_uses_retry_after_when_available(self) -> None:
        headers = httpx.Headers({"retry-after": "2.5"})
        err = RateLimitError(body={}, headers=headers)
        delay = compute_delay(0, CONFIG, err)
        assert delay == 2.5

    def test_retry_after_capped_by_max_delay(self) -> None:
        headers = httpx.Headers({"retry-after": "60"})
        err = RateLimitError(body={}, headers=headers)
        delay = compute_delay(0, CONFIG, err)
        assert delay == CONFIG.max_delay

    def test_exponential_backoff_without_retry_after(self) -> None:
        err = ServerError(502, body={}, headers=EMPTY_HEADERS)
        delay = compute_delay(0, CONFIG, err)
        # attempt 0: base_delay * 2^0 + jitter = 1.0 + [0, 1.0)
        assert 1.0 <= delay < 2.0

    def test_exponential_increases_with_attempt(self) -> None:
        err = ServerError(502, body={}, headers=EMPTY_HEADERS)
        delays = [compute_delay(a, CONFIG, err) for a in range(3)]
        # With high probability exponential part grows; check attempt 2 min > attempt 0 min
        # attempt 2: base=4.0 + jitter -> at least 4.0
        assert delays[2] >= 4.0

    def test_capped_by_max_delay(self) -> None:
        err = ServerError(502, body={}, headers=EMPTY_HEADERS)
        delay = compute_delay(10, CONFIG, err)
        assert delay <= CONFIG.max_delay


class TestWithRetry:
    @patch("lolzteam.runtime.retry.time.sleep")
    def test_succeeds_on_first_try(self, mock_sleep: object) -> None:
        result = with_retry(lambda: 42, CONFIG)
        assert result == 42

    @patch("lolzteam.runtime.retry.time.sleep")
    def test_retries_on_retryable_error(self, mock_sleep: object) -> None:
        calls = 0

        def fn() -> str:
            nonlocal calls
            calls += 1
            if calls < 3:
                raise RateLimitError(body={}, headers=EMPTY_HEADERS)
            return "ok"

        result = with_retry(fn, CONFIG)
        assert result == "ok"
        assert calls == 3

    @patch("lolzteam.runtime.retry.time.sleep")
    def test_raises_immediately_on_non_retryable(self, mock_sleep: object) -> None:
        def fn() -> str:
            raise AuthError(401, body={}, headers=EMPTY_HEADERS)

        with pytest.raises(AuthError):
            with_retry(fn, CONFIG)

    @patch("lolzteam.runtime.retry.time.sleep")
    def test_raises_after_max_retries_exhausted(self, mock_sleep: object) -> None:
        def fn() -> str:
            raise RateLimitError(body={}, headers=EMPTY_HEADERS)

        with pytest.raises(RateLimitError):
            with_retry(fn, CONFIG)


class TestAsyncWithRetry:
    @patch("lolzteam.runtime.retry.asyncio.sleep")
    async def test_succeeds_on_first_try(self, mock_sleep: object) -> None:
        result = await async_with_retry(async_value(42), CONFIG)
        assert result == 42

    @patch("lolzteam.runtime.retry.asyncio.sleep")
    async def test_retries_on_retryable_error(self, mock_sleep: object) -> None:
        calls = 0

        async def fn() -> str:
            nonlocal calls
            calls += 1
            if calls < 3:
                raise ServerError(502, body={}, headers=EMPTY_HEADERS)
            return "ok"

        result = await async_with_retry(fn, CONFIG)
        assert result == "ok"
        assert calls == 3

    @patch("lolzteam.runtime.retry.asyncio.sleep")
    async def test_raises_immediately_on_non_retryable(self, mock_sleep: object) -> None:
        async def fn() -> str:
            raise AuthError(401, body={}, headers=EMPTY_HEADERS)

        with pytest.raises(AuthError):
            await async_with_retry(fn, CONFIG)

    @patch("lolzteam.runtime.retry.asyncio.sleep")
    async def test_raises_after_max_retries_exhausted(self, mock_sleep: object) -> None:
        async def fn() -> str:
            raise RateLimitError(body={}, headers=EMPTY_HEADERS)

        with pytest.raises(RateLimitError):
            await async_with_retry(fn, CONFIG)


def async_value(value: int):  # noqa: ANN201
    """Helper that returns a callable producing an awaitable."""

    async def fn() -> int:
        return value

    return fn
