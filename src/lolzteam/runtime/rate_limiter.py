from __future__ import annotations

import asyncio
import threading
import time


class RateLimiter:
    def __init__(self, requests_per_minute: int) -> None:
        self._max_tokens = requests_per_minute
        self._tokens = float(requests_per_minute)
        self._refill_rate = requests_per_minute / 60.0  # tokens per second
        self._last_refill = time.monotonic()
        self._lock = threading.Lock()
        self._async_lock = asyncio.Lock()

    def acquire(self) -> None:
        with self._lock:
            self._refill()
            if self._tokens >= 1:
                self._tokens -= 1
                return
            wait = (1 - self._tokens) / self._refill_rate

        time.sleep(wait)

        with self._lock:
            self._refill()
            self._tokens -= 1

    async def async_acquire(self) -> None:
        async with self._async_lock:
            self._refill()
            if self._tokens >= 1:
                self._tokens -= 1
                return
            wait = (1 - self._tokens) / self._refill_rate

        await asyncio.sleep(wait)

        async with self._async_lock:
            self._refill()
            self._tokens -= 1

    def _refill(self) -> None:
        now = time.monotonic()
        elapsed = now - self._last_refill
        self._tokens = min(self._max_tokens, self._tokens + elapsed * self._refill_rate)
        self._last_refill = now
