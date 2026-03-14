# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING

from lolzteam.runtime.types import RequestOptions

if TYPE_CHECKING:
    from lolzteam.runtime.async_http_client import AsyncHttpClient
    from lolzteam.runtime.http_client import HttpClient

    from .types import (
        AutoPaymentsCreateBody,
        AutoPaymentsCreateResponse,
        AutoPaymentsDeleteBody,
        AutoPaymentsDeleteResponse,
        AutoPaymentsListResponse,
    )


class AutoPaymentsApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def list(self) -> AutoPaymentsListResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/auto-payments",
            )
        )

    def create(self, *, body: AutoPaymentsCreateBody) -> AutoPaymentsCreateResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/auto-payment",
                body=body,
            )
        )

    def delete(self, *, body: AutoPaymentsDeleteBody) -> AutoPaymentsDeleteResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path="/auto-payment",
                body=body,
            )
        )


class AsyncAutoPaymentsApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def list(self) -> AutoPaymentsListResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/auto-payments",
            )
        )

    async def create(self, *, body: AutoPaymentsCreateBody) -> AutoPaymentsCreateResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/auto-payment",
                body=body,
            )
        )

    async def delete(self, *, body: AutoPaymentsDeleteBody) -> AutoPaymentsDeleteResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path="/auto-payment",
                body=body,
            )
        )
