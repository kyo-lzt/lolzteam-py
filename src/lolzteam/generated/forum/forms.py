# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING

from lolzteam.runtime.types import RequestOptions

if TYPE_CHECKING:
    from lolzteam.runtime.async_http_client import AsyncHttpClient
    from lolzteam.runtime.http_client import HttpClient

    from .types import (
        FormsCreateBody,
        FormsCreateResponse,
        FormsListParams,
        FormsListResponse,
    )


class FormsApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def list(self, *, params: FormsListParams | None = None) -> FormsListResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/forms",
                query=params,
            )
        )

    def create(self, *, body: FormsCreateBody) -> FormsCreateResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/forms/save",
                body=body,
            )
        )


class AsyncFormsApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def list(self, *, params: FormsListParams | None = None) -> FormsListResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/forms",
                query=params,
            )
        )

    async def create(self, *, body: FormsCreateBody) -> FormsCreateResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/forms/save",
                body=body,
            )
        )
