# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Literal, TypedDict

# ─── Component Schemas ────────────────────────────────────────


UserIDModel = str | int


class Resp_NotificationModel(TypedDict):
    notification_id: int
    notification_create_date: int
    content_type: str
    content_id: int
    content_action: str
    notification_is_unread: bool
    creator_user_id: int
    creator_username: str
    creator_username_html: str
    notification_type: str
    links: dict[str, object]
    notification_html: str


class Resp_LinkModel(TypedDict):
    link_id: int
    link_title: str
    link_description: str
    links: dict[str, object]
    permissions: dict[str, object]


RoomIDModel = Literal[1, 2, 3, 4, 13]


class Resp_ChatboxMessageModel(TypedDict):
    can_report: bool
    date: int
    is_deleted: bool
    message: str
    message_id: int
    messageJson: str
    messageRaw: str
    room: dict[str, object]
    user: dict[str, object]


class Resp_UserModel(TypedDict):
    user_id: int
    username: str
    username_html: str
    user_message_count: int
    user_register_date: int
    user_like_count: int
    user_like2_count: int
    contest_count: int
    trophy_count: int
    short_link: str
    custom_title: str
    is_banned: int
    display_banner_id: int
    display_icon_group_id: int
    balance: str
    hold: str
    currency: str
    user_email: str
    user_unread_notification_count: int
    user_unread_conversation_count: int
    conv_welcome_message: str
    user_title: str
    user_deposit: int
    user_is_valid: bool
    user_is_verified: bool
    user_is_followed: bool
    user_last_seen_date: int
    links: dict[str, object]
    permissions: dict[str, object]
    user_is_ignored: bool
    user_is_visitor: bool
    user_group_id: int
    curator_titles: list[str]
    user_groups: list[dict[str, object]]
    fields: list[dict[str, object]]
    user_timezone_offset: int
    user_external_authentications: list[dict[str, object]]
    self_permissions: dict[str, object]
    edit_permissions: dict[str, object]
    birthday: dict[str, object]
    secret_answer_rendered: str
    secret_answer_first_letter: str
    user_following: dict[str, object]
    user_followers: dict[str, object]
    banner: str


class Resp_ThreadModel(TypedDict):
    thread_id: int
    forum_id: int
    thread_title: str
    thread_view_count: int
    creator_user_id: int
    creator_username: str
    creator_username_html: str
    thread_create_date: int
    thread_update_date: int
    user_is_ignored: bool
    thread_post_count: int
    thread_is_published: bool
    thread_is_deleted: bool
    thread_is_sticky: bool
    thread_is_closed: bool
    thread_is_followed: bool
    thread_is_starred: bool
    first_post: dict[str, object]
    thread_prefixes: list[object]
    thread_tags: dict[str, object]
    links: dict[str, object]
    permissions: dict[str, object]
    node_title: str
    restrictions: dict[str, object]
    last_post: dict[str, object]
    contest: dict[str, object]


class Resp_PostModel(TypedDict):
    post_id: int
    thread_id: int
    poster_user_id: int
    poster_username: str
    poster_username_html: str
    post_create_date: int
    post_body: str
    post_body_html: str
    post_body_plain_text: str
    signature: str
    signature_html: str
    signature_plain_text: str
    post_like_count: int
    user_is_ignored: bool
    post_is_published: bool
    post_is_deleted: bool
    post_update_date: int
    post_is_first_post: bool
    links: dict[str, object]
    permissions: dict[str, object]
    thread_is_deleted: bool


class Resp_PostCommentModel(TypedDict):
    post_comment_id: int
    post_id: int
    thread_id: int
    poster_user_id: int
    poster_username: str
    poster_username_html: str
    post_comment_create_date: int
    post_comment_body: str
    post_comment_body_html: str
    post_comment_body_plain_text: str
    post_comment_like_count: int
    user_is_ignored: bool
    post_comment_is_published: bool
    post_comment_is_deleted: bool
    post_comment_update_date: int
    links: dict[str, object]
    permissions: dict[str, object]


class Resp_ProfilePostModel(TypedDict):
    profile_post_id: int
    timeline_user_id: int
    poster_user_id: int
    poster_username: str
    poster_username_html: str
    post_create_date: int
    post_body: str
    post_body_html: str
    post_body_plain_text: str
    post_like_count: int
    post_comment_count: int
    post_comments_is_disabled: int
    timeline_username: str
    user_is_ignored: bool
    post_is_published: bool
    post_is_deleted: bool
    post_is_liked: bool
    post_is_sticked: bool
    links: dict[str, object]
    permissions: dict[str, object]
    timeline_user: dict[str, object]


class Resp_ProfilePostCommentModel(TypedDict):
    comment_id: int
    profile_post_id: int
    comment_user_id: int
    comment_username: str
    comment_username_html: str
    comment_create_date: int
    comment_body: str
    comment_body_html: str
    comment_body_plain_text: str
    user_is_ignored: bool
    timeline_user_id: int
    links: dict[str, object]
    permissions: dict[str, object]


class Resp_ConversationModel(TypedDict):
    conversation_id: int
    conversation_title: str
    creator_user_id: int
    creator_username: str
    creator_username_html: str
    conversation_create_date: int
    conversation_update_date: int
    conversation_last_read_date: int
    conversation_online_count: int
    is_starred: int
    is_group: int
    is_unread: int
    alerts: int
    permissions: dict[str, object]
    conversation_message_count: int
    conversation_is_new: bool
    creator_is_ignored: bool
    conversation_is_open: bool
    conversation_is_deleted: bool
    recipient: dict[str, object]
    recipients: list[dict[str, object]]
    links: dict[str, object]


class Resp_ConversationMessageModel(TypedDict):
    message_id: int
    conversation_id: int
    creator_user_id: int
    creator_username: str
    creator_username_html: str
    message_create_date: int
    message_is_unread: int
    message_need_translate: bool
    message_is_system: bool
    message_edit_date: int
    message_body: str
    message_body_html: str
    message_body_plain_text: str
    user_is_ignored: bool
    links: dict[str, object]
    permissions: dict[str, object]


class Resp_SystemInfo(TypedDict):
    visitor_id: int
    time: int


# ─── OAuthApi Types ────────────────────────────────────────


class _OAuthTokenBodyRequired(TypedDict):
    grant_type: Literal["client_credentials", "authorization_code", "refresh_token", "password"]
    client_id: str
    client_secret: str


class OAuthTokenBody(_OAuthTokenBodyRequired, total=False):
    scope: list[Literal["basic", "read", "post", "conversate", "market", "payment", "invoice"]]
    code: str
    redirect_uri: str
    refresh_token: str
    username: str
    password: str


class _OAuthTokenResponseRequired(TypedDict):
    access_token: str
    token_type: str
    expires_in: int


class OAuthTokenResponse(_OAuthTokenResponseRequired, total=False):
    refresh_token: str
    scope: str


# ─── AssetsApi Types ────────────────────────────────────────


class AssetsCssParams(TypedDict, total=False):
    css: list[str]


class AssetsCssResponse(TypedDict):
    contents: str
    system_info: dict[str, object]


# ─── CategoriesApi Types ────────────────────────────────────────


class CategoriesListParams(TypedDict, total=False):
    parent_category_id: int
    parent_forum_id: int
    order: Literal["natural", "list"]


class CategoriesListResponse(TypedDict):
    categories: list[dict[str, object]]
    categories_total: int
    system_info: dict[str, object]


class CategoriesGetResponse(TypedDict):
    category: dict[str, object]
    system_info: dict[str, object]


# ─── ForumsApi Types ────────────────────────────────────────


class ForumsListParams(TypedDict, total=False):
    parent_category_id: int
    parent_forum_id: int
    order: Literal["natural", "list"]


class ForumsListResponse(TypedDict):
    forums: list[dict[str, object]]
    forums_total: int
    tabs: list[dict[str, object]]
    system_info: dict[str, object]


class ForumsGroupedResponse(TypedDict):
    data: dict[str, object]
    tabs: list[dict[str, object]]
    system_info: dict[str, object]


class ForumsGetResponse(TypedDict):
    forum: dict[str, object]
    system_info: dict[str, object]


class ForumsFollowersResponse(TypedDict):
    users: list[dict[str, object]]
    system_info: dict[str, object]


class ForumsFollowBody(TypedDict, total=False):
    post: bool
    alert: bool
    email: bool
    prefix_ids: list[int]
    minimal_contest_amount: int


class ForumsFollowResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class ForumsUnfollowResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class ForumsFollowedParams(TypedDict, total=False):
    total: bool


class ForumsFollowedResponse(TypedDict):
    forums: list[dict[str, object]]
    system_info: dict[str, object]


class ForumsGetfeedoptionsResponse(TypedDict):
    forums: list[dict[str, object]]
    excluded_forums_ids: list[int]
    default_excluded_forums_ids: list[int]
    keywords: str
    system_info: dict[str, object]


class ForumsEditfeedoptionsBody(TypedDict, total=False):
    node_ids: list[int]
    keywords: list[str]


class ForumsEditfeedoptionsResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


# ─── LinksApi Types ────────────────────────────────────────


LinksListResponse = TypedDict(
    "LinksListResponse",
    {
        "link-forums": list[dict[str, object]],
        "link-forums_total": int,
        "system_info": dict[str, object],
    },
)


LinksGetResponse = TypedDict(
    "LinksGetResponse",
    {
        "link-forum": dict[str, object],
        "system_info": dict[str, object],
    },
)


# ─── PagesApi Types ────────────────────────────────────────


class PagesListParams(TypedDict, total=False):
    parent_page_id: int
    order: Literal["natural", "list"]


class PagesListResponse(TypedDict):
    pages: list[dict[str, object]]
    pages_total: int
    system_info: dict[str, object]


class PagesGetResponse(TypedDict):
    page: dict[str, object]
    system_info: dict[str, object]


# ─── NavigationApi Types ────────────────────────────────────────


class NavigationListParams(TypedDict, total=False):
    parent: int


class NavigationListResponse(TypedDict):
    elements: list[dict[str, object]]
    elements_count: int
    system_info: dict[str, object]


# ─── ThreadsApi Types ────────────────────────────────────────


ThreadsListParams = TypedDict(
    "ThreadsListParams",
    {
        "forum_id": int,
        "tab": str,
        "state": Literal["active", "closed"],
        "period": Literal["day", "week", "month", "year"],
        "title": str,
        "title_only": bool,
        "creator_user_id": int,
        "sticky": bool,
        "prefix_ids[]": list[int],
        "prefix_ids_not[]": list[int],
        "thread_tag_id": int,
        "page": int,
        "limit": int,
        "order": Literal[
            "post_date",
            "last_post_date",
            "reply_count",
            "reply_count_asc",
            "first_post_likes",
            "vote_count",
        ],
        "direction": Literal["asc", "desc"],
        "thread_create_date": int,
        "thread_update_date": int,
        "fields_include": list[Literal["*", "latest_posts"]],
    },
    total=False,
)


class ThreadsListResponse(TypedDict):
    threads: list[dict[str, object]]
    forum: dict[str, object]
    threads_total: int
    links: dict[str, object]
    system_info: dict[str, object]


class _ThreadsCreateBodyRequired(TypedDict):
    post_body: str
    forum_id: int


class ThreadsCreateBody(_ThreadsCreateBodyRequired, total=False):
    title: str
    title_en: str
    prefix_id: list[int]
    tags: list[str]
    hide_contacts: bool
    allow_ask_hidden_content: bool
    reply_group: Literal[0, 2, 21, 22, 23, 60, 351]
    comment_ignore_group: bool
    dont_alert_followers: bool
    schedule_date: str
    schedule_time: str
    watch_thread_state: bool
    watch_thread: bool
    watch_thread_email: bool


class ThreadsCreateResponse(TypedDict):
    thread: dict[str, object]
    system_info: dict[str, object]


class _ThreadsCreatecontestBodyRequired(TypedDict):
    post_body: str
    contest_type: Literal["by_finish_date"]
    prize_type: Literal["money", "upgrades"]
    require_like_count: int
    require_total_like_count: int


class ThreadsCreatecontestBody(_ThreadsCreatecontestBodyRequired, total=False):
    title: str
    title_en: str
    length_value: int
    length_option: Literal["minutes", "hours", "days"]
    count_winners: int
    prize_data_money: int | float
    is_money_places: bool
    prize_data_places: list[int | float]
    prize_data_upgrade: Literal[1, 6, 12, 14, 17, 19, 20, 21, 22]
    secret_answer: str
    tags: list[str]
    reply_group: Literal[0, 2, 21, 22, 23, 60, 351]
    comment_ignore_group: bool
    dont_alert_followers: bool
    hide_contacts: bool
    allow_ask_hidden_content: bool
    schedule_date: str
    schedule_time: str
    watch_thread_state: bool
    watch_thread: bool
    watch_thread_email: bool


class ThreadsCreatecontestResponse(TypedDict):
    thread: dict[str, object]
    system_info: dict[str, object]


class _ThreadsClaimBodyRequired(TypedDict):
    as_responder: str
    as_is_market_deal: bool
    as_amount: int | float
    transfer_type: Literal["guarantor", "safe", "notsafe"]
    post_body: str


class ThreadsClaimBody(_ThreadsClaimBodyRequired, total=False):
    as_market_item_id: int
    as_data: str
    currency: Literal["rub", "uah", "kzt", "byn", "usd", "eur", "gbp", "cny", "try"]
    pay_claim: Literal["now", "later"]
    as_funds_receipt: str
    as_tg_login_screenshot: str
    tags: list[str]
    hide_contacts: bool
    allow_ask_hidden_content: bool
    reply_group: Literal[0, 2, 21, 22, 23, 60, 351]
    comment_ignore_group: bool
    dont_alert_followers: bool
    schedule_date: str
    schedule_time: str
    watch_thread_state: bool
    watch_thread: bool
    watch_thread_email: bool


class ThreadsClaimResponse(TypedDict):
    thread: dict[str, object]
    system_info: dict[str, object]


class ThreadsGetParams(TypedDict, total=False):
    fields_include: list[Literal["*", "latest_posts"]]


class ThreadsGetResponse(TypedDict):
    thread: dict[str, object]
    system_info: dict[str, object]


class ThreadsEditBody(TypedDict, total=False):
    title: str
    title_en: str
    prefix_id: list[int]
    tags: list[str]
    discussion_open: bool
    hide_contacts: bool
    allow_ask_hidden_content: bool
    reply_group: Literal[0, 2, 21, 22, 23, 60, 351]
    comment_ignore_group: bool


class ThreadsEditResponse(TypedDict):
    thread: dict[str, object]
    system_info: dict[str, object]


class ThreadsDeleteBody(TypedDict, total=False):
    reason: str


class ThreadsDeleteResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class _ThreadsMoveBodyRequired(TypedDict):
    node_id: str


class ThreadsMoveBody(_ThreadsMoveBodyRequired, total=False):
    title: str
    title_en: str
    prefix_id: list[int]
    apply_thread_prefix: bool
    send_alert: bool


class ThreadsMoveResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class ThreadsBumpResponse(TypedDict):
    status: str
    message: str
    system_info: dict[str, object]


class ThreadsHideResponse(TypedDict):
    status: str
    message: str
    system_info: dict[str, object]


class ThreadsStarResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class ThreadsUnstarResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class ThreadsFollowersResponse(TypedDict):
    users: list[dict[str, object]]
    system_info: dict[str, object]


class ThreadsFollowBody(TypedDict, total=False):
    email: bool


class ThreadsFollowResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class ThreadsUnfollowResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class ThreadsFollowedParams(TypedDict, total=False):
    total: bool
    fields_include: list[Literal["*", "latest_posts"]]


class ThreadsFollowedResponse(TypedDict):
    threads: list[dict[str, object]]
    threads_total: int
    system_info: dict[str, object]


class ThreadsNavigationResponse(TypedDict):
    elements: list[dict[str, object]]
    elements_count: int
    system_info: dict[str, object]


class ThreadsPollGetResponse(TypedDict):
    poll: dict[str, object]
    system_info: dict[str, object]


class ThreadsPollVoteBody(TypedDict, total=False):
    response_id: int
    response_ids: list[int]


class ThreadsPollVoteResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class ThreadsUnreadParams(TypedDict, total=False):
    limit: int
    forum_id: int
    data_limit: int


class ThreadsUnreadResponse(TypedDict):
    threads: list[dict[str, object]]
    data: list[dict[str, object]]
    system_info: dict[str, object]


class ThreadsRecentParams(TypedDict, total=False):
    days: int
    limit: int
    forum_id: int
    data_limit: int


class ThreadsRecentResponse(TypedDict):
    threads: list[dict[str, object]]
    data: list[dict[str, object]]
    system_info: dict[str, object]


class ThreadsFinishResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


# ─── PostsApi Types ────────────────────────────────────────


class PostsListParams(TypedDict, total=False):
    thread_id: int
    page_of_post_id: int
    page: int
    limit: int
    order: Literal["natural", "natural_reverse", "post_likes", "post_likes_reverse"]


class PostsListResponse(TypedDict):
    posts: list[dict[str, object]]
    thread: dict[str, object]
    posts_total: int
    system_info: dict[str, object]


class _PostsCreateBodyRequired(TypedDict):
    post_body: str


class PostsCreateBody(_PostsCreateBodyRequired, total=False):
    thread_id: int
    quote_post_id: int


class PostsCreateResponse(TypedDict):
    post: dict[str, object]
    system_info: dict[str, object]


class PostsGetResponse(TypedDict):
    post: dict[str, object]
    system_info: dict[str, object]


class PostsEditBody(TypedDict, total=False):
    post_body: str


class PostsEditResponse(TypedDict):
    post: dict[str, object]
    system_info: dict[str, object]


class PostsDeleteBody(TypedDict, total=False):
    reason: str


class PostsDeleteResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class PostsLikesParams(TypedDict, total=False):
    page: int
    limit: int


class PostsLikesResponse(TypedDict):
    users: list[dict[str, object]]
    system_info: dict[str, object]


class PostsLikeResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class PostsUnlikeResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class PostsReportreasonsResponse(TypedDict):
    reasons: list[str]
    system_info: dict[str, object]


class PostsReportBody(TypedDict):
    message: str


class PostsReportResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class _PostsCommentsGetParamsRequired(TypedDict):
    post_id: int


class PostsCommentsGetParams(_PostsCommentsGetParamsRequired, total=False):
    before: int
    before_comment: int


class PostsCommentsGetResponse(TypedDict):
    comments: list[dict[str, object]]
    system_info: dict[str, object]


class PostsCommentsCreateBody(TypedDict):
    post_id: int
    comment_body: str


class PostsCommentsCreateResponse(TypedDict):
    comment: dict[str, object]
    system_info: dict[str, object]


class PostsCommentsEditBody(TypedDict):
    post_comment_id: int
    comment_body: str


class PostsCommentsEditResponse(TypedDict):
    comment: dict[str, object]
    system_info: dict[str, object]


class _PostsCommentsDeleteBodyRequired(TypedDict):
    post_comment_id: int


class PostsCommentsDeleteBody(_PostsCommentsDeleteBodyRequired, total=False):
    reason: str


class PostsCommentsDeleteResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class PostsCommentsReportBody(TypedDict):
    post_comment_id: int
    message: str


class PostsCommentsReportResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


# ─── UsersApi Types ────────────────────────────────────────


class UsersListParams(TypedDict, total=False):
    page: int
    limit: int
    fields_include: list[Literal["*", "alerts"]]


class UsersListResponse(TypedDict):
    users: list[dict[str, object]]
    users_total: int
    links: dict[str, object]
    system_info: dict[str, object]


class UsersFieldsResponse(TypedDict):
    fields: list[dict[str, object]]
    system_info: dict[str, object]


class UsersFindParams(TypedDict, total=False):
    username: str
    custom_fields: dict[str, str]
    fields_include: list[Literal["*", "alerts"]]


class UsersFindResponse(TypedDict):
    users: list[dict[str, object]]
    system_info: dict[str, object]


class UsersGetParams(TypedDict, total=False):
    fields_include: list[Literal["*", "alerts"]]


class UsersGetResponse(TypedDict):
    user: dict[str, object]
    system_info: dict[str, object]


class UsersEditBody(TypedDict, total=False):
    username: str
    user_title: str
    display_group_id: int
    display_icon_group_id: int
    display_banner_id: int
    conv_welcome_message: str
    user_dob_day: int
    user_dob_month: int
    user_dob_year: int
    secret_answer: str
    secret_answer_type: int
    short_link: str
    language_id: Literal[1, 2]
    gender: Literal["", "male", "female"]
    timezone: str
    receive_admin_email: bool
    activity_visible: bool
    show_dob_date: bool
    show_dob_year: bool
    hide_username_change_logs: bool
    allow_view_profile: Literal["none", "members", "followed"]
    allow_post_profile: Literal["none", "members", "followed"]
    allow_send_personal_conversation: Literal["none", "members", "followed"]
    allow_invite_group: Literal["none", "members", "followed"]
    allow_receive_news_feed: Literal["none", "members", "followed"]
    alert: dict[str, bool]
    fields: dict[str, object]


class UsersEditResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class UsersClaimsParams(TypedDict, total=False):
    type: Literal["market", "nomarket"]
    claim_state: Literal["active", "solved", "rejected", "settled"]


class UsersClaimsResponse(TypedDict):
    claims: list[dict[str, object]]
    stats: dict[str, object]
    system_info: dict[str, object]


class _UsersAvatarUploadBodyRequired(TypedDict):
    avatar: bytes


class UsersAvatarUploadBody(_UsersAvatarUploadBodyRequired, total=False):
    x: int
    y: int
    crop: int


class UsersAvatarUploadResponse(TypedDict):
    status: str
    message: str
    system_info: dict[str, object]


class UsersAvatarDeleteResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class UsersAvatarCropBody(TypedDict, total=False):
    x: int
    y: int
    crop: int


class UsersAvatarCropResponse(TypedDict):
    status: str
    message: str
    system_info: dict[str, object]


class _UsersBackgroundUploadBodyRequired(TypedDict):
    background: bytes


class UsersBackgroundUploadBody(_UsersBackgroundUploadBodyRequired, total=False):
    x: int
    y: int
    crop: int


class UsersBackgroundUploadResponse(TypedDict):
    status: str
    message: str
    system_info: dict[str, object]


class UsersBackgroundDeleteResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class UsersBackgroundCropBody(TypedDict, total=False):
    x: int
    y: int
    crop: int


class UsersBackgroundCropResponse(TypedDict):
    status: str
    message: str
    system_info: dict[str, object]


class UsersFollowersParams(TypedDict, total=False):
    order: Literal["natural", "follow_date", "follow_date_reverse"]
    page: int
    limit: int


class UsersFollowersResponse(TypedDict):
    users: list[dict[str, object]]
    users_total: int
    links: dict[str, object]
    system_info: dict[str, object]


class UsersFollowResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class UsersUnfollowResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class UsersFollowingsParams(TypedDict, total=False):
    order: Literal["natural", "follow_date", "follow_date_reverse"]
    page: int
    limit: int


class UsersFollowingsResponse(TypedDict):
    users: list[dict[str, object]]
    users_total: int
    system_info: dict[str, object]


class UsersLikesParams(TypedDict, total=False):
    node_id: int
    like_type: Literal["like", "like2"]
    type: Literal["gotten", "given"]
    page: int
    content_type: Literal["post", "post_comment", "profile_post", "profile_post_comment"]
    search_user_id: int
    stats: bool


class UsersLikesResponse(TypedDict):
    page: int
    perPage: int
    contentType: str
    totalLikes: int
    likes: dict[str, object]
    system_info: dict[str, object]


class UsersIgnoredParams(TypedDict, total=False):
    total: bool


class UsersIgnoredResponse(TypedDict):
    users: list[dict[str, object]]
    system_info: dict[str, object]


class UsersIgnoreResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class UsersIgnoreeditParams(TypedDict, total=False):
    ignore_conversations: bool
    ignore_content: bool
    restrict_view_profile: bool


class UsersIgnoreeditResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class UsersUnignoreResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class UsersContentsParams(TypedDict, total=False):
    page: int
    limit: int


class UsersContentsResponse(TypedDict):
    data: list[dict[str, object]]
    data_total: int
    user: dict[str, object]
    links: dict[str, object]
    system_info: dict[str, object]


class UsersTrophiesResponse(TypedDict):
    trophies: list[dict[str, object]]
    system_info: dict[str, object]


class UsersSecretanswertypesResponse(TypedDict):
    data: list[dict[str, object]]
    system_info: dict[str, object]


class UsersSaResetResponse(TypedDict):
    success: bool
    waiting_time: str
    system_info: dict[str, object]


class UsersSaCancelresetResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


# ─── ProfilePostsApi Types ────────────────────────────────────────


class ProfilePostsListParams(TypedDict, total=False):
    posts_user_id: int
    page: int
    limit: int
    fields_include: list[Literal["*", "latest_comments"]]


class ProfilePostsListResponse(TypedDict):
    profile_posts: list[dict[str, object]]
    totalProfilePosts: int
    canPostOnProfile: bool
    links: dict[str, object]
    system_info: dict[str, object]


class ProfilePostsGetResponse(TypedDict):
    profile_post: dict[str, object]
    system_info: dict[str, object]


class ProfilePostsEditBody(TypedDict, total=False):
    post_body: str
    disable_comments: bool


class ProfilePostsEditResponse(TypedDict):
    profile_post: dict[str, object]
    system_info: dict[str, object]


class ProfilePostsDeleteParams(TypedDict, total=False):
    reason: str


class ProfilePostsDeleteResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class ProfilePostsReportreasonsResponse(TypedDict):
    reasons: list[str]
    system_info: dict[str, object]


class ProfilePostsReportBody(TypedDict):
    message: str


class ProfilePostsReportResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class ProfilePostsCreateBody(TypedDict):
    user_id: str | int
    post_body: str


class ProfilePostsCreateResponse(TypedDict):
    profile_post: dict[str, object]
    system_info: dict[str, object]


class ProfilePostsStickResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class ProfilePostsUnstickResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class ProfilePostsLikesResponse(TypedDict):
    users: list[dict[str, object]]
    system_info: dict[str, object]


class ProfilePostsLikeResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class ProfilePostsUnlikeResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class _ProfilePostsCommentsListParamsRequired(TypedDict):
    profile_post_id: int


class ProfilePostsCommentsListParams(_ProfilePostsCommentsListParamsRequired, total=False):
    before: int
    limit: int


class ProfilePostsCommentsListResponse(TypedDict):
    comments: list[dict[str, object]]
    comments_total: int
    profile_post: dict[str, object]
    timeline_user: dict[str, object]
    system_info: dict[str, object]


class ProfilePostsCommentsCreateBody(TypedDict):
    profile_post_id: int
    comment_body: str


class ProfilePostsCommentsCreateResponse(TypedDict):
    comment: dict[str, object]
    system_info: dict[str, object]


class ProfilePostsCommentsEditBody(TypedDict):
    comment_id: int
    comment_body: str


class ProfilePostsCommentsEditResponse(TypedDict):
    comment: dict[str, object]
    system_info: dict[str, object]


class ProfilePostsCommentsDeleteBody(TypedDict):
    comment_id: int


class ProfilePostsCommentsDeleteResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class ProfilePostsCommentsGetResponse(TypedDict):
    comment: dict[str, object]
    system_info: dict[str, object]


class ProfilePostsCommentsReportBody(TypedDict):
    message: str


class ProfilePostsCommentsReportResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


# ─── ConversationsApi Types ────────────────────────────────────────


class ConversationsListParams(TypedDict, total=False):
    folder: Literal[
        "all", "unread", "groups", "market", "market_replacements", "staff", "giveaways", "p2p"
    ]
    page: int
    limit: int


class ConversationsListResponse(TypedDict):
    conversations: list[dict[str, object]]
    can_start: bool
    folders: list[dict[str, object]]
    links: dict[str, object]
    system_info: dict[str, object]


class ConversationsCreateBody(TypedDict, total=False):
    recipient_id: int
    recipients: list[str]
    is_group: bool
    title: str
    open_invite: bool
    allow_edit_messages: bool
    allow_sticky_messages: bool
    allow_delete_own_messages: bool
    message_body: str


class ConversationsCreateResponse(TypedDict):
    conversation: dict[str, object]
    system_info: dict[str, object]


class _ConversationsUpdateBodyRequired(TypedDict):
    conversation_id: int


class ConversationsUpdateBody(_ConversationsUpdateBodyRequired, total=False):
    title: str
    open_invite: bool
    history_open: bool
    allow_edit_messages: bool
    allow_sticky_messages: bool
    allow_delete_own_messages: bool


class ConversationsUpdateResponse(TypedDict):
    conversation: dict[str, object]
    system_info: dict[str, object]


class ConversationsDeleteBody(TypedDict):
    conversation_id: int
    delete_type: Literal["delete", "delete_ignore"]


class ConversationsDeleteResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class ConversationsStartBody(TypedDict):
    user_id: str | int


class ConversationsStartResponse(TypedDict):
    conversation: dict[str, object]
    system_info: dict[str, object]


class ConversationsSaveBody(TypedDict):
    link: str


class ConversationsSaveResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class ConversationsGetResponse(TypedDict):
    conversation: dict[str, object]
    system_info: dict[str, object]


class ConversationsMessagesListParams(TypedDict, total=False):
    page: int
    limit: int
    order: Literal["natural", "natural_reverse"]
    before: int
    after: int


class ConversationsMessagesListResponse(TypedDict):
    messages: list[dict[str, object]]
    messages_total: int
    links: dict[str, object]
    system_info: dict[str, object]


class _ConversationsMessagesCreateBodyRequired(TypedDict):
    message_body: str


class ConversationsMessagesCreateBody(_ConversationsMessagesCreateBodyRequired, total=False):
    reply_message_id: int


class ConversationsMessagesCreateResponse(TypedDict):
    message: dict[str, object]
    system_info: dict[str, object]


class ConversationsSearchBody(TypedDict, total=False):
    q: str
    conversation_id: int
    search_recipients: bool


class ConversationsSearchResponse(TypedDict):
    conversations: list[dict[str, object]]
    recipients: bool
    system_info: dict[str, object]


class ConversationsMessagesGetResponse(TypedDict):
    message: dict[str, object]
    system_info: dict[str, object]


class ConversationsMessagesEditBody(TypedDict):
    message_body: str


class ConversationsMessagesEditResponse(TypedDict):
    message: dict[str, object]
    system_info: dict[str, object]


class ConversationsMessagesDeleteResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class ConversationsInviteBody(TypedDict):
    recipients: list[str]


class ConversationsInviteResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class ConversationsKickBody(TypedDict):
    user_id: int


class ConversationsKickResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class ConversationsReadResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class ConversationsReadallResponse(TypedDict):
    status: str
    message: str
    system_info: dict[str, object]


class ConversationsMessagesStickResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class ConversationsMessagesUnstickResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class ConversationsStarResponse(TypedDict):
    status: str
    message: str
    system_info: dict[str, object]


class ConversationsUnstarResponse(TypedDict):
    status: str
    message: str
    system_info: dict[str, object]


class ConversationsAlertsEnableResponse(TypedDict):
    status: str
    message: str
    system_info: dict[str, object]


class ConversationsAlertsDisableResponse(TypedDict):
    status: str
    message: str
    system_info: dict[str, object]


# ─── NotificationsApi Types ────────────────────────────────────────


class NotificationsListParams(TypedDict, total=False):
    type: Literal["market", "nomarket"]
    page: int
    limit: int


class NotificationsListResponse(TypedDict):
    notifications: list[dict[str, object]]
    notifications_total: int
    links: dict[str, object]
    system_info: dict[str, object]


class NotificationsGetResponse(TypedDict):
    notification_id: int
    notification: dict[str, object]
    system_info: dict[str, object]


class NotificationsReadBody(TypedDict, total=False):
    notification_id: int


class NotificationsReadResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


# ─── TagsApi Types ────────────────────────────────────────


class TagsPopularResponse(TypedDict):
    tags: dict[str, object]
    system_info: dict[str, object]


class TagsListParams(TypedDict, total=False):
    page: int
    limit: int


class TagsListResponse(TypedDict):
    tags: dict[str, object]
    tags_total: int
    links: dict[str, object]
    system_info: dict[str, object]


class TagsGetParams(TypedDict, total=False):
    page: int
    limit: int


class TagsGetResponse(TypedDict):
    tag: dict[str, object]
    tagged: list[dict[str, object]]
    tagged_total: int
    links: dict[str, object]
    system_info: dict[str, object]


class TagsFindParams(TypedDict):
    tag: str


class TagsFindResponse(TypedDict):
    tags: list[str]
    ids: list[int]
    system_info: dict[str, object]


# ─── SearchApi Types ────────────────────────────────────────


class SearchAllBody(TypedDict, total=False):
    q: str
    tag: str
    forum_id: int
    user_id: str | int
    page: int
    limit: int


class SearchAllResponse(TypedDict):
    data: list[dict[str, object]]
    data_total: int
    users: list[dict[str, object]]
    links: dict[str, object]
    system_info: dict[str, object]


class SearchThreadsBody(TypedDict, total=False):
    q: str
    tag: str
    forum_id: int
    user_id: str | int
    page: int
    limit: int
    data_limit: int


class SearchThreadsResponse(TypedDict):
    data: list[dict[str, object]]
    data_total: int
    links: dict[str, object]
    system_info: dict[str, object]


class SearchPostsBody(TypedDict, total=False):
    q: str
    tag: str
    forum_id: int
    user_id: str | int
    page: int
    limit: int
    data_limit: int


class SearchPostsResponse(TypedDict):
    data: list[dict[str, object]]
    data_total: int
    links: dict[str, object]
    system_info: dict[str, object]


class SearchUsersBody(TypedDict, total=False):
    q: str


class SearchUsersResponse(TypedDict):
    users: list[dict[str, object]]
    system_info: dict[str, object]


class SearchProfilepostsBody(TypedDict, total=False):
    q: str
    user_id: int
    page: int
    limit: int


class SearchProfilepostsResponse(TypedDict):
    data: list[dict[str, object]]
    data_total: int
    links: dict[str, object]
    system_info: dict[str, object]


class SearchTaggedBody(TypedDict, total=False):
    tag: str
    tags: list[str]
    page: int
    limit: int


class SearchTaggedResponse(TypedDict):
    data: list[dict[str, object]]
    data_total: int
    search_tags: dict[str, object]
    system_info: dict[str, object]


class SearchResultsBody(TypedDict, total=False):
    page: int
    limit: int


class SearchResultsResponse(TypedDict):
    data: list[dict[str, object]]
    data_total: int
    search_tags: dict[str, object]
    system_info: dict[str, object]


# ─── BatchApi Types ────────────────────────────────────────


BatchExecuteBody = list[dict[str, object]]


class BatchExecuteResponse(TypedDict):
    jobs: dict[str, object]


# ─── ChatboxApi Types ────────────────────────────────────────


class ChatboxIndexParams(TypedDict, total=False):
    room_id: Literal[1, 2, 3, 4, 13]


class ChatboxIndexResponse(TypedDict):
    rooms: list[dict[str, object]]
    ban: object
    ignore: list[dict[str, object]]
    permissions: dict[str, object]
    commands: list[str]
    roomsOnline: dict[str, object]
    system_info: dict[str, object]


class _ChatboxGetmessagesParamsRequired(TypedDict):
    room_id: Literal[1, 2, 3, 4, 13]


class ChatboxGetmessagesParams(_ChatboxGetmessagesParamsRequired, total=False):
    before_message_id: int


class ChatboxGetmessagesResponse(TypedDict):
    messages: list[dict[str, object]]
    system_info: dict[str, object]


class _ChatboxPostmessageBodyRequired(TypedDict):
    room_id: Literal[1, 2, 3, 4, 13]
    message: str


class ChatboxPostmessageBody(_ChatboxPostmessageBodyRequired, total=False):
    reply_message_id: int


class ChatboxPostmessageResponse(TypedDict):
    message: dict[str, object]
    system_info: dict[str, object]


class ChatboxEditmessageBody(TypedDict):
    message_id: int
    message: str


class ChatboxEditmessageResponse(TypedDict):
    message: dict[str, object]
    system_info: dict[str, object]


class ChatboxDeletemessageBody(TypedDict):
    message_id: int


class ChatboxDeletemessageResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class ChatboxOnlineParams(TypedDict):
    room_id: Literal[1, 2, 3, 4, 13]


class ChatboxOnlineResponse(TypedDict):
    users: list[dict[str, object]]
    system_info: dict[str, object]


class ChatboxReportreasonsParams(TypedDict):
    message_id: int


class ChatboxReportreasonsResponse(TypedDict):
    reasons: list[str]
    system_info: dict[str, object]


class ChatboxReportBody(TypedDict):
    message_id: int
    reason: str


class ChatboxReportResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class ChatboxGetleaderboardParams(TypedDict, total=False):
    duration: Literal["day", "week", "month"]


class ChatboxGetleaderboardResponse(TypedDict):
    leaderboard: list[dict[str, object]]
    system_info: dict[str, object]


class ChatboxGetignoreResponse(TypedDict):
    ignored: list[dict[str, object]]
    system_info: dict[str, object]


class ChatboxPostignoreBody(TypedDict):
    user_id: str | int


class ChatboxPostignoreResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


class ChatboxDeleteignoreBody(TypedDict):
    user_id: str | int


class ChatboxDeleteignoreResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: dict[str, object]


# ─── FormsApi Types ────────────────────────────────────────


class FormsListParams(TypedDict, total=False):
    page: int


class FormsListResponse(TypedDict):
    forms: list[dict[str, object]]
    formsPerPage: int
    page: int
    totalForms: int
    system_info: dict[str, object]


class FormsCreateBody(TypedDict):
    form_id: Literal[1, 3]
    fields: dict[str, object]


class FormsCreateResponse(TypedDict):
    message: str
    content: dict[str, object]
    system_info: dict[str, object]
