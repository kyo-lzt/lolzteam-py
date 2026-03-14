# lolzteam-api

Fully typed Python API wrapper for [Lolzteam](https://lolz.live) Forum and Market APIs.

**151 Forum endpoints + 115 Market endpoints** — all generated from the official OpenAPI schemas.

## Installation

```bash
pip install lolzteam-api
```

## Quick Start

```python
from lolzteam import ForumClient, MarketClient

# Forum
forum = ForumClient(token="your_token")
threads = forum.threads.list()
thread = forum.threads.get(thread_id=123)
forum.close()

# Market
market = MarketClient(token="your_token")
items = market.category.steam()
item = market.managing.get(item_id=456)
market.close()
```

### Async

```python
import asyncio
from lolzteam import AsyncForumClient

async def main():
    async with AsyncForumClient(token="your_token") as forum:
        me = await forum.users.me()
        threads = await forum.threads.list()

asyncio.run(main())
```

### Context Manager

```python
with ForumClient(token="your_token") as forum:
    users = forum.users.search(params={"username": "test"})
```

## Features

- **Fully typed** — TypedDict params, bodies, and responses generated from OpenAPI schemas
- **Sync + Async** — `ForumClient` / `AsyncForumClient`, `MarketClient` / `AsyncMarketClient`
- **Auto-retry** — 429 (respects `Retry-After`), 502, 503 with exponential backoff + jitter
- **Rate limiting** — built-in token bucket (Forum: 300 req/min, Market: 120 req/min)
- **Proxy support** — via httpx
- **File uploads** — `multipart/form-data` for avatar/background endpoints
- **Zero config** — just pass your token

## Configuration

```python
client = ForumClient(
    # Required
    token="your_bearer_token",

    # Optional: proxy
    proxy="http://user:pass@host:port",

    # Optional: retry config
    max_retries=5,       # default: 3
    base_delay=2.0,      # default: 1.0s
    max_delay=60.0,      # default: 30.0s
)
```

## Error Handling

```python
from lolzteam.runtime.errors import (
    LolzteamError,    # Base error
    HttpError,        # HTTP error (status, body, headers)
    RateLimitError,   # 429 — has retry_after attribute
    AuthError,        # 401, 403
    NotFoundError,    # 404
    ServerError,      # 500, 502, 503
    NetworkError,     # Connection errors
)

try:
    thread = forum.threads.get(thread_id=999999)
except NotFoundError:
    print("Thread not found")
except RateLimitError as e:
    print(f"Rate limited, retry after {e.retry_after}s")
except HttpError as e:
    print(f"HTTP {e.status}: {e.body}")
```

## API Groups

### ForumClient

| Group | Methods | Description |
|-------|---------|-------------|
| `client.threads` | 22 | Threads CRUD, bump, follow, polls |
| `client.posts` | 15 | Posts, comments, reporting |
| `client.users` | 26 | Users, avatar/background upload, search |
| `client.profile_posts` | 18 | Profile posts and comments |
| `client.conversations` | 23 | Private conversations |
| `client.chatbox` | 12 | Chatbox messages |
| `client.forums` | 9 | Forum nodes |
| `client.search` | 7 | Search |
| `client.tags` | 4 | Thread tags |
| `client.notifications` | 3 | Notifications |
| `client.categories` | 2 | Forum categories |
| `client.forms` | 2 | Forms (P2P, complaints) |
| `client.links` | 2 | Links |
| `client.pages` | 2 | Pages |
| `client.assets` | 1 | Assets |
| `client.batch` | 1 | Batch requests |
| `client.navigation` | 1 | Navigation |
| `client.o_auth` | 1 | OAuth token |

### MarketClient

| Group | Methods | Description |
|-------|---------|-------------|
| `client.managing` | 40 | Item management (edit, bump, note, transfer) |
| `client.category` | 28 | Browse by game/platform (Steam, Fortnite, etc.) |
| `client.payments` | 12 | Payment history, invoices |
| `client.list` | 6 | Item listings with filters |
| `client.purchasing` | 5 | Buy items (fast buy, check, confirm) |
| `client.publishing` | 4 | Publish/sell items |
| `client.custom_discounts` | 4 | Custom discounts |
| `client.cart` | 3 | Shopping cart |
| `client.auto_payments` | 3 | Auto-payment rules |
| `client.profile` | 3 | User profiles |
| `client.proxy` | 3 | Proxy management |
| `client.imap` | 2 | IMAP email access |
| `client.batch` | 1 | Batch requests |

## Code Generation

All client code and types are **generated from OpenAPI 3.1.0 schemas** — not written by hand.

```bash
python -m codegen
```

This reads `schemas/forum.json` and `schemas/market.json`, resolves all `$ref` pointers, and emits typed Python files. Generated code is committed to the repo — no codegen step needed at install time.

### Where types are generated

| What | Where |
|------|-------|
| Generator source | `codegen/` (`__main__.py`, `parser.py`, `emitter.py`) |
| Forum types | `src/lolzteam/generated/forum/types.py` |
| Market types | `src/lolzteam/generated/market/types.py` |
| Forum API groups | `src/lolzteam/generated/forum/*.py` (18 files) |
| Market API groups | `src/lolzteam/generated/market/*.py` (14 files) |

## Project Structure

```
lolzteam-py/
  schemas/              OpenAPI 3.1.0 specs (forum.json, market.json)
  codegen/              Code generator (reads OpenAPI -> emits Python code)
  src/lolzteam/
    runtime/            HTTP client, retry, rate limiter, errors, auth
    generated/          Generated clients and types (committed to repo)
  tests/
  pyproject.toml
```

## Development

```bash
uv sync                          # Install deps
python -m codegen                # Regenerate from schemas
uv run ruff check --fix .        # Lint
uv run ruff format .             # Format
uv run pyright                   # Type check
uv run pytest                    # Test
```

## License

MIT
