# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING

from lolzteam.runtime.types import RequestOptions

if TYPE_CHECKING:
    from lolzteam.runtime.async_http_client import AsyncHttpClient
    from lolzteam.runtime.http_client import HttpClient

    from .types import (
        ProxyAddBody,
        ProxyAddResponse,
        ProxyDeleteBody,
        ProxyDeleteResponse,
        ProxyGetResponse,
    )


class ProxyApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def get(self) -> ProxyGetResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/proxy",
        ))

    def add(self, *, body: ProxyAddBody) -> ProxyAddResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path="/proxy",
            body=body,
        ))

    def delete(self, *, body: ProxyDeleteBody | None = None) -> ProxyDeleteResponse:
        return self._http.request(RequestOptions(
            method="DELETE",
            path="/proxy",
            body=body,
        ))


class AsyncProxyApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def get(self) -> ProxyGetResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/proxy",
        ))

    async def add(self, *, body: ProxyAddBody) -> ProxyAddResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path="/proxy",
            body=body,
        ))

    async def delete(self, *, body: ProxyDeleteBody | None = None) -> ProxyDeleteResponse:
        return await self._http.request(RequestOptions(
            method="DELETE",
            path="/proxy",
            body=body,
        ))
