# lolzteam-api-py

API wrapper for Lolzteam Forum and Market (sync + async).

## Project structure

```
schemas/          — OpenAPI 3.1.0 specs (symlinks to ../lolzteam-ts/schemas/)
codegen/          — Code generator (reads OpenAPI -> emits Python client code)
src/lolzteam/     — Library source
  runtime/        — HTTP client, retry, rate limiter, proxy, auth, errors
  generated/      — Generated clients and types (committed to repo)
tests/            — Tests
```

## Key commands

- `uv sync` — install deps
- `python -m codegen` — regenerate clients from OpenAPI schemas
- `uv run pyright` — type check
- `uv run ruff check --fix .` — lint fix
- `uv run ruff format .` — format
- `uv run pytest` — run tests

## Architecture

- **Two separate clients**: `ForumClient` / `AsyncForumClient` and `MarketClient` / `AsyncMarketClient`
- **DX pattern**: `client.threads.list()` — methods grouped by API tags
- **Sync + Async**: each group has both sync and async class variants
- **Codegen**: Python script reads OpenAPI JSON, resolves $refs, groups by tags, emits typed methods
- **Runtime**: httpx for HTTP (sync: `httpx.Client`, async: `httpx.AsyncClient`)
- **Generated code is committed** — no codegen needed at install time

## API details

- **Auth**: Bearer token only
- **Forum**: base URL `https://api.lolz.live`, rate limit 300 req/min
- **Market**: base URL `https://api.lzt.market`, rate limit 120 req/min
- **Retry**: 429 (Retry-After), 502, 503 — exponential backoff + jitter
- **Bodies**: `application/x-www-form-urlencoded`
- **Parameters**: snake_case preserved (1:1 with API)

## Conventions

- Python 3.11+, strict pyright, ruff
- TypedDict for params/body/response types
- Custom error hierarchy: `LolzteamError` -> `HttpError` / `NetworkError`
- No `Any`, real types only
