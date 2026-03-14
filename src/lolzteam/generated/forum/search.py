# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING

from lolzteam.runtime.types import RequestOptions

if TYPE_CHECKING:
    from lolzteam.runtime.async_http_client import AsyncHttpClient
    from lolzteam.runtime.http_client import HttpClient

    from .types import (
        SearchAllBody,
        SearchAllResponse,
        SearchPostsBody,
        SearchPostsResponse,
        SearchProfilepostsBody,
        SearchProfilepostsResponse,
        SearchResultsBody,
        SearchResultsResponse,
        SearchTaggedBody,
        SearchTaggedResponse,
        SearchThreadsBody,
        SearchThreadsResponse,
        SearchUsersBody,
        SearchUsersResponse,
    )


class SearchApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def all(self, *, body: SearchAllBody | None = None) -> SearchAllResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/search",
                body=body,
            )
        )

    def threads(self, *, body: SearchThreadsBody | None = None) -> SearchThreadsResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/search/threads",
                body=body,
            )
        )

    def posts(self, *, body: SearchPostsBody | None = None) -> SearchPostsResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/search/posts",
                body=body,
            )
        )

    def users(self, *, body: SearchUsersBody | None = None) -> SearchUsersResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/search/users",
                body=body,
            )
        )

    def profileposts(
        self, *, body: SearchProfilepostsBody | None = None
    ) -> SearchProfilepostsResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/search/profile-posts",
                body=body,
            )
        )

    def tagged(self, *, body: SearchTaggedBody | None = None) -> SearchTaggedResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/search/tagged",
                body=body,
            )
        )

    def results(
        self, search_id: str | int, *, body: SearchResultsBody | None = None
    ) -> SearchResultsResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/search/{search_id}/results",
                body=body,
            )
        )


class AsyncSearchApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def all(self, *, body: SearchAllBody | None = None) -> SearchAllResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/search",
                body=body,
            )
        )

    async def threads(self, *, body: SearchThreadsBody | None = None) -> SearchThreadsResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/search/threads",
                body=body,
            )
        )

    async def posts(self, *, body: SearchPostsBody | None = None) -> SearchPostsResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/search/posts",
                body=body,
            )
        )

    async def users(self, *, body: SearchUsersBody | None = None) -> SearchUsersResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/search/users",
                body=body,
            )
        )

    async def profileposts(
        self, *, body: SearchProfilepostsBody | None = None
    ) -> SearchProfilepostsResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/search/profile-posts",
                body=body,
            )
        )

    async def tagged(self, *, body: SearchTaggedBody | None = None) -> SearchTaggedResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/search/tagged",
                body=body,
            )
        )

    async def results(
        self, search_id: str | int, *, body: SearchResultsBody | None = None
    ) -> SearchResultsResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/search/{search_id}/results",
                body=body,
            )
        )
