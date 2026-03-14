# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING

from lolzteam.runtime.types import RequestOptions

if TYPE_CHECKING:
    from lolzteam.runtime.async_http_client import AsyncHttpClient
    from lolzteam.runtime.http_client import HttpClient

    from .types import (
        PostsCommentsCreateBody,
        PostsCommentsCreateResponse,
        PostsCommentsDeleteBody,
        PostsCommentsDeleteResponse,
        PostsCommentsEditBody,
        PostsCommentsEditResponse,
        PostsCommentsGetParams,
        PostsCommentsGetResponse,
        PostsCommentsReportBody,
        PostsCommentsReportResponse,
        PostsCreateBody,
        PostsCreateResponse,
        PostsDeleteBody,
        PostsDeleteResponse,
        PostsEditBody,
        PostsEditResponse,
        PostsGetResponse,
        PostsLikeResponse,
        PostsLikesParams,
        PostsLikesResponse,
        PostsListParams,
        PostsListResponse,
        PostsReportBody,
        PostsReportResponse,
        PostsReportreasonsResponse,
        PostsUnlikeResponse,
    )


class PostsApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def list(self, *, params: PostsListParams | None = None) -> PostsListResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/posts",
            query=params,
        ))

    def create(self, *, body: PostsCreateBody) -> PostsCreateResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path="/posts",
            body=body,
        ))

    def get(self, post_id: int) -> PostsGetResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path=f"/posts/{post_id}",
        ))

    def edit(self, post_id: int, *, body: PostsEditBody | None = None) -> PostsEditResponse:
        return self._http.request(RequestOptions(
            method="PUT",
            path=f"/posts/{post_id}",
            body=body,
        ))

    def delete(self, post_id: int, *, body: PostsDeleteBody | None = None) -> PostsDeleteResponse:
        return self._http.request(RequestOptions(
            method="DELETE",
            path=f"/posts/{post_id}",
            body=body,
        ))

    def likes(self, post_id: int, *, params: PostsLikesParams | None = None) -> PostsLikesResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path=f"/posts/{post_id}/likes",
            query=params,
        ))

    def like(self, post_id: int) -> PostsLikeResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path=f"/posts/{post_id}/likes",
        ))

    def unlike(self, post_id: int) -> PostsUnlikeResponse:
        return self._http.request(RequestOptions(
            method="DELETE",
            path=f"/posts/{post_id}/likes",
        ))

    def reportreasons(self, post_id: int) -> PostsReportreasonsResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path=f"/posts/{post_id}/report",
        ))

    def report(self, post_id: int, *, body: PostsReportBody) -> PostsReportResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path=f"/posts/{post_id}/report",
            body=body,
        ))

    def comments_get(self, *, params: PostsCommentsGetParams) -> PostsCommentsGetResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/posts/comments",
            query=params,
        ))

    def comments_create(self, *, body: PostsCommentsCreateBody) -> PostsCommentsCreateResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path="/posts/comments",
            body=body,
        ))

    def comments_edit(self, *, body: PostsCommentsEditBody) -> PostsCommentsEditResponse:
        return self._http.request(RequestOptions(
            method="PUT",
            path="/posts/comments",
            body=body,
        ))

    def comments_delete(self, *, body: PostsCommentsDeleteBody) -> PostsCommentsDeleteResponse:
        return self._http.request(RequestOptions(
            method="DELETE",
            path="/posts/comments",
            body=body,
        ))

    def comments_report(self, *, body: PostsCommentsReportBody) -> PostsCommentsReportResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path="/posts/comments/report",
            body=body,
        ))


class AsyncPostsApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def list(self, *, params: PostsListParams | None = None) -> PostsListResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/posts",
            query=params,
        ))

    async def create(self, *, body: PostsCreateBody) -> PostsCreateResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path="/posts",
            body=body,
        ))

    async def get(self, post_id: int) -> PostsGetResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path=f"/posts/{post_id}",
        ))

    async def edit(self, post_id: int, *, body: PostsEditBody | None = None) -> PostsEditResponse:
        return await self._http.request(RequestOptions(
            method="PUT",
            path=f"/posts/{post_id}",
            body=body,
        ))

    async def delete(self, post_id: int, *, body: PostsDeleteBody | None = None) -> PostsDeleteResponse:
        return await self._http.request(RequestOptions(
            method="DELETE",
            path=f"/posts/{post_id}",
            body=body,
        ))

    async def likes(self, post_id: int, *, params: PostsLikesParams | None = None) -> PostsLikesResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path=f"/posts/{post_id}/likes",
            query=params,
        ))

    async def like(self, post_id: int) -> PostsLikeResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path=f"/posts/{post_id}/likes",
        ))

    async def unlike(self, post_id: int) -> PostsUnlikeResponse:
        return await self._http.request(RequestOptions(
            method="DELETE",
            path=f"/posts/{post_id}/likes",
        ))

    async def reportreasons(self, post_id: int) -> PostsReportreasonsResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path=f"/posts/{post_id}/report",
        ))

    async def report(self, post_id: int, *, body: PostsReportBody) -> PostsReportResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path=f"/posts/{post_id}/report",
            body=body,
        ))

    async def comments_get(self, *, params: PostsCommentsGetParams) -> PostsCommentsGetResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/posts/comments",
            query=params,
        ))

    async def comments_create(self, *, body: PostsCommentsCreateBody) -> PostsCommentsCreateResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path="/posts/comments",
            body=body,
        ))

    async def comments_edit(self, *, body: PostsCommentsEditBody) -> PostsCommentsEditResponse:
        return await self._http.request(RequestOptions(
            method="PUT",
            path="/posts/comments",
            body=body,
        ))

    async def comments_delete(self, *, body: PostsCommentsDeleteBody) -> PostsCommentsDeleteResponse:
        return await self._http.request(RequestOptions(
            method="DELETE",
            path="/posts/comments",
            body=body,
        ))

    async def comments_report(self, *, body: PostsCommentsReportBody) -> PostsCommentsReportResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path="/posts/comments/report",
            body=body,
        ))
