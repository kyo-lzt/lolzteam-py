# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING

from lolzteam.runtime.types import RequestOptions

if TYPE_CHECKING:
    from lolzteam.runtime.async_http_client import AsyncHttpClient
    from lolzteam.runtime.http_client import HttpClient

    from .types import (
        ChatboxDeleteignoreBody,
        ChatboxDeleteignoreResponse,
        ChatboxDeletemessageBody,
        ChatboxDeletemessageResponse,
        ChatboxEditmessageBody,
        ChatboxEditmessageResponse,
        ChatboxGetignoreResponse,
        ChatboxGetleaderboardParams,
        ChatboxGetleaderboardResponse,
        ChatboxGetmessagesParams,
        ChatboxGetmessagesResponse,
        ChatboxIndexParams,
        ChatboxIndexResponse,
        ChatboxOnlineParams,
        ChatboxOnlineResponse,
        ChatboxPostignoreBody,
        ChatboxPostignoreResponse,
        ChatboxPostmessageBody,
        ChatboxPostmessageResponse,
        ChatboxReportBody,
        ChatboxReportResponse,
        ChatboxReportreasonsParams,
        ChatboxReportreasonsResponse,
    )


class ChatboxApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def index(self, *, params: ChatboxIndexParams | None = None) -> ChatboxIndexResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/chatbox",
            query=params,
        ))

    def getmessages(self, *, params: ChatboxGetmessagesParams) -> ChatboxGetmessagesResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/chatbox/messages",
            query=params,
        ))

    def postmessage(self, *, body: ChatboxPostmessageBody) -> ChatboxPostmessageResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path="/chatbox/messages",
            body=body,
        ))

    def editmessage(self, *, body: ChatboxEditmessageBody) -> ChatboxEditmessageResponse:
        return self._http.request(RequestOptions(
            method="PUT",
            path="/chatbox/messages",
            body=body,
        ))

    def deletemessage(self, *, body: ChatboxDeletemessageBody) -> ChatboxDeletemessageResponse:
        return self._http.request(RequestOptions(
            method="DELETE",
            path="/chatbox/messages",
            body=body,
        ))

    def online(self, *, params: ChatboxOnlineParams) -> ChatboxOnlineResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/chatbox/messages/online",
            query=params,
        ))

    def reportreasons(self, *, params: ChatboxReportreasonsParams) -> ChatboxReportreasonsResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/chatbox/messages/report",
            query=params,
        ))

    def report(self, *, body: ChatboxReportBody) -> ChatboxReportResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path="/chatbox/messages/report",
            body=body,
        ))

    def getleaderboard(self, *, params: ChatboxGetleaderboardParams | None = None) -> ChatboxGetleaderboardResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/chatbox/messages/leaderboard",
            query=params,
        ))

    def getignore(self) -> ChatboxGetignoreResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/chatbox/ignore",
        ))

    def postignore(self, *, body: ChatboxPostignoreBody) -> ChatboxPostignoreResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path="/chatbox/ignore",
            body=body,
        ))

    def deleteignore(self, *, body: ChatboxDeleteignoreBody) -> ChatboxDeleteignoreResponse:
        return self._http.request(RequestOptions(
            method="DELETE",
            path="/chatbox/ignore",
            body=body,
        ))


class AsyncChatboxApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def index(self, *, params: ChatboxIndexParams | None = None) -> ChatboxIndexResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/chatbox",
            query=params,
        ))

    async def getmessages(self, *, params: ChatboxGetmessagesParams) -> ChatboxGetmessagesResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/chatbox/messages",
            query=params,
        ))

    async def postmessage(self, *, body: ChatboxPostmessageBody) -> ChatboxPostmessageResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path="/chatbox/messages",
            body=body,
        ))

    async def editmessage(self, *, body: ChatboxEditmessageBody) -> ChatboxEditmessageResponse:
        return await self._http.request(RequestOptions(
            method="PUT",
            path="/chatbox/messages",
            body=body,
        ))

    async def deletemessage(self, *, body: ChatboxDeletemessageBody) -> ChatboxDeletemessageResponse:
        return await self._http.request(RequestOptions(
            method="DELETE",
            path="/chatbox/messages",
            body=body,
        ))

    async def online(self, *, params: ChatboxOnlineParams) -> ChatboxOnlineResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/chatbox/messages/online",
            query=params,
        ))

    async def reportreasons(self, *, params: ChatboxReportreasonsParams) -> ChatboxReportreasonsResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/chatbox/messages/report",
            query=params,
        ))

    async def report(self, *, body: ChatboxReportBody) -> ChatboxReportResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path="/chatbox/messages/report",
            body=body,
        ))

    async def getleaderboard(self, *, params: ChatboxGetleaderboardParams | None = None) -> ChatboxGetleaderboardResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/chatbox/messages/leaderboard",
            query=params,
        ))

    async def getignore(self) -> ChatboxGetignoreResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/chatbox/ignore",
        ))

    async def postignore(self, *, body: ChatboxPostignoreBody) -> ChatboxPostignoreResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path="/chatbox/ignore",
            body=body,
        ))

    async def deleteignore(self, *, body: ChatboxDeleteignoreBody) -> ChatboxDeleteignoreResponse:
        return await self._http.request(RequestOptions(
            method="DELETE",
            path="/chatbox/ignore",
            body=body,
        ))
