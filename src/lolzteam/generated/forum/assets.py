# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING

from lolzteam.runtime.types import RequestOptions

if TYPE_CHECKING:
    from lolzteam.runtime.async_http_client import AsyncHttpClient
    from lolzteam.runtime.http_client import HttpClient

    from .types import AssetsCssParams, AssetsCssResponse


class AssetsApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def css(self, *, params: AssetsCssParams | None = None) -> AssetsCssResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/css",
            query=params,
        ))


class AsyncAssetsApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def css(self, *, params: AssetsCssParams | None = None) -> AssetsCssResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/css",
            query=params,
        ))
