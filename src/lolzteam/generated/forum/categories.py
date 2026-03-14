# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING

from lolzteam.runtime.types import RequestOptions

if TYPE_CHECKING:
    from lolzteam.runtime.async_http_client import AsyncHttpClient
    from lolzteam.runtime.http_client import HttpClient

    from .types import (
        CategoriesGetResponse,
        CategoriesListParams,
        CategoriesListResponse,
    )


class CategoriesApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def list(self, *, params: CategoriesListParams | None = None) -> CategoriesListResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/categories",
            query=params,
        ))

    def get(self, category_id: int) -> CategoriesGetResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path=f"/categories/{category_id}",
        ))


class AsyncCategoriesApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def list(self, *, params: CategoriesListParams | None = None) -> CategoriesListResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/categories",
            query=params,
        ))

    async def get(self, category_id: int) -> CategoriesGetResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path=f"/categories/{category_id}",
        ))
