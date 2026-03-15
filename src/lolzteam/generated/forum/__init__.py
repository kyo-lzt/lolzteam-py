# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING

from lolzteam.runtime.async_http_client import AsyncHttpClient
from lolzteam.runtime.errors import ConfigError
from lolzteam.runtime.http_client import HttpClient
from lolzteam.runtime.types import (
    ClientConfig,
    OnRetryCallback,
    ProxyConfig,
    RateLimitConfig,
    RequestOptions,
    RetryConfig,
)

if TYPE_CHECKING:
    from .types import (
        AssetsCssParams,
        AssetsCssResponse,
        BatchExecuteBody,
        BatchExecuteResponse,
        CategoriesGetResponse,
        CategoriesListParams,
        CategoriesListResponse,
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
        ChatboxReportreasonsParams,
        ChatboxReportreasonsResponse,
        ChatboxReportResponse,
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
        ConversationsReadallResponse,
        ConversationsReadResponse,
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
        FormsCreateBody,
        FormsCreateResponse,
        FormsListParams,
        FormsListResponse,
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
        LinksGetResponse,
        LinksListResponse,
        NavigationListParams,
        NavigationListResponse,
        NotificationsGetResponse,
        NotificationsListParams,
        NotificationsListResponse,
        NotificationsReadBody,
        NotificationsReadResponse,
        OAuthTokenBody,
        OAuthTokenResponse,
        PagesGetResponse,
        PagesListParams,
        PagesListResponse,
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
        PostsReportreasonsResponse,
        PostsReportResponse,
        PostsUnlikeResponse,
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
        TagsFindParams,
        TagsFindResponse,
        TagsGetParams,
        TagsGetResponse,
        TagsListParams,
        TagsListResponse,
        TagsPopularResponse,
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


class OAuthApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def token(self, *, body: OAuthTokenBody) -> OAuthTokenResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/oauth/token",
                body=body,
                content_type="multipart",
            )
        )  # type: ignore[return-value]


class AsyncOAuthApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def token(self, *, body: OAuthTokenBody) -> OAuthTokenResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/oauth/token",
                body=body,
                content_type="multipart",
            )
        )  # type: ignore[return-value]


class AssetsApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def css(self, *, params: AssetsCssParams | None = None) -> AssetsCssResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/css",
                query=params,
            )
        )  # type: ignore[return-value]


class AsyncAssetsApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def css(self, *, params: AssetsCssParams | None = None) -> AssetsCssResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/css",
                query=params,
            )
        )  # type: ignore[return-value]


class CategoriesApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def list(self, *, params: CategoriesListParams | None = None) -> CategoriesListResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/categories",
                query=params,
            )
        )  # type: ignore[return-value]

    def get(self, category_id: int) -> CategoriesGetResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/categories/{category_id}",
            )
        )  # type: ignore[return-value]


class AsyncCategoriesApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def list(self, *, params: CategoriesListParams | None = None) -> CategoriesListResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/categories",
                query=params,
            )
        )  # type: ignore[return-value]

    async def get(self, category_id: int) -> CategoriesGetResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/categories/{category_id}",
            )
        )  # type: ignore[return-value]


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
        )  # type: ignore[return-value]

    def grouped(self) -> ForumsGroupedResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/forums/grouped",
            )
        )  # type: ignore[return-value]

    def get(self, forum_id: int) -> ForumsGetResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/forums/{forum_id}",
            )
        )  # type: ignore[return-value]

    def followers(self, forum_id: int) -> ForumsFollowersResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/forums/{forum_id}/followers",
            )
        )  # type: ignore[return-value]

    def follow(
        self, forum_id: int, *, body: ForumsFollowBody | None = None
    ) -> ForumsFollowResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/forums/{forum_id}/followers",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def unfollow(self, forum_id: int) -> ForumsUnfollowResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/forums/{forum_id}/followers",
            )
        )  # type: ignore[return-value]

    def followed(self, *, params: ForumsFollowedParams | None = None) -> ForumsFollowedResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/forums/followed",
                query=params,
            )
        )  # type: ignore[return-value]

    def getfeedoptions(self) -> ForumsGetfeedoptionsResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/forums/feed/options",
            )
        )  # type: ignore[return-value]

    def editfeedoptions(
        self, *, body: ForumsEditfeedoptionsBody | None = None
    ) -> ForumsEditfeedoptionsResponse:
        return self._http.request(
            RequestOptions(
                method="PUT",
                path="/forums/feed/options",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


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
        )  # type: ignore[return-value]

    async def grouped(self) -> ForumsGroupedResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/forums/grouped",
            )
        )  # type: ignore[return-value]

    async def get(self, forum_id: int) -> ForumsGetResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/forums/{forum_id}",
            )
        )  # type: ignore[return-value]

    async def followers(self, forum_id: int) -> ForumsFollowersResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/forums/{forum_id}/followers",
            )
        )  # type: ignore[return-value]

    async def follow(
        self, forum_id: int, *, body: ForumsFollowBody | None = None
    ) -> ForumsFollowResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/forums/{forum_id}/followers",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def unfollow(self, forum_id: int) -> ForumsUnfollowResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/forums/{forum_id}/followers",
            )
        )  # type: ignore[return-value]

    async def followed(
        self, *, params: ForumsFollowedParams | None = None
    ) -> ForumsFollowedResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/forums/followed",
                query=params,
            )
        )  # type: ignore[return-value]

    async def getfeedoptions(self) -> ForumsGetfeedoptionsResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/forums/feed/options",
            )
        )  # type: ignore[return-value]

    async def editfeedoptions(
        self, *, body: ForumsEditfeedoptionsBody | None = None
    ) -> ForumsEditfeedoptionsResponse:
        return await self._http.request(
            RequestOptions(
                method="PUT",
                path="/forums/feed/options",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


class LinksApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def list(self) -> LinksListResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/link-forums",
            )
        )  # type: ignore[return-value]

    def get(self, link_id: int) -> LinksGetResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/link-forums/{link_id}",
            )
        )  # type: ignore[return-value]


class AsyncLinksApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def list(self) -> LinksListResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/link-forums",
            )
        )  # type: ignore[return-value]

    async def get(self, link_id: int) -> LinksGetResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/link-forums/{link_id}",
            )
        )  # type: ignore[return-value]


class PagesApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def list(self, *, params: PagesListParams | None = None) -> PagesListResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/pages",
                query=params,
            )
        )  # type: ignore[return-value]

    def get(self, page_id: int) -> PagesGetResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/pages/{page_id}",
            )
        )  # type: ignore[return-value]


class AsyncPagesApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def list(self, *, params: PagesListParams | None = None) -> PagesListResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/pages",
                query=params,
            )
        )  # type: ignore[return-value]

    async def get(self, page_id: int) -> PagesGetResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/pages/{page_id}",
            )
        )  # type: ignore[return-value]


class NavigationApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def list(self, *, params: NavigationListParams | None = None) -> NavigationListResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/navigation",
                query=params,
            )
        )  # type: ignore[return-value]


class AsyncNavigationApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def list(self, *, params: NavigationListParams | None = None) -> NavigationListResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/navigation",
                query=params,
            )
        )  # type: ignore[return-value]


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
        )  # type: ignore[return-value]

    def create(self, *, body: ThreadsCreateBody) -> ThreadsCreateResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/threads",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def createcontest(self, *, body: ThreadsCreatecontestBody) -> ThreadsCreatecontestResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/contests",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def claim(self, *, body: ThreadsClaimBody) -> ThreadsClaimResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/claims",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def get(self, thread_id: int, *, params: ThreadsGetParams | None = None) -> ThreadsGetResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/threads/{thread_id}",
                query=params,
            )
        )  # type: ignore[return-value]

    def edit(self, thread_id: int, *, body: ThreadsEditBody | None = None) -> ThreadsEditResponse:
        return self._http.request(
            RequestOptions(
                method="PUT",
                path=f"/threads/{thread_id}",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def delete(
        self, thread_id: int, *, body: ThreadsDeleteBody | None = None
    ) -> ThreadsDeleteResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/threads/{thread_id}",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def move(self, thread_id: int, *, body: ThreadsMoveBody) -> ThreadsMoveResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/threads/{thread_id}/move",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def bump(self, thread_id: int) -> ThreadsBumpResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/threads/{thread_id}/bump",
            )
        )  # type: ignore[return-value]

    def hide(self, thread_id: int) -> ThreadsHideResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/threads/{thread_id}/hide",
            )
        )  # type: ignore[return-value]

    def star(self, thread_id: int) -> ThreadsStarResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/threads/{thread_id}/star",
            )
        )  # type: ignore[return-value]

    def unstar(self, thread_id: int) -> ThreadsUnstarResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/threads/{thread_id}/star",
            )
        )  # type: ignore[return-value]

    def followers(self, thread_id: int) -> ThreadsFollowersResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/threads/{thread_id}/followers",
            )
        )  # type: ignore[return-value]

    def follow(
        self, thread_id: int, *, body: ThreadsFollowBody | None = None
    ) -> ThreadsFollowResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/threads/{thread_id}/followers",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def unfollow(self, thread_id: int) -> ThreadsUnfollowResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/threads/{thread_id}/followers",
            )
        )  # type: ignore[return-value]

    def followed(self, *, params: ThreadsFollowedParams | None = None) -> ThreadsFollowedResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/threads/followed",
                query=params,
            )
        )  # type: ignore[return-value]

    def navigation(self, thread_id: int) -> ThreadsNavigationResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/threads/{thread_id}/navigation",
            )
        )  # type: ignore[return-value]

    def poll_get(self, thread_id: int) -> ThreadsPollGetResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/threads/{thread_id}/poll",
            )
        )  # type: ignore[return-value]

    def poll_vote(
        self, thread_id: int, *, body: ThreadsPollVoteBody | None = None
    ) -> ThreadsPollVoteResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/threads/{thread_id}/poll/votes",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def unread(self, *, params: ThreadsUnreadParams | None = None) -> ThreadsUnreadResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/threads/new",
                query=params,
            )
        )  # type: ignore[return-value]

    def recent(self, *, params: ThreadsRecentParams | None = None) -> ThreadsRecentResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/threads/recent",
                query=params,
            )
        )  # type: ignore[return-value]

    def finish(self, thread_id: int) -> ThreadsFinishResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/contests/{thread_id}/finish",
            )
        )  # type: ignore[return-value]


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
        )  # type: ignore[return-value]

    async def create(self, *, body: ThreadsCreateBody) -> ThreadsCreateResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/threads",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def createcontest(
        self, *, body: ThreadsCreatecontestBody
    ) -> ThreadsCreatecontestResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/contests",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def claim(self, *, body: ThreadsClaimBody) -> ThreadsClaimResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/claims",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def get(
        self, thread_id: int, *, params: ThreadsGetParams | None = None
    ) -> ThreadsGetResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/threads/{thread_id}",
                query=params,
            )
        )  # type: ignore[return-value]

    async def edit(
        self, thread_id: int, *, body: ThreadsEditBody | None = None
    ) -> ThreadsEditResponse:
        return await self._http.request(
            RequestOptions(
                method="PUT",
                path=f"/threads/{thread_id}",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def delete(
        self, thread_id: int, *, body: ThreadsDeleteBody | None = None
    ) -> ThreadsDeleteResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/threads/{thread_id}",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def move(self, thread_id: int, *, body: ThreadsMoveBody) -> ThreadsMoveResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/threads/{thread_id}/move",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def bump(self, thread_id: int) -> ThreadsBumpResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/threads/{thread_id}/bump",
            )
        )  # type: ignore[return-value]

    async def hide(self, thread_id: int) -> ThreadsHideResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/threads/{thread_id}/hide",
            )
        )  # type: ignore[return-value]

    async def star(self, thread_id: int) -> ThreadsStarResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/threads/{thread_id}/star",
            )
        )  # type: ignore[return-value]

    async def unstar(self, thread_id: int) -> ThreadsUnstarResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/threads/{thread_id}/star",
            )
        )  # type: ignore[return-value]

    async def followers(self, thread_id: int) -> ThreadsFollowersResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/threads/{thread_id}/followers",
            )
        )  # type: ignore[return-value]

    async def follow(
        self, thread_id: int, *, body: ThreadsFollowBody | None = None
    ) -> ThreadsFollowResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/threads/{thread_id}/followers",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def unfollow(self, thread_id: int) -> ThreadsUnfollowResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/threads/{thread_id}/followers",
            )
        )  # type: ignore[return-value]

    async def followed(
        self, *, params: ThreadsFollowedParams | None = None
    ) -> ThreadsFollowedResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/threads/followed",
                query=params,
            )
        )  # type: ignore[return-value]

    async def navigation(self, thread_id: int) -> ThreadsNavigationResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/threads/{thread_id}/navigation",
            )
        )  # type: ignore[return-value]

    async def poll_get(self, thread_id: int) -> ThreadsPollGetResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/threads/{thread_id}/poll",
            )
        )  # type: ignore[return-value]

    async def poll_vote(
        self, thread_id: int, *, body: ThreadsPollVoteBody | None = None
    ) -> ThreadsPollVoteResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/threads/{thread_id}/poll/votes",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def unread(self, *, params: ThreadsUnreadParams | None = None) -> ThreadsUnreadResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/threads/new",
                query=params,
            )
        )  # type: ignore[return-value]

    async def recent(self, *, params: ThreadsRecentParams | None = None) -> ThreadsRecentResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/threads/recent",
                query=params,
            )
        )  # type: ignore[return-value]

    async def finish(self, thread_id: int) -> ThreadsFinishResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/contests/{thread_id}/finish",
            )
        )  # type: ignore[return-value]


class PostsApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def list(self, *, params: PostsListParams | None = None) -> PostsListResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/posts",
                query=params,
            )
        )  # type: ignore[return-value]

    def create(self, *, body: PostsCreateBody) -> PostsCreateResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/posts",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def get(self, post_id: int) -> PostsGetResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/posts/{post_id}",
            )
        )  # type: ignore[return-value]

    def edit(self, post_id: int, *, body: PostsEditBody | None = None) -> PostsEditResponse:
        return self._http.request(
            RequestOptions(
                method="PUT",
                path=f"/posts/{post_id}",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def delete(self, post_id: int, *, body: PostsDeleteBody | None = None) -> PostsDeleteResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/posts/{post_id}",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def likes(self, post_id: int, *, params: PostsLikesParams | None = None) -> PostsLikesResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/posts/{post_id}/likes",
                query=params,
            )
        )  # type: ignore[return-value]

    def like(self, post_id: int) -> PostsLikeResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/posts/{post_id}/likes",
            )
        )  # type: ignore[return-value]

    def unlike(self, post_id: int) -> PostsUnlikeResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/posts/{post_id}/likes",
            )
        )  # type: ignore[return-value]

    def reportreasons(self, post_id: int) -> PostsReportreasonsResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/posts/{post_id}/report",
            )
        )  # type: ignore[return-value]

    def report(self, post_id: int, *, body: PostsReportBody) -> PostsReportResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/posts/{post_id}/report",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def comments_get(self, *, params: PostsCommentsGetParams) -> PostsCommentsGetResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/posts/comments",
                query=params,
            )
        )  # type: ignore[return-value]

    def comments_create(self, *, body: PostsCommentsCreateBody) -> PostsCommentsCreateResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/posts/comments",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def comments_edit(self, *, body: PostsCommentsEditBody) -> PostsCommentsEditResponse:
        return self._http.request(
            RequestOptions(
                method="PUT",
                path="/posts/comments",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def comments_delete(self, *, body: PostsCommentsDeleteBody) -> PostsCommentsDeleteResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path="/posts/comments",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def comments_report(self, *, body: PostsCommentsReportBody) -> PostsCommentsReportResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/posts/comments/report",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


class AsyncPostsApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def list(self, *, params: PostsListParams | None = None) -> PostsListResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/posts",
                query=params,
            )
        )  # type: ignore[return-value]

    async def create(self, *, body: PostsCreateBody) -> PostsCreateResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/posts",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def get(self, post_id: int) -> PostsGetResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/posts/{post_id}",
            )
        )  # type: ignore[return-value]

    async def edit(self, post_id: int, *, body: PostsEditBody | None = None) -> PostsEditResponse:
        return await self._http.request(
            RequestOptions(
                method="PUT",
                path=f"/posts/{post_id}",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def delete(
        self, post_id: int, *, body: PostsDeleteBody | None = None
    ) -> PostsDeleteResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/posts/{post_id}",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def likes(
        self, post_id: int, *, params: PostsLikesParams | None = None
    ) -> PostsLikesResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/posts/{post_id}/likes",
                query=params,
            )
        )  # type: ignore[return-value]

    async def like(self, post_id: int) -> PostsLikeResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/posts/{post_id}/likes",
            )
        )  # type: ignore[return-value]

    async def unlike(self, post_id: int) -> PostsUnlikeResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/posts/{post_id}/likes",
            )
        )  # type: ignore[return-value]

    async def reportreasons(self, post_id: int) -> PostsReportreasonsResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/posts/{post_id}/report",
            )
        )  # type: ignore[return-value]

    async def report(self, post_id: int, *, body: PostsReportBody) -> PostsReportResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/posts/{post_id}/report",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def comments_get(self, *, params: PostsCommentsGetParams) -> PostsCommentsGetResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/posts/comments",
                query=params,
            )
        )  # type: ignore[return-value]

    async def comments_create(
        self, *, body: PostsCommentsCreateBody
    ) -> PostsCommentsCreateResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/posts/comments",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def comments_edit(self, *, body: PostsCommentsEditBody) -> PostsCommentsEditResponse:
        return await self._http.request(
            RequestOptions(
                method="PUT",
                path="/posts/comments",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def comments_delete(
        self, *, body: PostsCommentsDeleteBody
    ) -> PostsCommentsDeleteResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path="/posts/comments",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def comments_report(
        self, *, body: PostsCommentsReportBody
    ) -> PostsCommentsReportResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/posts/comments/report",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


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
        )  # type: ignore[return-value]

    def fields(self) -> UsersFieldsResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/users/fields",
            )
        )  # type: ignore[return-value]

    def find(self, *, params: UsersFindParams | None = None) -> UsersFindResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/users/find",
                query=params,
            )
        )  # type: ignore[return-value]

    def get(
        self, user_id: UserIDModel, *, params: UsersGetParams | None = None
    ) -> UsersGetResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}",
                query=params,
            )
        )  # type: ignore[return-value]

    def edit(self, user_id: UserIDModel, *, body: UsersEditBody | None = None) -> UsersEditResponse:
        return self._http.request(
            RequestOptions(
                method="PUT",
                path=f"/users/{user_id}",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def claims(
        self, user_id: UserIDModel, *, params: UsersClaimsParams | None = None
    ) -> UsersClaimsResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}/claims",
                query=params,
            )
        )  # type: ignore[return-value]

    def avatar_upload(
        self, user_id: UserIDModel, *, body: UsersAvatarUploadBody
    ) -> UsersAvatarUploadResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/users/{user_id}/avatar",
                body=body,
                content_type="multipart",
            )
        )  # type: ignore[return-value]

    def avatar_delete(self, user_id: UserIDModel) -> UsersAvatarDeleteResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/users/{user_id}/avatar",
            )
        )  # type: ignore[return-value]

    def avatar_crop(
        self, user_id: UserIDModel, *, body: UsersAvatarCropBody | None = None
    ) -> UsersAvatarCropResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/users/{user_id}/avatar/crop",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def background_upload(
        self, user_id: UserIDModel, *, body: UsersBackgroundUploadBody
    ) -> UsersBackgroundUploadResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/users/{user_id}/background",
                body=body,
                content_type="multipart",
            )
        )  # type: ignore[return-value]

    def background_delete(self, user_id: UserIDModel) -> UsersBackgroundDeleteResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/users/{user_id}/background",
            )
        )  # type: ignore[return-value]

    def background_crop(
        self, user_id: UserIDModel, *, body: UsersBackgroundCropBody
    ) -> UsersBackgroundCropResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/users/{user_id}/background/crop",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def followers(
        self, user_id: UserIDModel, *, params: UsersFollowersParams | None = None
    ) -> UsersFollowersResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}/followers",
                query=params,
            )
        )  # type: ignore[return-value]

    def follow(self, user_id: UserIDModel) -> UsersFollowResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/users/{user_id}/followers",
            )
        )  # type: ignore[return-value]

    def unfollow(self, user_id: UserIDModel) -> UsersUnfollowResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/users/{user_id}/followers",
            )
        )  # type: ignore[return-value]

    def followings(
        self, user_id: UserIDModel, *, params: UsersFollowingsParams | None = None
    ) -> UsersFollowingsResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}/followings",
                query=params,
            )
        )  # type: ignore[return-value]

    def likes(
        self, user_id: UserIDModel, *, params: UsersLikesParams | None = None
    ) -> UsersLikesResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}/likes",
                query=params,
            )
        )  # type: ignore[return-value]

    def ignored(self, *, params: UsersIgnoredParams | None = None) -> UsersIgnoredResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/users/ignored",
                query=params,
            )
        )  # type: ignore[return-value]

    def ignore(self, user_id: UserIDModel) -> UsersIgnoreResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/users/{user_id}/ignore",
            )
        )  # type: ignore[return-value]

    def ignoreedit(
        self, user_id: UserIDModel, *, params: UsersIgnoreeditParams | None = None
    ) -> UsersIgnoreeditResponse:
        return self._http.request(
            RequestOptions(
                method="PUT",
                path=f"/users/{user_id}/ignore",
                query=params,
            )
        )  # type: ignore[return-value]

    def unignore(self, user_id: UserIDModel) -> UsersUnignoreResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/users/{user_id}/ignore",
            )
        )  # type: ignore[return-value]

    def contents(
        self, user_id: UserIDModel, *, params: UsersContentsParams | None = None
    ) -> UsersContentsResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}/timeline",
                query=params,
            )
        )  # type: ignore[return-value]

    def trophies(self, user_id: UserIDModel) -> UsersTrophiesResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}/trophies",
            )
        )  # type: ignore[return-value]

    def secretanswertypes(self) -> UsersSecretanswertypesResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/users/secret-answer/types",
            )
        )  # type: ignore[return-value]

    def sa_reset(self) -> UsersSaResetResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/account/secret-answer/reset",
            )
        )  # type: ignore[return-value]

    def sa_cancelreset(self) -> UsersSaCancelresetResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path="/account/secret-answer/reset",
            )
        )  # type: ignore[return-value]


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
        )  # type: ignore[return-value]

    async def fields(self) -> UsersFieldsResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/users/fields",
            )
        )  # type: ignore[return-value]

    async def find(self, *, params: UsersFindParams | None = None) -> UsersFindResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/users/find",
                query=params,
            )
        )  # type: ignore[return-value]

    async def get(
        self, user_id: UserIDModel, *, params: UsersGetParams | None = None
    ) -> UsersGetResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}",
                query=params,
            )
        )  # type: ignore[return-value]

    async def edit(
        self, user_id: UserIDModel, *, body: UsersEditBody | None = None
    ) -> UsersEditResponse:
        return await self._http.request(
            RequestOptions(
                method="PUT",
                path=f"/users/{user_id}",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def claims(
        self, user_id: UserIDModel, *, params: UsersClaimsParams | None = None
    ) -> UsersClaimsResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}/claims",
                query=params,
            )
        )  # type: ignore[return-value]

    async def avatar_upload(
        self, user_id: UserIDModel, *, body: UsersAvatarUploadBody
    ) -> UsersAvatarUploadResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/users/{user_id}/avatar",
                body=body,
                content_type="multipart",
            )
        )  # type: ignore[return-value]

    async def avatar_delete(self, user_id: UserIDModel) -> UsersAvatarDeleteResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/users/{user_id}/avatar",
            )
        )  # type: ignore[return-value]

    async def avatar_crop(
        self, user_id: UserIDModel, *, body: UsersAvatarCropBody | None = None
    ) -> UsersAvatarCropResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/users/{user_id}/avatar/crop",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def background_upload(
        self, user_id: UserIDModel, *, body: UsersBackgroundUploadBody
    ) -> UsersBackgroundUploadResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/users/{user_id}/background",
                body=body,
                content_type="multipart",
            )
        )  # type: ignore[return-value]

    async def background_delete(self, user_id: UserIDModel) -> UsersBackgroundDeleteResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/users/{user_id}/background",
            )
        )  # type: ignore[return-value]

    async def background_crop(
        self, user_id: UserIDModel, *, body: UsersBackgroundCropBody
    ) -> UsersBackgroundCropResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/users/{user_id}/background/crop",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def followers(
        self, user_id: UserIDModel, *, params: UsersFollowersParams | None = None
    ) -> UsersFollowersResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}/followers",
                query=params,
            )
        )  # type: ignore[return-value]

    async def follow(self, user_id: UserIDModel) -> UsersFollowResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/users/{user_id}/followers",
            )
        )  # type: ignore[return-value]

    async def unfollow(self, user_id: UserIDModel) -> UsersUnfollowResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/users/{user_id}/followers",
            )
        )  # type: ignore[return-value]

    async def followings(
        self, user_id: UserIDModel, *, params: UsersFollowingsParams | None = None
    ) -> UsersFollowingsResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}/followings",
                query=params,
            )
        )  # type: ignore[return-value]

    async def likes(
        self, user_id: UserIDModel, *, params: UsersLikesParams | None = None
    ) -> UsersLikesResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}/likes",
                query=params,
            )
        )  # type: ignore[return-value]

    async def ignored(self, *, params: UsersIgnoredParams | None = None) -> UsersIgnoredResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/users/ignored",
                query=params,
            )
        )  # type: ignore[return-value]

    async def ignore(self, user_id: UserIDModel) -> UsersIgnoreResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/users/{user_id}/ignore",
            )
        )  # type: ignore[return-value]

    async def ignoreedit(
        self, user_id: UserIDModel, *, params: UsersIgnoreeditParams | None = None
    ) -> UsersIgnoreeditResponse:
        return await self._http.request(
            RequestOptions(
                method="PUT",
                path=f"/users/{user_id}/ignore",
                query=params,
            )
        )  # type: ignore[return-value]

    async def unignore(self, user_id: UserIDModel) -> UsersUnignoreResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/users/{user_id}/ignore",
            )
        )  # type: ignore[return-value]

    async def contents(
        self, user_id: UserIDModel, *, params: UsersContentsParams | None = None
    ) -> UsersContentsResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}/timeline",
                query=params,
            )
        )  # type: ignore[return-value]

    async def trophies(self, user_id: UserIDModel) -> UsersTrophiesResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}/trophies",
            )
        )  # type: ignore[return-value]

    async def secretanswertypes(self) -> UsersSecretanswertypesResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/users/secret-answer/types",
            )
        )  # type: ignore[return-value]

    async def sa_reset(self) -> UsersSaResetResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/account/secret-answer/reset",
            )
        )  # type: ignore[return-value]

    async def sa_cancelreset(self) -> UsersSaCancelresetResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path="/account/secret-answer/reset",
            )
        )  # type: ignore[return-value]


class ProfilePostsApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def list(
        self, user_id: UserIDModel, *, params: ProfilePostsListParams | None = None
    ) -> ProfilePostsListResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}/profile-posts",
                query=params,
            )
        )  # type: ignore[return-value]

    def get(self, profile_post_id: int) -> ProfilePostsGetResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/profile-posts/{profile_post_id}",
            )
        )  # type: ignore[return-value]

    def edit(
        self, profile_post_id: int, *, body: ProfilePostsEditBody | None = None
    ) -> ProfilePostsEditResponse:
        return self._http.request(
            RequestOptions(
                method="PUT",
                path=f"/profile-posts/{profile_post_id}",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def delete(
        self, profile_post_id: int, *, params: ProfilePostsDeleteParams | None = None
    ) -> ProfilePostsDeleteResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/profile-posts/{profile_post_id}",
                query=params,
            )
        )  # type: ignore[return-value]

    def reportreasons(self, profile_post_id: int) -> ProfilePostsReportreasonsResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/profile-posts/{profile_post_id}/report",
            )
        )  # type: ignore[return-value]

    def report(
        self, profile_post_id: int, *, body: ProfilePostsReportBody
    ) -> ProfilePostsReportResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/profile-posts/{profile_post_id}/report",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def create(self, *, body: ProfilePostsCreateBody) -> ProfilePostsCreateResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/profile-posts",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def stick(self, profile_post_id: int) -> ProfilePostsStickResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/profile-posts/{profile_post_id}/stick",
            )
        )  # type: ignore[return-value]

    def unstick(self, profile_post_id: int) -> ProfilePostsUnstickResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/profile-posts/{profile_post_id}/stick",
            )
        )  # type: ignore[return-value]

    def likes(self, profile_post_id: int) -> ProfilePostsLikesResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/profile-posts/{profile_post_id}/likes",
            )
        )  # type: ignore[return-value]

    def like(self, profile_post_id: int) -> ProfilePostsLikeResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/profile-posts/{profile_post_id}/likes",
            )
        )  # type: ignore[return-value]

    def unlike(self, profile_post_id: int) -> ProfilePostsUnlikeResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/profile-posts/{profile_post_id}/likes",
            )
        )  # type: ignore[return-value]

    def comments_list(
        self, *, params: ProfilePostsCommentsListParams
    ) -> ProfilePostsCommentsListResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/profile-posts/comments",
                query=params,
            )
        )  # type: ignore[return-value]

    def comments_create(
        self, *, body: ProfilePostsCommentsCreateBody
    ) -> ProfilePostsCommentsCreateResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/profile-posts/comments",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def comments_edit(
        self, *, body: ProfilePostsCommentsEditBody
    ) -> ProfilePostsCommentsEditResponse:
        return self._http.request(
            RequestOptions(
                method="PUT",
                path="/profile-posts/comments",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def comments_delete(
        self, *, body: ProfilePostsCommentsDeleteBody
    ) -> ProfilePostsCommentsDeleteResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path="/profile-posts/comments",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def comments_get(
        self, profile_post_id: int, comment_id: int
    ) -> ProfilePostsCommentsGetResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/profile-posts/{profile_post_id}/comments/{comment_id}",
            )
        )  # type: ignore[return-value]

    def comments_report(
        self, comment_id: int, *, body: ProfilePostsCommentsReportBody
    ) -> ProfilePostsCommentsReportResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/profile-posts/comments/{comment_id}/report",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


class AsyncProfilePostsApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def list(
        self, user_id: UserIDModel, *, params: ProfilePostsListParams | None = None
    ) -> ProfilePostsListResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/users/{user_id}/profile-posts",
                query=params,
            )
        )  # type: ignore[return-value]

    async def get(self, profile_post_id: int) -> ProfilePostsGetResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/profile-posts/{profile_post_id}",
            )
        )  # type: ignore[return-value]

    async def edit(
        self, profile_post_id: int, *, body: ProfilePostsEditBody | None = None
    ) -> ProfilePostsEditResponse:
        return await self._http.request(
            RequestOptions(
                method="PUT",
                path=f"/profile-posts/{profile_post_id}",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def delete(
        self, profile_post_id: int, *, params: ProfilePostsDeleteParams | None = None
    ) -> ProfilePostsDeleteResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/profile-posts/{profile_post_id}",
                query=params,
            )
        )  # type: ignore[return-value]

    async def reportreasons(self, profile_post_id: int) -> ProfilePostsReportreasonsResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/profile-posts/{profile_post_id}/report",
            )
        )  # type: ignore[return-value]

    async def report(
        self, profile_post_id: int, *, body: ProfilePostsReportBody
    ) -> ProfilePostsReportResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/profile-posts/{profile_post_id}/report",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def create(self, *, body: ProfilePostsCreateBody) -> ProfilePostsCreateResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/profile-posts",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def stick(self, profile_post_id: int) -> ProfilePostsStickResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/profile-posts/{profile_post_id}/stick",
            )
        )  # type: ignore[return-value]

    async def unstick(self, profile_post_id: int) -> ProfilePostsUnstickResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/profile-posts/{profile_post_id}/stick",
            )
        )  # type: ignore[return-value]

    async def likes(self, profile_post_id: int) -> ProfilePostsLikesResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/profile-posts/{profile_post_id}/likes",
            )
        )  # type: ignore[return-value]

    async def like(self, profile_post_id: int) -> ProfilePostsLikeResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/profile-posts/{profile_post_id}/likes",
            )
        )  # type: ignore[return-value]

    async def unlike(self, profile_post_id: int) -> ProfilePostsUnlikeResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/profile-posts/{profile_post_id}/likes",
            )
        )  # type: ignore[return-value]

    async def comments_list(
        self, *, params: ProfilePostsCommentsListParams
    ) -> ProfilePostsCommentsListResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/profile-posts/comments",
                query=params,
            )
        )  # type: ignore[return-value]

    async def comments_create(
        self, *, body: ProfilePostsCommentsCreateBody
    ) -> ProfilePostsCommentsCreateResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/profile-posts/comments",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def comments_edit(
        self, *, body: ProfilePostsCommentsEditBody
    ) -> ProfilePostsCommentsEditResponse:
        return await self._http.request(
            RequestOptions(
                method="PUT",
                path="/profile-posts/comments",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def comments_delete(
        self, *, body: ProfilePostsCommentsDeleteBody
    ) -> ProfilePostsCommentsDeleteResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path="/profile-posts/comments",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def comments_get(
        self, profile_post_id: int, comment_id: int
    ) -> ProfilePostsCommentsGetResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/profile-posts/{profile_post_id}/comments/{comment_id}",
            )
        )  # type: ignore[return-value]

    async def comments_report(
        self, comment_id: int, *, body: ProfilePostsCommentsReportBody
    ) -> ProfilePostsCommentsReportResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/profile-posts/comments/{comment_id}/report",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


class ConversationsApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def list(self, *, params: ConversationsListParams | None = None) -> ConversationsListResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/conversations",
                query=params,
            )
        )  # type: ignore[return-value]

    def create(self, *, body: ConversationsCreateBody | None = None) -> ConversationsCreateResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/conversations",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def update(self, *, body: ConversationsUpdateBody) -> ConversationsUpdateResponse:
        return self._http.request(
            RequestOptions(
                method="PUT",
                path="/conversations",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def delete(self, *, body: ConversationsDeleteBody) -> ConversationsDeleteResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path="/conversations",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def start(self, *, body: ConversationsStartBody) -> ConversationsStartResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/conversations/start",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def save(self, *, body: ConversationsSaveBody) -> ConversationsSaveResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/conversations/save",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def get(self, conversation_id: int) -> ConversationsGetResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/conversations/{conversation_id}",
            )
        )  # type: ignore[return-value]

    def messages_list(
        self, conversation_id: int, *, params: ConversationsMessagesListParams | None = None
    ) -> ConversationsMessagesListResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/conversations/{conversation_id}/messages",
                query=params,
            )
        )  # type: ignore[return-value]

    def messages_create(
        self, conversation_id: int, *, body: ConversationsMessagesCreateBody
    ) -> ConversationsMessagesCreateResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/conversations/{conversation_id}/messages",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def search(self, *, body: ConversationsSearchBody | None = None) -> ConversationsSearchResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/conversations/search",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def messages_get(self, message_id: int) -> ConversationsMessagesGetResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/conversations/messages/{message_id}",
            )
        )  # type: ignore[return-value]

    def messages_edit(
        self, conversation_id: int, message_id: int, *, body: ConversationsMessagesEditBody
    ) -> ConversationsMessagesEditResponse:
        return self._http.request(
            RequestOptions(
                method="PUT",
                path=f"/conversations/{conversation_id}/messages/{message_id}",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def messages_delete(
        self, conversation_id: int, message_id: int
    ) -> ConversationsMessagesDeleteResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/conversations/{conversation_id}/messages/{message_id}",
            )
        )  # type: ignore[return-value]

    def invite(
        self, conversation_id: int, *, body: ConversationsInviteBody
    ) -> ConversationsInviteResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/conversations/{conversation_id}/invite",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def kick(
        self, conversation_id: int, *, body: ConversationsKickBody
    ) -> ConversationsKickResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/conversations/{conversation_id}/kick",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def read(self, conversation_id: int) -> ConversationsReadResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/conversations/{conversation_id}/read",
            )
        )  # type: ignore[return-value]

    def readall(self) -> ConversationsReadallResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/conversations/read-all",
            )
        )  # type: ignore[return-value]

    def messages_stick(
        self, conversation_id: int, message_id: int
    ) -> ConversationsMessagesStickResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/conversations/{conversation_id}/messages/{message_id}/stick",
            )
        )  # type: ignore[return-value]

    def messages_unstick(
        self, conversation_id: int, message_id: int
    ) -> ConversationsMessagesUnstickResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/conversations/{conversation_id}/messages/{message_id}/stick",
            )
        )  # type: ignore[return-value]

    def star(self, conversation_id: int) -> ConversationsStarResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/conversations/{conversation_id}/star",
            )
        )  # type: ignore[return-value]

    def unstar(self, conversation_id: int) -> ConversationsUnstarResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/conversations/{conversation_id}/star",
            )
        )  # type: ignore[return-value]

    def alerts_enable(self, conversation_id: int) -> ConversationsAlertsEnableResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/conversations/{conversation_id}/alerts",
            )
        )  # type: ignore[return-value]

    def alerts_disable(self, conversation_id: int) -> ConversationsAlertsDisableResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/conversations/{conversation_id}/alerts",
            )
        )  # type: ignore[return-value]


class AsyncConversationsApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def list(
        self, *, params: ConversationsListParams | None = None
    ) -> ConversationsListResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/conversations",
                query=params,
            )
        )  # type: ignore[return-value]

    async def create(
        self, *, body: ConversationsCreateBody | None = None
    ) -> ConversationsCreateResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/conversations",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def update(self, *, body: ConversationsUpdateBody) -> ConversationsUpdateResponse:
        return await self._http.request(
            RequestOptions(
                method="PUT",
                path="/conversations",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def delete(self, *, body: ConversationsDeleteBody) -> ConversationsDeleteResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path="/conversations",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def start(self, *, body: ConversationsStartBody) -> ConversationsStartResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/conversations/start",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def save(self, *, body: ConversationsSaveBody) -> ConversationsSaveResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/conversations/save",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def get(self, conversation_id: int) -> ConversationsGetResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/conversations/{conversation_id}",
            )
        )  # type: ignore[return-value]

    async def messages_list(
        self, conversation_id: int, *, params: ConversationsMessagesListParams | None = None
    ) -> ConversationsMessagesListResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/conversations/{conversation_id}/messages",
                query=params,
            )
        )  # type: ignore[return-value]

    async def messages_create(
        self, conversation_id: int, *, body: ConversationsMessagesCreateBody
    ) -> ConversationsMessagesCreateResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/conversations/{conversation_id}/messages",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def search(
        self, *, body: ConversationsSearchBody | None = None
    ) -> ConversationsSearchResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/conversations/search",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def messages_get(self, message_id: int) -> ConversationsMessagesGetResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/conversations/messages/{message_id}",
            )
        )  # type: ignore[return-value]

    async def messages_edit(
        self, conversation_id: int, message_id: int, *, body: ConversationsMessagesEditBody
    ) -> ConversationsMessagesEditResponse:
        return await self._http.request(
            RequestOptions(
                method="PUT",
                path=f"/conversations/{conversation_id}/messages/{message_id}",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def messages_delete(
        self, conversation_id: int, message_id: int
    ) -> ConversationsMessagesDeleteResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/conversations/{conversation_id}/messages/{message_id}",
            )
        )  # type: ignore[return-value]

    async def invite(
        self, conversation_id: int, *, body: ConversationsInviteBody
    ) -> ConversationsInviteResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/conversations/{conversation_id}/invite",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def kick(
        self, conversation_id: int, *, body: ConversationsKickBody
    ) -> ConversationsKickResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/conversations/{conversation_id}/kick",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def read(self, conversation_id: int) -> ConversationsReadResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/conversations/{conversation_id}/read",
            )
        )  # type: ignore[return-value]

    async def readall(self) -> ConversationsReadallResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/conversations/read-all",
            )
        )  # type: ignore[return-value]

    async def messages_stick(
        self, conversation_id: int, message_id: int
    ) -> ConversationsMessagesStickResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/conversations/{conversation_id}/messages/{message_id}/stick",
            )
        )  # type: ignore[return-value]

    async def messages_unstick(
        self, conversation_id: int, message_id: int
    ) -> ConversationsMessagesUnstickResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/conversations/{conversation_id}/messages/{message_id}/stick",
            )
        )  # type: ignore[return-value]

    async def star(self, conversation_id: int) -> ConversationsStarResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/conversations/{conversation_id}/star",
            )
        )  # type: ignore[return-value]

    async def unstar(self, conversation_id: int) -> ConversationsUnstarResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/conversations/{conversation_id}/star",
            )
        )  # type: ignore[return-value]

    async def alerts_enable(self, conversation_id: int) -> ConversationsAlertsEnableResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/conversations/{conversation_id}/alerts",
            )
        )  # type: ignore[return-value]

    async def alerts_disable(self, conversation_id: int) -> ConversationsAlertsDisableResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/conversations/{conversation_id}/alerts",
            )
        )  # type: ignore[return-value]


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
        )  # type: ignore[return-value]

    def get(self, notification_id: int) -> NotificationsGetResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/notifications/{notification_id}/content",
            )
        )  # type: ignore[return-value]

    def read(self, *, body: NotificationsReadBody | None = None) -> NotificationsReadResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/notifications/read",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


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
        )  # type: ignore[return-value]

    async def get(self, notification_id: int) -> NotificationsGetResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/notifications/{notification_id}/content",
            )
        )  # type: ignore[return-value]

    async def read(self, *, body: NotificationsReadBody | None = None) -> NotificationsReadResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/notifications/read",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


class TagsApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def popular(self) -> TagsPopularResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/tags",
            )
        )  # type: ignore[return-value]

    def list(self, *, params: TagsListParams | None = None) -> TagsListResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/tags/list",
                query=params,
            )
        )  # type: ignore[return-value]

    def get(self, tag_id: int, *, params: TagsGetParams | None = None) -> TagsGetResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/tags/{tag_id}",
                query=params,
            )
        )  # type: ignore[return-value]

    def find(self, *, params: TagsFindParams) -> TagsFindResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/tags/find",
                query=params,
            )
        )  # type: ignore[return-value]


class AsyncTagsApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def popular(self) -> TagsPopularResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/tags",
            )
        )  # type: ignore[return-value]

    async def list(self, *, params: TagsListParams | None = None) -> TagsListResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/tags/list",
                query=params,
            )
        )  # type: ignore[return-value]

    async def get(self, tag_id: int, *, params: TagsGetParams | None = None) -> TagsGetResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/tags/{tag_id}",
                query=params,
            )
        )  # type: ignore[return-value]

    async def find(self, *, params: TagsFindParams) -> TagsFindResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/tags/find",
                query=params,
            )
        )  # type: ignore[return-value]


class SearchApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def all(self, *, body: SearchAllBody | None = None) -> SearchAllResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/search",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def threads(self, *, body: SearchThreadsBody | None = None) -> SearchThreadsResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/search/threads",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def posts(self, *, body: SearchPostsBody | None = None) -> SearchPostsResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/search/posts",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def users(self, *, body: SearchUsersBody | None = None) -> SearchUsersResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/search/users",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def profileposts(
        self, *, body: SearchProfilepostsBody | None = None
    ) -> SearchProfilepostsResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/search/profile-posts",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def tagged(self, *, body: SearchTaggedBody | None = None) -> SearchTaggedResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/search/tagged",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def results(
        self, search_id: str | int, *, params: SearchResultsBody | None = None
    ) -> SearchResultsResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/search/{search_id}/results",
                query=params,
            )
        )  # type: ignore[return-value]


class AsyncSearchApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def all(self, *, body: SearchAllBody | None = None) -> SearchAllResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/search",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def threads(self, *, body: SearchThreadsBody | None = None) -> SearchThreadsResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/search/threads",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def posts(self, *, body: SearchPostsBody | None = None) -> SearchPostsResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/search/posts",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def users(self, *, body: SearchUsersBody | None = None) -> SearchUsersResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/search/users",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def profileposts(
        self, *, body: SearchProfilepostsBody | None = None
    ) -> SearchProfilepostsResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/search/profile-posts",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def tagged(self, *, body: SearchTaggedBody | None = None) -> SearchTaggedResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/search/tagged",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def results(
        self, search_id: str | int, *, params: SearchResultsBody | None = None
    ) -> SearchResultsResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/search/{search_id}/results",
                query=params,
            )
        )  # type: ignore[return-value]


class BatchApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def execute(self, *, body: BatchExecuteBody | None = None) -> BatchExecuteResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/batch",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


class AsyncBatchApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def execute(self, *, body: BatchExecuteBody | None = None) -> BatchExecuteResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/batch",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


class ChatboxApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def index(self, *, params: ChatboxIndexParams | None = None) -> ChatboxIndexResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/chatbox",
                query=params,
            )
        )  # type: ignore[return-value]

    def getmessages(self, *, params: ChatboxGetmessagesParams) -> ChatboxGetmessagesResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/chatbox/messages",
                query=params,
            )
        )  # type: ignore[return-value]

    def postmessage(self, *, body: ChatboxPostmessageBody) -> ChatboxPostmessageResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/chatbox/messages",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def editmessage(self, *, body: ChatboxEditmessageBody) -> ChatboxEditmessageResponse:
        return self._http.request(
            RequestOptions(
                method="PUT",
                path="/chatbox/messages",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def deletemessage(self, *, body: ChatboxDeletemessageBody) -> ChatboxDeletemessageResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path="/chatbox/messages",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def online(self, *, params: ChatboxOnlineParams) -> ChatboxOnlineResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/chatbox/messages/online",
                query=params,
            )
        )  # type: ignore[return-value]

    def reportreasons(self, *, params: ChatboxReportreasonsParams) -> ChatboxReportreasonsResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/chatbox/messages/report",
                query=params,
            )
        )  # type: ignore[return-value]

    def report(self, *, body: ChatboxReportBody) -> ChatboxReportResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/chatbox/messages/report",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def getleaderboard(
        self, *, params: ChatboxGetleaderboardParams | None = None
    ) -> ChatboxGetleaderboardResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/chatbox/messages/leaderboard",
                query=params,
            )
        )  # type: ignore[return-value]

    def getignore(self) -> ChatboxGetignoreResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/chatbox/ignore",
            )
        )  # type: ignore[return-value]

    def postignore(self, *, body: ChatboxPostignoreBody) -> ChatboxPostignoreResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/chatbox/ignore",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def deleteignore(self, *, body: ChatboxDeleteignoreBody) -> ChatboxDeleteignoreResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path="/chatbox/ignore",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


class AsyncChatboxApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def index(self, *, params: ChatboxIndexParams | None = None) -> ChatboxIndexResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/chatbox",
                query=params,
            )
        )  # type: ignore[return-value]

    async def getmessages(self, *, params: ChatboxGetmessagesParams) -> ChatboxGetmessagesResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/chatbox/messages",
                query=params,
            )
        )  # type: ignore[return-value]

    async def postmessage(self, *, body: ChatboxPostmessageBody) -> ChatboxPostmessageResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/chatbox/messages",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def editmessage(self, *, body: ChatboxEditmessageBody) -> ChatboxEditmessageResponse:
        return await self._http.request(
            RequestOptions(
                method="PUT",
                path="/chatbox/messages",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def deletemessage(
        self, *, body: ChatboxDeletemessageBody
    ) -> ChatboxDeletemessageResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path="/chatbox/messages",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def online(self, *, params: ChatboxOnlineParams) -> ChatboxOnlineResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/chatbox/messages/online",
                query=params,
            )
        )  # type: ignore[return-value]

    async def reportreasons(
        self, *, params: ChatboxReportreasonsParams
    ) -> ChatboxReportreasonsResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/chatbox/messages/report",
                query=params,
            )
        )  # type: ignore[return-value]

    async def report(self, *, body: ChatboxReportBody) -> ChatboxReportResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/chatbox/messages/report",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def getleaderboard(
        self, *, params: ChatboxGetleaderboardParams | None = None
    ) -> ChatboxGetleaderboardResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/chatbox/messages/leaderboard",
                query=params,
            )
        )  # type: ignore[return-value]

    async def getignore(self) -> ChatboxGetignoreResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/chatbox/ignore",
            )
        )  # type: ignore[return-value]

    async def postignore(self, *, body: ChatboxPostignoreBody) -> ChatboxPostignoreResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/chatbox/ignore",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def deleteignore(self, *, body: ChatboxDeleteignoreBody) -> ChatboxDeleteignoreResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path="/chatbox/ignore",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


class FormsApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def list(self, *, params: FormsListParams | None = None) -> FormsListResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/forms",
                query=params,
            )
        )  # type: ignore[return-value]

    def create(self, *, body: FormsCreateBody) -> FormsCreateResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/forms/save",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


class AsyncFormsApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def list(self, *, params: FormsListParams | None = None) -> FormsListResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/forms",
                query=params,
            )
        )  # type: ignore[return-value]

    async def create(self, *, body: FormsCreateBody) -> FormsCreateResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/forms/save",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


class ForumClient:
    def __init__(
        self,
        config: ClientConfig | None = None,
        *,
        token: str | None = None,
        base_url: str = "https://prod-api.lolz.live",
        proxy: str | None = None,
        max_retries: int = 3,
        base_delay: float = 1.0,
        max_delay: float = 30.0,
        requests_per_minute: int = 300,
        on_retry: OnRetryCallback | None = None,
    ) -> None:
        if config is None:
            if token is None:
                raise ConfigError("either config or token must be provided")
            import warnings

            warnings.warn(
                "ForumClient(token=...) is deprecated, "
                "use ForumClient(ClientConfig(token=..., ...)) instead",
                DeprecationWarning,
                stacklevel=2,
            )
            config = ClientConfig(
                token=token,
                base_url=base_url,
                proxy=ProxyConfig(url=proxy) if proxy else None,
                retry=RetryConfig(
                    max_retries=max_retries, base_delay=base_delay, max_delay=max_delay
                ),
                rate_limit=RateLimitConfig(requests_per_minute=requests_per_minute),
                on_retry=on_retry,
            )
        self._http = HttpClient(config)
        self.o_auth = OAuthApi(self._http)
        self.assets = AssetsApi(self._http)
        self.categories = CategoriesApi(self._http)
        self.forums = ForumsApi(self._http)
        self.links = LinksApi(self._http)
        self.pages = PagesApi(self._http)
        self.navigation = NavigationApi(self._http)
        self.threads = ThreadsApi(self._http)
        self.posts = PostsApi(self._http)
        self.users = UsersApi(self._http)
        self.profile_posts = ProfilePostsApi(self._http)
        self.conversations = ConversationsApi(self._http)
        self.notifications = NotificationsApi(self._http)
        self.tags = TagsApi(self._http)
        self.search = SearchApi(self._http)
        self.batch = BatchApi(self._http)
        self.chatbox = ChatboxApi(self._http)
        self.forms = FormsApi(self._http)

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> ForumClient:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()


class AsyncForumClient:
    def __init__(
        self,
        config: ClientConfig | None = None,
        *,
        token: str | None = None,
        base_url: str = "https://prod-api.lolz.live",
        proxy: str | None = None,
        max_retries: int = 3,
        base_delay: float = 1.0,
        max_delay: float = 30.0,
        requests_per_minute: int = 300,
        on_retry: OnRetryCallback | None = None,
    ) -> None:
        if config is None:
            if token is None:
                raise ConfigError("either config or token must be provided")
            import warnings

            warnings.warn(
                "AsyncForumClient(token=...) is deprecated, "
                "use AsyncForumClient(ClientConfig(token=..., ...)) instead",
                DeprecationWarning,
                stacklevel=2,
            )
            config = ClientConfig(
                token=token,
                base_url=base_url,
                proxy=ProxyConfig(url=proxy) if proxy else None,
                retry=RetryConfig(
                    max_retries=max_retries, base_delay=base_delay, max_delay=max_delay
                ),
                rate_limit=RateLimitConfig(requests_per_minute=requests_per_minute),
                on_retry=on_retry,
            )
        self._http = AsyncHttpClient(config)
        self.o_auth = AsyncOAuthApi(self._http)
        self.assets = AsyncAssetsApi(self._http)
        self.categories = AsyncCategoriesApi(self._http)
        self.forums = AsyncForumsApi(self._http)
        self.links = AsyncLinksApi(self._http)
        self.pages = AsyncPagesApi(self._http)
        self.navigation = AsyncNavigationApi(self._http)
        self.threads = AsyncThreadsApi(self._http)
        self.posts = AsyncPostsApi(self._http)
        self.users = AsyncUsersApi(self._http)
        self.profile_posts = AsyncProfilePostsApi(self._http)
        self.conversations = AsyncConversationsApi(self._http)
        self.notifications = AsyncNotificationsApi(self._http)
        self.tags = AsyncTagsApi(self._http)
        self.search = AsyncSearchApi(self._http)
        self.batch = AsyncBatchApi(self._http)
        self.chatbox = AsyncChatboxApi(self._http)
        self.forms = AsyncFormsApi(self._http)

    async def close(self) -> None:
        await self._http.close()

    async def __aenter__(self) -> AsyncForumClient:
        return self

    async def __aexit__(self, *args: object) -> None:
        await self.close()
