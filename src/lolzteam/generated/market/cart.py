# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING

from lolzteam.runtime.types import RequestOptions

if TYPE_CHECKING:
    from lolzteam.runtime.async_http_client import AsyncHttpClient
    from lolzteam.runtime.http_client import HttpClient

    from .types import (
        CartAddBody,
        CartAddResponse,
        CartDeleteBody,
        CartDeleteResponse,
        CartGetParams,
        CartGetResponse,
    )


class CartApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def get(self, *, params: CartGetParams | None = None) -> CartGetResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/cart",
            query=params,
        ))

    def add(self, *, body: CartAddBody) -> CartAddResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path="/cart",
            body=body,
        ))

    def delete(self, *, body: CartDeleteBody | None = None) -> CartDeleteResponse:
        return self._http.request(RequestOptions(
            method="DELETE",
            path="/cart",
            body=body,
        ))


class AsyncCartApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def get(self, *, params: CartGetParams | None = None) -> CartGetResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/cart",
            query=params,
        ))

    async def add(self, *, body: CartAddBody) -> CartAddResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path="/cart",
            body=body,
        ))

    async def delete(self, *, body: CartDeleteBody | None = None) -> CartDeleteResponse:
        return await self._http.request(RequestOptions(
            method="DELETE",
            path="/cart",
            body=body,
        ))
