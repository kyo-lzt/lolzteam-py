# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING

from lolzteam.runtime.types import RequestOptions

if TYPE_CHECKING:
    from lolzteam.runtime.async_http_client import AsyncHttpClient
    from lolzteam.runtime.http_client import HttpClient

    from .types import LinksGetResponse, LinksListResponse


class LinksApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def list(self) -> LinksListResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/link-forums",
        ))

    def get(self, link_id: int) -> LinksGetResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path=f"/link-forums/{link_id}",
        ))


class AsyncLinksApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def list(self) -> LinksListResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/link-forums",
        ))

    async def get(self, link_id: int) -> LinksGetResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path=f"/link-forums/{link_id}",
        ))
