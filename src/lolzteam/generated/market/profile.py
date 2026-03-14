# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING

from lolzteam.runtime.types import RequestOptions

if TYPE_CHECKING:
    from lolzteam.runtime.async_http_client import AsyncHttpClient
    from lolzteam.runtime.http_client import HttpClient

    from .types import (
        ProfileClaimsParams,
        ProfileClaimsResponse,
        ProfileEditBody,
        ProfileEditResponse,
        ProfileGetParams,
        ProfileGetResponse,
    )


class ProfileApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def claims(self, *, params: ProfileClaimsParams | None = None) -> ProfileClaimsResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/claims",
            query=params,
        ))

    def get(self, *, params: ProfileGetParams | None = None) -> ProfileGetResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/me",
            query=params,
        ))

    def edit(self, *, body: ProfileEditBody | None = None) -> ProfileEditResponse:
        return self._http.request(RequestOptions(
            method="PUT",
            path="/me",
            body=body,
        ))


class AsyncProfileApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def claims(self, *, params: ProfileClaimsParams | None = None) -> ProfileClaimsResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/claims",
            query=params,
        ))

    async def get(self, *, params: ProfileGetParams | None = None) -> ProfileGetResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/me",
            query=params,
        ))

    async def edit(self, *, body: ProfileEditBody | None = None) -> ProfileEditResponse:
        return await self._http.request(RequestOptions(
            method="PUT",
            path="/me",
            body=body,
        ))
