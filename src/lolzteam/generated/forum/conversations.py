# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING

from lolzteam.runtime.types import RequestOptions

if TYPE_CHECKING:
    from lolzteam.runtime.async_http_client import AsyncHttpClient
    from lolzteam.runtime.http_client import HttpClient

    from .types import (
        ConversationsAlertsDisableResponse,
        ConversationsAlertsEnableResponse,
        ConversationsCreateBody,
        ConversationsCreateResponse,
        ConversationsDeleteBody,
        ConversationsDeleteResponse,
        ConversationsGetResponse,
        ConversationsInviteBody,
        ConversationsInviteResponse,
        ConversationsKickBody,
        ConversationsKickResponse,
        ConversationsListParams,
        ConversationsListResponse,
        ConversationsMessagesCreateBody,
        ConversationsMessagesCreateResponse,
        ConversationsMessagesDeleteResponse,
        ConversationsMessagesEditBody,
        ConversationsMessagesEditResponse,
        ConversationsMessagesGetResponse,
        ConversationsMessagesListParams,
        ConversationsMessagesListResponse,
        ConversationsMessagesStickResponse,
        ConversationsMessagesUnstickResponse,
        ConversationsReadResponse,
        ConversationsReadallResponse,
        ConversationsSaveBody,
        ConversationsSaveResponse,
        ConversationsSearchBody,
        ConversationsSearchResponse,
        ConversationsStarResponse,
        ConversationsStartBody,
        ConversationsStartResponse,
        ConversationsUnstarResponse,
        ConversationsUpdateBody,
        ConversationsUpdateResponse,
    )


class ConversationsApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def list(self, *, params: ConversationsListParams | None = None) -> ConversationsListResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/conversations",
            query=params,
        ))

    def create(self, *, body: ConversationsCreateBody | None = None) -> ConversationsCreateResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path="/conversations",
            body=body,
        ))

    def update(self, *, body: ConversationsUpdateBody) -> ConversationsUpdateResponse:
        return self._http.request(RequestOptions(
            method="PUT",
            path="/conversations",
            body=body,
        ))

    def delete(self, *, body: ConversationsDeleteBody) -> ConversationsDeleteResponse:
        return self._http.request(RequestOptions(
            method="DELETE",
            path="/conversations",
            body=body,
        ))

    def start(self, *, body: ConversationsStartBody) -> ConversationsStartResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path="/conversations/start",
            body=body,
        ))

    def save(self, *, body: ConversationsSaveBody) -> ConversationsSaveResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path="/conversations/save",
            body=body,
        ))

    def get(self, conversation_id: int) -> ConversationsGetResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path=f"/conversations/{conversation_id}",
        ))

    def messages_list(self, conversation_id: int, *, params: ConversationsMessagesListParams | None = None) -> ConversationsMessagesListResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path=f"/conversations/{conversation_id}/messages",
            query=params,
        ))

    def messages_create(self, conversation_id: int, *, body: ConversationsMessagesCreateBody) -> ConversationsMessagesCreateResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path=f"/conversations/{conversation_id}/messages",
            body=body,
        ))

    def search(self, *, body: ConversationsSearchBody | None = None) -> ConversationsSearchResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path="/conversations/search",
            body=body,
        ))

    def messages_get(self, message_id: int) -> ConversationsMessagesGetResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path=f"/conversations/messages/{message_id}",
        ))

    def messages_edit(self, conversation_id: int, message_id: int, *, body: ConversationsMessagesEditBody) -> ConversationsMessagesEditResponse:
        return self._http.request(RequestOptions(
            method="PUT",
            path=f"/conversations/{conversation_id}/messages/{message_id}",
            body=body,
        ))

    def messages_delete(self, conversation_id: int, message_id: int) -> ConversationsMessagesDeleteResponse:
        return self._http.request(RequestOptions(
            method="DELETE",
            path=f"/conversations/{conversation_id}/messages/{message_id}",
        ))

    def invite(self, conversation_id: int, *, body: ConversationsInviteBody) -> ConversationsInviteResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path=f"/conversations/{conversation_id}/invite",
            body=body,
        ))

    def kick(self, conversation_id: int, *, body: ConversationsKickBody) -> ConversationsKickResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path=f"/conversations/{conversation_id}/kick",
            body=body,
        ))

    def read(self, conversation_id: int) -> ConversationsReadResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path=f"/conversations/{conversation_id}/read",
        ))

    def readall(self) -> ConversationsReadallResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path="/conversations/read-all",
        ))

    def messages_stick(self, conversation_id: int, message_id: int) -> ConversationsMessagesStickResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path=f"/conversations/{conversation_id}/messages/{message_id}/stick",
        ))

    def messages_unstick(self, conversation_id: int, message_id: int) -> ConversationsMessagesUnstickResponse:
        return self._http.request(RequestOptions(
            method="DELETE",
            path=f"/conversations/{conversation_id}/messages/{message_id}/stick",
        ))

    def star(self, conversation_id: int) -> ConversationsStarResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path=f"/conversations/{conversation_id}/star",
        ))

    def unstar(self, conversation_id: int) -> ConversationsUnstarResponse:
        return self._http.request(RequestOptions(
            method="DELETE",
            path=f"/conversations/{conversation_id}/star",
        ))

    def alerts_enable(self, conversation_id: int) -> ConversationsAlertsEnableResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path=f"/conversations/{conversation_id}/alerts",
        ))

    def alerts_disable(self, conversation_id: int) -> ConversationsAlertsDisableResponse:
        return self._http.request(RequestOptions(
            method="DELETE",
            path=f"/conversations/{conversation_id}/alerts",
        ))


class AsyncConversationsApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def list(self, *, params: ConversationsListParams | None = None) -> ConversationsListResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/conversations",
            query=params,
        ))

    async def create(self, *, body: ConversationsCreateBody | None = None) -> ConversationsCreateResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path="/conversations",
            body=body,
        ))

    async def update(self, *, body: ConversationsUpdateBody) -> ConversationsUpdateResponse:
        return await self._http.request(RequestOptions(
            method="PUT",
            path="/conversations",
            body=body,
        ))

    async def delete(self, *, body: ConversationsDeleteBody) -> ConversationsDeleteResponse:
        return await self._http.request(RequestOptions(
            method="DELETE",
            path="/conversations",
            body=body,
        ))

    async def start(self, *, body: ConversationsStartBody) -> ConversationsStartResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path="/conversations/start",
            body=body,
        ))

    async def save(self, *, body: ConversationsSaveBody) -> ConversationsSaveResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path="/conversations/save",
            body=body,
        ))

    async def get(self, conversation_id: int) -> ConversationsGetResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path=f"/conversations/{conversation_id}",
        ))

    async def messages_list(self, conversation_id: int, *, params: ConversationsMessagesListParams | None = None) -> ConversationsMessagesListResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path=f"/conversations/{conversation_id}/messages",
            query=params,
        ))

    async def messages_create(self, conversation_id: int, *, body: ConversationsMessagesCreateBody) -> ConversationsMessagesCreateResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path=f"/conversations/{conversation_id}/messages",
            body=body,
        ))

    async def search(self, *, body: ConversationsSearchBody | None = None) -> ConversationsSearchResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path="/conversations/search",
            body=body,
        ))

    async def messages_get(self, message_id: int) -> ConversationsMessagesGetResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path=f"/conversations/messages/{message_id}",
        ))

    async def messages_edit(self, conversation_id: int, message_id: int, *, body: ConversationsMessagesEditBody) -> ConversationsMessagesEditResponse:
        return await self._http.request(RequestOptions(
            method="PUT",
            path=f"/conversations/{conversation_id}/messages/{message_id}",
            body=body,
        ))

    async def messages_delete(self, conversation_id: int, message_id: int) -> ConversationsMessagesDeleteResponse:
        return await self._http.request(RequestOptions(
            method="DELETE",
            path=f"/conversations/{conversation_id}/messages/{message_id}",
        ))

    async def invite(self, conversation_id: int, *, body: ConversationsInviteBody) -> ConversationsInviteResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path=f"/conversations/{conversation_id}/invite",
            body=body,
        ))

    async def kick(self, conversation_id: int, *, body: ConversationsKickBody) -> ConversationsKickResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path=f"/conversations/{conversation_id}/kick",
            body=body,
        ))

    async def read(self, conversation_id: int) -> ConversationsReadResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path=f"/conversations/{conversation_id}/read",
        ))

    async def readall(self) -> ConversationsReadallResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path="/conversations/read-all",
        ))

    async def messages_stick(self, conversation_id: int, message_id: int) -> ConversationsMessagesStickResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path=f"/conversations/{conversation_id}/messages/{message_id}/stick",
        ))

    async def messages_unstick(self, conversation_id: int, message_id: int) -> ConversationsMessagesUnstickResponse:
        return await self._http.request(RequestOptions(
            method="DELETE",
            path=f"/conversations/{conversation_id}/messages/{message_id}/stick",
        ))

    async def star(self, conversation_id: int) -> ConversationsStarResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path=f"/conversations/{conversation_id}/star",
        ))

    async def unstar(self, conversation_id: int) -> ConversationsUnstarResponse:
        return await self._http.request(RequestOptions(
            method="DELETE",
            path=f"/conversations/{conversation_id}/star",
        ))

    async def alerts_enable(self, conversation_id: int) -> ConversationsAlertsEnableResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path=f"/conversations/{conversation_id}/alerts",
        ))

    async def alerts_disable(self, conversation_id: int) -> ConversationsAlertsDisableResponse:
        return await self._http.request(RequestOptions(
            method="DELETE",
            path=f"/conversations/{conversation_id}/alerts",
        ))
