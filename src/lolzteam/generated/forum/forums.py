# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING

from lolzteam.runtime.types import RequestOptions

if TYPE_CHECKING:
    from lolzteam.runtime.async_http_client import AsyncHttpClient
    from lolzteam.runtime.http_client import HttpClient

    from .types import (
        ForumsEditfeedoptionsBody,
        ForumsEditfeedoptionsResponse,
        ForumsFollowBody,
        ForumsFollowedParams,
        ForumsFollowedResponse,
        ForumsFollowersResponse,
        ForumsFollowResponse,
        ForumsGetfeedoptionsResponse,
        ForumsGetResponse,
        ForumsGroupedResponse,
        ForumsListParams,
        ForumsListResponse,
        ForumsUnfollowResponse,
    )


class ForumsApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def list(self, *, params: ForumsListParams | None = None) -> ForumsListResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/forums",
                query=params,
            )
        )

    def grouped(self) -> ForumsGroupedResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/forums/grouped",
            )
        )

    def get(self, forum_id: int) -> ForumsGetResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/forums/{forum_id}",
            )
        )

    def followers(self, forum_id: int) -> ForumsFollowersResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/forums/{forum_id}/followers",
            )
        )

    def follow(
        self, forum_id: int, *, body: ForumsFollowBody | None = None
    ) -> ForumsFollowResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/forums/{forum_id}/followers",
                body=body,
            )
        )

    def unfollow(self, forum_id: int) -> ForumsUnfollowResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/forums/{forum_id}/followers",
            )
        )

    def followed(self, *, params: ForumsFollowedParams | None = None) -> ForumsFollowedResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/forums/followed",
                query=params,
            )
        )

    def getfeedoptions(self) -> ForumsGetfeedoptionsResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/forums/feed/options",
            )
        )

    def editfeedoptions(
        self, *, body: ForumsEditfeedoptionsBody | None = None
    ) -> ForumsEditfeedoptionsResponse:
        return self._http.request(
            RequestOptions(
                method="PUT",
                path="/forums/feed/options",
                body=body,
            )
        )


class AsyncForumsApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def list(self, *, params: ForumsListParams | None = None) -> ForumsListResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/forums",
                query=params,
            )
        )

    async def grouped(self) -> ForumsGroupedResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/forums/grouped",
            )
        )

    async def get(self, forum_id: int) -> ForumsGetResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/forums/{forum_id}",
            )
        )

    async def followers(self, forum_id: int) -> ForumsFollowersResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/forums/{forum_id}/followers",
            )
        )

    async def follow(
        self, forum_id: int, *, body: ForumsFollowBody | None = None
    ) -> ForumsFollowResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/forums/{forum_id}/followers",
                body=body,
            )
        )

    async def unfollow(self, forum_id: int) -> ForumsUnfollowResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/forums/{forum_id}/followers",
            )
        )

    async def followed(
        self, *, params: ForumsFollowedParams | None = None
    ) -> ForumsFollowedResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/forums/followed",
                query=params,
            )
        )

    async def getfeedoptions(self) -> ForumsGetfeedoptionsResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/forums/feed/options",
            )
        )

    async def editfeedoptions(
        self, *, body: ForumsEditfeedoptionsBody | None = None
    ) -> ForumsEditfeedoptionsResponse:
        return await self._http.request(
            RequestOptions(
                method="PUT",
                path="/forums/feed/options",
                body=body,
            )
        )
