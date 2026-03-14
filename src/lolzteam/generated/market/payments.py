# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING

from lolzteam.runtime.types import RequestOptions

if TYPE_CHECKING:
    from lolzteam.runtime.async_http_client import AsyncHttpClient
    from lolzteam.runtime.http_client import HttpClient

    from .types import (
        PaymentsBalanceListResponse,
        PaymentsBalanceexchangeBody,
        PaymentsBalanceexchangeResponse,
        PaymentsCancelBody,
        PaymentsCancelResponse,
        PaymentsCurrencyResponse,
        PaymentsFeeParams,
        PaymentsFeeResponse,
        PaymentsHistoryParams,
        PaymentsHistoryResponse,
        PaymentsInvoiceCreateBody,
        PaymentsInvoiceCreateResponse,
        PaymentsInvoiceGetParams,
        PaymentsInvoiceGetResponse,
        PaymentsInvoiceListParams,
        PaymentsInvoiceListResponse,
        PaymentsPayoutBody,
        PaymentsPayoutResponse,
        PaymentsPayoutservicesResponse,
        PaymentsTransferBody,
        PaymentsTransferResponse,
    )


class PaymentsApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def invoice_get(self, *, params: PaymentsInvoiceGetParams | None = None) -> PaymentsInvoiceGetResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/invoice",
            query=params,
        ))

    def invoice_create(self, *, body: PaymentsInvoiceCreateBody) -> PaymentsInvoiceCreateResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path="/invoice",
            body=body,
        ))

    def invoice_list(self, *, params: PaymentsInvoiceListParams | None = None) -> PaymentsInvoiceListResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/invoice/list",
            query=params,
        ))

    def currency(self) -> PaymentsCurrencyResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/currency",
        ))

    def balance_list(self) -> PaymentsBalanceListResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/balance/exchange",
        ))

    def balanceexchange(self, *, body: PaymentsBalanceexchangeBody) -> PaymentsBalanceexchangeResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path="/balance/exchange",
            body=body,
        ))

    def transfer(self, *, body: PaymentsTransferBody) -> PaymentsTransferResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path="/balance/transfer",
            body=body,
        ))

    def fee(self, *, params: PaymentsFeeParams | None = None) -> PaymentsFeeResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/balance/transfer/fee",
            query=params,
        ))

    def cancel(self, *, body: PaymentsCancelBody) -> PaymentsCancelResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path="/balance/transfer/cancel",
            body=body,
        ))

    def history(self, *, params: PaymentsHistoryParams | None = None) -> PaymentsHistoryResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/user/payments",
            query=params,
        ))

    def payoutservices(self) -> PaymentsPayoutservicesResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/balance/payout/services",
        ))

    def payout(self, *, body: PaymentsPayoutBody) -> PaymentsPayoutResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path="/balance/payout",
            body=body,
        ))


class AsyncPaymentsApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def invoice_get(self, *, params: PaymentsInvoiceGetParams | None = None) -> PaymentsInvoiceGetResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/invoice",
            query=params,
        ))

    async def invoice_create(self, *, body: PaymentsInvoiceCreateBody) -> PaymentsInvoiceCreateResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path="/invoice",
            body=body,
        ))

    async def invoice_list(self, *, params: PaymentsInvoiceListParams | None = None) -> PaymentsInvoiceListResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/invoice/list",
            query=params,
        ))

    async def currency(self) -> PaymentsCurrencyResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/currency",
        ))

    async def balance_list(self) -> PaymentsBalanceListResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/balance/exchange",
        ))

    async def balanceexchange(self, *, body: PaymentsBalanceexchangeBody) -> PaymentsBalanceexchangeResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path="/balance/exchange",
            body=body,
        ))

    async def transfer(self, *, body: PaymentsTransferBody) -> PaymentsTransferResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path="/balance/transfer",
            body=body,
        ))

    async def fee(self, *, params: PaymentsFeeParams | None = None) -> PaymentsFeeResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/balance/transfer/fee",
            query=params,
        ))

    async def cancel(self, *, body: PaymentsCancelBody) -> PaymentsCancelResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path="/balance/transfer/cancel",
            body=body,
        ))

    async def history(self, *, params: PaymentsHistoryParams | None = None) -> PaymentsHistoryResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/user/payments",
            query=params,
        ))

    async def payoutservices(self) -> PaymentsPayoutservicesResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/balance/payout/services",
        ))

    async def payout(self, *, body: PaymentsPayoutBody) -> PaymentsPayoutResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path="/balance/payout",
            body=body,
        ))
