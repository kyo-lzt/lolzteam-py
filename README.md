# lolzteam-py

Python API wrapper for Lolzteam Forum and Market (sync + async). Clients and types are generated from OpenAPI specs.

## Requirements

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)

## Setup

```bash
git clone https://github.com/kyo-lzt/lolzteam-py.git
cd lolzteam-py
uv sync
```

## Code Generation

```bash
python -m codegen
```

Reads schemas from `schemas/forum.json` and `schemas/market.json`, generates typed clients into:

| What | Where |
|------|-------|
| Forum types | `src/lolzteam/generated/forum/types.py` |
| Market types | `src/lolzteam/generated/market/types.py` |
| Forum client | `src/lolzteam/generated/forum/__init__.py` |
| Market client | `src/lolzteam/generated/market/__init__.py` |

Generator source — `codegen/` (`__main__.py`, `parser.py`, `emitter.py`).

## Project Structure

```
schemas/              — OpenAPI 3.1.0 specs
codegen/              — Code generator
src/lolzteam/
  runtime/            — HTTP client, retry, rate limiter, proxy, errors
  generated/          — Generated code (committed to repo)
tests/
pyproject.toml
```

## Commands

```bash
uv sync                      # Install dependencies
python -m codegen             # Generate clients from schemas
uv run pyright                # Type check
uv run ruff check --fix .     # Lint
uv run ruff format .          # Format
uv run pytest                 # Tests
```

## License

MIT
