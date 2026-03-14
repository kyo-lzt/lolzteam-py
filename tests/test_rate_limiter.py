from __future__ import annotations

import threading
import time

from lolzteam.runtime.rate_limiter import RateLimiter


class TestRateLimiter:
    def test_acquire_when_tokens_available(self) -> None:
        limiter = RateLimiter(requests_per_minute=300)
        start = time.monotonic()
        limiter.acquire()
        elapsed = time.monotonic() - start
        assert elapsed < 0.05  # should be near-instant

    def test_acquire_respects_rate_limit(self) -> None:
        # 60 rpm = 1 req/sec, so second acquire should wait ~1s
        limiter = RateLimiter(requests_per_minute=60)
        # Drain the bucket to 0
        for _ in range(60):
            limiter.acquire()

        start = time.monotonic()
        limiter.acquire()
        elapsed = time.monotonic() - start
        assert elapsed >= 0.5  # should wait roughly 1/refill_rate for 1 token

    def test_thread_safety(self) -> None:
        limiter = RateLimiter(requests_per_minute=600)
        errors: list[Exception] = []
        count = 0
        lock = threading.Lock()

        def worker() -> None:
            nonlocal count
            try:
                for _ in range(10):
                    limiter.acquire()
                    with lock:
                        count += 1
            except Exception as e:
                errors.append(e)

        threads = [threading.Thread(target=worker) for _ in range(5)]
        for t in threads:
            t.start()
        for t in threads:
            t.join(timeout=10)

        assert not errors
        assert count == 50
