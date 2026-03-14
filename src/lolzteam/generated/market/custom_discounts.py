# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING

from lolzteam.runtime.types import RequestOptions

if TYPE_CHECKING:
    from lolzteam.runtime.async_http_client import AsyncHttpClient
    from lolzteam.runtime.http_client import HttpClient

    from .types import (
        CustomDiscountsCreateBody,
        CustomDiscountsCreateResponse,
        CustomDiscountsDeleteBody,
        CustomDiscountsDeleteResponse,
        CustomDiscountsEditBody,
        CustomDiscountsEditResponse,
        CustomDiscountsGetResponse,
    )


class CustomDiscountsApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def get(self) -> CustomDiscountsGetResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/custom-discounts",
            )
        )

    def create(self, *, body: CustomDiscountsCreateBody) -> CustomDiscountsCreateResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/custom-discounts",
                body=body,
            )
        )

    def edit(self, *, body: CustomDiscountsEditBody) -> CustomDiscountsEditResponse:
        return self._http.request(
            RequestOptions(
                method="PUT",
                path="/custom-discounts",
                body=body,
            )
        )

    def delete(self, *, body: CustomDiscountsDeleteBody) -> CustomDiscountsDeleteResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path="/custom-discounts",
                body=body,
            )
        )


class AsyncCustomDiscountsApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def get(self) -> CustomDiscountsGetResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/custom-discounts",
            )
        )

    async def create(self, *, body: CustomDiscountsCreateBody) -> CustomDiscountsCreateResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/custom-discounts",
                body=body,
            )
        )

    async def edit(self, *, body: CustomDiscountsEditBody) -> CustomDiscountsEditResponse:
        return await self._http.request(
            RequestOptions(
                method="PUT",
                path="/custom-discounts",
                body=body,
            )
        )

    async def delete(self, *, body: CustomDiscountsDeleteBody) -> CustomDiscountsDeleteResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path="/custom-discounts",
                body=body,
            )
        )
