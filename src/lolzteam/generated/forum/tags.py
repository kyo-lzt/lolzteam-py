# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING

from lolzteam.runtime.types import RequestOptions

if TYPE_CHECKING:
    from lolzteam.runtime.async_http_client import AsyncHttpClient
    from lolzteam.runtime.http_client import HttpClient

    from .types import (
        TagsFindParams,
        TagsFindResponse,
        TagsGetParams,
        TagsGetResponse,
        TagsListParams,
        TagsListResponse,
        TagsPopularResponse,
    )


class TagsApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def popular(self) -> TagsPopularResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/tags",
            )
        )

    def list(self, *, params: TagsListParams | None = None) -> TagsListResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/tags/list",
                query=params,
            )
        )

    def get(self, tag_id: int, *, params: TagsGetParams | None = None) -> TagsGetResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/tags/{tag_id}",
                query=params,
            )
        )

    def find(self, *, params: TagsFindParams) -> TagsFindResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/tags/find",
                query=params,
            )
        )


class AsyncTagsApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def popular(self) -> TagsPopularResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/tags",
            )
        )

    async def list(self, *, params: TagsListParams | None = None) -> TagsListResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/tags/list",
                query=params,
            )
        )

    async def get(self, tag_id: int, *, params: TagsGetParams | None = None) -> TagsGetResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/tags/{tag_id}",
                query=params,
            )
        )

    async def find(self, *, params: TagsFindParams) -> TagsFindResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/tags/find",
                query=params,
            )
        )
