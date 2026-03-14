# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING

from lolzteam.runtime.types import RequestOptions

if TYPE_CHECKING:
    from lolzteam.runtime.async_http_client import AsyncHttpClient
    from lolzteam.runtime.http_client import HttpClient

    from .types import (
        UsersAvatarCropBody,
        UsersAvatarCropResponse,
        UsersAvatarDeleteResponse,
        UsersAvatarUploadBody,
        UsersAvatarUploadResponse,
        UsersBackgroundCropBody,
        UsersBackgroundCropResponse,
        UsersBackgroundDeleteResponse,
        UsersBackgroundUploadBody,
        UsersBackgroundUploadResponse,
        UsersClaimsParams,
        UsersClaimsResponse,
        UsersContentsParams,
        UsersContentsResponse,
        UsersEditBody,
        UsersEditResponse,
        UsersFieldsResponse,
        UsersFindParams,
        UsersFindResponse,
        UsersFollowersParams,
        UsersFollowersResponse,
        UsersFollowingsParams,
        UsersFollowingsResponse,
        UsersFollowResponse,
        UsersGetParams,
        UsersGetResponse,
        UsersIgnoredParams,
        UsersIgnoredResponse,
        UsersIgnoreeditParams,
        UsersIgnoreeditResponse,
        UsersIgnoreResponse,
        UsersLikesParams,
        UsersLikesResponse,
        UsersListParams,
        UsersListResponse,
        UsersSaCancelresetResponse,
        UsersSaResetResponse,
        UsersSecretanswertypesResponse,
        UsersTrophiesResponse,
        UsersUnfollowResponse,
        UsersUnignoreResponse,
    )


class UsersApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def list(self, *, params: UsersListParams | None = None) -> UsersListResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/users",
                query=params,
            )
        )

    def fields(self) -> UsersFieldsResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/users/fields",
            )
        )

    def find(self, *, params: UsersFindParams | None = None) -> UsersFindResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/users/find",
                query=params,
            )
        )

    def get(self, user_id: str | int, *, params: UsersGetParams | None = None) -> UsersGetResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}",
                query=params,
            )
        )

    def edit(self, user_id: str | int, *, body: UsersEditBody | None = None) -> UsersEditResponse:
        return self._http.request(
            RequestOptions(
                method="PUT",
                path=f"/users/{user_id}",
                body=body,
            )
        )

    def claims(
        self, user_id: str | int, *, params: UsersClaimsParams | None = None
    ) -> UsersClaimsResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}/claims",
                query=params,
            )
        )

    def avatar_upload(
        self, user_id: str | int, *, body: UsersAvatarUploadBody
    ) -> UsersAvatarUploadResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/users/{user_id}/avatar",
                body=body,
                content_type="multipart",
            )
        )

    def avatar_delete(self, user_id: str | int) -> UsersAvatarDeleteResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/users/{user_id}/avatar",
            )
        )

    def avatar_crop(
        self, user_id: str | int, *, body: UsersAvatarCropBody | None = None
    ) -> UsersAvatarCropResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/users/{user_id}/avatar/crop",
                body=body,
            )
        )

    def background_upload(
        self, user_id: str | int, *, body: UsersBackgroundUploadBody
    ) -> UsersBackgroundUploadResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/users/{user_id}/background",
                body=body,
                content_type="multipart",
            )
        )

    def background_delete(self, user_id: str | int) -> UsersBackgroundDeleteResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/users/{user_id}/background",
            )
        )

    def background_crop(
        self, user_id: str | int, *, body: UsersBackgroundCropBody
    ) -> UsersBackgroundCropResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/users/{user_id}/background/crop",
                body=body,
            )
        )

    def followers(
        self, user_id: str | int, *, params: UsersFollowersParams | None = None
    ) -> UsersFollowersResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}/followers",
                query=params,
            )
        )

    def follow(self, user_id: str | int) -> UsersFollowResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/users/{user_id}/followers",
            )
        )

    def unfollow(self, user_id: str | int) -> UsersUnfollowResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/users/{user_id}/followers",
            )
        )

    def followings(
        self, user_id: str | int, *, params: UsersFollowingsParams | None = None
    ) -> UsersFollowingsResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}/followings",
                query=params,
            )
        )

    def likes(
        self, user_id: str | int, *, params: UsersLikesParams | None = None
    ) -> UsersLikesResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}/likes",
                query=params,
            )
        )

    def ignored(self, *, params: UsersIgnoredParams | None = None) -> UsersIgnoredResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/users/ignored",
                query=params,
            )
        )

    def ignore(self, user_id: str | int) -> UsersIgnoreResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/users/{user_id}/ignore",
            )
        )

    def ignoreedit(
        self, user_id: str | int, *, params: UsersIgnoreeditParams | None = None
    ) -> UsersIgnoreeditResponse:
        return self._http.request(
            RequestOptions(
                method="PUT",
                path=f"/users/{user_id}/ignore",
                query=params,
            )
        )

    def unignore(self, user_id: str | int) -> UsersUnignoreResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/users/{user_id}/ignore",
            )
        )

    def contents(
        self, user_id: str | int, *, params: UsersContentsParams | None = None
    ) -> UsersContentsResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}/timeline",
                query=params,
            )
        )

    def trophies(self, user_id: str | int) -> UsersTrophiesResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}/trophies",
            )
        )

    def secretanswertypes(self) -> UsersSecretanswertypesResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/users/secret-answer/types",
            )
        )

    def sa_reset(self) -> UsersSaResetResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/account/secret-answer/reset",
            )
        )

    def sa_cancelreset(self) -> UsersSaCancelresetResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path="/account/secret-answer/reset",
            )
        )


class AsyncUsersApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def list(self, *, params: UsersListParams | None = None) -> UsersListResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/users",
                query=params,
            )
        )

    async def fields(self) -> UsersFieldsResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/users/fields",
            )
        )

    async def find(self, *, params: UsersFindParams | None = None) -> UsersFindResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/users/find",
                query=params,
            )
        )

    async def get(
        self, user_id: str | int, *, params: UsersGetParams | None = None
    ) -> UsersGetResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}",
                query=params,
            )
        )

    async def edit(
        self, user_id: str | int, *, body: UsersEditBody | None = None
    ) -> UsersEditResponse:
        return await self._http.request(
            RequestOptions(
                method="PUT",
                path=f"/users/{user_id}",
                body=body,
            )
        )

    async def claims(
        self, user_id: str | int, *, params: UsersClaimsParams | None = None
    ) -> UsersClaimsResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}/claims",
                query=params,
            )
        )

    async def avatar_upload(
        self, user_id: str | int, *, body: UsersAvatarUploadBody
    ) -> UsersAvatarUploadResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/users/{user_id}/avatar",
                body=body,
                content_type="multipart",
            )
        )

    async def avatar_delete(self, user_id: str | int) -> UsersAvatarDeleteResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/users/{user_id}/avatar",
            )
        )

    async def avatar_crop(
        self, user_id: str | int, *, body: UsersAvatarCropBody | None = None
    ) -> UsersAvatarCropResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/users/{user_id}/avatar/crop",
                body=body,
            )
        )

    async def background_upload(
        self, user_id: str | int, *, body: UsersBackgroundUploadBody
    ) -> UsersBackgroundUploadResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/users/{user_id}/background",
                body=body,
                content_type="multipart",
            )
        )

    async def background_delete(self, user_id: str | int) -> UsersBackgroundDeleteResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/users/{user_id}/background",
            )
        )

    async def background_crop(
        self, user_id: str | int, *, body: UsersBackgroundCropBody
    ) -> UsersBackgroundCropResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/users/{user_id}/background/crop",
                body=body,
            )
        )

    async def followers(
        self, user_id: str | int, *, params: UsersFollowersParams | None = None
    ) -> UsersFollowersResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}/followers",
                query=params,
            )
        )

    async def follow(self, user_id: str | int) -> UsersFollowResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/users/{user_id}/followers",
            )
        )

    async def unfollow(self, user_id: str | int) -> UsersUnfollowResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/users/{user_id}/followers",
            )
        )

    async def followings(
        self, user_id: str | int, *, params: UsersFollowingsParams | None = None
    ) -> UsersFollowingsResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}/followings",
                query=params,
            )
        )

    async def likes(
        self, user_id: str | int, *, params: UsersLikesParams | None = None
    ) -> UsersLikesResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}/likes",
                query=params,
            )
        )

    async def ignored(self, *, params: UsersIgnoredParams | None = None) -> UsersIgnoredResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/users/ignored",
                query=params,
            )
        )

    async def ignore(self, user_id: str | int) -> UsersIgnoreResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/users/{user_id}/ignore",
            )
        )

    async def ignoreedit(
        self, user_id: str | int, *, params: UsersIgnoreeditParams | None = None
    ) -> UsersIgnoreeditResponse:
        return await self._http.request(
            RequestOptions(
                method="PUT",
                path=f"/users/{user_id}/ignore",
                query=params,
            )
        )

    async def unignore(self, user_id: str | int) -> UsersUnignoreResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/users/{user_id}/ignore",
            )
        )

    async def contents(
        self, user_id: str | int, *, params: UsersContentsParams | None = None
    ) -> UsersContentsResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}/timeline",
                query=params,
            )
        )

    async def trophies(self, user_id: str | int) -> UsersTrophiesResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}/trophies",
            )
        )

    async def secretanswertypes(self) -> UsersSecretanswertypesResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/users/secret-answer/types",
            )
        )

    async def sa_reset(self) -> UsersSaResetResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/account/secret-answer/reset",
            )
        )

    async def sa_cancelreset(self) -> UsersSaCancelresetResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path="/account/secret-answer/reset",
            )
        )
