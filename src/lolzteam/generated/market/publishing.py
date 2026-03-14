# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING

from lolzteam.runtime.types import RequestOptions

if TYPE_CHECKING:
    from lolzteam.runtime.async_http_client import AsyncHttpClient
    from lolzteam.runtime.http_client import HttpClient

    from .types import (
        PublishingAddBody,
        PublishingAddResponse,
        PublishingCheckBody,
        PublishingCheckResponse,
        PublishingExternalBody,
        PublishingExternalResponse,
        PublishingFastsellBody,
        PublishingFastsellResponse,
    )


class PublishingApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def fastsell(self, *, body: PublishingFastsellBody) -> PublishingFastsellResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path="/item/fast-sell",
            body=body,
        ))

    def add(self, *, body: PublishingAddBody) -> PublishingAddResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path="/item/add",
            body=body,
        ))

    def check(self, item_id: int, *, body: PublishingCheckBody | None = None) -> PublishingCheckResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/goods/check",
            body=body,
        ))

    def external(self, item_id: int, *, body: PublishingExternalBody) -> PublishingExternalResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/external-account",
            body=body,
        ))


class AsyncPublishingApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def fastsell(self, *, body: PublishingFastsellBody) -> PublishingFastsellResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path="/item/fast-sell",
            body=body,
        ))

    async def add(self, *, body: PublishingAddBody) -> PublishingAddResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path="/item/add",
            body=body,
        ))

    async def check(self, item_id: int, *, body: PublishingCheckBody | None = None) -> PublishingCheckResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/goods/check",
            body=body,
        ))

    async def external(self, item_id: int, *, body: PublishingExternalBody) -> PublishingExternalResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/external-account",
            body=body,
        ))
