# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING

from lolzteam.runtime.types import RequestOptions

if TYPE_CHECKING:
    from lolzteam.runtime.async_http_client import AsyncHttpClient
    from lolzteam.runtime.http_client import HttpClient

    from .types import (
        NotificationsGetResponse,
        NotificationsListParams,
        NotificationsListResponse,
        NotificationsReadBody,
        NotificationsReadResponse,
    )


class NotificationsApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def list(self, *, params: NotificationsListParams | None = None) -> NotificationsListResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/notifications",
                query=params,
            )
        )

    def get(self, notification_id: int) -> NotificationsGetResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/notifications/{notification_id}/content",
            )
        )

    def read(self, *, body: NotificationsReadBody | None = None) -> NotificationsReadResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/notifications/read",
                body=body,
            )
        )


class AsyncNotificationsApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def list(
        self, *, params: NotificationsListParams | None = None
    ) -> NotificationsListResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/notifications",
                query=params,
            )
        )

    async def get(self, notification_id: int) -> NotificationsGetResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/notifications/{notification_id}/content",
            )
        )

    async def read(self, *, body: NotificationsReadBody | None = None) -> NotificationsReadResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/notifications/read",
                body=body,
            )
        )
