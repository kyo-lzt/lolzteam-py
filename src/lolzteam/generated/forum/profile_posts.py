# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING

from lolzteam.runtime.types import RequestOptions

if TYPE_CHECKING:
    from lolzteam.runtime.async_http_client import AsyncHttpClient
    from lolzteam.runtime.http_client import HttpClient

    from .types import (
        ProfilePostsCommentsCreateBody,
        ProfilePostsCommentsCreateResponse,
        ProfilePostsCommentsDeleteBody,
        ProfilePostsCommentsDeleteResponse,
        ProfilePostsCommentsEditBody,
        ProfilePostsCommentsEditResponse,
        ProfilePostsCommentsGetResponse,
        ProfilePostsCommentsListParams,
        ProfilePostsCommentsListResponse,
        ProfilePostsCommentsReportBody,
        ProfilePostsCommentsReportResponse,
        ProfilePostsCreateBody,
        ProfilePostsCreateResponse,
        ProfilePostsDeleteParams,
        ProfilePostsDeleteResponse,
        ProfilePostsEditBody,
        ProfilePostsEditResponse,
        ProfilePostsGetResponse,
        ProfilePostsLikeResponse,
        ProfilePostsLikesResponse,
        ProfilePostsListParams,
        ProfilePostsListResponse,
        ProfilePostsReportBody,
        ProfilePostsReportreasonsResponse,
        ProfilePostsReportResponse,
        ProfilePostsStickResponse,
        ProfilePostsUnlikeResponse,
        ProfilePostsUnstickResponse,
    )


class ProfilePostsApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def list(
        self, user_id: str | int, *, params: ProfilePostsListParams | None = None
    ) -> ProfilePostsListResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}/profile-posts",
                query=params,
            )
        )

    def get(self, profile_post_id: int) -> ProfilePostsGetResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/profile-posts/{profile_post_id}",
            )
        )

    def edit(
        self, profile_post_id: int, *, body: ProfilePostsEditBody | None = None
    ) -> ProfilePostsEditResponse:
        return self._http.request(
            RequestOptions(
                method="PUT",
                path=f"/profile-posts/{profile_post_id}",
                body=body,
            )
        )

    def delete(
        self, profile_post_id: int, *, params: ProfilePostsDeleteParams | None = None
    ) -> ProfilePostsDeleteResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/profile-posts/{profile_post_id}",
                query=params,
            )
        )

    def reportreasons(self, profile_post_id: int) -> ProfilePostsReportreasonsResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/profile-posts/{profile_post_id}/report",
            )
        )

    def report(
        self, profile_post_id: int, *, body: ProfilePostsReportBody
    ) -> ProfilePostsReportResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/profile-posts/{profile_post_id}/report",
                body=body,
            )
        )

    def create(self, *, body: ProfilePostsCreateBody) -> ProfilePostsCreateResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/profile-posts",
                body=body,
            )
        )

    def stick(self, profile_post_id: int) -> ProfilePostsStickResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/profile-posts/{profile_post_id}/stick",
            )
        )

    def unstick(self, profile_post_id: int) -> ProfilePostsUnstickResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/profile-posts/{profile_post_id}/stick",
            )
        )

    def likes(self, profile_post_id: int) -> ProfilePostsLikesResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/profile-posts/{profile_post_id}/likes",
            )
        )

    def like(self, profile_post_id: int) -> ProfilePostsLikeResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/profile-posts/{profile_post_id}/likes",
            )
        )

    def unlike(self, profile_post_id: int) -> ProfilePostsUnlikeResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/profile-posts/{profile_post_id}/likes",
            )
        )

    def comments_list(
        self, *, params: ProfilePostsCommentsListParams
    ) -> ProfilePostsCommentsListResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/profile-posts/comments",
                query=params,
            )
        )

    def comments_create(
        self, *, body: ProfilePostsCommentsCreateBody
    ) -> ProfilePostsCommentsCreateResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/profile-posts/comments",
                body=body,
            )
        )

    def comments_edit(
        self, *, body: ProfilePostsCommentsEditBody
    ) -> ProfilePostsCommentsEditResponse:
        return self._http.request(
            RequestOptions(
                method="PUT",
                path="/profile-posts/comments",
                body=body,
            )
        )

    def comments_delete(
        self, *, body: ProfilePostsCommentsDeleteBody
    ) -> ProfilePostsCommentsDeleteResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path="/profile-posts/comments",
                body=body,
            )
        )

    def comments_get(
        self, profile_post_id: int, comment_id: int
    ) -> ProfilePostsCommentsGetResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/profile-posts/{profile_post_id}/comments/{comment_id}",
            )
        )

    def comments_report(
        self, comment_id: int, *, body: ProfilePostsCommentsReportBody
    ) -> ProfilePostsCommentsReportResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/profile-posts/comments/{comment_id}/report",
                body=body,
            )
        )


class AsyncProfilePostsApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def list(
        self, user_id: str | int, *, params: ProfilePostsListParams | None = None
    ) -> ProfilePostsListResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}/profile-posts",
                query=params,
            )
        )

    async def get(self, profile_post_id: int) -> ProfilePostsGetResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/profile-posts/{profile_post_id}",
            )
        )

    async def edit(
        self, profile_post_id: int, *, body: ProfilePostsEditBody | None = None
    ) -> ProfilePostsEditResponse:
        return await self._http.request(
            RequestOptions(
                method="PUT",
                path=f"/profile-posts/{profile_post_id}",
                body=body,
            )
        )

    async def delete(
        self, profile_post_id: int, *, params: ProfilePostsDeleteParams | None = None
    ) -> ProfilePostsDeleteResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/profile-posts/{profile_post_id}",
                query=params,
            )
        )

    async def reportreasons(self, profile_post_id: int) -> ProfilePostsReportreasonsResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/profile-posts/{profile_post_id}/report",
            )
        )

    async def report(
        self, profile_post_id: int, *, body: ProfilePostsReportBody
    ) -> ProfilePostsReportResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/profile-posts/{profile_post_id}/report",
                body=body,
            )
        )

    async def create(self, *, body: ProfilePostsCreateBody) -> ProfilePostsCreateResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/profile-posts",
                body=body,
            )
        )

    async def stick(self, profile_post_id: int) -> ProfilePostsStickResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/profile-posts/{profile_post_id}/stick",
            )
        )

    async def unstick(self, profile_post_id: int) -> ProfilePostsUnstickResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/profile-posts/{profile_post_id}/stick",
            )
        )

    async def likes(self, profile_post_id: int) -> ProfilePostsLikesResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/profile-posts/{profile_post_id}/likes",
            )
        )

    async def like(self, profile_post_id: int) -> ProfilePostsLikeResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/profile-posts/{profile_post_id}/likes",
            )
        )

    async def unlike(self, profile_post_id: int) -> ProfilePostsUnlikeResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/profile-posts/{profile_post_id}/likes",
            )
        )

    async def comments_list(
        self, *, params: ProfilePostsCommentsListParams
    ) -> ProfilePostsCommentsListResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/profile-posts/comments",
                query=params,
            )
        )

    async def comments_create(
        self, *, body: ProfilePostsCommentsCreateBody
    ) -> ProfilePostsCommentsCreateResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/profile-posts/comments",
                body=body,
            )
        )

    async def comments_edit(
        self, *, body: ProfilePostsCommentsEditBody
    ) -> ProfilePostsCommentsEditResponse:
        return await self._http.request(
            RequestOptions(
                method="PUT",
                path="/profile-posts/comments",
                body=body,
            )
        )

    async def comments_delete(
        self, *, body: ProfilePostsCommentsDeleteBody
    ) -> ProfilePostsCommentsDeleteResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path="/profile-posts/comments",
                body=body,
            )
        )

    async def comments_get(
        self, profile_post_id: int, comment_id: int
    ) -> ProfilePostsCommentsGetResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/profile-posts/{profile_post_id}/comments/{comment_id}",
            )
        )

    async def comments_report(
        self, comment_id: int, *, body: ProfilePostsCommentsReportBody
    ) -> ProfilePostsCommentsReportResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/profile-posts/comments/{comment_id}/report",
                body=body,
            )
        )
