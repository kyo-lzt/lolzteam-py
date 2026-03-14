# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING

from lolzteam.runtime.types import RequestOptions

if TYPE_CHECKING:
    from lolzteam.runtime.async_http_client import AsyncHttpClient
    from lolzteam.runtime.http_client import HttpClient

    from .types import (
        PurchasingCheckResponse,
        PurchasingConfirmBody,
        PurchasingConfirmResponse,
        PurchasingDiscountcancelResponse,
        PurchasingDiscountrequestBody,
        PurchasingDiscountrequestResponse,
        PurchasingFastbuyBody,
        PurchasingFastbuyResponse,
    )


class PurchasingApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def fastbuy(
        self, item_id: int, *, body: PurchasingFastbuyBody | None = None
    ) -> PurchasingFastbuyResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/fast-buy",
                body=body,
            )
        )

    def check(self, item_id: int) -> PurchasingCheckResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/check-account",
            )
        )

    def confirm(
        self, item_id: int, *, body: PurchasingConfirmBody | None = None
    ) -> PurchasingConfirmResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/confirm-buy",
                body=body,
            )
        )

    def discountrequest(
        self, item_id: int, *, body: PurchasingDiscountrequestBody
    ) -> PurchasingDiscountrequestResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/discount",
                body=body,
            )
        )

    def discountcancel(self, item_id: int) -> PurchasingDiscountcancelResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/{item_id}/discount",
            )
        )


class AsyncPurchasingApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def fastbuy(
        self, item_id: int, *, body: PurchasingFastbuyBody | None = None
    ) -> PurchasingFastbuyResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/fast-buy",
                body=body,
            )
        )

    async def check(self, item_id: int) -> PurchasingCheckResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/check-account",
            )
        )

    async def confirm(
        self, item_id: int, *, body: PurchasingConfirmBody | None = None
    ) -> PurchasingConfirmResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/confirm-buy",
                body=body,
            )
        )

    async def discountrequest(
        self, item_id: int, *, body: PurchasingDiscountrequestBody
    ) -> PurchasingDiscountrequestResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/discount",
                body=body,
            )
        )

    async def discountcancel(self, item_id: int) -> PurchasingDiscountcancelResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/{item_id}/discount",
            )
        )
