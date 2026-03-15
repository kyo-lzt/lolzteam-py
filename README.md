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
from lolzteam import ForumClient

with ForumClient(token="your_token") as forum:
    categories = forum.categories.list()
    threads = forum.threads.list(forum_id=876)
```

## Usage

### Synchronous

```python
from lolzteam import ForumClient, MarketClient

forum = ForumClient(token="your_token")
categories = forum.categories.list()
threads = forum.threads.list(forum_id=876)
user = forum.users.get(user_id=1)
forum.close()

market = MarketClient(token="your_token")
accounts = market.list.latest(category_name="steam")
market.close()
```

### Asynchronous

```python
from lolzteam import AsyncForumClient, AsyncMarketClient

async with AsyncForumClient(token="your_token") as forum:
    categories = await forum.categories.list()
    threads = await forum.threads.list(forum_id=876)

async with AsyncMarketClient(token="your_token") as market:
    accounts = await market.list.latest(category_name="steam")
```

Forum API groups: `o_auth`, `assets`, `categories`, `forums`, `links`, `pages`, `navigation`, `threads`, `posts`, `users`, `profile_posts`, `conversations`, `notifications`, `tags`, `search`, `batch`, `chatbox`, `forms`.

Market API groups: `category`, `list`, `managing`, `profile`, `cart`, `purchasing`, `custom_discounts`, `publishing`, `payments`, `auto_payments`, `proxy`, `imap`, `batch`.

## Configuration

```python
forum = ForumClient(
    token="your_token",
    proxy="http://user:pass@127.0.0.1:8080",
    max_retries=5,
    base_delay=1.0,
    max_delay=30.0,
    requests_per_minute=300,
)
```

| Parameter | Type | Default (Forum) | Default (Market) | Description |
|---|---|---|---|---|
| `token` | `str` | *required* | *required* | API access token |
| `base_url` | `str` | `https://prod-api.lolz.live` | `https://prod-api.lzt.market` | API base URL |
| `proxy` | `str \| None` | `None` | `None` | Proxy URL |
| `max_retries` | `int` | `3` | `3` | Maximum retry attempts |
| `base_delay` | `float` | `1.0` | `1.0` | Initial retry delay in seconds |
| `max_delay` | `float` | `30.0` | `30.0` | Maximum retry delay in seconds |
| `requests_per_minute` | `int` | `300` | `120` | Rate limiter capacity |

## Retry Logic

Failed requests are retried automatically for transient errors. The delay uses exponential backoff with jitter. `Retry-After` header on 429 responses is respected.

| Status | Retried | Behavior |
|--------|---------|----------|
| 429 | Yes | Uses `Retry-After` header if present |
| 502, 503 | Yes | Exponential backoff with jitter |
| 401, 403 | No | Thrown immediately |
| 404 | No | Thrown immediately |
| Other | No | Thrown immediately |

Delay formula: `min(base_delay * 2^attempt + random(0, base_delay), max_delay)`

## Proxy

Pass a proxy URL directly to the client constructor. Supported schemes: `http`, `https`, `socks5`.

```python
# HTTP proxy
forum = ForumClient(token="your_token", proxy="http://127.0.0.1:8080")

# Authenticated proxy
forum = ForumClient(token="your_token", proxy="http://user:pass@127.0.0.1:8080")

# SOCKS5 proxy
forum = ForumClient(token="your_token", proxy="socks5://127.0.0.1:1080")
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
