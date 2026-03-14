# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from lolzteam.runtime.types import RequestOptions

if TYPE_CHECKING:
    from lolzteam.runtime.async_http_client import AsyncHttpClient
    from lolzteam.runtime.http_client import HttpClient

    from .types import (
        ListDownloadParams,
        ListDownloadResponse,
        ListFavoritesParams,
        ListFavoritesResponse,
        ListOrdersParams,
        ListOrdersResponse,
        ListStatesParams,
        ListStatesResponse,
        ListUserParams,
        ListUserResponse,
        ListViewedParams,
        ListViewedResponse,
    )


class ListApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def user(self, *, params: ListUserParams | None = None) -> ListUserResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/user/items",
                query=params,
            )
        )

    def orders(self, *, params: ListOrdersParams | None = None) -> ListOrdersResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/user/orders",
                query=params,
            )
        )

    def states(self, *, params: ListStatesParams | None = None) -> ListStatesResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/user/item-states",
                query=params,
            )
        )

    def download(
        self, type: Literal["items", "orders"], *, params: ListDownloadParams | None = None
    ) -> ListDownloadResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/user/{type}/download",
                query=params,
            )
        )

    def favorites(self, *, params: ListFavoritesParams | None = None) -> ListFavoritesResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/fave",
                query=params,
            )
        )

    def viewed(self, *, params: ListViewedParams | None = None) -> ListViewedResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/viewed",
                query=params,
            )
        )


class AsyncListApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def user(self, *, params: ListUserParams | None = None) -> ListUserResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/user/items",
                query=params,
            )
        )

    async def orders(self, *, params: ListOrdersParams | None = None) -> ListOrdersResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/user/orders",
                query=params,
            )
        )

    async def states(self, *, params: ListStatesParams | None = None) -> ListStatesResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/user/item-states",
                query=params,
            )
        )

    async def download(
        self, type: Literal["items", "orders"], *, params: ListDownloadParams | None = None
    ) -> ListDownloadResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/user/{type}/download",
                query=params,
            )
        )

    async def favorites(
        self, *, params: ListFavoritesParams | None = None
    ) -> ListFavoritesResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/fave",
                query=params,
            )
        )

    async def viewed(self, *, params: ListViewedParams | None = None) -> ListViewedResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/viewed",
                query=params,
            )
        )
