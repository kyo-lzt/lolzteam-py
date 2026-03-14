from __future__ import annotations

from typing import TYPE_CHECKING, Any
from urllib.parse import urlencode, urlparse

import httpx

from lolzteam.runtime.auth import apply_auth
from lolzteam.runtime.errors import ConfigError, NetworkError, create_http_error
from lolzteam.runtime.rate_limiter import RateLimiter
from lolzteam.runtime.retry import async_with_retry

if TYPE_CHECKING:
    from types import TracebackType

    from lolzteam.runtime.types import ClientConfig, RequestOptions

DEFAULT_BASE_URL = "https://api.zelenka.guru"


def _serialize_value(key: str, value: object) -> list[tuple[str, str]]:
    """Serialize a single key-value pair into form-encoded pairs."""
    if value is None:
        return []
    if isinstance(value, bool):
        return [(key, "true" if value else "false")]
    if isinstance(value, list):
        pairs: list[tuple[str, str]] = []
        for item in value:  # pyright: ignore[reportUnknownVariableType]
            if isinstance(item, bool):
                pairs.append((key, "true" if item else "false"))
            else:
                pairs.append((key, str(item)))  # pyright: ignore[reportUnknownArgumentType]
        return pairs
    if isinstance(value, dict):
        pairs = []
        for sub_key, sub_value in value.items():  # pyright: ignore[reportUnknownVariableType]
            if sub_value is not None:
                if isinstance(sub_value, bool):
                    pairs.append((f"{key}[{sub_key}]", "true" if sub_value else "false"))
                else:
                    pairs.append((f"{key}[{sub_key}]", str(sub_value)))  # pyright: ignore[reportUnknownArgumentType]
        return pairs
    return [(key, str(value))]


def _build_params(data: dict[str, object]) -> list[tuple[str, str]]:
    """Build a list of (key, value) pairs from a dict, handling lists/bools/dicts."""
    pairs: list[tuple[str, str]] = []
    for key, value in data.items():
        pairs.extend(_serialize_value(key, value))
    return pairs


def _build_query_string(query: dict[str, object]) -> str:
    return urlencode(_build_params(query))


def _encode_form_body(body: dict[str, object]) -> str:
    return urlencode(_build_params(body))


def _split_multipart_body(
    body: dict[str, object],
) -> tuple[dict[str, str], dict[str, tuple[str, bytes, str]]]:
    """Split body into data fields and file fields for multipart upload."""
    data: dict[str, str] = {}
    files: dict[str, tuple[str, bytes, str]] = {}
    for key, value in body.items():
        if value is None:
            continue
        if isinstance(value, bytes):
            files[key] = (key, value, "application/octet-stream")
        elif isinstance(value, bool):
            data[key] = "true" if value else "false"
        else:
            data[key] = str(value)
    return data, files


class AsyncHttpClient:
    def __init__(self, config: ClientConfig) -> None:
        self._token = config.token
        self._base_url = (config.base_url or DEFAULT_BASE_URL).rstrip("/")
        self._retry_config = config.retry

        self._rate_limiter: RateLimiter | None = None
        if config.rate_limit is not None:
            self._rate_limiter = RateLimiter(config.rate_limit.requests_per_minute)

        proxy: str | None = None
        if config.proxy is not None:
            parsed = urlparse(config.proxy.url)
            if parsed.scheme not in ("http", "https", "socks5"):
                msg = f"unsupported proxy scheme: {parsed.scheme or '<none>'}"
                raise ConfigError(msg)
            if not parsed.hostname:
                raise ConfigError("proxy URL has no host")
            proxy = config.proxy.url
        self._client = httpx.AsyncClient(proxy=proxy)

    async def request(self, options: RequestOptions) -> Any:
        if self._rate_limiter is not None:
            await self._rate_limiter.async_acquire()
        return await async_with_retry(
            lambda: self._execute(options),
            self._retry_config,
        )

    async def _execute(self, options: RequestOptions) -> Any:
        url = f"{self._base_url}{options.path}"
        if options.query is not None:
            qs = _build_query_string(options.query)
            if qs:
                url = f"{url}?{qs}"

        headers = apply_auth(dict(options.headers or {}), self._token)

        content: str | None = None
        data: dict[str, str] | None = None
        files: dict[str, tuple[str, bytes, str]] | None = None

        if options.body is not None and options.method != "GET":
            if options.content_type == "multipart":
                data, files = _split_multipart_body(options.body)
            else:
                headers["Content-Type"] = "application/x-www-form-urlencoded"
                content = _encode_form_body(options.body)

        try:
            response = await self._client.request(
                method=options.method,
                url=url,
                headers=headers,
                content=content,
                data=data,
                files=files,
            )
        except httpx.HTTPError as error:
            raise NetworkError(error) from error

        try:
            body = response.json()
        except Exception:
            body = None

        if not response.is_success:
            raise create_http_error(response.status_code, body, response.headers)

        return body

    async def close(self) -> None:
        await self._client.aclose()

    async def __aenter__(self) -> AsyncHttpClient:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self.close()
