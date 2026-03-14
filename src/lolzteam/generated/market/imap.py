# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING

from lolzteam.runtime.types import RequestOptions

if TYPE_CHECKING:
    from lolzteam.runtime.async_http_client import AsyncHttpClient
    from lolzteam.runtime.http_client import HttpClient

    from .types import (
        ImapCreateBody,
        ImapCreateResponse,
        ImapDeleteBody,
        ImapDeleteResponse,
    )


class ImapApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def create(self, *, body: ImapCreateBody) -> ImapCreateResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path="/imap",
            body=body,
        ))

    def delete(self, *, body: ImapDeleteBody) -> ImapDeleteResponse:
        return self._http.request(RequestOptions(
            method="DELETE",
            path="/imap",
            body=body,
        ))


class AsyncImapApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def create(self, *, body: ImapCreateBody) -> ImapCreateResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path="/imap",
            body=body,
        ))

    async def delete(self, *, body: ImapDeleteBody) -> ImapDeleteResponse:
        return await self._http.request(RequestOptions(
            method="DELETE",
            path="/imap",
            body=body,
        ))
