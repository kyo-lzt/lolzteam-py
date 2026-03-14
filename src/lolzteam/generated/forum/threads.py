# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING

from lolzteam.runtime.types import RequestOptions

if TYPE_CHECKING:
    from lolzteam.runtime.async_http_client import AsyncHttpClient
    from lolzteam.runtime.http_client import HttpClient

    from .types import (
        ThreadsBumpResponse,
        ThreadsClaimBody,
        ThreadsClaimResponse,
        ThreadsCreateBody,
        ThreadsCreatecontestBody,
        ThreadsCreatecontestResponse,
        ThreadsCreateResponse,
        ThreadsDeleteBody,
        ThreadsDeleteResponse,
        ThreadsEditBody,
        ThreadsEditResponse,
        ThreadsFinishResponse,
        ThreadsFollowBody,
        ThreadsFollowedParams,
        ThreadsFollowedResponse,
        ThreadsFollowersResponse,
        ThreadsFollowResponse,
        ThreadsGetParams,
        ThreadsGetResponse,
        ThreadsHideResponse,
        ThreadsListParams,
        ThreadsListResponse,
        ThreadsMoveBody,
        ThreadsMoveResponse,
        ThreadsNavigationResponse,
        ThreadsPollGetResponse,
        ThreadsPollVoteBody,
        ThreadsPollVoteResponse,
        ThreadsRecentParams,
        ThreadsRecentResponse,
        ThreadsStarResponse,
        ThreadsUnfollowResponse,
        ThreadsUnreadParams,
        ThreadsUnreadResponse,
        ThreadsUnstarResponse,
    )


class ThreadsApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def list(self, *, params: ThreadsListParams | None = None) -> ThreadsListResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/threads",
                query=params,
            )
        )

    def create(self, *, body: ThreadsCreateBody) -> ThreadsCreateResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/threads",
                body=body,
            )
        )

    def createcontest(self, *, body: ThreadsCreatecontestBody) -> ThreadsCreatecontestResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/contests",
                body=body,
            )
        )

    def claim(self, *, body: ThreadsClaimBody) -> ThreadsClaimResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/claims",
                body=body,
            )
        )

    def get(self, thread_id: int, *, params: ThreadsGetParams | None = None) -> ThreadsGetResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/threads/{thread_id}",
                query=params,
            )
        )

    def edit(self, thread_id: int, *, body: ThreadsEditBody | None = None) -> ThreadsEditResponse:
        return self._http.request(
            RequestOptions(
                method="PUT",
                path=f"/threads/{thread_id}",
                body=body,
            )
        )

    def delete(
        self, thread_id: int, *, body: ThreadsDeleteBody | None = None
    ) -> ThreadsDeleteResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/threads/{thread_id}",
                body=body,
            )
        )

    def move(self, thread_id: int, *, body: ThreadsMoveBody) -> ThreadsMoveResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/threads/{thread_id}/move",
                body=body,
            )
        )

    def bump(self, thread_id: int) -> ThreadsBumpResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/threads/{thread_id}/bump",
            )
        )

    def hide(self, thread_id: int) -> ThreadsHideResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/threads/{thread_id}/hide",
            )
        )

    def star(self, thread_id: int) -> ThreadsStarResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/threads/{thread_id}/star",
            )
        )

    def unstar(self, thread_id: int) -> ThreadsUnstarResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/threads/{thread_id}/star",
            )
        )

    def followers(self, thread_id: int) -> ThreadsFollowersResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/threads/{thread_id}/followers",
            )
        )

    def follow(
        self, thread_id: int, *, body: ThreadsFollowBody | None = None
    ) -> ThreadsFollowResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/threads/{thread_id}/followers",
                body=body,
            )
        )

    def unfollow(self, thread_id: int) -> ThreadsUnfollowResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/threads/{thread_id}/followers",
            )
        )

    def followed(self, *, params: ThreadsFollowedParams | None = None) -> ThreadsFollowedResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/threads/followed",
                query=params,
            )
        )

    def navigation(self, thread_id: int) -> ThreadsNavigationResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/threads/{thread_id}/navigation",
            )
        )

    def poll_get(self, thread_id: int) -> ThreadsPollGetResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/threads/{thread_id}/poll",
            )
        )

    def poll_vote(
        self, thread_id: int, *, body: ThreadsPollVoteBody | None = None
    ) -> ThreadsPollVoteResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/threads/{thread_id}/poll/votes",
                body=body,
            )
        )

    def unread(self, *, params: ThreadsUnreadParams | None = None) -> ThreadsUnreadResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/threads/new",
                query=params,
            )
        )

    def recent(self, *, params: ThreadsRecentParams | None = None) -> ThreadsRecentResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/threads/recent",
                query=params,
            )
        )

    def finish(self, thread_id: int) -> ThreadsFinishResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/contests/{thread_id}/finish",
            )
        )


class AsyncThreadsApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def list(self, *, params: ThreadsListParams | None = None) -> ThreadsListResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/threads",
                query=params,
            )
        )

    async def create(self, *, body: ThreadsCreateBody) -> ThreadsCreateResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/threads",
                body=body,
            )
        )

    async def createcontest(
        self, *, body: ThreadsCreatecontestBody
    ) -> ThreadsCreatecontestResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/contests",
                body=body,
            )
        )

    async def claim(self, *, body: ThreadsClaimBody) -> ThreadsClaimResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/claims",
                body=body,
            )
        )

    async def get(
        self, thread_id: int, *, params: ThreadsGetParams | None = None
    ) -> ThreadsGetResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/threads/{thread_id}",
                query=params,
            )
        )

    async def edit(
        self, thread_id: int, *, body: ThreadsEditBody | None = None
    ) -> ThreadsEditResponse:
        return await self._http.request(
            RequestOptions(
                method="PUT",
                path=f"/threads/{thread_id}",
                body=body,
            )
        )

    async def delete(
        self, thread_id: int, *, body: ThreadsDeleteBody | None = None
    ) -> ThreadsDeleteResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/threads/{thread_id}",
                body=body,
            )
        )

    async def move(self, thread_id: int, *, body: ThreadsMoveBody) -> ThreadsMoveResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/threads/{thread_id}/move",
                body=body,
            )
        )

    async def bump(self, thread_id: int) -> ThreadsBumpResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/threads/{thread_id}/bump",
            )
        )

    async def hide(self, thread_id: int) -> ThreadsHideResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/threads/{thread_id}/hide",
            )
        )

    async def star(self, thread_id: int) -> ThreadsStarResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/threads/{thread_id}/star",
            )
        )

    async def unstar(self, thread_id: int) -> ThreadsUnstarResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/threads/{thread_id}/star",
            )
        )

    async def followers(self, thread_id: int) -> ThreadsFollowersResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/threads/{thread_id}/followers",
            )
        )

    async def follow(
        self, thread_id: int, *, body: ThreadsFollowBody | None = None
    ) -> ThreadsFollowResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/threads/{thread_id}/followers",
                body=body,
            )
        )

    async def unfollow(self, thread_id: int) -> ThreadsUnfollowResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/threads/{thread_id}/followers",
            )
        )

    async def followed(
        self, *, params: ThreadsFollowedParams | None = None
    ) -> ThreadsFollowedResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/threads/followed",
                query=params,
            )
        )

    async def navigation(self, thread_id: int) -> ThreadsNavigationResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/threads/{thread_id}/navigation",
            )
        )

    async def poll_get(self, thread_id: int) -> ThreadsPollGetResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/threads/{thread_id}/poll",
            )
        )

    async def poll_vote(
        self, thread_id: int, *, body: ThreadsPollVoteBody | None = None
    ) -> ThreadsPollVoteResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/threads/{thread_id}/poll/votes",
                body=body,
            )
        )

    async def unread(self, *, params: ThreadsUnreadParams | None = None) -> ThreadsUnreadResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/threads/new",
                query=params,
            )
        )

    async def recent(self, *, params: ThreadsRecentParams | None = None) -> ThreadsRecentResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/threads/recent",
                query=params,
            )
        )

    async def finish(self, thread_id: int) -> ThreadsFinishResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/contests/{thread_id}/finish",
            )
        )
