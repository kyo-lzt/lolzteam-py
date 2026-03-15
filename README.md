# lolzteam-py

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![CI](https://github.com/kyo-lzt/lolzteam-py/actions/workflows/ci.yml/badge.svg)](https://github.com/kyo-lzt/lolzteam-py/actions)

Python API wrapper for the [Lolzteam](https://lolz.live) Forum and Market APIs. **266 endpoints** (151 Forum + 115 Market) with sync and async support, auto-generated from OpenAPI specifications.

## Features

- **Complete API coverage** -- 266 endpoints across Forum and Market clients
- **Auto-generated** -- clients and types generated from OpenAPI 3.1.0 specs, always in sync
- **Dual sync/async** -- powered by httpx, same interface for both
- **Proxy support** -- HTTP, HTTPS, and SOCKS5
- **Retry logic** -- exponential backoff with jitter, respects `Retry-After` headers
- **Rate limiting** -- token bucket algorithm, thread-safe for sync and async
- **Strict typing** -- pyright strict mode, full type inference for every endpoint
- **Context managers** -- `with`/`async with` for automatic cleanup

## Quick Start

```bash
pip install lolzteam-api
```

```python
from lolzteam import ClientConfig, ForumClient

config = ClientConfig(token="your_token")

with ForumClient(config) as forum:
    categories = forum.categories.list()
    threads = forum.threads.list(forum_id=876)
```

## Usage

### Synchronous

```python
from lolzteam import ClientConfig, ForumClient, MarketClient

config = ClientConfig(token="your_token")

forum = ForumClient(config)
categories = forum.categories.list()
threads = forum.threads.list(forum_id=876)
user = forum.users.get(user_id=1)
forum.close()

market = MarketClient(config)
accounts = market.list.latest(category_name="steam")
market.close()
```

### Asynchronous

```python
from lolzteam import AsyncForumClient, AsyncMarketClient, ClientConfig

config = ClientConfig(token="your_token")

async with AsyncForumClient(config) as forum:
    categories = await forum.categories.list()
    threads = await forum.threads.list(forum_id=876)

async with AsyncMarketClient(config) as market:
    accounts = await market.list.latest(category_name="steam")
```

Forum API groups: `o_auth`, `assets`, `categories`, `forums`, `links`, `pages`, `navigation`, `threads`, `posts`, `users`, `profile_posts`, `conversations`, `notifications`, `tags`, `search`, `batch`, `chatbox`, `forms`.

Market API groups: `category`, `list`, `managing`, `profile`, `cart`, `purchasing`, `custom_discounts`, `publishing`, `payments`, `auto_payments`, `proxy`, `imap`, `batch`.

## Configuration

```python
from lolzteam import ClientConfig, ForumClient
from lolzteam.runtime import ProxyConfig, RateLimitConfig, RetryConfig

config = ClientConfig(
    token="your_token",
    proxy=ProxyConfig(url="http://user:pass@127.0.0.1:8080"),
    retry=RetryConfig(max_retries=5, base_delay=1.0, max_delay=30.0),
    rate_limit=RateLimitConfig(requests_per_minute=300),
    search_rate_limit=RateLimitConfig(requests_per_minute=20),
    on_retry=lambda info: print(f"Retry #{info.attempt}: {info.error}"),
    timeout=30.0,
)

forum = ForumClient(config)
```

| Field | Type | Default | Description |
|---|---|---|---|
| `token` | `str` | *required* | API access token |
| `base_url` | `str` | `""` | API base URL (clients provide their own default) |
| `proxy` | `ProxyConfig \| None` | `None` | Proxy configuration |
| `retry` | `RetryConfig \| None` | `RetryConfig()` | Retry configuration (`None` to disable) |
| `rate_limit` | `RateLimitConfig \| None` | `None` | Rate limiter for standard requests |
| `search_rate_limit` | `RateLimitConfig \| None` | `None` | Rate limiter for search requests |
| `on_retry` | `OnRetryCallback \| None` | `None` | Callback invoked before each retry |
| `timeout` | `float \| None` | `None` | Request timeout in seconds |

`RetryConfig` fields: `max_retries` (default `3`), `base_delay` (default `1.0`s), `max_delay` (default `30.0`s).

> **Backwards compatibility:** The flat-parameter style `ForumClient(token=..., proxy=..., max_retries=...)` still works but is deprecated and emits a `DeprecationWarning`. Migrate to `ClientConfig` for access to all options.

## Retry Logic

Failed requests are retried automatically for transient errors. The delay uses exponential backoff with jitter. `Retry-After` header on 429 responses is respected.

| Status | Retried | Behavior |
|--------|---------|----------|
| 429 | Yes | Uses `Retry-After` header if present |
| 502, 503, 504 | Yes | Exponential backoff with jitter |
| Network errors | Yes | Timeout and connection errors |
| 401, 403 | No | Thrown immediately |
| 404 | No | Thrown immediately |
| Other | No | Thrown immediately |

Delay formula: `min(base_delay * 2^attempt + random(0, base_delay), max_delay)`

```python
from lolzteam import ClientConfig, ForumClient
from lolzteam.runtime import RetryConfig

# Disable retry
config = ClientConfig(token="...", retry=None)
client = ForumClient(config)

# on_retry callback
config = ClientConfig(
    token="...",
    on_retry=lambda info: print(f"Retry #{info.attempt}"),
)
client = ForumClient(config)
```

## Proxy

Pass a `ProxyConfig` with the proxy URL. Supported schemes: `http`, `https`, `socks5`.

```python
from lolzteam import ClientConfig, ForumClient
from lolzteam.runtime import ProxyConfig

# HTTP proxy
config = ClientConfig(token="your_token", proxy=ProxyConfig(url="http://127.0.0.1:8080"))

# Authenticated proxy
config = ClientConfig(token="your_token", proxy=ProxyConfig(url="http://user:pass@127.0.0.1:8080"))

# SOCKS5 proxy
config = ClientConfig(token="your_token", proxy=ProxyConfig(url="socks5://127.0.0.1:1080"))

forum = ForumClient(config)
```

## Error Handling

All errors inherit from `LolzteamError`. HTTP errors carry the status code, response body, and headers.

```python
from lolzteam.runtime import (
    LolzteamError, HttpError, RateLimitError,
    AuthError, NotFoundError, ServerError, NetworkError,
)

try:
    user = forum.users.get(user_id=1)
except AuthError:
    print("Invalid or expired token")
except NotFoundError:
    print("User not found")
except RateLimitError as e:
    print(f"Rate limited, retry after {e.retry_after}s")
except ServerError as e:
    print(f"Server error: HTTP {e.status}")
except NetworkError:
    print("Connection failed")
```

Error hierarchy:

```
LolzteamError
├── HttpError
│   ├── RateLimitError    (429)
│   ├── AuthError         (401, 403)
│   ├── NotFoundError     (404)
│   └── ServerError       (500, 502, 503)
├── NetworkError
└── ConfigError
```

## Rate Limits

The built-in rate limiter uses a token bucket algorithm. Thread-safe for sync clients, uses `asyncio.Lock` for async clients. When the bucket is empty, requests wait until tokens refill -- no requests are dropped.

| Client | Default limit |
|--------|---------------|
| Forum  | 300 req/min   |
| Market | 120 req/min   |
| Market (search) | 20 req/min |

```python
from lolzteam import ClientConfig, MarketClient
from lolzteam.runtime import RateLimitConfig

config = ClientConfig(
    token="...",
    search_rate_limit=RateLimitConfig(requests_per_minute=30),
)
client = MarketClient(config)
```

## Code Generation

Clients and types are auto-generated from OpenAPI 3.1.0 specs in `schemas/`:

```bash
python -m codegen
```

| Input | Output |
|-------|--------|
| `schemas/forum.json` | `generated/forum/__init__.py`, `generated/forum/types.py` |
| `schemas/market.json` | `generated/market/__init__.py`, `generated/market/types.py` |

Generator source is in `codegen/`.

## Project Structure

```
schemas/                        OpenAPI 3.1.0 specifications
codegen/                        Code generator (parser, emitter, transforms)
src/lolzteam/
  runtime/
    http_client.py              Sync HTTP client (httpx)
    async_http_client.py        Async HTTP client (httpx)
    retry.py                    Retry logic (exponential backoff + jitter)
    rate_limiter.py             Token bucket rate limiter
    errors.py                   Error hierarchy
    auth.py                     Authentication
    types.py                    Config and request types
  generated/
    forum/                      Generated Forum client and types
    market/                     Generated Market client and types
tests/
pyproject.toml
```

## Commands

```bash
uv sync                        # Install dependencies
python -m codegen              # Generate clients from OpenAPI specs
uv run pyright                 # Type check (strict mode)
uv run ruff check --fix .      # Lint and auto-fix
uv run ruff format .           # Format code
uv run pytest                  # Run tests
```

## License

[MIT](LICENSE)
