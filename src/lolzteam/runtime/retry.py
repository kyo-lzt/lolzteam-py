from __future__ import annotations

import asyncio
import random
import time
from typing import TYPE_CHECKING, TypeVar

from lolzteam.runtime.errors import NetworkError, RateLimitError, ServerError
from lolzteam.runtime.types import RetryInfo

if TYPE_CHECKING:
    from collections.abc import Awaitable, Callable

    from lolzteam.runtime.types import (
        OnRetryCallback,
        OnRetryCallbackAsync,
        RequestOptions,
        RetryConfig,
    )

_T = TypeVar("_T")


def is_retryable(error: Exception) -> bool:
    if isinstance(error, RateLimitError):
        return True
    if isinstance(error, ServerError) and error.status in (502, 503, 504):
        return True
    return isinstance(error, NetworkError) and error.is_transient


def compute_delay(attempt: int, config: RetryConfig, error: Exception) -> float:
    if isinstance(error, RateLimitError) and error.retry_after is not None:
        return min(error.retry_after, config.max_delay)
    exponential = config.base_delay * (2**attempt)
    jitter = random.random() * config.base_delay
    return min(exponential + jitter, config.max_delay)


def with_retry(
    fn: Callable[[], _T],
    config: RetryConfig,
    options: RequestOptions,
    on_retry: OnRetryCallback | None = None,
) -> _T:
    for attempt in range(config.max_retries + 1):
        try:
            return fn()
        except Exception as error:
            if not is_retryable(error) or attempt == config.max_retries:
                raise
            delay = compute_delay(attempt, config, error)
            if on_retry is not None:
                on_retry(
                    RetryInfo(
                        attempt=attempt,
                        delay=delay,
                        error=error,
                        method=options.method,
                        path=options.path,
                    )
                )
            time.sleep(delay)
    msg = "unreachable: max_retries must be >= 0"
    raise RuntimeError(msg)


async def async_with_retry(
    fn: Callable[[], Awaitable[_T]],
    config: RetryConfig,
    options: RequestOptions,
    on_retry: OnRetryCallbackAsync | None = None,
) -> _T:
    for attempt in range(config.max_retries + 1):
        try:
            return await fn()
        except Exception as error:
            if not is_retryable(error) or attempt == config.max_retries:
                raise
            delay = compute_delay(attempt, config, error)
            if on_retry is not None:
                await on_retry(
                    RetryInfo(
                        attempt=attempt,
                        delay=delay,
                        error=error,
                        method=options.method,
                        path=options.path,
                    )
                )
            await asyncio.sleep(delay)
    msg = "unreachable: max_retries must be >= 0"
    raise RuntimeError(msg)
