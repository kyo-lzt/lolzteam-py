# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Literal, TypedDict

# ─── Component Schemas ────────────────────────────────────────


UserIDModel = str | int


class Resp_NotificationModelLinks(TypedDict):
    content: str
    creator_avatar: str


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
    links: Resp_NotificationModelLinks
    notification_html: str


class Resp_LinkModelLinks(TypedDict):
    target: str
    detail: str


class Resp_LinkModelPermissions(TypedDict):
    view: bool


class Resp_LinkModel(TypedDict):
    link_id: int
    link_title: str
    link_description: str
    links: Resp_LinkModelLinks
    permissions: Resp_LinkModelPermissions


RoomIDModel = Literal[1, 2, 3, 4, 13]


class Resp_ChatboxMessageModelRoom(TypedDict):
    can_report: bool
    eng: bool
    market: bool
    room_id: int
    title: str


class Resp_ChatboxMessageModelUserRenderedAvatars(TypedDict):
    l: str
    m: str
    s: str


class Resp_ChatboxMessageModelUserRendered(TypedDict):
    username: str
    avatars: Resp_ChatboxMessageModelUserRenderedAvatars
    link: str


class Resp_ChatboxMessageModelUserUniq_banner(TypedDict):
    banner_css: str
    banner_text: str
    banner_icon: str
    username_icon: str


class Resp_ChatboxMessageModelUser(TypedDict):
    avatar_date: int
    background_date: int
    contest_count: int
    custom_title: str
    display_banner_id: int
    display_icon_group_id: int
    display_style_group_id: int
    is_admin: bool
    is_banned: bool
    is_moderator: bool
    is_staff: bool
    last_activity: int
    like2_count: int
    like_count: int
    message_count: int
    register_date: int
    rendered: Resp_ChatboxMessageModelUserRendered
    short_link: str
    trophy_points: int
    uniq_banner: Resp_ChatboxMessageModelUserUniq_banner
    uniq_username_css: str
    user_id: int
    username: str


class Resp_ChatboxMessageModel(TypedDict):
    can_report: bool
    date: int
    is_deleted: bool
    message: str
    message_id: int
    messageJson: str
    messageRaw: str
    room: Resp_ChatboxMessageModelRoom
    user: Resp_ChatboxMessageModelUser


class Resp_UserModelLinks(TypedDict):
    permalink: str
    detail: str
    avatar: str
    avatar_big: str
    avatar_small: str
    followers: str
    followings: str
    ignore: str
    background_l: str
    background_m: str
    status: str
    timeline: str


class Resp_UserModelPermissions(TypedDict):
    edit: bool
    follow: bool
    ignore: bool
    profile_post: bool


class Resp_UserModelUser_groups(TypedDict):
    user_group_id: int
    user_group_title: str
    user_group_title_en: str
    user_group_banner_css_class: str
    user_group_banner_text: str
    user_group_banner_text_en: str
    display_group_selectable: bool
    display_banner_selectable: bool
    display_icon_selectable: bool
    is_primary_group: bool
    user_group_icon_class: str


class Resp_UserModelFieldsChoices(TypedDict):
    key: str
    value: str


class _Resp_UserModelFieldsRequired(TypedDict):
    id: str
    title: str
    description: str
    position: str
    is_required: bool
    is_multi_choice: bool
    choices: list[Resp_UserModelFieldsChoices]
    values: list[object]


class Resp_UserModelFields(_Resp_UserModelFieldsRequired, total=False):
    value: str


class Resp_UserModelUser_external_authentications(TypedDict):
    provider: str
    provider_key: str


class Resp_UserModelSelf_permissions(TypedDict):
    create_conversation: bool


class Resp_UserModelEdit_permissions(TypedDict):
    password: bool
    user_email: bool
    username: bool
    user_title: bool
    short_link: bool
    hide_username_logs: bool
    primary_group_id: bool
    secondary_group_ids: bool
    user_dob_day: bool
    user_dob_month: bool
    user_dob_year: bool
    fields: bool


class Resp_UserModelBirthdayTimeStamp(TypedDict):
    date: str
    timezone_type: int
    timezone: str


class Resp_UserModelBirthday(TypedDict):
    age: int
    timeStamp: Resp_UserModelBirthdayTimeStamp
    format: str


class Resp_UserModelUser_followingUsers(TypedDict):
    user_id: int
    username: str
    username_html: str
    avatar: str


class Resp_UserModelUser_following(TypedDict):
    users: list[Resp_UserModelUser_followingUsers]
    count: int


class Resp_UserModelUser_followersUsers(TypedDict):
    user_id: int
    username: str
    username_html: str
    avatar: str


class Resp_UserModelUser_followers(TypedDict):
    users: list[Resp_UserModelUser_followersUsers]
    count: int


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
    links: Resp_UserModelLinks
    permissions: Resp_UserModelPermissions
    user_is_ignored: bool
    user_is_visitor: bool
    user_group_id: int
    curator_titles: list[str]
    user_groups: list[Resp_UserModelUser_groups]
    fields: list[Resp_UserModelFields]
    user_timezone_offset: int
    user_external_authentications: list[Resp_UserModelUser_external_authentications]
    self_permissions: Resp_UserModelSelf_permissions
    edit_permissions: Resp_UserModelEdit_permissions
    birthday: Resp_UserModelBirthday
    secret_answer_rendered: str
    secret_answer_first_letter: str
    user_following: Resp_UserModelUser_following
    user_followers: Resp_UserModelUser_followers
    banner: str


class Resp_ThreadModelFirst_postLinks(TypedDict):
    permalink: str
    detail: str
    thread: str
    poster: str
    likes: str
    report: str
    poster_avatar: str


class Resp_ThreadModelFirst_postPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    reply: bool
    like: bool
    report: bool


class Resp_ThreadModelFirst_post(TypedDict):
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
    post_is_liked: bool
    links: Resp_ThreadModelFirst_postLinks
    permissions: Resp_ThreadModelFirst_postPermissions
    thread_is_deleted: bool


Resp_ThreadModelThread_tags = TypedDict(
    "Resp_ThreadModelThread_tags",
    {
        "97491": str,
        "193431": str,
        "206": str,
    },
)


class Resp_ThreadModelLinks(TypedDict):
    permalink: str
    detail: str
    followers: str
    forum: str
    posts: str
    first_poster: str
    first_poster_avatar: str
    first_post: str
    last_post: str


class Resp_ThreadModelPermissionsBump(TypedDict):
    can: bool
    available_count: int
    error: object
    next_available_time: object


class Resp_ThreadModelPermissions(TypedDict):
    view: bool
    delete: bool
    follow: bool
    post: bool
    edit: bool
    edit_title: bool
    edit_tags: bool
    bump: Resp_ThreadModelPermissionsBump


class Resp_ThreadModelRestrictions(TypedDict):
    reply_delay: int
    max_reply_count: int


class Resp_ThreadModelLast_postLinks(TypedDict):
    permalink: str
    detail: str
    thread: str
    poster: str
    likes: str
    report: str
    poster_avatar: str


class Resp_ThreadModelLast_postPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    reply: bool
    like: bool
    report: bool


class Resp_ThreadModelLast_post(TypedDict):
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
    post_is_liked: bool
    links: Resp_ThreadModelLast_postLinks
    permissions: Resp_ThreadModelLast_postPermissions
    thread_is_deleted: bool


class Resp_ThreadModelContestPermissions(TypedDict):
    can_finish: bool
    can_participate: bool
    can_participate_error: str
    can_view_user_list: bool


class Resp_ThreadModelContest(TypedDict):
    type: str
    finish_date: int
    now_count_members: int
    needed_members: int
    is_finished: int
    count_winners: int
    require_like_count: int
    require_total_like_count: int
    prize_type: str
    prize_type_phrase: str
    prize_data: int
    is_money_places: int
    chance_to_win: float
    winners: list[int]
    already_participate: bool
    permissions: Resp_ThreadModelContestPermissions


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
    first_post: Resp_ThreadModelFirst_post
    thread_prefixes: list[object]
    thread_tags: Resp_ThreadModelThread_tags
    links: Resp_ThreadModelLinks
    permissions: Resp_ThreadModelPermissions
    node_title: str
    restrictions: Resp_ThreadModelRestrictions
    last_post: Resp_ThreadModelLast_post
    contest: Resp_ThreadModelContest


class Resp_PostModelLinks(TypedDict):
    permalink: str
    detail: str
    thread: str
    poster: str
    likes: str
    report: str
    poster_avatar: str


class Resp_PostModelPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    reply: bool
    like: bool
    report: bool


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
    links: Resp_PostModelLinks
    permissions: Resp_PostModelPermissions
    thread_is_deleted: bool


class Resp_PostCommentModelLinks(TypedDict):
    permalink: str
    detail: str
    post: str
    thread: str
    poster: str
    likes: str
    report: str
    poster_avatar: str


class Resp_PostCommentModelPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    reply: bool
    like: bool
    report: bool


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
    links: Resp_PostCommentModelLinks
    permissions: Resp_PostCommentModelPermissions


class Resp_ProfilePostModelLinks(TypedDict):
    permalink: str
    detail: str
    timeline: str
    timeline_user: str
    poster: str
    likes: str
    comments: str
    report: str
    poster_avatar: str


class Resp_ProfilePostModelPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    like: bool
    comment: bool
    report: bool
    stick: bool


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
    links: Resp_ProfilePostModelLinks
    permissions: Resp_ProfilePostModelPermissions
    timeline_user: Resp_UserModel


class Resp_ProfilePostCommentModelLinks(TypedDict):
    detail: str
    profile_post: str
    timeline: str
    timeline_user: str
    poster: str
    poster_avatar: str


class Resp_ProfilePostCommentModelPermissions(TypedDict):
    view: bool
    delete: bool


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
    links: Resp_ProfilePostCommentModelLinks
    permissions: Resp_ProfilePostCommentModelPermissions


class Resp_ConversationModelPermissions(TypedDict):
    view: bool
    reply: bool
    invite: bool
    manage_invite_links: bool
    kick: bool
    upload_avatar: bool
    editOwnPost: bool
    stickyMessages: bool


class Resp_ConversationModelRecipient(TypedDict):
    user_id: int
    username: str
    username_html: str
    last_activity: int
    is_online: bool
    contacts_changed: bool
    avatar: str


class Resp_ConversationModelRecipients(TypedDict):
    user_id: int
    username: str
    username_html: str
    last_activity: int
    is_online: bool
    contacts_changed: bool
    avatar: str


class Resp_ConversationModelLinks(TypedDict):
    permalink: str
    detail: str
    messages: str
    avatar: str


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
    permissions: Resp_ConversationModelPermissions
    conversation_message_count: int
    conversation_is_new: bool
    creator_is_ignored: bool
    conversation_is_open: bool
    conversation_is_deleted: bool
    recipient: Resp_ConversationModelRecipient
    recipients: list[Resp_ConversationModelRecipients]
    links: Resp_ConversationModelLinks


class Resp_ConversationMessageModelLinks(TypedDict):
    detail: str
    conversation: str
    creator: str
    creator_avatar: str


Resp_ConversationMessageModelPermissions = TypedDict(
    "Resp_ConversationMessageModelPermissions",
    {
        "view": bool,
        "edit": bool,
        "delete": bool,
        "stick-unstick": bool,
    },
)


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
    links: Resp_ConversationMessageModelLinks
    permissions: Resp_ConversationMessageModelPermissions


class Resp_SystemInfo(TypedDict):
    visitor_id: int
    time: int


# ─── OAuthApi Types ────────────────────────────────────────


class OAuthTokenClientCredentialsBody(TypedDict):
    grant_type: Literal["client_credentials"]
    client_id: str
    client_secret: str
    scope: list[Literal["basic", "read", "post", "conversate", "market", "payment", "invoice"]]


class OAuthTokenAuthorizationCodeBody(TypedDict):
    grant_type: Literal["authorization_code"]
    code: str
    client_id: str
    client_secret: str
    redirect_uri: str
    scope: list[Literal["basic", "read", "post", "conversate", "market", "payment", "invoice"]]


class OAuthTokenRefreshTokenBody(TypedDict):
    grant_type: Literal["refresh_token"]
    refresh_token: str
    client_id: str
    client_secret: str


class OAuthTokenPasswordBody(TypedDict):
    grant_type: Literal["password"]
    username: str
    password: str
    client_id: str
    client_secret: str
    scope: list[Literal["basic", "read", "post", "conversate", "market", "payment", "invoice"]]


OAuthTokenBody = (
    OAuthTokenClientCredentialsBody
    | OAuthTokenAuthorizationCodeBody
    | OAuthTokenRefreshTokenBody
    | OAuthTokenPasswordBody
)


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
    system_info: Resp_SystemInfo


# ─── CategoriesApi Types ────────────────────────────────────────


class CategoriesListParams(TypedDict, total=False):
    parent_category_id: int
    parent_forum_id: int
    order: Literal["natural", "list"]


CategoriesListResponseCategoriesLinks = TypedDict(
    "CategoriesListResponseCategoriesLinks",
    {
        "permalink": str,
        "detail": str,
        "sub-categories": str,
        "sub-forums": str,
    },
)


class CategoriesListResponseCategoriesPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool


class CategoriesListResponseCategories(TypedDict):
    category_id: int
    category_title: str
    category_description: str
    links: CategoriesListResponseCategoriesLinks
    permissions: CategoriesListResponseCategoriesPermissions


class CategoriesListResponse(TypedDict):
    categories: list[CategoriesListResponseCategories]
    categories_total: int
    system_info: Resp_SystemInfo


CategoriesGetResponseCategoryLinks = TypedDict(
    "CategoriesGetResponseCategoryLinks",
    {
        "permalink": str,
        "detail": str,
        "sub-categories": str,
        "sub-forums": str,
    },
)


class CategoriesGetResponseCategoryPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool


class CategoriesGetResponseCategory(TypedDict):
    category_id: int
    category_title: str
    category_description: str
    links: CategoriesGetResponseCategoryLinks
    permissions: CategoriesGetResponseCategoryPermissions


class CategoriesGetResponse(TypedDict):
    category: CategoriesGetResponseCategory
    system_info: Resp_SystemInfo


# ─── ForumsApi Types ────────────────────────────────────────


class ForumsListParams(TypedDict, total=False):
    parent_category_id: int
    parent_forum_id: int
    order: Literal["natural", "list"]


class ForumsListResponseForumsForum_prefixesGroup_prefixes(TypedDict):
    prefix_id: int
    prefix_title: str


class ForumsListResponseForumsForum_prefixes(TypedDict):
    group_title: str
    group_prefixes: list[ForumsListResponseForumsForum_prefixesGroup_prefixes]


ForumsListResponseForumsLinks = TypedDict(
    "ForumsListResponseForumsLinks",
    {
        "permalink": str,
        "detail": str,
        "sub-categories": str,
        "sub-forums": str,
        "threads": str,
        "followers": str,
    },
)


class ForumsListResponseForumsPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    create_thread: bool
    tag_thread: bool
    follow: bool


class ForumsListResponseForums(TypedDict):
    forum_id: int
    forum_title: str
    forum_description: str
    forum_thread_count: int
    forum_post_count: int
    forum_prefixes: list[ForumsListResponseForumsForum_prefixes]
    thread_default_prefix_id: int
    thread_prefix_is_required: bool
    links: ForumsListResponseForumsLinks
    permissions: ForumsListResponseForumsPermissions
    forum_is_followed: bool


class ForumsListResponseTabs(TypedDict):
    link_title: str
    isDefault: bool
    title: str
    isHidden: bool


class ForumsListResponse(TypedDict):
    forums: list[ForumsListResponseForums]
    forums_total: int
    tabs: list[ForumsListResponseTabs]
    system_info: Resp_SystemInfo


ForumsGroupedResponseData00Links = TypedDict(
    "ForumsGroupedResponseData00Links",
    {
        "permalink": str,
        "detail": str,
        "sub-categories": str,
        "sub-forums": str,
        "threads": str,
        "followers": str,
    },
)


class ForumsGroupedResponseData00Permissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    create_thread: bool
    tag_thread: bool
    follow: bool


class ForumsGroupedResponseData00(TypedDict):
    forum_id: int
    forum_title: str
    forum_description: str
    forum_thread_count: int
    forum_post_count: int
    parent_node_id: int
    links: ForumsGroupedResponseData00Links
    permissions: ForumsGroupedResponseData00Permissions
    forum_is_followed: bool


ForumsGroupedResponseData0 = TypedDict(
    "ForumsGroupedResponseData0",
    {
        "0": ForumsGroupedResponseData00,
    },
)


ForumsGroupedResponseData = TypedDict(
    "ForumsGroupedResponseData",
    {
        "0": ForumsGroupedResponseData0,
    },
)


class ForumsGroupedResponseTabs(TypedDict):
    link_title: str
    isDefault: bool
    title: str
    isHidden: bool


class ForumsGroupedResponse(TypedDict):
    data: ForumsGroupedResponseData
    tabs: list[ForumsGroupedResponseTabs]
    system_info: Resp_SystemInfo


class ForumsGetResponseForumForum_prefixesGroup_prefixes(TypedDict):
    prefix_id: int
    prefix_title: str


class ForumsGetResponseForumForum_prefixes(TypedDict):
    group_title: str
    group_prefixes: list[ForumsGetResponseForumForum_prefixesGroup_prefixes]


ForumsGetResponseForumLinks = TypedDict(
    "ForumsGetResponseForumLinks",
    {
        "permalink": str,
        "detail": str,
        "sub-categories": str,
        "sub-forums": str,
        "threads": str,
        "followers": str,
    },
)


class ForumsGetResponseForumPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    create_thread: bool
    upload_attachment: bool
    tag_thread: bool
    follow: bool


class ForumsGetResponseForum(TypedDict):
    forum_id: int
    forum_title: str
    forum_description: str
    forum_thread_count: int
    forum_post_count: int
    forum_prefixes: list[ForumsGetResponseForumForum_prefixes]
    thread_default_prefix_id: int
    thread_prefix_is_required: bool
    links: ForumsGetResponseForumLinks
    permissions: ForumsGetResponseForumPermissions
    forum_is_followed: bool


class ForumsGetResponse(TypedDict):
    forum: ForumsGetResponseForum
    system_info: Resp_SystemInfo


class ForumsFollowersResponseUsersFollow(TypedDict):
    post: bool
    alert: bool
    email: bool


class ForumsFollowersResponseUsers(TypedDict):
    user_id: int
    username: str
    follow: ForumsFollowersResponseUsersFollow


class ForumsFollowersResponse(TypedDict):
    users: list[ForumsFollowersResponseUsers]
    system_info: Resp_SystemInfo


class ForumsFollowBody(TypedDict, total=False):
    post: bool
    alert: bool
    email: bool
    prefix_ids: list[int]
    minimal_contest_amount: int


class ForumsFollowResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ForumsUnfollowResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ForumsFollowedParams(TypedDict, total=False):
    total: bool


class ForumsFollowedResponseForumsForum_prefixesGroup_prefixes(TypedDict):
    prefix_id: int
    prefix_title: str


class ForumsFollowedResponseForumsForum_prefixes(TypedDict):
    group_title: str
    group_prefixes: list[ForumsFollowedResponseForumsForum_prefixesGroup_prefixes]


ForumsFollowedResponseForumsLinks = TypedDict(
    "ForumsFollowedResponseForumsLinks",
    {
        "permalink": str,
        "detail": str,
        "sub-categories": str,
        "sub-forums": str,
        "threads": str,
        "followers": str,
    },
)


class ForumsFollowedResponseForumsPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    create_thread: bool
    upload_attachment: bool
    tag_thread: bool
    follow: bool


class ForumsFollowedResponseForumsFollow(TypedDict):
    post: bool
    alert: bool
    email: bool


class ForumsFollowedResponseForums(TypedDict):
    forum_id: int
    forum_title: str
    forum_description: str
    forum_thread_count: int
    forum_post_count: int
    forum_prefixes: list[ForumsFollowedResponseForumsForum_prefixes]
    thread_default_prefix_id: int
    thread_prefix_is_required: bool
    links: ForumsFollowedResponseForumsLinks
    permissions: ForumsFollowedResponseForumsPermissions
    forum_is_followed: bool
    follow: ForumsFollowedResponseForumsFollow


class ForumsFollowedResponse(TypedDict):
    forums: list[ForumsFollowedResponseForums]
    system_info: Resp_SystemInfo


ForumsGetfeedoptionsResponseForumsLinks = TypedDict(
    "ForumsGetfeedoptionsResponseForumsLinks",
    {
        "permalink": str,
        "detail": str,
        "sub-categories": str,
        "sub-forums": str,
        "threads": str,
        "followers": str,
    },
)


class ForumsGetfeedoptionsResponseForumsPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    create_thread: bool
    tag_thread: bool
    follow: bool


class ForumsGetfeedoptionsResponseForums(TypedDict):
    forum_id: int
    forum_title: str
    forum_description: str
    parent_node_id: int
    links: ForumsGetfeedoptionsResponseForumsLinks
    permissions: ForumsGetfeedoptionsResponseForumsPermissions
    forum_is_followed: bool
    has_children: bool


class ForumsGetfeedoptionsResponse(TypedDict):
    forums: list[ForumsGetfeedoptionsResponseForums]
    excluded_forums_ids: list[int]
    default_excluded_forums_ids: list[int]
    keywords: str
    system_info: Resp_SystemInfo


class ForumsEditfeedoptionsBody(TypedDict, total=False):
    node_ids: list[int]
    keywords: list[str]


class ForumsEditfeedoptionsResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


# ─── LinksApi Types ────────────────────────────────────────


LinksListResponse = TypedDict(
    "LinksListResponse",
    {
        "link-forums": list[Resp_LinkModel],
        "link-forums_total": int,
        "system_info": Resp_SystemInfo,
    },
)


LinksGetResponse = TypedDict(
    "LinksGetResponse",
    {
        "link-forum": Resp_LinkModel,
        "system_info": Resp_SystemInfo,
    },
)


# ─── PagesApi Types ────────────────────────────────────────


class PagesListParams(TypedDict, total=False):
    parent_page_id: int
    order: Literal["natural", "list"]


PagesListResponsePagesLinks = TypedDict(
    "PagesListResponsePagesLinks",
    {
        "permalink": str,
        "detail": str,
        "sub-pages": str,
    },
)


class PagesListResponsePagesPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool


class PagesListResponsePages(TypedDict):
    page_id: int
    page_title: str
    page_description: str
    links: PagesListResponsePagesLinks
    permissions: PagesListResponsePagesPermissions


class PagesListResponse(TypedDict):
    pages: list[PagesListResponsePages]
    pages_total: int
    system_info: Resp_SystemInfo


PagesGetResponsePageLinks = TypedDict(
    "PagesGetResponsePageLinks",
    {
        "permalink": str,
        "detail": str,
        "sub-pages": str,
    },
)


class PagesGetResponsePagePermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool


class PagesGetResponsePage(TypedDict):
    page_id: int
    page_title: str
    page_description: str
    page_view_count: int
    links: PagesGetResponsePageLinks
    permissions: PagesGetResponsePagePermissions
    page_html: str


class PagesGetResponse(TypedDict):
    page: PagesGetResponsePage
    system_info: Resp_SystemInfo


# ─── NavigationApi Types ────────────────────────────────────────


class NavigationListParams(TypedDict, total=False):
    parent: int


NavigationListResponseElementsLinks = TypedDict(
    "NavigationListResponseElementsLinks",
    {
        "permalink": str,
        "detail": str,
        "sub-categories": str,
        "sub-forums": str,
        "sub-elements": str,
    },
)


class NavigationListResponseElementsPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool


class NavigationListResponseElements(TypedDict):
    category_id: int
    category_title: str
    category_description: str
    links: NavigationListResponseElementsLinks
    permissions: NavigationListResponseElementsPermissions
    navigation_type: str
    navigation_id: int
    navigation_parent_id: int
    has_sub_elements: bool


class NavigationListResponse(TypedDict):
    elements: list[NavigationListResponseElements]
    elements_count: int
    system_info: Resp_SystemInfo


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


ThreadsListResponseForumLinks = TypedDict(
    "ThreadsListResponseForumLinks",
    {
        "permalink": str,
        "detail": str,
        "sub-categories": str,
        "sub-forums": str,
        "threads": str,
        "followers": str,
    },
)


class ThreadsListResponseForumPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    create_thread: bool
    upload_attachment: bool
    tag_thread: bool
    follow: bool


class ThreadsListResponseForum(TypedDict):
    forum_id: int
    forum_title: str
    forum_description: str
    forum_thread_count: int
    forum_post_count: int
    forum_prefixes: list[object]
    thread_default_prefix_id: int
    thread_prefix_is_required: bool
    links: ThreadsListResponseForumLinks
    permissions: ThreadsListResponseForumPermissions
    forum_is_followed: bool


class ThreadsListResponseLinks(TypedDict):
    pages: int
    page: int
    next: str


class ThreadsListResponse(TypedDict):
    threads: list[Resp_ThreadModel]
    forum: ThreadsListResponseForum
    threads_total: int
    links: ThreadsListResponseLinks
    system_info: Resp_SystemInfo


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
    reply_group: Literal[0, 2, 21, 22, 23, 60, 351]  # default: 2
    comment_ignore_group: bool
    dont_alert_followers: bool
    schedule_date: str
    schedule_time: str
    watch_thread_state: bool
    watch_thread: bool
    watch_thread_email: bool


ThreadsCreateBody_DEFAULTS: dict[str, object] = {
    "reply_group": 2,
}


class ThreadsCreateResponse(TypedDict):
    thread: Resp_ThreadModel
    system_info: Resp_SystemInfo


class _ThreadsCreatecontestBodyRequired(TypedDict):
    post_body: str
    contest_type: Literal["by_finish_date"]  # default: "by_finish_date"
    prize_type: Literal["money", "upgrades"]
    require_like_count: int
    require_total_like_count: int


class ThreadsCreatecontestBody(_ThreadsCreatecontestBodyRequired, total=False):
    title: str
    title_en: str
    length_value: int
    length_option: Literal["minutes", "hours", "days"]
    count_winners: int
    prize_data_money: float
    is_money_places: bool
    prize_data_places: list[float]
    prize_data_upgrade: Literal[1, 6, 12, 14, 17, 19, 20, 21, 22]
    secret_answer: str
    tags: list[str]
    reply_group: Literal[0, 2, 21, 22, 23, 60, 351]  # default: 2
    comment_ignore_group: bool
    dont_alert_followers: bool
    hide_contacts: bool
    allow_ask_hidden_content: bool
    schedule_date: str
    schedule_time: str
    watch_thread_state: bool
    watch_thread: bool
    watch_thread_email: bool


ThreadsCreatecontestBody_DEFAULTS: dict[str, object] = {
    "contest_type": "by_finish_date",
    "reply_group": 2,
}


class ThreadsCreatecontestResponse(TypedDict):
    thread: Resp_ThreadModel
    system_info: Resp_SystemInfo


class _ThreadsClaimBodyRequired(TypedDict):
    as_responder: str
    as_is_market_deal: bool
    as_amount: float
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
    reply_group: Literal[0, 2, 21, 22, 23, 60, 351]  # default: 2
    comment_ignore_group: bool
    dont_alert_followers: bool
    schedule_date: str
    schedule_time: str
    watch_thread_state: bool
    watch_thread: bool
    watch_thread_email: bool


ThreadsClaimBody_DEFAULTS: dict[str, object] = {
    "reply_group": 2,
}


class ThreadsClaimResponse(TypedDict):
    thread: Resp_ThreadModel
    system_info: Resp_SystemInfo


class ThreadsGetParams(TypedDict, total=False):
    fields_include: list[Literal["*", "latest_posts"]]


class ThreadsGetResponse(TypedDict):
    thread: Resp_ThreadModel
    system_info: Resp_SystemInfo


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
    thread: Resp_ThreadModel
    system_info: Resp_SystemInfo


class ThreadsDeleteBody(TypedDict, total=False):
    reason: str


class ThreadsDeleteResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


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
    system_info: Resp_SystemInfo


class ThreadsBumpResponse(TypedDict):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ThreadsHideResponse(TypedDict):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ThreadsStarResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ThreadsUnstarResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ThreadsFollowersResponseUsersFollow(TypedDict):
    alert: bool
    email: bool


class ThreadsFollowersResponseUsers(TypedDict):
    user_id: int
    username: str
    follow: ThreadsFollowersResponseUsersFollow


class ThreadsFollowersResponse(TypedDict):
    users: list[ThreadsFollowersResponseUsers]
    system_info: Resp_SystemInfo


class ThreadsFollowBody(TypedDict, total=False):
    email: bool


class ThreadsFollowResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ThreadsUnfollowResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ThreadsFollowedParams(TypedDict, total=False):
    total: bool
    fields_include: list[Literal["*", "latest_posts"]]


class ThreadsFollowedResponseThreadsFirst_postLike_users(TypedDict):
    user_id: int
    username: str
    display_style_group_id: int
    is_banned: int
    uniq_username_css: str


class ThreadsFollowedResponseThreadsFirst_postLinks(TypedDict):
    permalink: str
    detail: str
    thread: str
    poster: str
    likes: str
    report: str
    attachments: str
    poster_avatar: str


class ThreadsFollowedResponseThreadsFirst_postPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    reply: bool
    like: bool
    report: bool
    upload_attachment: bool


class ThreadsFollowedResponseThreadsFirst_post(TypedDict):
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
    post_attachment_count: int
    like_users: list[ThreadsFollowedResponseThreadsFirst_postLike_users]
    user_is_ignored: bool
    post_is_published: bool
    post_is_deleted: bool
    post_update_date: int
    post_is_first_post: bool
    links: ThreadsFollowedResponseThreadsFirst_postLinks
    permissions: ThreadsFollowedResponseThreadsFirst_postPermissions


ThreadsFollowedResponseThreadsThread_tags = TypedDict(
    "ThreadsFollowedResponseThreadsThread_tags",
    {
        "1403": str,
        "8176": str,
        "38": str,
        "1953": str,
        "523": str,
    },
)


class ThreadsFollowedResponseThreadsLinks(TypedDict):
    permalink: str
    detail: str
    followers: str
    forum: str
    posts: str
    first_poster: str
    first_poster_avatar: str
    first_post: str
    last_post: str


class ThreadsFollowedResponseThreadsPermissions(TypedDict):
    view: bool
    delete: bool
    follow: bool
    post: bool
    upload_attachment: bool
    edit: bool
    edit_title: bool
    edit_tags: bool


ThreadsFollowedResponseThreadsForumLinks = TypedDict(
    "ThreadsFollowedResponseThreadsForumLinks",
    {
        "permalink": str,
        "detail": str,
        "sub-categories": str,
        "sub-forums": str,
        "threads": str,
        "followers": str,
    },
)


class ThreadsFollowedResponseThreadsForumPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    create_thread: bool
    upload_attachment: bool
    tag_thread: bool
    follow: bool


class ThreadsFollowedResponseThreadsForum(TypedDict):
    forum_id: int
    forum_title: str
    forum_description: str
    forum_thread_count: int
    forum_post_count: int
    forum_prefixes: list[object]
    thread_default_prefix_id: int
    thread_prefix_is_required: bool
    links: ThreadsFollowedResponseThreadsForumLinks
    permissions: ThreadsFollowedResponseThreadsForumPermissions
    forum_is_followed: bool


class ThreadsFollowedResponseThreadsFollow(TypedDict):
    alert: bool
    email: bool


class ThreadsFollowedResponseThreads(TypedDict):
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
    thread_is_followed: bool
    first_post: ThreadsFollowedResponseThreadsFirst_post
    thread_prefixes: list[object]
    thread_tags: ThreadsFollowedResponseThreadsThread_tags
    links: ThreadsFollowedResponseThreadsLinks
    permissions: ThreadsFollowedResponseThreadsPermissions
    forum: ThreadsFollowedResponseThreadsForum
    follow: ThreadsFollowedResponseThreadsFollow


class ThreadsFollowedResponse(TypedDict):
    threads: list[ThreadsFollowedResponseThreads]
    threads_total: int
    system_info: Resp_SystemInfo


ThreadsNavigationResponseElementsLinks = TypedDict(
    "ThreadsNavigationResponseElementsLinks",
    {
        "permalink": str,
        "detail": str,
        "sub-categories": str,
        "sub-forums": str,
        "sub-elements": str,
    },
)


class ThreadsNavigationResponseElementsPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool


class ThreadsNavigationResponseElements(TypedDict):
    category_id: int
    category_title: str
    category_description: str
    links: ThreadsNavigationResponseElementsLinks
    permissions: ThreadsNavigationResponseElementsPermissions
    navigation_type: str
    navigation_id: int
    navigation_depth: int
    navigation_parent_id: int
    has_sub_elements: bool


class ThreadsNavigationResponse(TypedDict):
    elements: list[ThreadsNavigationResponseElements]
    elements_count: int
    system_info: Resp_SystemInfo


class ThreadsPollGetResponsePollResponses(TypedDict):
    response_id: int
    response_answer: str
    response_vote_count: int


class ThreadsPollGetResponsePollPermissions(TypedDict):
    vote: bool
    result: bool


class ThreadsPollGetResponsePollLinks(TypedDict):
    vote: str


class ThreadsPollGetResponsePoll(TypedDict):
    poll_id: int
    poll_question: str
    poll_vote_count: int
    poll_max_votes: int
    poll_is_open: bool
    poll_is_voted: bool
    responses: list[ThreadsPollGetResponsePollResponses]
    permissions: ThreadsPollGetResponsePollPermissions
    links: ThreadsPollGetResponsePollLinks


class ThreadsPollGetResponse(TypedDict):
    poll: ThreadsPollGetResponsePoll
    system_info: Resp_SystemInfo


class ThreadsPollVoteBody(TypedDict, total=False):
    response_id: int
    response_ids: list[int]


class ThreadsPollVoteResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ThreadsUnreadParams(TypedDict, total=False):
    limit: int
    forum_id: int
    data_limit: int


class ThreadsUnreadResponseDataFirst_postLike_users(TypedDict):
    user_id: int
    username: str
    display_style_group_id: int
    is_banned: int
    uniq_username_css: str


class ThreadsUnreadResponseDataFirst_postLinks(TypedDict):
    permalink: str
    detail: str
    thread: str
    poster: str
    likes: str
    report: str
    attachments: str
    poster_avatar: str


class ThreadsUnreadResponseDataFirst_postPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    reply: bool
    like: bool
    report: bool
    upload_attachment: bool


class ThreadsUnreadResponseDataFirst_post(TypedDict):
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
    post_attachment_count: int
    like_users: list[ThreadsUnreadResponseDataFirst_postLike_users]
    user_is_ignored: bool
    post_is_published: bool
    post_is_deleted: bool
    post_update_date: int
    post_is_first_post: bool
    links: ThreadsUnreadResponseDataFirst_postLinks
    permissions: ThreadsUnreadResponseDataFirst_postPermissions


class ThreadsUnreadResponseDataLinks(TypedDict):
    permalink: str
    detail: str
    followers: str
    forum: str
    posts: str
    first_poster: str
    first_poster_avatar: str
    first_post: str
    last_poster: str
    last_post: str


class ThreadsUnreadResponseDataPermissions(TypedDict):
    view: bool
    delete: bool
    follow: bool
    post: bool
    upload_attachment: bool
    edit: bool


ThreadsUnreadResponseDataForumLinks = TypedDict(
    "ThreadsUnreadResponseDataForumLinks",
    {
        "permalink": str,
        "detail": str,
        "sub-categories": str,
        "sub-forums": str,
        "threads": str,
        "followers": str,
    },
)


class ThreadsUnreadResponseDataForumPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    create_thread: bool
    upload_attachment: bool
    tag_thread: bool
    follow: bool


class ThreadsUnreadResponseDataForum(TypedDict):
    forum_id: int
    forum_title: str
    forum_description: str
    forum_thread_count: int
    forum_post_count: int
    forum_prefixes: list[object]
    thread_default_prefix_id: int
    thread_prefix_is_required: bool
    links: ThreadsUnreadResponseDataForumLinks
    permissions: ThreadsUnreadResponseDataForumPermissions
    forum_is_followed: bool


class ThreadsUnreadResponseData(TypedDict):
    content_type: str
    content_id: int
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
    thread_is_followed: bool
    first_post: ThreadsUnreadResponseDataFirst_post
    thread_prefixes: list[object]
    thread_tags: list[object]
    links: ThreadsUnreadResponseDataLinks
    permissions: ThreadsUnreadResponseDataPermissions
    forum: ThreadsUnreadResponseDataForum


class ThreadsUnreadResponse(TypedDict):
    threads: list[Resp_ThreadModel]
    data: list[ThreadsUnreadResponseData]
    system_info: Resp_SystemInfo


class ThreadsRecentParams(TypedDict, total=False):
    days: int
    limit: int
    forum_id: int
    data_limit: int


class ThreadsRecentResponseDataFirst_postLinks(TypedDict):
    permalink: str
    detail: str
    thread: str
    poster: str
    likes: str
    report: str
    attachments: str
    poster_avatar: str


class ThreadsRecentResponseDataFirst_postPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    reply: bool
    like: bool
    report: bool
    upload_attachment: bool


class ThreadsRecentResponseDataFirst_post(TypedDict):
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
    post_attachment_count: int
    user_is_ignored: bool
    post_is_published: bool
    post_is_deleted: bool
    post_update_date: int
    post_is_first_post: bool
    links: ThreadsRecentResponseDataFirst_postLinks
    permissions: ThreadsRecentResponseDataFirst_postPermissions


class ThreadsRecentResponseDataLinks(TypedDict):
    permalink: str
    detail: str
    followers: str
    forum: str
    posts: str
    first_poster: str
    first_poster_avatar: str
    first_post: str
    last_poster: str
    last_post: str


class ThreadsRecentResponseDataPermissions(TypedDict):
    view: bool
    delete: bool
    follow: bool
    post: bool
    upload_attachment: bool
    edit: bool


ThreadsRecentResponseDataForumLinks = TypedDict(
    "ThreadsRecentResponseDataForumLinks",
    {
        "permalink": str,
        "detail": str,
        "sub-categories": str,
        "sub-forums": str,
        "threads": str,
        "followers": str,
    },
)


class ThreadsRecentResponseDataForumPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    create_thread: bool
    upload_attachment: bool
    tag_thread: bool
    follow: bool


class ThreadsRecentResponseDataForum(TypedDict):
    forum_id: int
    forum_title: str
    forum_description: str
    forum_thread_count: int
    forum_post_count: int
    forum_prefixes: list[object]
    thread_default_prefix_id: int
    thread_prefix_is_required: bool
    links: ThreadsRecentResponseDataForumLinks
    permissions: ThreadsRecentResponseDataForumPermissions
    forum_is_followed: bool


class ThreadsRecentResponseData(TypedDict):
    content_type: str
    content_id: int
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
    thread_is_followed: bool
    first_post: ThreadsRecentResponseDataFirst_post
    thread_prefixes: list[object]
    thread_tags: list[object]
    links: ThreadsRecentResponseDataLinks
    permissions: ThreadsRecentResponseDataPermissions
    forum: ThreadsRecentResponseDataForum


class ThreadsRecentResponse(TypedDict):
    threads: list[Resp_ThreadModel]
    data: list[ThreadsRecentResponseData]
    system_info: Resp_SystemInfo


class ThreadsFinishResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


# ─── PostsApi Types ────────────────────────────────────────


class PostsListParams(TypedDict, total=False):
    thread_id: int
    page_of_post_id: int
    page: int
    limit: int
    order: Literal["natural", "natural_reverse", "post_likes", "post_likes_reverse"]


class PostsListResponse(TypedDict):
    posts: list[Resp_ThreadModel]
    thread: Resp_ThreadModel
    posts_total: int
    system_info: Resp_SystemInfo


class _PostsCreateBodyRequired(TypedDict):
    post_body: str


class PostsCreateBody(_PostsCreateBodyRequired, total=False):
    thread_id: int
    quote_post_id: int


class PostsCreateResponse(TypedDict):
    post: Resp_PostModel
    system_info: Resp_SystemInfo


class PostsGetResponse(TypedDict):
    post: Resp_PostModel
    system_info: Resp_SystemInfo


class PostsEditBody(TypedDict, total=False):
    post_body: str


class PostsEditResponse(TypedDict):
    post: Resp_PostModel
    system_info: Resp_SystemInfo


class PostsDeleteBody(TypedDict, total=False):
    reason: str


class PostsDeleteResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class PostsLikesParams(TypedDict, total=False):
    page: int
    limit: int


class PostsLikesResponseUsers(TypedDict):
    user_id: int
    username: str


class PostsLikesResponse(TypedDict):
    users: list[PostsLikesResponseUsers]
    system_info: Resp_SystemInfo


class PostsLikeResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class PostsUnlikeResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class PostsReportreasonsResponse(TypedDict):
    reasons: list[str]
    system_info: Resp_SystemInfo


class PostsReportBody(TypedDict):
    message: str


class PostsReportResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class _PostsCommentsGetParamsRequired(TypedDict):
    post_id: int


class PostsCommentsGetParams(_PostsCommentsGetParamsRequired, total=False):
    before: int
    before_comment: int


class PostsCommentsGetResponse(TypedDict):
    comments: list[Resp_PostCommentModel]
    system_info: Resp_SystemInfo


class PostsCommentsCreateBody(TypedDict):
    post_id: int
    comment_body: str


class PostsCommentsCreateResponseCommentLinks(TypedDict):
    permalink: str
    detail: str
    post: str
    thread: str
    poster: str
    likes: str
    report: str
    poster_avatar: str


class PostsCommentsCreateResponseCommentPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    reply: bool
    like: bool
    report: bool


class PostsCommentsCreateResponseComment(TypedDict):
    post_comment_id: int
    post_id: int
    thread_id: int
    poster_user_id: int
    poster_username: str
    poster_username_html: str
    post_comment_body: str
    post_comment_body_html: str
    post_comment_body_plain_text: str
    post_comment_like_count: int
    user_is_ignored: bool
    post_comment_is_published: bool
    post_comment_is_deleted: bool
    post_comment_update_date: int
    links: PostsCommentsCreateResponseCommentLinks
    permissions: PostsCommentsCreateResponseCommentPermissions


class PostsCommentsCreateResponse(TypedDict):
    comment: PostsCommentsCreateResponseComment
    system_info: Resp_SystemInfo


class PostsCommentsEditBody(TypedDict):
    post_comment_id: int
    comment_body: str


class PostsCommentsEditResponseCommentLinks(TypedDict):
    permalink: str
    detail: str
    post: str
    thread: str
    poster: str
    likes: str
    report: str
    poster_avatar: str


class PostsCommentsEditResponseCommentPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    reply: bool
    like: bool
    report: bool


class PostsCommentsEditResponseComment(TypedDict):
    post_comment_id: int
    post_id: int
    thread_id: int
    poster_user_id: int
    poster_username: str
    poster_username_html: str
    post_comment_body: str
    post_comment_body_html: str
    post_comment_body_plain_text: str
    post_comment_like_count: int
    user_is_ignored: bool
    post_comment_is_published: bool
    post_comment_is_deleted: bool
    post_comment_update_date: int
    links: PostsCommentsEditResponseCommentLinks
    permissions: PostsCommentsEditResponseCommentPermissions


class PostsCommentsEditResponse(TypedDict):
    comment: PostsCommentsEditResponseComment
    system_info: Resp_SystemInfo


class _PostsCommentsDeleteBodyRequired(TypedDict):
    post_comment_id: int


class PostsCommentsDeleteBody(_PostsCommentsDeleteBodyRequired, total=False):
    reason: str


class PostsCommentsDeleteResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class PostsCommentsReportBody(TypedDict):
    post_comment_id: int
    message: str


class PostsCommentsReportResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


# ─── UsersApi Types ────────────────────────────────────────


class UsersListParams(TypedDict, total=False):
    page: int
    limit: int
    fields_include: list[Literal["*", "alerts"]]


class UsersListResponseLinks(TypedDict):
    pages: int
    page: int
    next: str


class UsersListResponse(TypedDict):
    users: list[Resp_UserModel]
    users_total: int
    links: UsersListResponseLinks
    system_info: Resp_SystemInfo


class UsersFieldsResponseFields(TypedDict):
    id: str
    title: str
    description: str
    position: str
    is_required: bool


class UsersFieldsResponse(TypedDict):
    fields: list[UsersFieldsResponseFields]
    system_info: Resp_SystemInfo


class UsersFindParams(TypedDict, total=False):
    username: str
    custom_fields: dict[str, str]
    fields_include: list[Literal["*", "alerts"]]


class UsersFindResponse(TypedDict):
    users: list[Resp_UserModel]
    system_info: Resp_SystemInfo


class UsersGetParams(TypedDict, total=False):
    fields_include: list[Literal["*", "alerts"]]


class UsersGetResponse(TypedDict):
    user: Resp_UserModel
    system_info: Resp_SystemInfo


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
    timezone: Literal[
        "Pacific/Midway",
        "Pacific/Honolulu",
        "Pacific/Marquesas",
        "America/Anchorage",
        "America/Los_Angeles",
        "America/Santa_Isabel",
        "America/Tijuana",
        "America/Denver",
        "America/Chihuahua",
        "America/Phoenix",
        "America/Chicago",
        "America/Belize",
        "America/Mexico_City",
        "Pacific/Easter",
        "America/New_York",
        "America/Havana",
        "America/Bogota",
        "America/Caracas",
        "America/Halifax",
        "America/Goose_Bay",
        "America/Asuncion",
        "America/Santiago",
        "America/Cuiaba",
        "America/La_Paz",
        "America/St_Johns",
        "America/Argentina/Buenos_Aires",
        "America/Argentina/San_Luis",
        "America/Argentina/Mendoza",
        "Atlantic/Stanley",
        "America/Godthab",
        "America/Montevideo",
        "America/Sao_Paulo",
        "America/Miquelon",
        "America/Noronha",
        "Atlantic/Cape_Verde",
        "Atlantic/Azores",
        "Europe/London",
        "Africa/Casablanca",
        "Atlantic/Reykjavik",
        "Europe/Amsterdam",
        "Africa/Algiers",
        "Africa/Windhoek",
        "Africa/Tunis",
        "Europe/Athens",
        "Africa/Johannesburg",
        "Europe/Kaliningrad",
        "Asia/Amman",
        "Asia/Beirut",
        "Africa/Cairo",
        "Asia/Jerusalem",
        "Asia/Gaza",
        "Asia/Damascus",
        "Europe/Moscow",
        "Europe/Minsk",
        "Africa/Nairobi",
        "Asia/Tehran",
        "Asia/Dubai",
        "Asia/Yerevan",
        "Asia/Baku",
        "Indian/Mauritius",
        "Asia/Kabul",
        "Asia/Yekaterinburg",
        "Asia/Tashkent",
        "Asia/Kolkata",
        "Asia/Kathmandu",
        "Asia/Novosibirsk",
        "Asia/Dhaka",
        "Asia/Almaty",
        "Asia/Rangoon",
        "Asia/Krasnoyarsk",
        "Asia/Bangkok",
        "Asia/Irkutsk",
        "Asia/Hong_Kong",
        "Asia/Singapore",
        "Australia/Perth",
        "Asia/Yakutsk",
        "Asia/Tokyo",
        "Asia/Seoul",
        "Australia/Adelaide",
        "Australia/Darwin",
        "Asia/Vladivostok",
        "Asia/Magadan",
        "Australia/Brisbane",
        "Australia/Sydney",
        "Pacific/Noumea",
        "Pacific/Norfolk",
        "Asia/Anadyr",
        "Pacific/Auckland",
        "Pacific/Fiji",
        "Pacific/Chatham",
        "Pacific/Tongatapu",
        "Pacific/Apia",
        "Pacific/Kiritimati",
    ]
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
    system_info: Resp_SystemInfo


class UsersClaimsParams(TypedDict, total=False):
    type: Literal["market", "nomarket"]
    claim_state: Literal["active", "solved", "rejected", "settled"]


class UsersClaimsResponseClaims(TypedDict):
    thread_id: int
    claim_date: int
    claim_state: str
    message_body: str
    message_body_html: str
    message_body_plain_text: str
    amount: int
    amount_formatted: str
    author: Resp_UserModel


class UsersClaimsResponseStatsMarket(TypedDict):
    total: int
    solved: int
    settled: int
    rejected: int


class UsersClaimsResponseStatsNoMarket(TypedDict):
    total: int
    solved: int
    settled: int
    rejected: int


class UsersClaimsResponseStats(TypedDict):
    market: UsersClaimsResponseStatsMarket
    noMarket: UsersClaimsResponseStatsNoMarket


class UsersClaimsResponse(TypedDict):
    claims: list[UsersClaimsResponseClaims]
    stats: UsersClaimsResponseStats
    system_info: Resp_SystemInfo


class _UsersAvatarUploadBodyRequired(TypedDict):
    avatar: bytes


class UsersAvatarUploadBody(_UsersAvatarUploadBodyRequired, total=False):
    x: int
    y: int
    crop: int


class UsersAvatarUploadResponse(TypedDict):
    status: str
    message: str
    system_info: Resp_SystemInfo


class UsersAvatarDeleteResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class UsersAvatarCropBody(TypedDict, total=False):
    x: int
    y: int
    crop: int


class UsersAvatarCropResponse(TypedDict):
    status: str
    message: str
    system_info: Resp_SystemInfo


class _UsersBackgroundUploadBodyRequired(TypedDict):
    background: bytes


class UsersBackgroundUploadBody(_UsersBackgroundUploadBodyRequired, total=False):
    x: int
    y: int
    crop: int


class UsersBackgroundUploadResponse(TypedDict):
    status: str
    message: str
    system_info: Resp_SystemInfo


class UsersBackgroundDeleteResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class UsersBackgroundCropBody(TypedDict, total=False):
    x: int
    y: int
    crop: int


class UsersBackgroundCropResponse(TypedDict):
    status: str
    message: str
    system_info: Resp_SystemInfo


class UsersFollowersParams(TypedDict, total=False):
    order: Literal["natural", "follow_date", "follow_date_reverse"]
    page: int
    limit: int


class UsersFollowersResponseUsersLinks(TypedDict):
    permalink: str
    detail: str
    avatar: str
    avatar_big: str
    avatar_small: str
    followers: str
    followings: str
    ignore: str
    timeline: str


class UsersFollowersResponseUsersPermissions(TypedDict):
    edit: bool
    follow: bool
    ignore: bool
    profile_post: bool


class UsersFollowersResponseUsersCustom_fields(TypedDict):
    _4: str
    lztInnovation20Link: str
    lztInnovation30Link: str
    lztInnovationLink: str


class UsersFollowersResponseUsers(TypedDict):
    content_type: str
    content_id: int
    follow_date: int
    user_id: int
    username: str
    username_html: str
    user_message_count: int
    user_register_date: int
    user_like_count: int
    user_like2_count: int
    contest_count: int
    trophy_count: int
    custom_title: str
    is_banned: int
    user_title: str
    user_is_valid: bool
    user_is_verified: bool
    user_is_followed: bool
    user_last_seen_date: int
    user_following_count: int
    user_followers_count: int
    links: UsersFollowersResponseUsersLinks
    permissions: UsersFollowersResponseUsersPermissions
    user_is_ignored: bool
    user_is_visitor: bool
    user_group_id: int
    custom_fields: UsersFollowersResponseUsersCustom_fields


class UsersFollowersResponseLinks(TypedDict):
    pages: int
    page: int
    next: str


class UsersFollowersResponse(TypedDict):
    users: list[UsersFollowersResponseUsers]
    users_total: int
    links: UsersFollowersResponseLinks
    system_info: Resp_SystemInfo


class UsersFollowResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class UsersUnfollowResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class UsersFollowingsParams(TypedDict, total=False):
    order: Literal["natural", "follow_date", "follow_date_reverse"]
    page: int
    limit: int


class UsersFollowingsResponseUsersLinks(TypedDict):
    permalink: str
    detail: str
    avatar: str
    avatar_big: str
    avatar_small: str
    followers: str
    followings: str
    ignore: str
    timeline: str


class UsersFollowingsResponseUsersPermissions(TypedDict):
    edit: bool
    follow: bool
    ignore: bool
    profile_post: bool


class UsersFollowingsResponseUsersCustom_fields(TypedDict):
    _4: str
    allowSelfUnban: list[object]
    discord: str
    github: str
    jabber: str
    lztAwardUserTrophy: str
    lztCuratorNodeTitle: str
    lztCuratorNodeTitleEn: str
    lztDeposit: str
    lztInnovation20Link: str
    lztInnovation30Link: str
    lztInnovationLink: str
    lztLikesIncreasing: str
    lztLikesZeroing: str
    lztSympathyIncreasing: str
    lztSympathyZeroing: str
    maecenasValue: str
    scamURL: str
    steam: str
    telegram: str
    vk: str


class UsersFollowingsResponseUsers(TypedDict):
    content_type: str
    content_id: int
    follow_date: int
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
    user_title: str
    user_is_valid: bool
    user_is_verified: bool
    user_is_followed: bool
    user_last_seen_date: int
    user_following_count: int
    user_followers_count: int
    links: UsersFollowingsResponseUsersLinks
    permissions: UsersFollowingsResponseUsersPermissions
    user_is_ignored: bool
    user_is_visitor: bool
    user_group_id: int
    custom_fields: UsersFollowingsResponseUsersCustom_fields


class UsersFollowingsResponse(TypedDict):
    users: list[UsersFollowingsResponseUsers]
    users_total: int
    system_info: Resp_SystemInfo


class UsersLikesParams(TypedDict, total=False):
    node_id: int
    like_type: Literal["like", "like2"]
    type: Literal["gotten", "given"]  # default: "gotten"
    page: int
    content_type: Literal[
        "post", "post_comment", "profile_post", "profile_post_comment"
    ]  # default: "post"
    search_user_id: int
    stats: bool


UsersLikesParams_DEFAULTS: dict[str, object] = {
    "type": "gotten",
    "content_type": "post",
}


class UsersLikesResponseLikes1234567890(TypedDict):
    like_id: int
    content_type: str
    content_id: int
    like_user_id: int
    like_date: int
    content_user_id: int
    content_state: str
    user: Resp_UserModel
    actionUser: Resp_UserModel
    messageHtml: str
    post_date: int


UsersLikesResponseLikes = TypedDict(
    "UsersLikesResponseLikes",
    {
        "1234567890": UsersLikesResponseLikes1234567890,
    },
)


class UsersLikesResponse(TypedDict):
    page: int
    perPage: int
    contentType: str
    totalLikes: int
    likes: UsersLikesResponseLikes
    system_info: Resp_SystemInfo


class UsersIgnoredParams(TypedDict, total=False):
    total: bool


class UsersIgnoredResponseUsersCustom_fields(TypedDict):
    _4: str
    scamURL: object
    lztLikesZeroing: object
    lztLikesIncreasing: object
    lztSympathyZeroing: object
    lztSympathyIncreasing: object
    telegram: object
    vk: str
    discord: str
    steam: str
    matrix: object
    jabber: str
    github: str


class UsersIgnoredResponseUsersIgnored_info(TypedDict):
    ignore_content: int
    ignore_conversations: int
    restrict_view_profile: int


class UsersIgnoredResponseUsersRenderedAvatars(TypedDict):
    l: str
    m: str
    s: str


class UsersIgnoredResponseUsersRendered(TypedDict):
    username: str
    avatars: UsersIgnoredResponseUsersRenderedAvatars
    backgrounds: list[object]
    link: str


class UsersIgnoredResponseUsers(TypedDict):
    can_edit: bool
    can_follow: bool
    can_ignore: bool
    can_post_profile: bool
    can_view_profile: bool
    can_view_profile_posts: bool
    can_warn: bool
    contest_count: int
    conv_welcome_message: str
    convertedDeposit: int
    custom_fields: UsersIgnoredResponseUsersCustom_fields
    deposit: int
    homepage: str
    ignored_info: UsersIgnoredResponseUsersIgnored_info
    is_admin: bool
    is_banned: bool
    is_followed: bool
    is_ignored: bool
    is_moderator: bool
    is_staff: bool
    last_activity: int
    like2_count: int
    like_count: int
    location: str
    message_count: int
    register_date: int
    rendered: UsersIgnoredResponseUsersRendered
    short_link: str
    trophy_points: int
    user_id: int
    user_title: str
    username: str
    view_url: str
    warning_points: int


class UsersIgnoredResponse(TypedDict):
    users: list[UsersIgnoredResponseUsers]
    system_info: Resp_SystemInfo


class UsersIgnoreResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class UsersIgnoreeditParams(TypedDict, total=False):
    ignore_conversations: bool
    ignore_content: bool
    restrict_view_profile: bool


class UsersIgnoreeditResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class UsersUnignoreResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class UsersContentsParams(TypedDict, total=False):
    page: int
    limit: int


class UsersContentsResponseDataLike_users(TypedDict):
    user_id: int
    username: str
    display_style_group_id: int
    is_banned: int
    uniq_username_css: str


class UsersContentsResponseDataLinks(TypedDict):
    permalink: str
    detail: str
    thread: str
    poster: str
    likes: str
    report: str
    attachments: str
    poster_avatar: str


class UsersContentsResponseDataPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    reply: bool
    like: bool
    report: bool
    upload_attachment: bool


class UsersContentsResponseDataThreadLinks(TypedDict):
    permalink: str
    detail: str
    followers: str
    forum: str
    posts: str
    first_poster: str
    first_poster_avatar: str
    first_post: str
    last_poster: str
    last_post: str


class UsersContentsResponseDataThreadPermissions(TypedDict):
    view: bool
    delete: bool
    follow: bool
    post: bool
    upload_attachment: bool


class UsersContentsResponseDataThread(TypedDict):
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
    thread_is_followed: bool
    thread_prefixes: list[object]
    thread_tags: list[object]
    links: UsersContentsResponseDataThreadLinks
    permissions: UsersContentsResponseDataThreadPermissions


class UsersContentsResponseData(TypedDict):
    content_type: str
    content_id: int
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
    post_attachment_count: int
    like_users: list[UsersContentsResponseDataLike_users]
    user_is_ignored: bool
    post_is_published: bool
    post_is_deleted: bool
    post_update_date: int
    post_is_first_post: bool
    links: UsersContentsResponseDataLinks
    permissions: UsersContentsResponseDataPermissions
    thread: UsersContentsResponseDataThread


class UsersContentsResponseLinks(TypedDict):
    pages: int
    page: int
    next: str


class UsersContentsResponse(TypedDict):
    data: list[UsersContentsResponseData]
    data_total: int
    user: Resp_UserModel
    links: UsersContentsResponseLinks
    system_info: Resp_SystemInfo


class UsersTrophiesResponseTrophies(TypedDict):
    trophy_id: int
    title: str
    description: str
    trophy_url: str


class UsersTrophiesResponse(TypedDict):
    trophies: list[UsersTrophiesResponseTrophies]
    system_info: Resp_SystemInfo


class UsersSecretanswertypesResponseData(TypedDict):
    sa_id: int
    renderedPhrase: str


class UsersSecretanswertypesResponse(TypedDict):
    data: list[UsersSecretanswertypesResponseData]
    system_info: Resp_SystemInfo


class UsersSaResetResponse(TypedDict):
    success: bool
    waiting_time: str
    system_info: Resp_SystemInfo


class UsersSaCancelresetResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


# ─── ProfilePostsApi Types ────────────────────────────────────────


class ProfilePostsListParams(TypedDict, total=False):
    posts_user_id: int
    page: int
    limit: int
    fields_include: list[Literal["*", "latest_comments"]]


class ProfilePostsListResponseLinks(TypedDict):
    pages: int
    page: int
    next: str


class ProfilePostsListResponse(TypedDict):
    profile_posts: list[Resp_ProfilePostModel]
    totalProfilePosts: int
    canPostOnProfile: bool
    links: ProfilePostsListResponseLinks
    system_info: Resp_SystemInfo


class ProfilePostsGetResponse(TypedDict):
    profile_post: Resp_ProfilePostModel
    system_info: Resp_SystemInfo


class ProfilePostsEditBody(TypedDict, total=False):
    post_body: str
    disable_comments: bool


class ProfilePostsEditResponseProfile_postLinks(TypedDict):
    permalink: str
    detail: str
    timeline: str
    timeline_user: str
    poster: str
    likes: str
    comments: str
    report: str
    poster_avatar: str


class ProfilePostsEditResponseProfile_postPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    like: bool
    comment: bool
    report: bool


class ProfilePostsEditResponseProfile_post(TypedDict):
    profile_post_id: int
    timeline_user_id: int
    poster_user_id: int
    poster_username: str
    poster_username_html: str
    post_create_date: int
    post_body: str
    post_like_count: int
    post_comment_count: int
    timeline_username: str
    user_is_ignored: bool
    post_is_published: bool
    post_is_deleted: bool
    links: ProfilePostsEditResponseProfile_postLinks
    permissions: ProfilePostsEditResponseProfile_postPermissions


class ProfilePostsEditResponse(TypedDict):
    profile_post: ProfilePostsEditResponseProfile_post
    system_info: Resp_SystemInfo


class ProfilePostsDeleteParams(TypedDict, total=False):
    reason: str


class ProfilePostsDeleteResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ProfilePostsReportreasonsResponse(TypedDict):
    reasons: list[str]
    system_info: Resp_SystemInfo


class ProfilePostsReportBody(TypedDict):
    message: str


class ProfilePostsReportResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ProfilePostsCreateBody(TypedDict):
    user_id: UserIDModel
    post_body: str


class ProfilePostsCreateResponseProfile_postLinks(TypedDict):
    permalink: str
    detail: str
    timeline: str
    timeline_user: str
    poster: str
    likes: str
    comments: str
    report: str
    poster_avatar: str


class ProfilePostsCreateResponseProfile_postPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    like: bool
    comment: bool
    report: bool


class ProfilePostsCreateResponseProfile_post(TypedDict):
    profile_post_id: int
    timeline_user_id: int
    poster_user_id: int
    poster_username: str
    poster_username_html: str
    post_create_date: int
    post_body: str
    post_like_count: int
    post_comment_count: int
    timeline_username: str
    user_is_ignored: bool
    post_is_published: bool
    post_is_deleted: bool
    links: ProfilePostsCreateResponseProfile_postLinks
    permissions: ProfilePostsCreateResponseProfile_postPermissions


class ProfilePostsCreateResponse(TypedDict):
    profile_post: ProfilePostsCreateResponseProfile_post
    system_info: Resp_SystemInfo


class ProfilePostsStickResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ProfilePostsUnstickResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ProfilePostsLikesResponseUsers(TypedDict):
    user_id: int
    username: str


class ProfilePostsLikesResponse(TypedDict):
    users: list[ProfilePostsLikesResponseUsers]
    system_info: Resp_SystemInfo


class ProfilePostsLikeResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ProfilePostsUnlikeResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class _ProfilePostsCommentsListParamsRequired(TypedDict):
    profile_post_id: int


class ProfilePostsCommentsListParams(_ProfilePostsCommentsListParamsRequired, total=False):
    before: int
    limit: int


class ProfilePostsCommentsListResponseProfile_postLinks(TypedDict):
    permalink: str
    detail: str
    timeline: str
    timeline_user: str
    poster: str
    likes: str
    comments: str
    report: str
    poster_avatar: str


class ProfilePostsCommentsListResponseProfile_postPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    like: bool
    comment: bool
    report: bool


class ProfilePostsCommentsListResponseProfile_post(TypedDict):
    profile_post_id: int
    timeline_user_id: int
    poster_user_id: int
    poster_username: str
    poster_username_html: str
    post_create_date: int
    post_body: str
    post_like_count: int
    post_comment_count: int
    timeline_username: str
    user_is_ignored: bool
    post_is_published: bool
    post_is_deleted: bool
    links: ProfilePostsCommentsListResponseProfile_postLinks
    permissions: ProfilePostsCommentsListResponseProfile_postPermissions


class ProfilePostsCommentsListResponse(TypedDict):
    comments: list[Resp_ProfilePostCommentModel]
    comments_total: int
    profile_post: ProfilePostsCommentsListResponseProfile_post
    timeline_user: Resp_UserModel
    system_info: Resp_SystemInfo


class ProfilePostsCommentsCreateBody(TypedDict):
    profile_post_id: int
    comment_body: str


class ProfilePostsCommentsCreateResponseCommentLinks(TypedDict):
    detail: str
    profile_post: str
    timeline: str
    timeline_user: str
    poster: str
    poster_avatar: str


class ProfilePostsCommentsCreateResponseCommentPermissions(TypedDict):
    view: bool
    delete: bool


class ProfilePostsCommentsCreateResponseComment(TypedDict):
    comment_id: int
    profile_post_id: int
    comment_user_id: int
    comment_username: str
    comment_username_html: str
    comment_create_date: int
    comment_body: str
    user_is_ignored: bool
    timeline_user_id: int
    links: ProfilePostsCommentsCreateResponseCommentLinks
    permissions: ProfilePostsCommentsCreateResponseCommentPermissions


class ProfilePostsCommentsCreateResponse(TypedDict):
    comment: ProfilePostsCommentsCreateResponseComment
    system_info: Resp_SystemInfo


class ProfilePostsCommentsEditBody(TypedDict):
    comment_id: int
    comment_body: str


class ProfilePostsCommentsEditResponseCommentLinks(TypedDict):
    detail: str
    profile_post: str
    timeline: str
    timeline_user: str
    poster: str
    poster_avatar: str


class ProfilePostsCommentsEditResponseCommentPermissions(TypedDict):
    view: bool
    delete: bool


class ProfilePostsCommentsEditResponseComment(TypedDict):
    comment_id: int
    profile_post_id: int
    comment_user_id: int
    comment_username: str
    comment_username_html: str
    comment_create_date: int
    comment_body: str
    user_is_ignored: bool
    timeline_user_id: int
    links: ProfilePostsCommentsEditResponseCommentLinks
    permissions: ProfilePostsCommentsEditResponseCommentPermissions


class ProfilePostsCommentsEditResponse(TypedDict):
    comment: ProfilePostsCommentsEditResponseComment
    system_info: Resp_SystemInfo


class ProfilePostsCommentsDeleteBody(TypedDict):
    comment_id: int


class ProfilePostsCommentsDeleteResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ProfilePostsCommentsGetResponse(TypedDict):
    comment: Resp_ProfilePostCommentModel
    system_info: Resp_SystemInfo


class ProfilePostsCommentsReportBody(TypedDict):
    message: str


class ProfilePostsCommentsReportResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


# ─── ConversationsApi Types ────────────────────────────────────────


class ConversationsListParams(TypedDict, total=False):
    folder: Literal[
        "all", "unread", "groups", "market", "market_replacements", "staff", "giveaways", "p2p"
    ]
    page: int
    limit: int


class ConversationsListResponseFolders(TypedDict):
    id: str
    title: str
    name: str


class ConversationsListResponseLinks(TypedDict):
    pages: int
    page: int
    next: str


class ConversationsListResponse(TypedDict):
    conversations: list[Resp_ConversationModel]
    can_start: bool
    folders: list[ConversationsListResponseFolders]
    links: ConversationsListResponseLinks
    system_info: Resp_SystemInfo


class ConversationsCreateBody(TypedDict, total=False):
    recipient_id: int
    recipients: list[str]
    is_group: bool  # default: False
    title: str
    open_invite: bool
    allow_edit_messages: bool
    allow_sticky_messages: bool
    allow_delete_own_messages: bool
    message_body: str


ConversationsCreateBody_DEFAULTS: dict[str, object] = {
    "is_group": False,
}


class ConversationsCreateResponse(TypedDict):
    conversation: Resp_ConversationModel
    system_info: Resp_SystemInfo


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
    conversation: Resp_ConversationModel
    system_info: Resp_SystemInfo


class ConversationsDeleteBody(TypedDict):
    conversation_id: int
    delete_type: Literal["delete", "delete_ignore"]


class ConversationsDeleteResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ConversationsStartBody(TypedDict):
    user_id: UserIDModel


class ConversationsStartResponse(TypedDict):
    conversation: Resp_ConversationModel
    system_info: Resp_SystemInfo


class ConversationsSaveBody(TypedDict):
    link: str


class ConversationsSaveResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ConversationsGetResponse(TypedDict):
    conversation: Resp_ConversationModel
    system_info: Resp_SystemInfo


class ConversationsMessagesListParams(TypedDict, total=False):
    page: int
    limit: int
    order: Literal["natural", "natural_reverse"]
    before: int
    after: int


class ConversationsMessagesListResponseLinks(TypedDict):
    pages: int
    page: int
    next: str


class ConversationsMessagesListResponse(TypedDict):
    messages: list[Resp_ConversationMessageModel]
    messages_total: int
    links: ConversationsMessagesListResponseLinks
    system_info: Resp_SystemInfo


class _ConversationsMessagesCreateBodyRequired(TypedDict):
    message_body: str


class ConversationsMessagesCreateBody(_ConversationsMessagesCreateBodyRequired, total=False):
    reply_message_id: int


class ConversationsMessagesCreateResponse(TypedDict):
    message: Resp_ConversationMessageModel
    system_info: Resp_SystemInfo


class ConversationsSearchBody(TypedDict, total=False):
    q: str
    conversation_id: int
    search_recipients: bool


class ConversationsSearchResponse(TypedDict):
    conversations: list[Resp_ConversationModel]
    recipients: bool
    system_info: Resp_SystemInfo


class ConversationsMessagesGetResponse(TypedDict):
    message: Resp_ConversationModel
    system_info: Resp_SystemInfo


class ConversationsMessagesEditBody(TypedDict):
    message_body: str


class ConversationsMessagesEditResponse(TypedDict):
    message: Resp_ConversationModel
    system_info: Resp_SystemInfo


class ConversationsMessagesDeleteResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ConversationsInviteBody(TypedDict):
    recipients: list[str]


class ConversationsInviteResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ConversationsKickBody(TypedDict):
    user_id: int


class ConversationsKickResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ConversationsReadResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ConversationsReadallResponse(TypedDict):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ConversationsMessagesStickResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ConversationsMessagesUnstickResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ConversationsStarResponse(TypedDict):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ConversationsUnstarResponse(TypedDict):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ConversationsAlertsEnableResponse(TypedDict):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ConversationsAlertsDisableResponse(TypedDict):
    status: str
    message: str
    system_info: Resp_SystemInfo


# ─── NotificationsApi Types ────────────────────────────────────────


class NotificationsListParams(TypedDict, total=False):
    type: Literal["market", "nomarket"]
    page: int
    limit: int


class NotificationsListResponseLinks(TypedDict):
    read: str
    pages: int
    page: int
    next: str


class NotificationsListResponse(TypedDict):
    notifications: list[Resp_NotificationModel]
    notifications_total: int
    links: NotificationsListResponseLinks
    system_info: Resp_SystemInfo


class NotificationsGetResponse(TypedDict):
    notification_id: int
    notification: Resp_NotificationModel
    system_info: Resp_SystemInfo


class NotificationsReadBody(TypedDict, total=False):
    notification_id: int


class NotificationsReadResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


# ─── TagsApi Types ────────────────────────────────────────


TagsPopularResponseTags = TypedDict(
    "TagsPopularResponseTags",
    {
        "000": str,
    },
)


class TagsPopularResponse(TypedDict):
    tags: TagsPopularResponseTags
    system_info: Resp_SystemInfo


class TagsListParams(TypedDict, total=False):
    page: int
    limit: int


TagsListResponseTags = TypedDict(
    "TagsListResponseTags",
    {
        "1": str,
        "2": str,
        "3": str,
        "4": str,
        "5": str,
        "6": str,
        "7": str,
        "8": str,
        "9": str,
        "10": str,
        "11": str,
        "12": str,
        "14": str,
        "15": str,
        "16": str,
        "17": str,
        "18": str,
        "19": str,
        "20": str,
    },
)


class TagsListResponseLinks(TypedDict):
    pages: int
    page: int
    next: str


class TagsListResponse(TypedDict):
    tags: TagsListResponseTags
    tags_total: int
    links: TagsListResponseLinks
    system_info: Resp_SystemInfo


class TagsGetParams(TypedDict, total=False):
    page: int
    limit: int


class TagsGetResponseTagLinks(TypedDict):
    permalink: str
    detail: str


class TagsGetResponseTag(TypedDict):
    tag_id: int
    tag_text: str
    tag_use_count: int
    links: TagsGetResponseTagLinks


class TagsGetResponseTaggedFirst_postLinks(TypedDict):
    permalink: str
    detail: str
    thread: str
    poster: str
    likes: str
    report: str
    attachments: str
    poster_avatar: str


class TagsGetResponseTaggedFirst_postPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    reply: bool
    like: bool
    report: bool
    upload_attachment: bool


class TagsGetResponseTaggedFirst_post(TypedDict):
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
    post_attachment_count: int
    user_is_ignored: bool
    post_is_published: bool
    post_is_deleted: bool
    post_update_date: int
    post_is_first_post: bool
    links: TagsGetResponseTaggedFirst_postLinks
    permissions: TagsGetResponseTaggedFirst_postPermissions


class TagsGetResponseTaggedThread_prefixes(TypedDict):
    prefix_id: int
    prefix_title: str


TagsGetResponseTaggedThread_tags = TypedDict(
    "TagsGetResponseTaggedThread_tags",
    {
        "1": str,
        "654": str,
    },
)


class TagsGetResponseTaggedLinks(TypedDict):
    permalink: str
    detail: str
    followers: str
    forum: str
    posts: str
    first_poster: str
    first_poster_avatar: str
    first_post: str
    last_poster: str
    last_post: str


class TagsGetResponseTaggedPermissions(TypedDict):
    view: bool
    delete: bool
    follow: bool
    post: bool
    upload_attachment: bool
    edit: bool


class TagsGetResponseTaggedForumForum_prefixesGroup_prefixes(TypedDict):
    prefix_id: int
    prefix_title: str


class TagsGetResponseTaggedForumForum_prefixes(TypedDict):
    group_title: str
    group_prefixes: list[TagsGetResponseTaggedForumForum_prefixesGroup_prefixes]


TagsGetResponseTaggedForumLinks = TypedDict(
    "TagsGetResponseTaggedForumLinks",
    {
        "permalink": str,
        "detail": str,
        "sub-categories": str,
        "sub-forums": str,
        "threads": str,
        "followers": str,
    },
)


class TagsGetResponseTaggedForumPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    create_thread: bool
    upload_attachment: bool
    tag_thread: bool
    follow: bool


class TagsGetResponseTaggedForum(TypedDict):
    forum_id: int
    forum_title: str
    forum_description: str
    forum_thread_count: int
    forum_post_count: int
    forum_prefixes: list[TagsGetResponseTaggedForumForum_prefixes]
    thread_default_prefix_id: int
    thread_prefix_is_required: bool
    links: TagsGetResponseTaggedForumLinks
    permissions: TagsGetResponseTaggedForumPermissions
    forum_is_followed: bool


class TagsGetResponseTagged(TypedDict):
    content_type: str
    content_id: int
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
    thread_is_followed: bool
    first_post: TagsGetResponseTaggedFirst_post
    thread_prefixes: list[TagsGetResponseTaggedThread_prefixes]
    thread_tags: TagsGetResponseTaggedThread_tags
    links: TagsGetResponseTaggedLinks
    permissions: TagsGetResponseTaggedPermissions
    forum: TagsGetResponseTaggedForum


class TagsGetResponseLinks(TypedDict):
    pages: int
    page: int
    next: str


class TagsGetResponse(TypedDict):
    tag: TagsGetResponseTag
    tagged: list[TagsGetResponseTagged]
    tagged_total: int
    links: TagsGetResponseLinks
    system_info: Resp_SystemInfo


class TagsFindParams(TypedDict):
    tag: str


class TagsFindResponse(TypedDict):
    tags: list[str]
    ids: list[int]
    system_info: Resp_SystemInfo


# ─── SearchApi Types ────────────────────────────────────────


class SearchAllBody(TypedDict, total=False):
    q: str
    tag: str
    forum_id: int
    user_id: UserIDModel
    page: int
    limit: int


class SearchAllResponseDataFirst_postLinks(TypedDict):
    permalink: str
    detail: str
    thread: str
    poster: str
    likes: str
    report: str
    poster_avatar: str


class SearchAllResponseDataFirst_postPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    reply: bool
    like: bool
    report: bool


class SearchAllResponseDataFirst_post(TypedDict):
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
    post_is_liked: bool
    links: SearchAllResponseDataFirst_postLinks
    permissions: SearchAllResponseDataFirst_postPermissions
    thread_is_deleted: bool


class SearchAllResponseDataLinks(TypedDict):
    permalink: str
    detail: str
    followers: str
    forum: str
    posts: str
    first_poster: str
    first_poster_avatar: str
    first_post: str
    last_poster: str
    last_post: str


class SearchAllResponseDataPermissionsBump(TypedDict):
    can: bool
    available_count: int
    error: object
    next_available_time: object


class SearchAllResponseDataPermissions(TypedDict):
    view: bool
    delete: bool
    follow: bool
    post: bool
    edit: bool
    bump: SearchAllResponseDataPermissionsBump


SearchAllResponseDataForumLinks = TypedDict(
    "SearchAllResponseDataForumLinks",
    {
        "permalink": str,
        "detail": str,
        "sub-categories": str,
        "sub-forums": str,
        "threads": str,
        "followers": str,
    },
)


class SearchAllResponseDataForumPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    create_thread: bool
    tag_thread: bool
    follow: bool


class SearchAllResponseDataForum(TypedDict):
    forum_id: int
    forum_title: str
    forum_description: str
    forum_thread_count: int
    forum_post_count: int
    parent_node_id: int
    forum_prefixes: list[object]
    thread_default_prefix_id: int
    thread_prefix_is_required: bool
    links: SearchAllResponseDataForumLinks
    permissions: SearchAllResponseDataForumPermissions
    forum_is_followed: bool


class SearchAllResponseDataLast_postLinks(TypedDict):
    permalink: str
    detail: str
    thread: str
    poster: str
    likes: str
    report: str
    poster_avatar: str


class SearchAllResponseDataLast_postPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    reply: bool
    like: bool
    report: bool


class SearchAllResponseDataLast_post(TypedDict):
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
    post_is_liked: bool
    links: SearchAllResponseDataLast_postLinks
    permissions: SearchAllResponseDataLast_postPermissions
    thread_is_deleted: bool


class SearchAllResponseData(TypedDict):
    content_type: str
    content_id: str
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
    first_post: SearchAllResponseDataFirst_post
    thread_prefixes: list[object]
    thread_tags: list[object]
    links: SearchAllResponseDataLinks
    permissions: SearchAllResponseDataPermissions
    node_title: str
    forum: SearchAllResponseDataForum
    last_post: SearchAllResponseDataLast_post


class SearchAllResponseLinks(TypedDict):
    pages: int
    page: int
    next: str


class SearchAllResponse(TypedDict):
    data: list[SearchAllResponseData]
    data_total: int
    users: list[Resp_UserModel]
    links: SearchAllResponseLinks
    system_info: Resp_SystemInfo


class SearchThreadsBody(TypedDict, total=False):
    q: str
    tag: str
    forum_id: int
    user_id: UserIDModel
    page: int
    limit: int
    data_limit: int


class SearchThreadsResponseDataFirst_postLinks(TypedDict):
    permalink: str
    detail: str
    thread: str
    poster: str
    likes: str
    report: str
    attachments: str
    poster_avatar: str


class SearchThreadsResponseDataFirst_postPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    reply: bool
    like: bool
    report: bool
    upload_attachment: bool


class SearchThreadsResponseDataFirst_post(TypedDict):
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
    post_attachment_count: int
    user_is_ignored: bool
    post_is_published: bool
    post_is_deleted: bool
    post_update_date: int
    post_is_first_post: bool
    links: SearchThreadsResponseDataFirst_postLinks
    permissions: SearchThreadsResponseDataFirst_postPermissions


class SearchThreadsResponseDataLinks(TypedDict):
    permalink: str
    detail: str
    followers: str
    forum: str
    posts: str
    first_poster: str
    first_poster_avatar: str
    first_post: str
    last_post: str


class SearchThreadsResponseDataPermissions(TypedDict):
    view: bool
    delete: bool
    follow: bool
    post: bool
    upload_attachment: bool
    edit: bool


SearchThreadsResponseDataForumLinks = TypedDict(
    "SearchThreadsResponseDataForumLinks",
    {
        "permalink": str,
        "detail": str,
        "sub-categories": str,
        "sub-forums": str,
        "threads": str,
        "followers": str,
    },
)


class SearchThreadsResponseDataForumPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    create_thread: bool
    upload_attachment: bool
    tag_thread: bool
    follow: bool


class SearchThreadsResponseDataForum(TypedDict):
    forum_id: int
    forum_title: str
    forum_description: str
    forum_thread_count: int
    forum_post_count: int
    forum_prefixes: list[object]
    thread_default_prefix_id: int
    thread_prefix_is_required: bool
    links: SearchThreadsResponseDataForumLinks
    permissions: SearchThreadsResponseDataForumPermissions
    forum_is_followed: bool


class SearchThreadsResponseData(TypedDict):
    content_type: str
    content_id: int
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
    thread_is_followed: bool
    first_post: SearchThreadsResponseDataFirst_post
    thread_prefixes: list[object]
    thread_tags: list[object]
    links: SearchThreadsResponseDataLinks
    permissions: SearchThreadsResponseDataPermissions
    forum: SearchThreadsResponseDataForum


class SearchThreadsResponseLinks(TypedDict):
    pages: int
    page: int
    next: str


class SearchThreadsResponse(TypedDict):
    data: list[SearchThreadsResponseData]
    data_total: int
    links: SearchThreadsResponseLinks
    system_info: Resp_SystemInfo


class SearchPostsBody(TypedDict, total=False):
    q: str
    tag: str
    forum_id: int
    user_id: UserIDModel
    page: int
    limit: int
    data_limit: int


class SearchPostsResponseDataFirst_postLinks(TypedDict):
    permalink: str
    detail: str
    thread: str
    poster: str
    likes: str
    report: str
    attachments: str
    poster_avatar: str


class SearchPostsResponseDataFirst_postPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    reply: bool
    like: bool
    report: bool
    upload_attachment: bool


class SearchPostsResponseDataFirst_post(TypedDict):
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
    post_attachment_count: int
    user_is_ignored: bool
    post_is_published: bool
    post_is_deleted: bool
    post_update_date: int
    post_is_first_post: bool
    links: SearchPostsResponseDataFirst_postLinks
    permissions: SearchPostsResponseDataFirst_postPermissions


class SearchPostsResponseDataLinks(TypedDict):
    permalink: str
    detail: str
    followers: str
    forum: str
    posts: str
    first_poster: str
    first_poster_avatar: str
    first_post: str
    last_post: str


class SearchPostsResponseDataPermissions(TypedDict):
    view: bool
    delete: bool
    follow: bool
    post: bool
    upload_attachment: bool
    edit: bool


SearchPostsResponseDataForumLinks = TypedDict(
    "SearchPostsResponseDataForumLinks",
    {
        "permalink": str,
        "detail": str,
        "sub-categories": str,
        "sub-forums": str,
        "threads": str,
        "followers": str,
    },
)


class SearchPostsResponseDataForumPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    create_thread: bool
    upload_attachment: bool
    tag_thread: bool
    follow: bool


class SearchPostsResponseDataForum(TypedDict):
    forum_id: int
    forum_title: str
    forum_description: str
    forum_thread_count: int
    forum_post_count: int
    forum_prefixes: list[object]
    thread_default_prefix_id: int
    thread_prefix_is_required: bool
    links: SearchPostsResponseDataForumLinks
    permissions: SearchPostsResponseDataForumPermissions
    forum_is_followed: bool


class SearchPostsResponseData(TypedDict):
    content_type: str
    content_id: int
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
    thread_is_followed: bool
    first_post: SearchPostsResponseDataFirst_post
    thread_prefixes: list[object]
    thread_tags: list[object]
    links: SearchPostsResponseDataLinks
    permissions: SearchPostsResponseDataPermissions
    forum: SearchPostsResponseDataForum


class SearchPostsResponseLinks(TypedDict):
    pages: int
    page: int
    next: str


class SearchPostsResponse(TypedDict):
    data: list[SearchPostsResponseData]
    data_total: int
    links: SearchPostsResponseLinks
    system_info: Resp_SystemInfo


class SearchUsersBody(TypedDict, total=False):
    q: str


class SearchUsersResponse(TypedDict):
    users: list[Resp_UserModel]
    system_info: Resp_SystemInfo


class SearchProfilepostsBody(TypedDict, total=False):
    q: str
    user_id: int
    page: int
    limit: int


class SearchProfilepostsResponseDataLinks(TypedDict):
    permalink: str
    detail: str
    timeline: str
    timeline_user: str
    poster: str
    likes: str
    comments: str
    report: str
    poster_avatar: str


class SearchProfilepostsResponseDataPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    like: bool
    comment: bool
    report: bool


class SearchProfilepostsResponseData(TypedDict):
    content_type: str
    content_id: int
    profile_post_id: int
    timeline_user_id: int
    poster_user_id: int
    poster_username: str
    poster_username_html: str
    post_create_date: int
    post_body: str
    post_like_count: int
    post_comment_count: int
    timeline_username: str
    user_is_ignored: bool
    post_is_published: bool
    post_is_deleted: bool
    links: SearchProfilepostsResponseDataLinks
    permissions: SearchProfilepostsResponseDataPermissions
    timeline_user: Resp_UserModel


class SearchProfilepostsResponseLinks(TypedDict):
    pages: int
    page: int
    next: str


class SearchProfilepostsResponse(TypedDict):
    data: list[SearchProfilepostsResponseData]
    data_total: int
    links: SearchProfilepostsResponseLinks
    system_info: Resp_SystemInfo


class SearchTaggedBody(TypedDict, total=False):
    tag: str
    tags: list[str]
    page: int
    limit: int


class SearchTaggedResponseDataFirst_postLinks(TypedDict):
    permalink: str
    detail: str
    thread: str
    poster: str
    likes: str
    report: str
    attachments: str
    poster_avatar: str


class SearchTaggedResponseDataFirst_postPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    reply: bool
    like: bool
    report: bool
    upload_attachment: bool


class SearchTaggedResponseDataFirst_post(TypedDict):
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
    post_attachment_count: int
    user_is_ignored: bool
    post_is_published: bool
    post_is_deleted: bool
    post_update_date: int
    post_is_first_post: bool
    links: SearchTaggedResponseDataFirst_postLinks
    permissions: SearchTaggedResponseDataFirst_postPermissions


SearchTaggedResponseDataThread_tags = TypedDict(
    "SearchTaggedResponseDataThread_tags",
    {
        "160179": str,
    },
)


class SearchTaggedResponseDataLinks(TypedDict):
    permalink: str
    detail: str
    followers: str
    forum: str
    posts: str
    first_poster: str
    first_poster_avatar: str
    first_post: str
    last_post: str


class SearchTaggedResponseDataPermissions(TypedDict):
    view: bool
    delete: bool
    follow: bool
    post: bool
    upload_attachment: bool
    edit: bool
    edit_title: bool
    edit_tags: bool


class SearchTaggedResponseDataForumForum_prefixesGroup_prefixes(TypedDict):
    prefix_id: int
    prefix_title: str


class SearchTaggedResponseDataForumForum_prefixes(TypedDict):
    group_title: str
    group_prefixes: list[SearchTaggedResponseDataForumForum_prefixesGroup_prefixes]


SearchTaggedResponseDataForumLinks = TypedDict(
    "SearchTaggedResponseDataForumLinks",
    {
        "permalink": str,
        "detail": str,
        "sub-categories": str,
        "sub-forums": str,
        "threads": str,
        "followers": str,
    },
)


class SearchTaggedResponseDataForumPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    create_thread: bool
    upload_attachment: bool
    tag_thread: bool
    follow: bool


class SearchTaggedResponseDataForum(TypedDict):
    forum_id: int
    forum_title: str
    forum_description: str
    forum_thread_count: int
    forum_post_count: int
    forum_prefixes: list[SearchTaggedResponseDataForumForum_prefixes]
    thread_default_prefix_id: int
    thread_prefix_is_required: bool
    links: SearchTaggedResponseDataForumLinks
    permissions: SearchTaggedResponseDataForumPermissions
    forum_is_followed: bool


class SearchTaggedResponseData(TypedDict):
    content_type: str
    content_id: int
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
    thread_is_followed: bool
    first_post: SearchTaggedResponseDataFirst_post
    thread_prefixes: list[object]
    thread_tags: SearchTaggedResponseDataThread_tags
    links: SearchTaggedResponseDataLinks
    permissions: SearchTaggedResponseDataPermissions
    forum: SearchTaggedResponseDataForum


SearchTaggedResponseSearch_tags = TypedDict(
    "SearchTaggedResponseSearch_tags",
    {
        "160179": str,
    },
)


class SearchTaggedResponse(TypedDict):
    data: list[SearchTaggedResponseData]
    data_total: int
    search_tags: SearchTaggedResponseSearch_tags
    system_info: Resp_SystemInfo


class SearchResultsBody(TypedDict, total=False):
    page: int
    limit: int


class SearchResultsResponseDataFirst_postLinks(TypedDict):
    permalink: str
    detail: str
    thread: str
    poster: str
    likes: str
    report: str
    attachments: str
    poster_avatar: str


class SearchResultsResponseDataFirst_postPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    reply: bool
    like: bool
    report: bool
    upload_attachment: bool


class SearchResultsResponseDataFirst_post(TypedDict):
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
    post_attachment_count: int
    user_is_ignored: bool
    post_is_published: bool
    post_is_deleted: bool
    post_update_date: int
    post_is_first_post: bool
    links: SearchResultsResponseDataFirst_postLinks
    permissions: SearchResultsResponseDataFirst_postPermissions


SearchResultsResponseDataThread_tags = TypedDict(
    "SearchResultsResponseDataThread_tags",
    {
        "160179": str,
    },
)


class SearchResultsResponseDataLinks(TypedDict):
    permalink: str
    detail: str
    followers: str
    forum: str
    posts: str
    first_poster: str
    first_poster_avatar: str
    first_post: str
    last_post: str


class SearchResultsResponseDataPermissions(TypedDict):
    view: bool
    delete: bool
    follow: bool
    post: bool
    upload_attachment: bool
    edit: bool
    edit_title: bool
    edit_tags: bool


class SearchResultsResponseDataForumForum_prefixesGroup_prefixes(TypedDict):
    prefix_id: int
    prefix_title: str


class SearchResultsResponseDataForumForum_prefixes(TypedDict):
    group_title: str
    group_prefixes: list[SearchResultsResponseDataForumForum_prefixesGroup_prefixes]


SearchResultsResponseDataForumLinks = TypedDict(
    "SearchResultsResponseDataForumLinks",
    {
        "permalink": str,
        "detail": str,
        "sub-categories": str,
        "sub-forums": str,
        "threads": str,
        "followers": str,
    },
)


class SearchResultsResponseDataForumPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    create_thread: bool
    upload_attachment: bool
    tag_thread: bool
    follow: bool


class SearchResultsResponseDataForum(TypedDict):
    forum_id: int
    forum_title: str
    forum_description: str
    forum_thread_count: int
    forum_post_count: int
    forum_prefixes: list[SearchResultsResponseDataForumForum_prefixes]
    thread_default_prefix_id: int
    thread_prefix_is_required: bool
    links: SearchResultsResponseDataForumLinks
    permissions: SearchResultsResponseDataForumPermissions
    forum_is_followed: bool


class SearchResultsResponseData(TypedDict):
    content_type: str
    content_id: int
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
    thread_is_followed: bool
    first_post: SearchResultsResponseDataFirst_post
    thread_prefixes: list[object]
    thread_tags: SearchResultsResponseDataThread_tags
    links: SearchResultsResponseDataLinks
    permissions: SearchResultsResponseDataPermissions
    forum: SearchResultsResponseDataForum


SearchResultsResponseSearch_tags = TypedDict(
    "SearchResultsResponseSearch_tags",
    {
        "160179": str,
    },
)


class SearchResultsResponse(TypedDict):
    data: list[SearchResultsResponseData]
    data_total: int
    search_tags: SearchResultsResponseSearch_tags
    system_info: Resp_SystemInfo


# ─── BatchApi Types ────────────────────────────────────────


BatchExecuteBody = list[dict[str, object]]


class BatchExecuteResponseJobs(TypedDict):
    job_id: dict[str, object]


class BatchExecuteResponse(TypedDict):
    jobs: BatchExecuteResponseJobs


# ─── ChatboxApi Types ────────────────────────────────────────


class ChatboxIndexParams(TypedDict, total=False):
    room_id: RoomIDModel


class ChatboxIndexResponseRooms(TypedDict):
    can_report: bool
    eng: bool
    market: bool
    room_id: int
    title: str


class ChatboxIndexResponseIgnoreRenderedAvatars(TypedDict):
    l: str
    m: str
    s: str


class ChatboxIndexResponseIgnoreRendered(TypedDict):
    username: str
    avatars: ChatboxIndexResponseIgnoreRenderedAvatars
    link: str


class ChatboxIndexResponseIgnore(TypedDict):
    avatar_date: int
    background_date: int
    contest_count: int
    custom_title: str
    display_banner_id: int
    display_icon_group_id: int
    display_style_group_id: int
    is_admin: bool
    is_banned: bool
    is_moderator: bool
    is_staff: bool
    last_activity: int
    like2_count: int
    like_count: int
    message_count: int
    register_date: int
    rendered: ChatboxIndexResponseIgnoreRendered
    short_link: object
    trophy_points: int
    uniq_banner: object
    uniq_username_css: str
    user_id: int
    username: str


class ChatboxIndexResponsePermissions(TypedDict):
    deleteAnyMessage: bool
    editAnyMessage: bool
    viewAnyMessage: bool
    viewMessages: bool
    postMessage: bool
    ban: bool


ChatboxIndexResponseRoomsOnline = TypedDict(
    "ChatboxIndexResponseRoomsOnline",
    {
        "chat:0": int,
    },
)


class ChatboxIndexResponse(TypedDict):
    rooms: list[ChatboxIndexResponseRooms]
    ban: object
    ignore: list[ChatboxIndexResponseIgnore]
    permissions: ChatboxIndexResponsePermissions
    commands: list[str]
    roomsOnline: ChatboxIndexResponseRoomsOnline
    system_info: Resp_SystemInfo


class _ChatboxGetmessagesParamsRequired(TypedDict):
    room_id: RoomIDModel


class ChatboxGetmessagesParams(_ChatboxGetmessagesParamsRequired, total=False):
    before_message_id: int


class ChatboxGetmessagesResponse(TypedDict):
    messages: list[Resp_ChatboxMessageModel]
    system_info: Resp_SystemInfo


class _ChatboxPostmessageBodyRequired(TypedDict):
    room_id: RoomIDModel
    message: str


class ChatboxPostmessageBody(_ChatboxPostmessageBodyRequired, total=False):
    reply_message_id: int


class ChatboxPostmessageResponse(TypedDict):
    message: Resp_ChatboxMessageModel
    system_info: Resp_SystemInfo


class ChatboxEditmessageBody(TypedDict):
    message_id: int
    message: str


class ChatboxEditmessageResponse(TypedDict):
    message: Resp_ChatboxMessageModel
    system_info: Resp_SystemInfo


class ChatboxDeletemessageBody(TypedDict):
    message_id: int


class ChatboxDeletemessageResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ChatboxOnlineParams(TypedDict):
    room_id: RoomIDModel


class ChatboxOnlineResponseUsersRenderedAvatars(TypedDict):
    l: str
    m: str
    s: str


class ChatboxOnlineResponseUsersRendered(TypedDict):
    username: str
    avatars: ChatboxOnlineResponseUsersRenderedAvatars
    link: str


class ChatboxOnlineResponseUsersUniq_banner(TypedDict):
    banner_css: str
    banner_text: str
    banner_icon: str
    username_icon: str


class ChatboxOnlineResponseUsers(TypedDict):
    avatar_date: int
    background_date: int
    contest_count: int
    custom_title: str
    display_banner_id: int
    display_icon_group_id: int
    display_style_group_id: int
    is_admin: bool
    is_banned: bool
    is_moderator: bool
    is_staff: bool
    last_activity: int
    like2_count: int
    like_count: int
    message_count: int
    register_date: int
    rendered: ChatboxOnlineResponseUsersRendered
    short_link: str
    trophy_points: int
    uniq_banner: ChatboxOnlineResponseUsersUniq_banner
    uniq_username_css: str
    user_id: int
    username: str


class ChatboxOnlineResponse(TypedDict):
    users: list[ChatboxOnlineResponseUsers]
    system_info: Resp_SystemInfo


class ChatboxReportreasonsParams(TypedDict):
    message_id: int


class ChatboxReportreasonsResponse(TypedDict):
    reasons: list[str]
    system_info: Resp_SystemInfo


class ChatboxReportBody(TypedDict):
    message_id: int
    reason: str


class ChatboxReportResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ChatboxGetleaderboardParams(TypedDict, total=False):
    duration: Literal["day", "week", "month"]


class ChatboxGetleaderboardResponseLeaderboardRenderedAvatars(TypedDict):
    l: str
    m: str
    s: str


class ChatboxGetleaderboardResponseLeaderboardRendered(TypedDict):
    username: str
    avatars: ChatboxGetleaderboardResponseLeaderboardRenderedAvatars
    link: str


class ChatboxGetleaderboardResponseLeaderboardUniq_banner(TypedDict):
    banner_css: str
    banner_text: str
    banner_icon: str


class ChatboxGetleaderboardResponseLeaderboard(TypedDict):
    count: int
    user_id: int
    avatar_date: int
    background_date: int
    contest_count: int
    custom_title: str
    display_banner_id: int
    display_icon_group_id: int
    display_style_group_id: int
    is_banned: bool
    last_activity: int
    like2_count: int
    like_count: int
    message_count: int
    register_date: int
    rendered: ChatboxGetleaderboardResponseLeaderboardRendered
    short_link: object
    trophy_points: int
    uniq_banner: ChatboxGetleaderboardResponseLeaderboardUniq_banner
    uniq_username_css: str
    username: str


class ChatboxGetleaderboardResponse(TypedDict):
    leaderboard: list[ChatboxGetleaderboardResponseLeaderboard]
    system_info: Resp_SystemInfo


class ChatboxGetignoreResponseIgnoredRenderedAvatars(TypedDict):
    l: str
    m: str
    s: str


class ChatboxGetignoreResponseIgnoredRendered(TypedDict):
    username: str
    avatars: ChatboxGetignoreResponseIgnoredRenderedAvatars
    link: str


class ChatboxGetignoreResponseIgnored(TypedDict):
    avatar_date: int
    background_date: int
    contest_count: int
    custom_title: str
    display_banner_id: int
    display_icon_group_id: int
    display_style_group_id: int
    is_banned: bool
    last_activity: int
    like2_count: int
    like_count: int
    message_count: int
    register_date: int
    rendered: ChatboxGetignoreResponseIgnoredRendered
    short_link: object
    trophy_points: int
    uniq_banner: object
    uniq_username_css: str
    user_id: int
    username: str


class ChatboxGetignoreResponse(TypedDict):
    ignored: list[ChatboxGetignoreResponseIgnored]
    system_info: Resp_SystemInfo


class ChatboxPostignoreBody(TypedDict):
    user_id: UserIDModel


class ChatboxPostignoreResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ChatboxDeleteignoreBody(TypedDict):
    user_id: UserIDModel


class ChatboxDeleteignoreResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


# ─── FormsApi Types ────────────────────────────────────────


class FormsListParams(TypedDict, total=False):
    page: int


class FormsListResponseFormsFieldsFieldChoices(TypedDict):
    buy: str
    sell: str


class FormsListResponseFormsFields(TypedDict):
    field_id: int
    title: str
    fieldChoices: FormsListResponseFormsFieldsFieldChoices
    required: int
    max_length: int
    default_value: str


class FormsListResponseForms(TypedDict):
    form_id: int
    title: str
    description: str
    fields: list[FormsListResponseFormsFields]


class FormsListResponse(TypedDict):
    forms: list[FormsListResponseForms]
    formsPerPage: int
    page: int
    totalForms: int
    system_info: Resp_SystemInfo


class FormsCreateP2PTradeBody(TypedDict):
    form_id: Literal[1]  # default: 1
    fields: dict[str, object]


class FormsCreateComplaintBody(TypedDict):
    form_id: Literal[3]  # default: 3
    fields: dict[str, object]


FormsCreateBody = FormsCreateP2PTradeBody | FormsCreateComplaintBody


class FormsCreateResponseContentLinks(TypedDict):
    permalink: str
    detail: str
    followers: str
    forum: str
    posts: str
    first_poster: str
    first_poster_avatar: str
    first_post: str


class FormsCreateResponseContentPermissions(TypedDict):
    view: bool
    delete: bool
    follow: bool
    post: bool


class FormsCreateResponseContent(TypedDict):
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
    thread_prefixes: list[object]
    thread_tags: list[object]
    links: FormsCreateResponseContentLinks
    permissions: FormsCreateResponseContentPermissions
    node_title: str


class FormsCreateResponse(TypedDict):
    message: str
    content: FormsCreateResponseContent
    system_info: Resp_SystemInfo
