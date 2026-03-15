from __future__ import annotations

from unittest.mock import patch

import httpx
import pytest

from lolzteam.runtime.errors import (
    AuthError,
    HttpError,
    NetworkError,
    NotFoundError,
    RateLimitError,
    ServerError,
)
from lolzteam.runtime.retry import (
    async_with_retry,
    compute_delay,
    is_retryable,
    with_retry,
)
from lolzteam.runtime.types import RequestOptions, RetryConfig, RetryInfo

EMPTY_HEADERS = httpx.Headers()
CONFIG = RetryConfig(max_retries=3, base_delay=1.0, max_delay=30.0)
DUMMY_OPTS = RequestOptions(method="GET", path="/test")


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

    def test_server_error_504_is_retryable(self) -> None:
        err = ServerError(504, body={}, headers=EMPTY_HEADERS)
        assert is_retryable(err) is True

    def test_auth_error_is_not_retryable(self) -> None:
        err = AuthError(401, body={}, headers=EMPTY_HEADERS)
        assert is_retryable(err) is False

    def test_not_found_error_is_not_retryable(self) -> None:
        err = NotFoundError(body={}, headers=EMPTY_HEADERS)
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
        assert 1.0 <= delay < 2.0

    def test_exponential_increases_with_attempt(self) -> None:
        err = ServerError(502, body={}, headers=EMPTY_HEADERS)
        delays = [compute_delay(a, CONFIG, err) for a in range(3)]
        assert delays[2] >= 4.0

    def test_capped_by_max_delay(self) -> None:
        err = ServerError(502, body={}, headers=EMPTY_HEADERS)
        delay = compute_delay(10, CONFIG, err)
        assert delay <= CONFIG.max_delay

    def test_rate_limit_without_retry_after_uses_backoff(self) -> None:
        err = RateLimitError(body={}, headers=EMPTY_HEADERS)
        delay = compute_delay(0, CONFIG, err)
        assert 1.0 <= delay < 2.0

    def test_attempt_1_doubles_base(self) -> None:
        err = ServerError(502, body={}, headers=EMPTY_HEADERS)
        delay = compute_delay(1, CONFIG, err)
        assert 2.0 <= delay < 3.0


class TestWithRetry:
    @patch("lolzteam.runtime.retry.time.sleep")
    def test_succeeds_on_first_try(self, mock_sleep: object) -> None:
        result = with_retry(lambda: 42, CONFIG, DUMMY_OPTS)
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

        result = with_retry(fn, CONFIG, DUMMY_OPTS)
        assert result == "ok"
        assert calls == 3

    @patch("lolzteam.runtime.retry.time.sleep")
    def test_raises_immediately_on_non_retryable(self, mock_sleep: object) -> None:
        def fn() -> str:
            raise AuthError(401, body={}, headers=EMPTY_HEADERS)

        with pytest.raises(AuthError):
            with_retry(fn, CONFIG, DUMMY_OPTS)

    @patch("lolzteam.runtime.retry.time.sleep")
    def test_raises_after_max_retries_exhausted(self, mock_sleep: object) -> None:
        def fn() -> str:
            raise RateLimitError(body={}, headers=EMPTY_HEADERS)

        with pytest.raises(RateLimitError):
            with_retry(fn, CONFIG, DUMMY_OPTS)

    @patch("lolzteam.runtime.retry.time.sleep")
    def test_does_not_retry_server_500(self, mock_sleep: object) -> None:
        calls = 0

        def fn() -> str:
            nonlocal calls
            calls += 1
            raise ServerError(500, body={}, headers=EMPTY_HEADERS)

        with pytest.raises(ServerError):
            with_retry(fn, CONFIG, DUMMY_OPTS)
        assert calls == 1

    @patch("lolzteam.runtime.retry.time.sleep")
    def test_does_not_retry_not_found(self, mock_sleep: object) -> None:
        calls = 0

        def fn() -> str:
            nonlocal calls
            calls += 1
            raise NotFoundError(body={}, headers=EMPTY_HEADERS)

        with pytest.raises(NotFoundError):
            with_retry(fn, CONFIG, DUMMY_OPTS)
        assert calls == 1

    @patch("lolzteam.runtime.retry.time.sleep")
    def test_retries_502_then_succeeds(self, mock_sleep: object) -> None:
        calls = 0

        def fn() -> str:
            nonlocal calls
            calls += 1
            if calls == 1:
                raise ServerError(502, body={}, headers=EMPTY_HEADERS)
            return "recovered"

        result = with_retry(fn, CONFIG, DUMMY_OPTS)
        assert result == "recovered"
        assert calls == 2

    @patch("lolzteam.runtime.retry.time.sleep")
    def test_on_retry_callback_called(self, mock_sleep: object) -> None:
        retries: list[int] = []

        def on_retry(info: RetryInfo) -> None:
            retries.append(info.attempt)

        calls = 0

        def fn() -> str:
            nonlocal calls
            calls += 1
            if calls <= 2:
                raise RateLimitError(body={}, headers=EMPTY_HEADERS)
            return "ok"

        result = with_retry(fn, CONFIG, DUMMY_OPTS, on_retry=on_retry)
        assert result == "ok"
        assert retries == [0, 1]


class TestAsyncWithRetry:
    @patch("lolzteam.runtime.retry.asyncio.sleep")
    async def test_succeeds_on_first_try(self, mock_sleep: object) -> None:
        result = await async_with_retry(async_value(42), CONFIG, DUMMY_OPTS)
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

        result = await async_with_retry(fn, CONFIG, DUMMY_OPTS)
        assert result == "ok"
        assert calls == 3

    @patch("lolzteam.runtime.retry.asyncio.sleep")
    async def test_raises_immediately_on_non_retryable(self, mock_sleep: object) -> None:
        async def fn() -> str:
            raise AuthError(401, body={}, headers=EMPTY_HEADERS)

        with pytest.raises(AuthError):
            await async_with_retry(fn, CONFIG, DUMMY_OPTS)

    @patch("lolzteam.runtime.retry.asyncio.sleep")
    async def test_raises_after_max_retries_exhausted(self, mock_sleep: object) -> None:
        async def fn() -> str:
            raise RateLimitError(body={}, headers=EMPTY_HEADERS)

        with pytest.raises(RateLimitError):
            await async_with_retry(fn, CONFIG, DUMMY_OPTS)

    @patch("lolzteam.runtime.retry.asyncio.sleep")
    async def test_does_not_retry_network_error(self, mock_sleep: object) -> None:
        calls = 0

        async def fn() -> str:
            nonlocal calls
            calls += 1
            raise NetworkError(ConnectionError("refused"))

        with pytest.raises(NetworkError):
            await async_with_retry(fn, CONFIG, DUMMY_OPTS)
        assert calls == 1

    @patch("lolzteam.runtime.retry.asyncio.sleep")
    async def test_retries_503_then_succeeds(self, mock_sleep: object) -> None:
        calls = 0

        async def fn() -> str:
            nonlocal calls
            calls += 1
            if calls == 1:
                raise ServerError(503, body={}, headers=EMPTY_HEADERS)
            return "recovered"

        result = await async_with_retry(fn, CONFIG, DUMMY_OPTS)
        assert result == "recovered"
        assert calls == 2


def async_value(value: int):  # noqa: ANN201
    """Helper that returns a callable producing an awaitable."""

    async def fn() -> int:
        return value

    return fn
