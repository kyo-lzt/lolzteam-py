# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING

from lolzteam.runtime.types import RequestOptions

if TYPE_CHECKING:
    from lolzteam.runtime.async_http_client import AsyncHttpClient
    from lolzteam.runtime.http_client import HttpClient

    from .types import PagesGetResponse, PagesListParams, PagesListResponse


class PagesApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def list(self, *, params: PagesListParams | None = None) -> PagesListResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/pages",
            query=params,
        ))

    def get(self, page_id: int) -> PagesGetResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path=f"/pages/{page_id}",
        ))


class AsyncPagesApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def list(self, *, params: PagesListParams | None = None) -> PagesListResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/pages",
            query=params,
        ))

    async def get(self, page_id: int) -> PagesGetResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path=f"/pages/{page_id}",
        ))
