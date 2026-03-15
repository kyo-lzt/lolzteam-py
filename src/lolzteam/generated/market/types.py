# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Literal, TypedDict

# ─── Component Schemas ────────────────────────────────────────


class DiscountModel(TypedDict):
    category_id: int
    discount_id: int
    discount_percent: int
    discount_user_id: int
    max_price: int
    min_price: int
    user_id: int


CategoryIDModel = Literal[
    1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 28, 30, 31
]


class UserModelBalances(TypedDict):
    balance: str
    balance_id: int
    convertedBalance: float
    custom_title: object
    fullTitle: str
    merchant_id: int
    title: str
    type: str
    user_id: int


class UserModelCustom_fields(TypedDict):
    _4: str
    allowSelfUnban: list[object]
    ban_reason: str
    discord: str
    github: str
    jabber: str
    lztAwardUserTrophy: str
    lztLikesIncreasing: str
    lztLikesZeroing: str
    lztSympathyIncreasing: str
    lztSympathyZeroing: str
    lztUnbanAmount: str
    maecenasValue: str
    scamURL: str
    steam: str
    telegram: str
    vk: str
    favoritePorn: str
    favoriteVape: str
    favoriteAnime: str
    matrix: str


class UserModelDob(TypedDict):
    year: int
    month: int
    day: int


class UserModelFeedback_data12345(TypedDict):
    positive: int
    negative: int


UserModelFeedback_data = TypedDict(
    "UserModelFeedback_data",
    {
        "12345": UserModelFeedback_data12345,
    },
)


class UserModelImap_dataDomainZone(TypedDict):
    domain: str
    imap_server: str
    port: int
    secure: bool


UserModelImap_data = TypedDict(
    "UserModelImap_data",
    {
        "domain.zone": UserModelImap_dataDomainZone,
    },
)


class UserModelPublic_tags(TypedDict):
    background_color: str
    tag_id: int
    title: str


class UserModelRenderedAvatars(TypedDict):
    l: str
    m: str
    s: str


class UserModelRenderedBackgrounds(TypedDict):
    l: str
    m: str


class UserModelRendered(TypedDict):
    username: str
    avatars: UserModelRenderedAvatars
    backgrounds: UserModelRenderedBackgrounds
    link: str


UserModelRestore_data = TypedDict(
    "UserModelRestore_data",
    {
        "12345": int,
    },
)


class UserModelTags(TypedDict):
    tag_id: int
    title: str
    isDefault: bool
    forOwnedAccountsOnly: bool
    bc: str


class UserModelTelegram_client(TypedDict):
    telegram_api_id: str
    telegram_api_hash: str
    telegram_device_model: str
    telegram_system_version: str
    telegram_app_version: str
    telegram_system_lang_code: str
    telegram_lang_code: str
    telegram_lang_pack: str


class UserModel(TypedDict):
    active_items_count: int
    activity_visible: bool
    age: int
    balance: str
    balances: list[UserModelBalances]
    bump_item_period: int
    can_edit: bool
    can_follow: bool
    can_ignore: bool
    can_post_profile: bool
    can_view_profile: bool
    can_view_profile_posts: bool
    can_warn: bool
    contest_count: int
    conv_welcome_message: str
    convertedBalance: int
    convertedDeposit: int
    convertedHold: int
    currency: str
    currencyPhrase: str
    custom_account_download_format: str
    custom_fields: UserModelCustom_fields
    custom_title: str
    deposit: int
    dob: UserModelDob
    feedback_data: UserModelFeedback_data
    hold: str
    homepage: str
    imap_data: UserModelImap_data
    is_admin: bool
    is_banned: bool
    is_followed: bool
    is_ignored: bool
    is_moderator: bool
    is_staff: bool
    is_super_admin: bool
    joined_date: int
    last_activity: int
    like2_count: int
    like_count: int
    location: str
    market_custom_title: str
    max_discount_percent: int
    message_count: int
    paid_mail_left: int
    public_tags: list[UserModelPublic_tags]
    register_date: int
    rendered: UserModelRendered
    restore_count: int
    restore_data: UserModelRestore_data
    short_link: str
    sold_items_count: int
    tags: list[UserModelTags]
    telegram_client: UserModelTelegram_client
    trophy_points: int
    user_allow_ask_discount: bool
    user_id: int
    user_title: str
    username: str
    view_url: str
    visible: bool
    warning_points: int


class BalanceModel(TypedDict):
    balance: str
    balance_id: int
    custom_title: object
    fullTitle: str
    merchant_id: int
    title: str
    type: str
    user_id: int


class ExtraModel(TypedDict, total=False):
    proxy: str
    close_item: bool
    region: str
    service: Literal[
        "AdguardVPN",
        "PIAVPN",
        "cyberghostVPN",
        "hotspotShieldVPN",
        "mullvadVPN",
        "pureVPN",
        "tunnelbearVPN",
        "ultraVPN",
        "vanishVPN",
        "vyprVPN",
        "windscribeVPN",
        "planetVPN",
        "start",
        "ivi",
        "telegram",
        "discord",
        "discord_trial",
    ]
    system: Literal["laser", "scroll", "magic"]
    confirmationCode: str
    cookies: str
    login_without_cookies: bool
    cookie_login: bool
    mfa_file: str
    dota2_mmr: int
    ea_games: bool
    uplay_games: bool
    the_quarry: bool
    warframe: bool
    ark: bool
    ark_ascended: bool
    genshin_currency: int
    honkai_currency: int
    zenless_currency: int
    password: str
    telegramClient: str
    telegramJson: str
    checkChannels: bool
    checkSpam: bool
    checkHypixelBan: bool


class ConfirmationCodeModelCodeData(TypedDict):
    code: str
    date: int
    textPlain: str


class ConfirmationCodeModel(TypedDict):
    item: ItemModel
    codeData: ConfirmationCodeModelCodeData


CurrencyModel = Literal["rub", "uah", "kzt", "byn", "usd", "eur", "gbp", "cny", "try", "jpy", "brl"]


DatePeriodModel = Literal["day", "month", "year"]


YesNoNoMatterScheme = Literal["yes", "no", "nomatter"]


class ItemListModel(TypedDict):
    items: list[ItemFromListModel]
    totalItems: int
    totalItemsPrice: object
    hasNextPage: bool
    perPage: int
    page: int
    searchUrl: str
    stickyItems: list[ItemFromListModel]
    system_info: Resp_SystemInfo


class ItemFromListModelBumpSettings(TypedDict, total=False):
    canBumpItem: bool
    canBumpItemGlobally: bool
    shortErrorPhrase: str
    errorPhrase: str


class ItemFromListModelSeller(TypedDict, total=False):
    user_id: int
    sold_items_count: int
    active_item_count: int
    restore_data: str
    username: str
    avatar_date: int
    is_banned: int
    display_style_group_id: int
    restore_percents: int


class ItemFromListModel(TypedDict, total=False):
    item_id: int
    item_state: str
    category_id: int
    published_date: int
    title: str
    description: str
    price: int
    update_stat_date: int
    refreshed_date: int
    view_count: int
    is_sticky: int
    item_origin: str
    extended_guarantee: int
    nsb: int
    allow_ask_discount: int
    title_en: str
    description_en: str
    item_domain: str
    resale_item_origin: str
    isIgnored: int
    guarantee: bool
    canViewLoginData: bool
    canUpdateItemStats: bool
    canViewEmailLoginData: bool
    showGetEmailCodeButton: bool
    canOpenItem: bool
    canCloseItem: bool
    canEditItem: bool
    canDeleteItem: bool
    canStickItem: bool
    canUnstickItem: bool
    bumpSettings: ItemFromListModelBumpSettings
    canBumpItem: bool
    canBuyItem: bool
    rub_price: int
    price_currency: str
    canValidateAccount: bool
    canResellItemAfterPurchase: bool
    canViewAccountLink: bool
    itemOriginPhrase: str
    tags: list[str]
    note_text: str
    description_html: str
    description_html_en: str
    seller: ItemFromListModelSeller


ItemModelGuarantee = TypedDict(
    "ItemModelGuarantee",
    {
        "duration": int,
        "class": str,
        "durationPhrase": str,
        "endDate": int,
        "active": bool,
        "cancelled": bool,
        "remainingTime": int,
        "remainingTimePhrase": str,
        "cancelledReason": str,
        "cancelledReasonPhrase": str,
    },
)


class ItemModelLoginData(TypedDict):
    raw: str
    encodedRaw: str
    login: str
    password: str
    encodedPassword: str
    oldPassword: str
    encodedOldPassword: object


class ItemModelCopyFormatData(TypedDict):
    title_link: str
    login_data: str
    full: str


class ItemModelBuyer(TypedDict):
    user_id: int
    operation_date: int
    visitorIsBuyer: bool
    username: str
    is_banned: int
    display_style_group_id: int
    display_icon_group_id: int
    uniq_username_css: str
    uniq_banner: str
    user_group_id: int


class ItemModelAccountLinks(TypedDict):
    link: str
    text: str
    iconClass: str


class ItemModelTags1234567890(TypedDict):
    tag_id: int
    title: str
    isDefault: bool
    forOwnedAccountsOnly: bool
    bc: str


ItemModelTags = TypedDict(
    "ItemModelTags",
    {
        "1234567890": ItemModelTags1234567890,
    },
)


class ItemModelCustomFields(TypedDict):
    _4: str
    allowSelfUnban: list[object]
    ban_reason: str
    discord: str
    github: str
    jabber: str
    lztUnbanAmount: str
    steam: str
    telegram: str
    vk: str


class ItemModelExtraPrices(TypedDict):
    currency: str
    price: str
    priceValue: float


class ItemModelBumpSettings(TypedDict):
    canBumpItem: bool
    canBumpItemGlobally: bool
    shortErrorPhrase: object
    nextAllowedBumpDate: object
    errorPhrase: object


class ItemModelSellerContacts(TypedDict):
    ban_reason: str
    telegram: str


class ItemModelSeller(TypedDict):
    user_id: int
    username: str
    avatar_date: int
    is_banned: int
    display_style_group_id: int
    joined_date: int
    sold_items_count: int
    active_items_count: int
    restore_data: str
    effective_last_activity: int
    restore_percents: object
    isOnline: bool
    contacts: ItemModelSellerContacts


class ItemModel(TypedDict):
    item_id: int
    item_state: str
    category_id: int
    published_date: int
    title: str
    description: str
    price: int
    update_stat_date: int
    refreshed_date: int
    edit_date: int
    pending_deletion_date: int
    login: str
    temp_email: str
    view_count: int
    is_sticky: int
    information: str
    item_origin: str
    extended_guarantee: int
    nsb: int
    allow_ask_discount: int
    title_en: str
    description_en: str
    information_en: str
    email_type: str
    email_provider: str
    item_domain: str
    resale_item_origin: str
    note_text: str
    content_type: object
    content_id: object
    delete_date: int
    delete_user_id: int
    delete_username: str
    delete_reason: str
    user_allow_ask_discount: int
    max_discount_percent: int
    market_custom_title: str
    feedback_data: str
    buyer_display_icon_group_id: int
    buyer_uniq_banner: str
    buyer_avatar_date: int
    buyer_user_group_id: int
    is_fave: object
    in_cart: object
    cart_price: object
    canResellItem: bool
    priceWithSellerFee: float
    guarantee: ItemModelGuarantee
    canViewLoginData: bool
    canUpdateItemStats: bool
    canReportItem: bool
    canViewItemViews: bool
    loginData: ItemModelLoginData
    canViewEmailLoginData: bool
    copyFormatData: ItemModelCopyFormatData
    showGetEmailCodeButton: bool
    getEmailCodeDisplayLogin: object
    buyer: ItemModelBuyer
    isPersonalAccount: bool
    rub_price: int
    price_currency: str
    priceWithSellerFeeLabel: str
    canValidateAccount: bool
    canResellItemAfterPurchase: bool
    isSmallExf: bool
    account_last_activity: int
    canViewAccountLink: bool
    accountLinks: list[ItemModelAccountLinks]
    accountLink: str
    imagePreviewLinks: list[str]
    canChangePassword: bool
    canChangeEmailPassword: bool
    uniqueKeyExists: bool
    itemOriginPhrase: str
    visitorIsAuthor: bool
    canAskDiscount: bool
    tags: ItemModelTags
    customFields: ItemModelCustomFields
    externalAuth: list[object]
    isTrusted: bool
    isBirthdayToday: bool
    isIgnored: bool
    deposit: int
    extraPrices: list[ItemModelExtraPrices]
    canViewAccountLoginAndTempEmail: bool
    bumpSettings: ItemModelBumpSettings
    canCheckGuarantee: bool
    canShareItem: bool
    canCheckAiPrice: bool
    aiPrice: int
    aiPriceCheckDate: int
    needToRequireVideoToViewLoginData: bool
    canCheckAutoBuyPrice: bool
    autoBuyPrice: int
    autoBuyPriceCheckDate: int
    descriptionHtml: str
    descriptionEnHtml: str
    descriptionPlain: str
    descriptionEnPlain: str
    seller: ItemModelSeller


ItemIDModel = int


class InvoiceModel(TypedDict):
    additional_data: str
    amount: int
    comment: str
    expires_at: int
    invoice_date: int
    invoice_id: int
    is_test: bool
    merchant_id: int
    paid_date: int
    payer_user_id: int
    payment_id: str
    resend_attempts: int
    status: str
    url: str
    url_callback: str
    url_success: str
    user_id: int


class Resp_SystemInfo(TypedDict):
    visitor_id: int
    time: int
    log_id: int


# ─── CategoryApi Types ────────────────────────────────────────


CategoryAllParams = TypedDict(
    "CategoryAllParams",
    {
        "page": int,
        "pmin": int,
        "pmax": int,
        "title": str,
        "order_by": Literal[
            "price_to_up",
            "price_to_down",
            "pdate_to_down",
            "pdate_to_up",
            "pdate_to_down_upload",
            "pdate_to_up_upload",
            "edate_to_up",
            "edate_to_down",
            "ddate_to_up",
            "ddate_to_down",
        ],
        "tag_id[]": list[int],
        "not_tag_id[]": list[int],
        "public_tag_id[]": list[int],
        "not_public_tag_id[]": list[int],
        "origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "not_origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "user_id": int,
        "nsb": bool,
        "sb": bool,
        "nsb_by_me": bool,
        "sb_by_me": bool,
        "currency": Literal[
            "rub", "uah", "kzt", "byn", "usd", "eur", "gbp", "cny", "try", "jpy", "brl"
        ],
        "email_login_data": bool,
        "email_provider[]": list[
            Literal["other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"]
        ],
        "not_email_provider[]": Literal[
            "other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"
        ],
        "parse_same_item_ids": bool,
    },
    total=False,
)


class CategoryAllResponse(TypedDict):
    items: list[ItemFromListModel]
    totalItems: int
    totalItemsPrice: object
    hasNextPage: bool
    perPage: int
    page: int
    searchUrl: str
    stickyItems: list[ItemFromListModel]
    system_info: Resp_SystemInfo


CategorySteamParams = TypedDict(
    "CategorySteamParams",
    {
        "page": int,
        "pmin": int,
        "pmax": int,
        "title": str,
        "order_by": Literal[
            "price_to_up",
            "price_to_down",
            "pdate_to_down",
            "pdate_to_up",
            "pdate_to_down_upload",
            "pdate_to_up_upload",
            "edate_to_up",
            "edate_to_down",
            "ddate_to_up",
            "ddate_to_down",
        ],
        "tag_id[]": list[int],
        "not_tag_id[]": list[int],
        "public_tag_id[]": list[int],
        "not_public_tag_id[]": list[int],
        "origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "not_origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "user_id": int,
        "nsb": bool,
        "sb": bool,
        "nsb_by_me": bool,
        "sb_by_me": bool,
        "currency": Literal[
            "rub", "uah", "kzt", "byn", "usd", "eur", "gbp", "cny", "try", "jpy", "brl"
        ],
        "email_login_data": bool,
        "email_type[]": list[Literal["autoreg", "native", "no", "no_market"]],
        "email_provider[]": list[
            Literal["other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"]
        ],
        "not_email_provider[]": Literal[
            "other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"
        ],
        "parse_same_item_ids": bool,
        "item_domain": str,
        "game[]": list[int],
        "hours_played": dict[str, int],
        "hours_played_max": dict[str, int],
        "eg": Literal[-1, 0, 1],
        "vac[]": list[int],
        "vac_skip_game_check": bool,
        "rt": Literal["yes", "no", "nomatter"],
        "trade_ban": YesNoNoMatterScheme,
        "trade_limit": YesNoNoMatterScheme,
        "daybreak": int,
        "limit": YesNoNoMatterScheme,
        "mafile": YesNoNoMatterScheme,
        "reg": int,
        "reg_period": Literal["day", "month", "year"],
        "lmin": int,
        "lmax": int,
        "rmin": int,
        "rmax": int,
        "wingman_rmin": int,
        "wingman_rmax": int,
        "no_vac": bool,
        "mm_ban": YesNoNoMatterScheme,
        "balance_min": int,
        "balance_max": int,
        "inv_game": int,
        "inv_min": float,
        "inv_max": float,
        "friends_min": int,
        "friends_max": int,
        "gmin": int,
        "gmax": int,
        "win_count_min": int,
        "win_count_max": int,
        "medal_id[]": list[int],
        "medal_operator_or": bool,
        "medal_min": int,
        "medal_max": int,
        "gift[]": list[str],
        "gift_min": int,
        "gift_max": int,
        "recently_hours_min": int,
        "recently_hours_max": int,
        "country[]": list[str],
        "not_country[]": list[str],
        "cs2_profile_rank_min": int,
        "cs2_profile_rank_max": int,
        "solommr_min": int,
        "solommr_max": int,
        "d2_game_count_min": int,
        "d2_game_count_max": int,
        "d2_win_count_min": int,
        "d2_win_count_max": int,
        "d2_behavior_min": int,
        "d2_behavior_max": int,
        "faceit_lvl_min": int,
        "faceit_lvl_max": int,
        "points_min": int,
        "points_max": int,
        "relevant_gmin": int,
        "relevant_gmax": int,
        "last_trans_date": int,
        "last_trans_date_period": Literal["day", "month", "year"],
        "last_trans_date_later": int,
        "last_trans_date_period_later": DatePeriodModel,
        "no_trans": bool,
        "trans": bool,
        "gifts_purchase_min": float,
        "gifts_purchase_max": float,
        "refunds_purchase_min": float,
        "refunds_purchase_max": float,
        "ingame_purchase_min": float,
        "ingame_purchase_max": float,
        "games_purchase_min": float,
        "games_purchase_max": float,
        "purchase_min": float,
        "purchase_max": float,
        "has_activated_keys": YesNoNoMatterScheme,
        "elo_min": int,
        "elo_max": int,
        "cs2_map_rank": Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        "cs2_map_rmin": int,
        "cs2_map_rmax": int,
        "has_faceit": YesNoNoMatterScheme,
        "faceit_csgo_lvl_min": int,
        "faceit_csgo_lvl_max": int,
        "rust_deaths_min": int,
        "rust_deaths_max": int,
        "rust_kills_min": int,
        "rust_kills_max": int,
        "d2_last_match_date": int,
        "d2_last_match_date_period": Literal["day", "month", "year"],
        "cards_min": int,
        "cards_max": int,
        "cards_games_min": int,
        "cards_games_max": int,
        "skip_vac_inv": bool,
    },
    total=False,
)


class CategorySteamResponseItemsSteam_full_gamesList730(TypedDict):
    appid: int
    playtime_forever: float
    internal_game_id: int
    abbr: str
    title: str
    parentGameId: int
    img: str


CategorySteamResponseItemsSteam_full_gamesList = TypedDict(
    "CategorySteamResponseItemsSteam_full_gamesList",
    {
        "730": CategorySteamResponseItemsSteam_full_gamesList730,
    },
)


class CategorySteamResponseItemsSteam_full_games(TypedDict):
    list: CategorySteamResponseItemsSteam_full_gamesList
    total: int


CategorySteamResponseItemsGuarantee = TypedDict(
    "CategorySteamResponseItemsGuarantee",
    {
        "duration": int,
        "class": str,
        "durationPhrase": str,
        "endDate": object,
        "active": object,
        "cancelled": object,
        "remainingTime": object,
    },
)


class CategorySteamResponseItemsBumpSettings(TypedDict):
    canBumpItem: bool
    canBumpItemGlobally: bool
    shortErrorPhrase: object
    errorPhrase: object


class CategorySteamResponseItemsSteamData(TypedDict):
    steam_ban_type_id: list[object]


class CategorySteamResponseItemsSteamTransactions(TypedDict):
    date: str
    product: str
    type: str
    source: str
    amount: str


class CategorySteamResponseItemsAccountLinks(TypedDict):
    link: str
    text: str
    iconClass: str


class CategorySteamResponseItemsSeller(TypedDict):
    user_id: int
    sold_items_count: int
    active_items_count: int
    restore_data: str
    username: str
    avatar_date: int
    is_banned: int
    display_style_group_id: int
    restore_percents: int


class CategorySteamResponseItems(TypedDict):
    item_id: int
    item_state: str
    category_id: int
    published_date: int
    title: str
    description: str
    price: int
    update_stat_date: int
    refreshed_date: int
    edit_date: int
    view_count: int
    is_sticky: int
    item_origin: str
    extended_guarantee: int
    nsb: int
    allow_ask_discount: int
    title_en: str
    description_en: str
    email_type: str
    email_provider: str
    item_domain: str
    resale_item_origin: str
    steam_item_id: int
    steam_country: str
    steam_register_date: int
    steam_last_activity: int
    steam_full_games: CategorySteamResponseItemsSteam_full_games
    steam_community_ban: int
    steam_bans: str
    steam_cs2_profile_rank: int
    steam_balance: str
    steam_cs2_rank_id: int
    steam_is_limited: int
    steam_level: int
    steam_friend_count: int
    steam_cs2_last_activity: int
    steam_dota2_solo_mmr: int
    steam_cs2_ban_date: int
    steam_converted_balance: int
    steam_cards_count: int
    steam_cards_games: int
    steam_pubg_inv_value: int
    steam_cs2_inv_value: int
    steam_dota2_inv_value: int
    steam_tf2_inv_value: int
    steam_rust_inv_value: int
    steam_cs2_wingman_rank_id: int
    steam_game_count: int
    steam_steam_inv_value: int
    steam_inv_value: int
    steam_cs2_win_count: int
    steam_dota2_game_count: int
    steam_dota2_lose_count: int
    steam_dota2_win_count: int
    steam_hours_played_recently: str
    steam_faceit_level: int
    steam_points: int
    steam_last_transaction_date: int
    steam_relevant_game_count: int
    steam_gift_count: int
    steam_limit_spent: str
    steam_dota2_behavior: int
    steam_mfa: int
    steam_market: int
    steam_market_restrictions: int
    steam_market_ban_end_date: int
    steam_unturned_inv_value: int
    steam_cs2_last_launched: int
    steam_kf2_inv_value: int
    steam_dst_inv_value: int
    steam_cs2_premier_elo: int
    steam_has_activated_keys: int
    steam_cs2_ban_type: int
    steam_rust_kill_player: int
    steam_rust_deaths: int
    steam_total_gifts_rub: int
    steam_total_refunds_rub: int
    steam_total_ingame_rub: int
    steam_total_games_rub: int
    steam_total_purchased_rub: int
    steam_dota2_last_match_date: int
    feedback_data: str
    isIgnored: bool
    priceWithSellerFee: int
    guarantee: CategorySteamResponseItemsGuarantee
    canViewLoginData: bool
    canUpdateItemStats: bool
    canReportItem: bool
    canViewEmailLoginData: bool
    showGetEmailCodeButton: bool
    canOpenItem: bool
    canCloseItem: bool
    canEditItem: bool
    canDeleteItem: bool
    canStickItem: bool
    canUnstickItem: bool
    bumpSettings: CategorySteamResponseItemsBumpSettings
    canBumpItem: bool
    canBuyItem: bool
    rub_price: int
    price_currency: str
    canValidateAccount: bool
    canResellItemAfterPurchase: bool
    steamData: CategorySteamResponseItemsSteamData
    steamRelevantGameCount: int
    isSmallExf: bool
    account_last_activity: int
    hasCs2: bool
    hasDota2: bool
    hasPubg: bool
    hasTf2: bool
    hasRust: bool
    steam_cs2_ban_date_active: bool
    dota2CalibrationWarning: bool
    displayConvertedBalance: bool
    inventoryValue: list[object]
    steamCs2Medals: list[object]
    cs2RankExpired: bool
    steamDota2WinRate: int
    steamTransactions: list[CategorySteamResponseItemsSteamTransactions]
    hasPossibleBanInDota2: bool
    chineseAccount: bool
    cs2MapsRanks: list[object]
    cs2PremierElo: list[object]
    steamLifetimeTradeBan: bool
    canViewAccountLink: bool
    accountLinks: list[CategorySteamResponseItemsAccountLinks]
    accountLink: str
    emailLoginUrl: str
    canChangePassword: bool
    itemOriginPhrase: str
    sold_items_category_count: int
    restore_items_category_count: int
    tags: list[object]
    note_text: object
    hasPendingAutoBuy: bool
    descriptionHtml: str
    descriptionEnHtml: str
    descriptionPlain: str
    descriptionEnPlain: str
    seller: CategorySteamResponseItemsSeller


class CategorySteamResponse(TypedDict):
    items: list[CategorySteamResponseItems]
    totalItems: int
    totalItemsPrice: object
    hasNextPage: bool
    perPage: int
    page: int
    wasCached: bool
    cacheTTL: int
    lastModified: int
    serverTime: int
    searchUrl: str
    stickyItems: list[object]
    system_info: Resp_SystemInfo


CategoryFortniteParams = TypedDict(
    "CategoryFortniteParams",
    {
        "page": int,
        "pmin": int,
        "pmax": int,
        "title": str,
        "order_by": Literal[
            "price_to_up",
            "price_to_down",
            "pdate_to_down",
            "pdate_to_up",
            "pdate_to_down_upload",
            "pdate_to_up_upload",
            "edate_to_up",
            "edate_to_down",
            "ddate_to_up",
            "ddate_to_down",
        ],
        "tag_id[]": list[int],
        "not_tag_id[]": list[int],
        "public_tag_id[]": list[int],
        "not_public_tag_id[]": list[int],
        "origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "not_origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "user_id": int,
        "nsb": bool,
        "sb": bool,
        "nsb_by_me": bool,
        "sb_by_me": bool,
        "currency": Literal[
            "rub", "uah", "kzt", "byn", "usd", "eur", "gbp", "cny", "try", "jpy", "brl"
        ],
        "email_login_data": bool,
        "email_provider[]": list[
            Literal["other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"]
        ],
        "email_type[]": list[Literal["market", "autoreg", "native", "no"]],
        "not_email_provider[]": Literal[
            "other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"
        ],
        "parse_same_item_ids": bool,
        "temp_email": Literal["yes", "no", "nomatter"],
        "item_domain": str,
        "eg": Literal[-1, 0, 1, 2],
        "smin": int,
        "smax": int,
        "vbmin": int,
        "vbmax": int,
        "skin[]": list[str],
        "pickaxe[]": list[str],
        "glider[]": list[str],
        "dance[]": list[str],
        "change_email": Literal["yes", "no", "nomatter"],
        "platform[]": list[
            Literal[
                "Epic",
                "EpicAndroid",
                "EpicIOS",
                "EpicPC",
                "EpicPCKorea",
                "GooglePlay",
                "IOSAppStore",
                "Live",
                "Nintendo",
                "OneStoreKorea",
                "PSN",
                "Samsung",
            ]
        ],
        "skins_shop_min": int,
        "skins_shop_max": int,
        "pickaxes_shop_min": int,
        "pickaxes_shop_max": int,
        "dances_shop_min": int,
        "dances_shop_max": int,
        "gliders_shop_min": int,
        "gliders_shop_max": int,
        "skins_shop_vbmin": int,
        "skins_shop_vbmax": int,
        "pickaxes_shop_vbmin": int,
        "pickaxes_shop_vbmax": int,
        "dances_shop_vbmin": int,
        "dances_shop_vbmax": int,
        "gliders_shop_vbmin": int,
        "gliders_shop_vbmax": int,
        "bp": YesNoNoMatterScheme,
        "lmin": int,
        "lmax": int,
        "bp_lmin": int,
        "bp_lmax": int,
        "last_trans_date": int,
        "last_trans_date_period": Literal["day", "month", "year"],
        "no_trans": bool,
        "xbox_linkable": YesNoNoMatterScheme,
        "psn_linkable": YesNoNoMatterScheme,
        "daybreak": int,
        "rl_purchases": bool,
        "reg": int,
        "reg_period": Literal["day", "month", "year"],
        "refund_credits_min": int,
        "refund_credits_max": int,
        "pickaxe_min": int,
        "pickaxe_max": int,
        "dmin": int,
        "dmax": int,
        "gmin": int,
        "gmax": int,
        "country[]": list[str],
        "not_country[]": list[str],
    },
    total=False,
)


class CategoryFortniteResponseItemsBumpSettings(TypedDict):
    canBumpItem: bool
    canBumpItemGlobally: bool
    shortErrorPhrase: object
    errorPhrase: object


class CategoryFortniteResponseItemsFortniteSkins(TypedDict):
    id: str
    title: str
    rarity: str
    type: str
    from_shop: int


class CategoryFortniteResponseItemsFortnitePickaxe(TypedDict):
    id: str
    title: str
    rarity: str
    type: str
    from_shop: int


class CategoryFortniteResponseItemsFortniteDance(TypedDict):
    id: str
    title: str
    rarity: str
    type: str
    from_shop: int


class CategoryFortniteResponseItemsFortniteGliders(TypedDict):
    id: str
    title: str
    rarity: str
    type: str
    from_shop: int


class CategoryFortniteResponseItemsFortnitePastSeasons(TypedDict):
    numWins: int
    seasonXp: int
    purchasedVIP: bool
    survivorPrestige: int
    seasonLevel: int
    numLowBracket: int
    bookLevel: int
    numRoyalRoyales: int
    seasonNumber: int
    survivorTier: int
    numHighBracket: int


class CategoryFortniteResponseItemsFortniteTransactions(TypedDict):
    date: int
    title: str
    presentmentTotal: str
    orderType: str


class CategoryFortniteResponseItemsShopCounts(TypedDict):
    shopSkinsCount: int
    shopPickaxesCount: int
    shopDancesCount: int
    shopGlidersCount: int


class CategoryFortniteResponseItemsSeller(TypedDict):
    user_id: int
    sold_items_count: int
    active_items_count: int
    restore_data: str
    username: str
    avatar_date: int
    is_banned: int
    display_style_group_id: int
    restore_percents: int


class CategoryFortniteResponseItems(TypedDict):
    item_id: int
    item_state: str
    category_id: int
    published_date: int
    title: str
    description: str
    price: int
    update_stat_date: int
    refreshed_date: int
    edit_date: int
    view_count: int
    is_sticky: int
    item_origin: str
    extended_guarantee: int
    nsb: int
    allow_ask_discount: int
    title_en: str
    description_en: str
    email_type: str
    email_provider: str
    item_domain: str
    resale_item_origin: str
    fortnite_item_id: int
    fortnite_platform: str
    fortnite_register_date: int
    fortnite_last_activity: int
    fortnite_book_level: int
    fortnite_lifetime_wins: int
    fortnite_level: int
    fortnite_season_num: int
    fortnite_books_purchased: int
    fortnite_balance: int
    fortnite_skin_count: int
    fortnite_change_email: int
    fortnite_rl_purchases: int
    fortnite_next_change_email_date: int
    fortnite_last_trans_date: int
    fortnite_xbox_linkable: int
    fortnite_psn_linkable: int
    fortnite_shop_skins_count: int
    fortnite_shop_pickaxes_count: int
    fortnite_shop_dances_count: int
    fortnite_shop_gliders_count: int
    feedback_data: str
    isIgnored: bool
    priceWithSellerFee: int
    guarantee: object
    canViewLoginData: bool
    canUpdateItemStats: bool
    canReportItem: bool
    canViewEmailLoginData: bool
    showGetEmailCodeButton: bool
    canOpenItem: bool
    canCloseItem: bool
    canEditItem: bool
    canDeleteItem: bool
    canStickItem: bool
    canUnstickItem: bool
    bumpSettings: CategoryFortniteResponseItemsBumpSettings
    canBumpItem: bool
    canBuyItem: bool
    rub_price: int
    price_currency: str
    canValidateAccount: bool
    canResellItemAfterPurchase: bool
    fortniteSkins: list[CategoryFortniteResponseItemsFortniteSkins]
    fortnitePickaxe: list[CategoryFortniteResponseItemsFortnitePickaxe]
    fortniteDance: list[CategoryFortniteResponseItemsFortniteDance]
    fortniteGliders: list[CategoryFortniteResponseItemsFortniteGliders]
    fortnite_pickaxe_count: int
    fortnite_dance_count: int
    fortnite_glider_count: int
    fortnitePastSeasons: list[CategoryFortniteResponseItemsFortnitePastSeasons]
    isSmallExf: bool
    account_last_activity: int
    fortniteTransactions: list[CategoryFortniteResponseItemsFortniteTransactions]
    domain: str
    shopCounts: CategoryFortniteResponseItemsShopCounts
    canViewAccountLink: bool
    accountLinks: list[object]
    emailLoginUrl: str
    canChangePassword: bool
    itemOriginPhrase: str
    sold_items_category_count: int
    restore_items_category_count: int
    tags: list[object]
    note_text: object
    hasPendingAutoBuy: bool
    descriptionHtml: str
    descriptionEnHtml: str
    descriptionPlain: str
    descriptionEnPlain: str
    seller: CategoryFortniteResponseItemsSeller


class CategoryFortniteResponse(TypedDict):
    items: list[CategoryFortniteResponseItems]
    totalItems: int
    totalItemsPrice: object
    hasNextPage: bool
    perPage: int
    page: int
    wasCached: bool
    cacheTTL: int
    lastModified: int
    serverTime: int
    searchUrl: str
    stickyItems: list[object]
    system_info: Resp_SystemInfo


CategoryMihoyoParams = TypedDict(
    "CategoryMihoyoParams",
    {
        "page": int,
        "pmin": int,
        "pmax": int,
        "title": str,
        "order_by": Literal[
            "price_to_up",
            "price_to_down",
            "pdate_to_down",
            "pdate_to_up",
            "pdate_to_down_upload",
            "pdate_to_up_upload",
            "edate_to_up",
            "edate_to_down",
            "ddate_to_up",
            "ddate_to_down",
        ],
        "tag_id[]": list[int],
        "not_tag_id[]": list[int],
        "public_tag_id[]": list[int],
        "not_public_tag_id[]": list[int],
        "origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "not_origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "user_id": int,
        "nsb": bool,
        "sb": bool,
        "nsb_by_me": bool,
        "sb_by_me": bool,
        "currency": Literal[
            "rub", "uah", "kzt", "byn", "usd", "eur", "gbp", "cny", "try", "jpy", "brl"
        ],
        "email_login_data": bool,
        "email_provider[]": list[
            Literal["other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"]
        ],
        "not_email_provider[]": Literal[
            "other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"
        ],
        "email_type[]": list[Literal["autoreg", "native", "no"]],
        "parse_same_item_ids": bool,
        "item_domain": str,
        "email": Literal["yes", "no", "nomatter"],
        "ea": YesNoNoMatterScheme,
        "region": list[Literal["asia", "cht", "eu", "usa"]],
        "not_region": list[Literal["asia", "cht", "eu", "usa"]],
        "genshin_character[]": list[int],
        "genshin_character_constellations": dict[str, int],
        "genshin_character_constellations_max": dict[str, int],
        "genshin_weapon[]": list[int],
        "genshin_char_min": int,
        "genshin_char_max": int,
        "genshin_legendary_min": int,
        "genshin_legendary_max": int,
        "genshin_level_min": int,
        "genshin_level_max": int,
        "genshin_legendary_weapon_min": int,
        "genshin_legendary_weapon_max": int,
        "constellations_min": int,
        "constellations_max": int,
        "genshin_achievement_min": int,
        "genshin_achievement_max": int,
        "genshin_currency_min": int,
        "genshin_currency_max": int,
        "honkai_character[]": list[int],
        "honkai_character_eidolons": dict[str, int],
        "honkai_character_eidolons_max": dict[str, int],
        "honkai_weapon[]": list[int],
        "honkai_char_min": int,
        "honkai_char_max": int,
        "honkai_legendary_min": int,
        "honkai_legendary_max": int,
        "honkai_level_min": int,
        "honkai_level_max": int,
        "honkai_legendary_weapon_min": int,
        "honkai_legendary_weapon_max": int,
        "eidolons_min": int,
        "eidolons_max": int,
        "honkai_achievement_min": int,
        "honkai_achievement_max": int,
        "honkai_currency_min": int,
        "honkai_currency_max": int,
        "zenless_character[]": list[
            Literal[
                1011,
                1021,
                1031,
                1041,
                1051,
                1061,
                1071,
                1081,
                1091,
                1101,
                1111,
                1121,
                1131,
                1141,
                1151,
                1161,
                1171,
                1181,
                1191,
                1201,
                1211,
                1221,
                1241,
                1251,
                1261,
                1271,
                1281,
                1291,
                1301,
                1311,
                1321,
                1331,
                1341,
                1351,
                1361,
                1371,
                1381,
                1391,
                1401,
                1411,
                1421,
                1431,
                1441,
                1451,
                1461,
                1471,
                1481,
                1491,
            ]
        ],
        "zenless_character_cinemas": dict[str, int],
        "zenless_character_cinemas_max": dict[str, int],
        "zenless_weapon[]": list[int],
        "zenless_legendary_min": int,
        "zenless_legendary_max": int,
        "cinemas_min": int,
        "cinemas_max": int,
        "zenless_legendary_weapon_min": int,
        "zenless_legendary_weapon_max": int,
        "zenless_char_min": int,
        "zenless_char_max": int,
        "zenless_level_min": int,
        "zenless_level_max": int,
        "zenless_achievement_min": int,
        "zenless_achievement_max": int,
        "zenless_currency_min": int,
        "zenless_currency_max": int,
        "daybreak": int,
    },
    total=False,
)


class CategoryMihoyoResponseItemsBumpSettings(TypedDict):
    canBumpItem: bool
    canBumpItemGlobally: bool
    shortErrorPhrase: object
    errorPhrase: object


class CategoryMihoyoResponseItemsMihoyoLinkedAccounts(TypedDict):
    links: list[str]
    legacy: bool


class CategoryMihoyoResponseItemsHonkaiCharactersEquip(TypedDict):
    id: int
    level: int
    rank: int
    name: str
    desc: str
    icon: str
    rarity: int


class CategoryMihoyoResponseItemsHonkaiCharactersRelicsMain_property(TypedDict):
    property_type: int
    value: str
    times: int


class CategoryMihoyoResponseItemsHonkaiCharactersRelicsProperties(TypedDict):
    property_type: int
    value: str
    times: int


class CategoryMihoyoResponseItemsHonkaiCharactersRelics(TypedDict):
    id: int
    level: int
    pos: int
    name: str
    desc: str
    icon: str
    rarity: int
    main_property: CategoryMihoyoResponseItemsHonkaiCharactersRelicsMain_property
    properties: list[CategoryMihoyoResponseItemsHonkaiCharactersRelicsProperties]


class CategoryMihoyoResponseItemsHonkaiCharactersOrnamentsMain_property(TypedDict):
    property_type: int
    value: str
    times: int


class CategoryMihoyoResponseItemsHonkaiCharactersOrnamentsProperties(TypedDict):
    property_type: int
    value: str
    times: int


class CategoryMihoyoResponseItemsHonkaiCharactersOrnaments(TypedDict):
    id: int
    level: int
    pos: int
    name: str
    desc: str
    icon: str
    rarity: int
    main_property: CategoryMihoyoResponseItemsHonkaiCharactersOrnamentsMain_property
    properties: list[CategoryMihoyoResponseItemsHonkaiCharactersOrnamentsProperties]


class CategoryMihoyoResponseItemsHonkaiCharacters(TypedDict):
    id: int
    level: int
    name: str
    element: str
    icon: str
    rarity: int
    rank: int
    image: str
    equip: CategoryMihoyoResponseItemsHonkaiCharactersEquip
    relics: list[CategoryMihoyoResponseItemsHonkaiCharactersRelics]
    ornaments: list[CategoryMihoyoResponseItemsHonkaiCharactersOrnaments]
    base_type: int
    figure_path: str
    elementImage: str


class CategoryMihoyoResponseItemsGenshinCharactersWeapon(TypedDict):
    id: int
    name: str
    icon: str
    type: int
    rarity: int
    level: int
    promote_level: int
    type_name: str
    desc: str
    affix_level: int


class CategoryMihoyoResponseItemsGenshinCharactersReliquaries(TypedDict):
    id: int
    name: str
    icon: str
    pos: int
    rarity: int
    level: int
    pos_name: str


class CategoryMihoyoResponseItemsGenshinCharacters(TypedDict):
    id: int
    image: str
    icon: str
    name: str
    element: str
    fetter: int
    level: int
    rarity: int
    weapon: CategoryMihoyoResponseItemsGenshinCharactersWeapon
    reliquaries: list[CategoryMihoyoResponseItemsGenshinCharactersReliquaries]
    actived_constellation_num: int
    costumes: list[object]
    external: object
    background: str


class CategoryMihoyoResponseItemsZenlessCharactersWeaponProperties(TypedDict):
    property_name: str
    property_id: int
    base: str


class CategoryMihoyoResponseItemsZenlessCharactersWeaponMain_properties(TypedDict):
    property_name: str
    property_id: int
    base: str


class CategoryMihoyoResponseItemsZenlessCharactersWeapon(TypedDict):
    id: int
    level: int
    name: str
    star: int
    icon: str
    rarity: int
    properties: list[CategoryMihoyoResponseItemsZenlessCharactersWeaponProperties]
    main_properties: list[CategoryMihoyoResponseItemsZenlessCharactersWeaponMain_properties]
    talent_title: str
    talent_content: str
    profession: int
    starIcon: str
    rarityIcon: str


class CategoryMihoyoResponseItemsZenlessCharacters(TypedDict):
    id: int
    level: int
    name_mi18n: str
    full_name_mi18n: str
    element_type: int
    camp_name_mi18n: str
    avatar_profession: int
    rarity: int
    weapon: CategoryMihoyoResponseItemsZenlessCharactersWeapon
    rank: int
    name: str
    rarityIcon: str
    elementIcon: str
    professionIcon: str


class CategoryMihoyoResponseItemsAccountLinks(TypedDict):
    link: str
    text: str
    iconClass: str


class CategoryMihoyoResponseItemsSeller(TypedDict):
    user_id: int
    sold_items_count: int
    active_items_count: int
    restore_data: str
    username: str
    avatar_date: int
    is_banned: int
    display_style_group_id: int
    restore_percents: int


class CategoryMihoyoResponseItems(TypedDict):
    item_id: int
    item_state: str
    category_id: int
    published_date: int
    title: str
    description: str
    price: int
    update_stat_date: int
    refreshed_date: int
    edit_date: int
    view_count: int
    is_sticky: int
    item_origin: str
    extended_guarantee: int
    nsb: int
    allow_ask_discount: int
    title_en: str
    description_en: str
    email_type: str
    email_provider: str
    item_domain: str
    resale_item_origin: str
    mihoyo_item_id: int
    mihoyo_id: int
    mihoyo_email: int
    mihoyo_has_linked_accounts: int
    mihoyo_region: str
    mihoyo_last_activity: int
    mihoyo_genshin_level: int
    mihoyo_genshin_character_count: int
    mihoyo_genshin_achievement_count: int
    mihoyo_genshin_abyss_process: str
    mihoyo_genshin_legendary_characters_count: int
    mihoyo_genshin_constellations_count: int
    mihoyo_genshin_legendary_weapons_count: int
    mihoyo_genshin_activity_days: int
    mihoyo_genshin_currency: int
    mihoyo_honkai_level: int
    mihoyo_honkai_character_count: int
    mihoyo_honkai_achievement_count: int
    mihoyo_honkai_abyss_process: str
    mihoyo_honkai_legendary_characters_count: int
    mihoyo_honkai_eidolons_count: int
    mihoyo_honkai_legendary_weapons_count: int
    mihoyo_honkai_activity_days: int
    mihoyo_honkai_currency: int
    mihoyo_zenless_level: int
    mihoyo_zenless_character_count: int
    mihoyo_zenless_achievement_count: int
    mihoyo_zenless_abyss_process: str
    mihoyo_zenless_legendary_characters_count: int
    mihoyo_zenless_cinemas_count: int
    mihoyo_zenless_legendary_weapons_count: int
    mihoyo_zenless_activity_days: int
    mihoyo_zenless_currency: int
    feedback_data: str
    isIgnored: bool
    priceWithSellerFee: int
    guarantee: object
    canViewLoginData: bool
    canUpdateItemStats: bool
    canReportItem: bool
    canViewEmailLoginData: bool
    showGetEmailCodeButton: bool
    canOpenItem: bool
    canCloseItem: bool
    canEditItem: bool
    canDeleteItem: bool
    canStickItem: bool
    canUnstickItem: bool
    bumpSettings: CategoryMihoyoResponseItemsBumpSettings
    canBumpItem: bool
    canBuyItem: bool
    rub_price: int
    price_currency: str
    canValidateAccount: bool
    canResellItemAfterPurchase: bool
    mihoyoRegionPhrase: str
    mihoyoLinkedAccounts: CategoryMihoyoResponseItemsMihoyoLinkedAccounts
    mihoyoLinkedAccountsString: str
    honkaiCharacters: list[CategoryMihoyoResponseItemsHonkaiCharacters]
    genshinCharacters: list[CategoryMihoyoResponseItemsGenshinCharacters]
    zenlessCharacters: list[CategoryMihoyoResponseItemsZenlessCharacters]
    canViewAccountLink: bool
    accountLinks: list[CategoryMihoyoResponseItemsAccountLinks]
    accountLink: str
    emailLoginUrl: str
    canChangePassword: bool
    itemOriginPhrase: str
    sold_items_category_count: int
    restore_items_category_count: int
    tags: list[object]
    note_text: object
    hasPendingAutoBuy: bool
    descriptionHtml: str
    descriptionEnHtml: str
    descriptionPlain: str
    descriptionEnPlain: str
    seller: CategoryMihoyoResponseItemsSeller


class CategoryMihoyoResponse(TypedDict):
    items: list[CategoryMihoyoResponseItems]
    totalItems: int
    totalItemsPrice: object
    hasNextPage: bool
    perPage: int
    page: int
    wasCached: bool
    cacheTTL: int
    lastModified: int
    serverTime: int
    searchUrl: str
    stickyItems: list[object]
    system_info: Resp_SystemInfo


CategoryRiotParams = TypedDict(
    "CategoryRiotParams",
    {
        "page": int,
        "pmin": int,
        "pmax": int,
        "title": str,
        "order_by": Literal[
            "price_to_up",
            "price_to_down",
            "pdate_to_down",
            "pdate_to_up",
            "pdate_to_down_upload",
            "pdate_to_up_upload",
            "edate_to_up",
            "edate_to_down",
            "ddate_to_up",
            "ddate_to_down",
        ],
        "tag_id[]": list[int],
        "not_tag_id[]": list[int],
        "public_tag_id[]": list[int],
        "not_public_tag_id[]": list[int],
        "origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "not_origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "user_id": int,
        "nsb": bool,
        "sb": bool,
        "nsb_by_me": bool,
        "sb_by_me": bool,
        "currency": Literal[
            "rub", "uah", "kzt", "byn", "usd", "eur", "gbp", "cny", "try", "jpy", "brl"
        ],
        "email_login_data": bool,
        "email_provider[]": list[
            Literal["other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"]
        ],
        "not_email_provider[]": Literal[
            "other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"
        ],
        "parse_same_item_ids": bool,
        "email_type[]": list[Literal["autoreg", "native", "no"]],
        "item_domain": str,
        "rmin": int,
        "rmax": int,
        "last_rmin": int,
        "last_rmax": int,
        "previous_rmin": int,
        "previous_rmax": int,
        "weaponSkin[]": list[str],
        "buddy[]": list[str],
        "agent[]": list[str],
        "champion[]": list[str],
        "skin[]": list[str],
        "country[]": list[str],
        "not_country[]": list[str],
        "daybreak": int,
        "valorant_level_min": int,
        "valorant_level_max": int,
        "lol_level_min": int,
        "lol_level_max": int,
        "inv_min": int,
        "inv_max": int,
        "vp_min": int,
        "vp_max": int,
        "valorant_smin": int,
        "valorant_smax": int,
        "valorant_rank_type[]": list[Literal["ranked", "ranked_ready", "unrated"]],
        "amin": int,
        "amax": int,
        "valorant_region[]": list[str],
        "valorant_not_region[]": list[str],
        "lol_region[]": list[str],
        "lol_not_region[]": list[str],
        "knife": bool,
        "lol_smin": int,
        "lol_smax": int,
        "champion_min": int,
        "champion_max": int,
        "win_rate_min": int,
        "win_rate_max": int,
        "blue_min": int,
        "blue_max": int,
        "orange_min": int,
        "orange_max": int,
        "mythic_min": int,
        "mythic_max": int,
        "riot_min": int,
        "riot_max": int,
        "email": Literal["yes", "no", "nomatter"],
        "tel": Literal["yes", "no", "nomatter"],
        "valorant_knife_min": int,
        "valorant_knife_max": int,
        "rp_min": int,
        "rp_max": int,
        "fa_min": int,
        "fa_max": int,
        "lol_rank[]": list[
            Literal[
                "Unranked",
                "IRON IV",
                "IRON III",
                "IRON II",
                "IRON I",
                "BRONZE IV",
                "BRONZE III",
                "BRONZE II",
                "BRONZE I",
                "SILVER IV",
                "SILVER III",
                "SILVER II",
                "SILVER I",
                "GOLD IV",
                "GOLD III",
                "GOLD II",
                "GOLD I",
                "PLATINUM IV",
                "PLATINUM III",
                "PLATINUM II",
                "PLATINUM I",
                "EMERALD IV",
                "EMERALD III",
                "EMERALD II",
                "EMERALD I",
                "DIAMOND IV",
                "DIAMOND III",
                "DIAMOND II",
                "DIAMOND I",
                "MASTER I",
                "GRANDMASTER I",
                "CHALLENGER I",
            ]
        ],
    },
    total=False,
)


class CategoryRiotResponseItemsBumpSettings(TypedDict):
    canBumpItem: bool
    canBumpItemGlobally: bool
    shortErrorPhrase: object
    errorPhrase: object


class CategoryRiotResponseItemsValorantInventory(TypedDict):
    WeaponSkins: list[str]
    Agent: list[str]
    Buddy: list[str]


class CategoryRiotResponseItemsLolInventory(TypedDict):
    Champion: list[int]
    Skin: list[int]


class CategoryRiotResponseItemsAccountLinks(TypedDict):
    link: str
    text: str
    iconClass: str


class CategoryRiotResponseItemsSeller(TypedDict):
    user_id: int
    sold_items_count: int
    active_items_count: int
    restore_data: str
    username: str
    avatar_date: int
    is_banned: int
    display_style_group_id: int
    restore_percents: int


class CategoryRiotResponseItems(TypedDict):
    item_id: int
    item_state: str
    category_id: int
    published_date: int
    title: str
    description: str
    price: int
    update_stat_date: int
    refreshed_date: int
    edit_date: int
    view_count: int
    is_sticky: int
    item_origin: str
    extended_guarantee: int
    nsb: int
    allow_ask_discount: int
    title_en: str
    description_en: str
    email_type: str
    email_provider: str
    item_domain: str
    resale_item_origin: str
    riot_item_id: int
    riot_id: str
    riot_account_verified: int
    riot_email_verified: int
    riot_country: str
    riot_password_change: int
    riot_phone_verified: int
    riot_last_activity: int
    riot_valorant_wallet_vp: int
    riot_valorant_wallet_rp: int
    riot_valorant_wallet_fa: int
    riot_valorant_level: int
    riot_username: str
    riot_valorant_rank: int
    riot_valorant_region: str
    riot_valorant_skin_count: int
    riot_valorant_agent_count: int
    riot_valorant_previous_rank: int
    riot_valorant_last_rank: int
    riot_valorant_rank_type: str
    riot_valorant_inventory_value: int
    riot_valorant_knife: int
    riot_lol_region: str
    riot_lol_skin_count: int
    riot_lol_champion_count: int
    riot_lol_level: int
    riot_lol_wallet_blue: int
    riot_lol_wallet_orange: int
    riot_lol_wallet_mythic: int
    riot_lol_wallet_riot: int
    riot_lol_rank: str
    riot_lol_rank_win_rate: int
    feedback_data: str
    isIgnored: bool
    priceWithSellerFee: int
    guarantee: object
    canViewLoginData: bool
    canUpdateItemStats: bool
    canReportItem: bool
    canViewEmailLoginData: bool
    showGetEmailCodeButton: bool
    canOpenItem: bool
    canCloseItem: bool
    canEditItem: bool
    canDeleteItem: bool
    canStickItem: bool
    canUnstickItem: bool
    bumpSettings: CategoryRiotResponseItemsBumpSettings
    canBumpItem: bool
    canBuyItem: bool
    rub_price: int
    price_currency: str
    canValidateAccount: bool
    canResellItemAfterPurchase: bool
    valorantRegionPhrase: str
    valorantRankTitle: str
    valorantRankImgPath: str
    valorantPreviousRankTitle: str
    valorantLastRankTitle: str
    lolRegionPhrase: str
    isSmallExf: bool
    account_last_activity: int
    valorantInventory: CategoryRiotResponseItemsValorantInventory
    lolInventory: CategoryRiotResponseItemsLolInventory
    canViewAccountLink: bool
    accountLinks: list[CategoryRiotResponseItemsAccountLinks]
    accountLink: str
    emailLoginUrl: str
    canChangePassword: bool
    itemOriginPhrase: str
    sold_items_category_count: int
    restore_items_category_count: int
    tags: list[object]
    note_text: object
    hasPendingAutoBuy: bool
    descriptionHtml: str
    descriptionEnHtml: str
    descriptionPlain: str
    descriptionEnPlain: str
    seller: CategoryRiotResponseItemsSeller


class CategoryRiotResponse(TypedDict):
    items: list[CategoryRiotResponseItems]
    totalItems: int
    totalItemsPrice: object
    hasNextPage: bool
    perPage: int
    page: int
    wasCached: bool
    cacheTTL: int
    lastModified: int
    serverTime: int
    searchUrl: str
    stickyItems: list[object]
    system_info: Resp_SystemInfo


CategoryTelegramParams = TypedDict(
    "CategoryTelegramParams",
    {
        "page": int,
        "pmin": int,
        "pmax": int,
        "title": str,
        "order_by": Literal[
            "price_to_up",
            "price_to_down",
            "pdate_to_down",
            "pdate_to_up",
            "pdate_to_down_upload",
            "pdate_to_up_upload",
            "edate_to_up",
            "edate_to_down",
            "ddate_to_up",
            "ddate_to_down",
        ],
        "tag_id[]": list[int],
        "not_tag_id[]": list[int],
        "public_tag_id[]": list[int],
        "not_public_tag_id[]": list[int],
        "origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "dummy",
                "self_registration",
            ]
        ],
        "not_origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "dummy",
                "self_registration",
            ]
        ],
        "user_id": int,
        "nsb": bool,
        "sb": bool,
        "nsb_by_me": bool,
        "sb_by_me": bool,
        "currency": Literal[
            "rub", "uah", "kzt", "byn", "usd", "eur", "gbp", "cny", "try", "jpy", "brl"
        ],
        "email_login_data": bool,
        "email_provider[]": list[
            Literal["other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"]
        ],
        "not_email_provider[]": Literal[
            "other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"
        ],
        "parse_same_item_ids": bool,
        "spam": YesNoNoMatterScheme,
        "password": YesNoNoMatterScheme,
        "premium": Literal["yes", "no", "nomatter"],
        "premium_expiration": int,
        "premium_expiration_period": Literal["day", "month", "year"],
        "country[]": list[str],
        "not_country[]": list[str],
        "daybreak": int,
        "min_channels": int,
        "max_channels": int,
        "min_chats": int,
        "max_chats": int,
        "min_conversations": int,
        "max_conversations": int,
        "min_admin": int,
        "max_admin": int,
        "min_admin_sub": int,
        "max_admin_sub": int,
        "dig_min": int,
        "dig_max": int,
        "min_contacts": int,
        "max_contacts": int,
        "min_stars": int,
        "max_stars": int,
        "birthday": int,
        "birthday_period": Literal["day", "month", "year"],
        "birthday_after": int,
        "birthday_after_period": Literal["day", "month", "year"],
        "min_id": int,
        "max_id": int,
        "allow_geo_spamblock": bool,
        "min_gifts": int,
        "max_gifts": int,
        "min_nft_gifts": int,
        "max_nft_gifts": int,
        "min_gifts_stars": int,
        "max_gifts_stars": int,
        "min_gifts_convert_stars": int,
        "max_gifts_convert_stars": int,
        "dc_id[]": list[int],
        "not_dc_id[]": list[int],
        "email": Literal["yes", "no", "nomatter"],
        "min_bots": int,
        "max_bots": int,
        "min_bot_active_users": int,
        "max_bot_active_users": int,
    },
    total=False,
)


class CategoryTelegramResponseItemsBumpSettings(TypedDict):
    canBumpItem: bool
    canBumpItemGlobally: bool
    shortErrorPhrase: object
    errorPhrase: object


class CategoryTelegramResponseItemsTelegram_group_counters(TypedDict):
    chats: int
    channels: int
    conversations: int
    admin: int


class CategoryTelegramResponseItemsSeller(TypedDict):
    user_id: int
    sold_items_count: int
    active_items_count: int
    restore_data: str
    username: str
    avatar_date: int
    is_banned: int
    display_style_group_id: int
    restore_percents: object


class CategoryTelegramResponseItems(TypedDict):
    item_id: int
    item_state: str
    category_id: int
    published_date: int
    title: str
    description: str
    price: int
    update_stat_date: int
    refreshed_date: int
    edit_date: int
    view_count: int
    is_sticky: int
    item_origin: str
    extended_guarantee: int
    nsb: int
    allow_ask_discount: int
    title_en: str
    description_en: str
    email_type: str
    email_provider: object
    item_domain: str
    resale_item_origin: str
    telegram_item_id: int
    telegram_country: str
    telegram_last_seen: int
    telegram_premium: int
    telegram_stars_count: int
    telegram_birthday: int
    telegram_password: int
    telegram_premium_expires: int
    telegram_spam_block: object
    telegram_channels_count: int
    telegram_chats_count: int
    telegram_admin_count: int
    telegram_admin_subs_count: int
    telegram_conversations_count: int
    telegram_id_count: int
    telegram_contacts_count: int
    feedback_data: str
    isIgnored: bool
    priceWithSellerFee: int
    guarantee: object
    canViewLoginData: bool
    canUpdateItemStats: bool
    canReportItem: bool
    canViewEmailLoginData: bool
    showGetEmailCodeButton: bool
    canOpenItem: bool
    canCloseItem: bool
    canEditItem: bool
    canDeleteItem: bool
    canStickItem: bool
    canUnstickItem: bool
    bumpSettings: CategoryTelegramResponseItemsBumpSettings
    canBumpItem: bool
    canBuyItem: bool
    rub_price: int
    price_currency: str
    canValidateAccount: bool
    canResellItemAfterPurchase: bool
    telegram_group_counters: CategoryTelegramResponseItemsTelegram_group_counters
    canViewAccountLink: bool
    accountLinks: list[object]
    canChangePassword: bool
    itemOriginPhrase: str
    tags: list[object]
    note_text: object
    hasPendingAutoBuy: bool
    descriptionHtml: str
    descriptionEnHtml: str
    descriptionPlain: str
    descriptionEnPlain: str
    seller: CategoryTelegramResponseItemsSeller


class CategoryTelegramResponse(TypedDict):
    items: list[CategoryTelegramResponseItems]
    totalItems: int
    totalItemsPrice: object
    hasNextPage: bool
    perPage: int
    page: int
    wasCached: bool
    cacheTTL: int
    lastModified: int
    serverTime: int
    searchUrl: str
    stickyItems: list[object]
    system_info: Resp_SystemInfo


CategorySupercellParams = TypedDict(
    "CategorySupercellParams",
    {
        "page": int,
        "pmin": int,
        "pmax": int,
        "title": str,
        "order_by": Literal[
            "price_to_up",
            "price_to_down",
            "pdate_to_down",
            "pdate_to_up",
            "pdate_to_down_upload",
            "pdate_to_up_upload",
            "edate_to_up",
            "edate_to_down",
            "ddate_to_up",
            "ddate_to_down",
        ],
        "tag_id[]": list[int],
        "not_tag_id[]": list[int],
        "public_tag_id[]": list[int],
        "not_public_tag_id[]": list[int],
        "origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "not_origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "user_id": int,
        "nsb": bool,
        "sb": bool,
        "nsb_by_me": bool,
        "sb_by_me": bool,
        "currency": Literal[
            "rub", "uah", "kzt", "byn", "usd", "eur", "gbp", "cny", "try", "jpy", "brl"
        ],
        "email_login_data": bool,
        "email_provider[]": list[
            Literal["other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"]
        ],
        "not_email_provider[]": Literal[
            "other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"
        ],
        "parse_same_item_ids": bool,
        "daybreak": int,
        "email_type[]": list[Literal["autoreg", "native", "no"]],
        "item_domain": str,
        "eg": Literal[-1, 0, 1, 2],
        "tel": YesNoNoMatterScheme,
        "brawl_level_min": int,
        "brawl_level_max": int,
        "brawl_cup_min": int,
        "brawl_cup_max": int,
        "brawl_wins_min": int,
        "brawl_wins_max": int,
        "brawl_pass": YesNoNoMatterScheme,
        "brawler[]": list[str],
        "brawlers_min": int,
        "brawlers_max": int,
        "legendary_brawlers_min": int,
        "legendary_brawlers_max": int,
        "royale_level_min": int,
        "royale_level_max": int,
        "royale_cup_min": int,
        "royale_cup_max": int,
        "royale_wins_min": int,
        "royale_wins_max": int,
        "king_level_min": int,
        "king_level_max": int,
        "royale_pass": YesNoNoMatterScheme,
        "clash_level_min": int,
        "clash_level_max": int,
        "clash_cup_min": int,
        "clash_cup_max": int,
        "clash_wins_min": int,
        "clash_wins_max": int,
        "clash_pass": YesNoNoMatterScheme,
        "total_heroes_level_min": int,
        "total_heroes_level_max": int,
        "total_troops_level_min": int,
        "total_troops_level_max": int,
        "total_spells_level_min": int,
        "total_spells_level_max": int,
        "total_builder_heroes_level_min": int,
        "total_builder_heroes_level_max": int,
        "total_builder_troops_level_min": int,
        "total_builder_troops_level_max": int,
        "town_hall_level_min": int,
        "town_hall_level_max": int,
        "builder_hall_level_min": int,
        "builder_hall_level_max": int,
        "builder_hall_cup_min": int,
        "builder_hall_cup_max": int,
        "creation_year_min": int,
        "creation_year_max": int,
    },
    total=False,
)


class CategorySupercellResponseItemsBumpSettings(TypedDict):
    canBumpItem: bool
    canBumpItemGlobally: bool
    shortErrorPhrase: object
    errorPhrase: object


class CategorySupercellResponseItemsAccountLinks(TypedDict):
    link: str
    text: str
    iconClass: str


class CategorySupercellResponseItemsSeller(TypedDict):
    user_id: int
    sold_items_count: int
    active_items_count: int
    restore_data: str
    username: str
    avatar_date: int
    is_banned: int
    display_style_group_id: int
    restore_percents: object


class CategorySupercellResponseItems(TypedDict):
    item_id: int
    item_state: str
    category_id: int
    published_date: int
    title: str
    description: str
    price: int
    update_stat_date: int
    refreshed_date: int
    edit_date: int
    view_count: int
    is_sticky: int
    item_origin: str
    extended_guarantee: int
    nsb: int
    allow_ask_discount: int
    title_en: str
    description_en: str
    email_type: str
    email_provider: str
    item_domain: str
    resale_item_origin: str
    supercell_item_id: int
    supercell_id: str
    supercell_arena: str
    supercell_brawler_count: int
    supercell_last_activity: int
    supercell_legendary_brawler_count: int
    supercell_town_hall_level: int
    supercell_builder_hall_level: int
    supercell_builder_hall_cup_count: int
    supercell_phone: int
    supercell_laser_level: int
    supercell_scroll_level: int
    supercell_magic_level: int
    supercell_laser_trophies: int
    supercell_scroll_trophies: int
    supercell_magic_trophies: int
    supercell_laser_victories: int
    supercell_scroll_victories: int
    supercell_magic_victories: int
    supercell_laser_battle_pass: int
    supercell_scroll_battle_pass: int
    supercell_magic_battle_pass: int
    supercell_systems: str
    supercell_king_level: int
    supercell_total_heroes_level: int
    supercell_total_troops_level: int
    supercell_total_spells_level: int
    supercell_total_builder_heroes_level: int
    supercell_total_builder_troops_level: int
    feedback_data: str
    isIgnored: bool
    priceWithSellerFee: int
    guarantee: object
    canViewLoginData: bool
    canUpdateItemStats: bool
    canReportItem: bool
    canViewEmailLoginData: bool
    showGetEmailCodeButton: bool
    canOpenItem: bool
    canCloseItem: bool
    canEditItem: bool
    canDeleteItem: bool
    canStickItem: bool
    canUnstickItem: bool
    bumpSettings: CategorySupercellResponseItemsBumpSettings
    canBumpItem: bool
    canBuyItem: bool
    rub_price: int
    price_currency: str
    canValidateAccount: bool
    canResellItemAfterPurchase: bool
    isSmallExf: bool
    supercellBrawlers: list[object]
    canViewAccountLink: bool
    accountLinks: list[CategorySupercellResponseItemsAccountLinks]
    accountLink: str
    emailLoginUrl: str
    canChangePassword: bool
    itemOriginPhrase: str
    tags: list[object]
    note_text: object
    hasPendingAutoBuy: bool
    descriptionHtml: str
    descriptionEnHtml: str
    descriptionPlain: str
    descriptionEnPlain: str
    seller: CategorySupercellResponseItemsSeller


class CategorySupercellResponse(TypedDict):
    items: list[CategorySupercellResponseItems]
    totalItems: int
    totalItemsPrice: object
    hasNextPage: bool
    perPage: int
    page: int
    wasCached: bool
    cacheTTL: int
    lastModified: int
    serverTime: int
    searchUrl: str
    stickyItems: list[object]
    system_info: Resp_SystemInfo


CategoryEaParams = TypedDict(
    "CategoryEaParams",
    {
        "page": int,
        "pmin": int,
        "pmax": int,
        "title": str,
        "order_by": Literal[
            "price_to_up",
            "price_to_down",
            "pdate_to_down",
            "pdate_to_up",
            "pdate_to_down_upload",
            "pdate_to_up_upload",
            "edate_to_up",
            "edate_to_down",
            "ddate_to_up",
            "ddate_to_down",
        ],
        "tag_id[]": list[int],
        "not_tag_id[]": list[int],
        "public_tag_id[]": list[int],
        "not_public_tag_id[]": list[int],
        "origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "not_origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "user_id": int,
        "nsb": bool,
        "sb": bool,
        "nsb_by_me": bool,
        "sb_by_me": bool,
        "currency": Literal[
            "rub", "uah", "kzt", "byn", "usd", "eur", "gbp", "cny", "try", "jpy", "brl"
        ],
        "email_login_data": bool,
        "email_provider[]": list[
            Literal["other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"]
        ],
        "not_email_provider[]": Literal[
            "other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"
        ],
        "parse_same_item_ids": bool,
        "email_type[]": list[Literal["autoreg", "native", "no"]],
        "item_domain": str,
        "game[]": list[str],
        "country[]": list[str],
        "not_country[]": list[str],
        "gmin": int,
        "gmax": int,
        "al_rank_min": int,
        "al_rank_max": int,
        "al_level_min": int,
        "al_level_max": int,
        "has_ban": YesNoNoMatterScheme,
        "xbox_connected": YesNoNoMatterScheme,
        "steam_connected": YesNoNoMatterScheme,
        "psn_connected": YesNoNoMatterScheme,
        "subscription": Literal["EA Play", "EA Play Pro"],
        "subscription_length": int,
        "subscription_period": Literal["day", "month", "year"],
        "hours_played": dict[str, int],
        "hours_played_max": dict[str, int],
        "transactions": YesNoNoMatterScheme,
    },
    total=False,
)


class CategoryEaResponseItemsEa_gamesApexLegends(TypedDict):
    game_id: str
    title: str
    last_activity: int
    total_played: int
    img: str


CategoryEaResponseItemsEa_games = TypedDict(
    "CategoryEaResponseItemsEa_games",
    {
        "apex-legends": CategoryEaResponseItemsEa_gamesApexLegends,
    },
)


class CategoryEaResponseItemsBumpSettings(TypedDict):
    canBumpItem: bool
    canBumpItemGlobally: bool
    shortErrorPhrase: object
    errorPhrase: object


class CategoryEaResponseItemsAccountLinks(TypedDict):
    link: str
    text: str
    iconClass: str


class CategoryEaResponseItemsSeller(TypedDict):
    user_id: int
    sold_items_count: int
    active_items_count: int
    restore_data: str
    username: str
    avatar_date: int
    is_banned: int
    display_style_group_id: int
    restore_percents: int


class CategoryEaResponseItems(TypedDict):
    item_id: int
    item_state: str
    category_id: int
    published_date: int
    title: str
    description: str
    price: int
    update_stat_date: int
    refreshed_date: int
    edit_date: int
    view_count: int
    is_sticky: int
    item_origin: str
    extended_guarantee: int
    nsb: int
    allow_ask_discount: int
    title_en: str
    description_en: str
    email_type: str
    email_provider: str
    item_domain: str
    resale_item_origin: str
    ea_item_id: int
    ea_id: int
    ea_country: str
    ea_games: CategoryEaResponseItemsEa_games
    ea_game_count: int
    ea_last_activity: int
    ea_al_level: int
    ea_al_rank_score: int
    ea_subscription: str
    ea_subscription_end_date: int
    ea_username: str
    ea_xbox_connected: int
    ea_steam_connected: int
    ea_psn_connected: int
    ea_bans: list[object]
    ea_has_ban: int
    feedback_data: str
    isIgnored: bool
    priceWithSellerFee: int
    guarantee: object
    canViewLoginData: bool
    canUpdateItemStats: bool
    canReportItem: bool
    canViewEmailLoginData: bool
    showGetEmailCodeButton: bool
    canOpenItem: bool
    canCloseItem: bool
    canEditItem: bool
    canDeleteItem: bool
    canStickItem: bool
    canUnstickItem: bool
    bumpSettings: CategoryEaResponseItemsBumpSettings
    canBumpItem: bool
    canBuyItem: bool
    rub_price: int
    price_currency: str
    canValidateAccount: bool
    canResellItemAfterPurchase: bool
    canViewAccountLink: bool
    accountLinks: list[CategoryEaResponseItemsAccountLinks]
    accountLink: str
    emailLoginUrl: str
    canChangePassword: bool
    itemOriginPhrase: str
    sold_items_category_count: int
    restore_items_category_count: int
    tags: list[object]
    note_text: object
    hasPendingAutoBuy: bool
    descriptionHtml: str
    descriptionEnHtml: str
    descriptionPlain: str
    descriptionEnPlain: str
    seller: CategoryEaResponseItemsSeller


class CategoryEaResponse(TypedDict):
    items: list[CategoryEaResponseItems]
    totalItems: int
    totalItemsPrice: object
    hasNextPage: bool
    perPage: int
    page: int
    wasCached: bool
    cacheTTL: int
    lastModified: int
    serverTime: int
    searchUrl: str
    stickyItems: list[object]
    system_info: Resp_SystemInfo


CategoryWotParams = TypedDict(
    "CategoryWotParams",
    {
        "page": int,
        "pmin": int,
        "pmax": int,
        "title": str,
        "order_by": Literal[
            "price_to_up",
            "price_to_down",
            "pdate_to_down",
            "pdate_to_up",
            "pdate_to_down_upload",
            "pdate_to_up_upload",
            "edate_to_up",
            "edate_to_down",
            "ddate_to_up",
            "ddate_to_down",
        ],
        "tag_id[]": list[int],
        "not_tag_id[]": list[int],
        "public_tag_id[]": list[int],
        "not_public_tag_id[]": list[int],
        "origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "not_origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "user_id": int,
        "nsb": bool,
        "sb": bool,
        "nsb_by_me": bool,
        "sb_by_me": bool,
        "currency": Literal[
            "rub", "uah", "kzt", "byn", "usd", "eur", "gbp", "cny", "try", "jpy", "brl"
        ],
        "email_login_data": bool,
        "email_provider[]": list[
            Literal["other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"]
        ],
        "not_email_provider[]": Literal[
            "other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"
        ],
        "parse_same_item_ids": bool,
        "email_type[]": list[Literal["autoreg", "native", "no"]],
        "item_domain": str,
        "tel": Literal["yes", "no", "nomatter"],
        "daybreak": int,
        "battles_min": int,
        "battles_max": int,
        "gold_min": int,
        "gold_max": int,
        "silver_min": int,
        "silver_max": int,
        "top_min": int,
        "top_max": int,
        "prem_min": int,
        "prem_max": int,
        "top_prem_min": int,
        "top_prem_max": int,
        "win_pmin": int,
        "win_pmax": int,
        "tank[]": list[int],
        "region[]": list[Literal["asia", "eu", "na", "ru"]],
        "not_region[]": list[Literal["asia", "eu", "na", "ru"]],
        "premium": Literal["yes", "no", "nomatter"],
        "premium_expiration": int,
        "premium_expiration_period": Literal["day", "month", "year"],
        "clan": Literal["yes", "no", "nomatter"],
        "clan_role[]": list[
            Literal[
                "commander",
                "executive_officer",
                "personnel_officer",
                "combat_officer",
                "intelligence_officer",
                "quartermaster",
                "recruitment_officer",
                "junior_officer",
                "private",
                "recruit",
                "reservist",
            ]
        ],
        "not_clan_role[]": list[
            Literal[
                "commander",
                "executive_officer",
                "personnel_officer",
                "combat_officer",
                "intelligence_officer",
                "quartermaster",
                "recruitment_officer",
                "junior_officer",
                "private",
                "recruit",
                "reservist",
            ]
        ],
        "clan_gold_min": int,
        "clan_gold_max": int,
        "clan_credits_min": int,
        "clan_credits_max": int,
        "clan_crystal_min": int,
        "clan_crystal_max": int,
        "country[]": list[str],
        "not_country[]": list[str],
    },
    total=False,
)


class CategoryWotResponseItemsBumpSettings(TypedDict):
    canBumpItem: bool
    canBumpItemGlobally: bool
    shortErrorPhrase: object
    errorPhrase: object


class CategoryWotResponseItemsWotTopPremiumTanks00000(TypedDict, total=False):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    short_name: str
    tier: int


CategoryWotResponseItemsWotTopPremiumTanks = TypedDict(
    "CategoryWotResponseItemsWotTopPremiumTanks",
    {
        "00000": CategoryWotResponseItemsWotTopPremiumTanks00000,
    },
)


class CategoryWotResponseItemsWotTanks00000(TypedDict, total=False):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    short_name: str
    tier: int


CategoryWotResponseItemsWotTanks = TypedDict(
    "CategoryWotResponseItemsWotTanks",
    {
        "00000": CategoryWotResponseItemsWotTanks00000,
    },
)


class CategoryWotResponseItemsWotPremiumTanks30465(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    short_name: str
    tier: int


class CategoryWotResponseItemsWotPremiumTanks60945(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    short_name: str
    tier: int


class CategoryWotResponseItemsWotPremiumTanks51233(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    short_name: str
    tier: int


class CategoryWotResponseItemsWotPremiumTanks57377(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    short_name: str
    tier: int


class CategoryWotResponseItemsWotPremiumTanks62497(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    short_name: str
    tier: int


class CategoryWotResponseItemsWotPremiumTanks55569(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    short_name: str
    tier: int


class CategoryWotResponseItemsWotPremiumTanks7937025(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    short_name: str
    tier: int


class CategoryWotResponseItemsWotPremiumTanks50977(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    short_name: str
    tier: int


class CategoryWotResponseItemsWotPremiumTanks51585(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    short_name: str
    tier: int


class CategoryWotResponseItemsWotPremiumTanks46097(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    short_name: str
    tier: int


class CategoryWotResponseItemsWotPremiumTanks47873(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    short_name: str
    tier: int


class CategoryWotResponseItemsWotPremiumTanks43841(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    short_name: str
    tier: int


CategoryWotResponseItemsWotPremiumTanks = TypedDict(
    "CategoryWotResponseItemsWotPremiumTanks",
    {
        "30465": CategoryWotResponseItemsWotPremiumTanks30465,
        "60945": CategoryWotResponseItemsWotPremiumTanks60945,
        "51233": CategoryWotResponseItemsWotPremiumTanks51233,
        "57377": CategoryWotResponseItemsWotPremiumTanks57377,
        "62497": CategoryWotResponseItemsWotPremiumTanks62497,
        "55569": CategoryWotResponseItemsWotPremiumTanks55569,
        "7937025": CategoryWotResponseItemsWotPremiumTanks7937025,
        "50977": CategoryWotResponseItemsWotPremiumTanks50977,
        "51585": CategoryWotResponseItemsWotPremiumTanks51585,
        "46097": CategoryWotResponseItemsWotPremiumTanks46097,
        "47873": CategoryWotResponseItemsWotPremiumTanks47873,
        "43841": CategoryWotResponseItemsWotPremiumTanks43841,
    },
)


class CategoryWotResponseItemsWotTopTanks00000(TypedDict, total=False):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    short_name: str
    tier: int


CategoryWotResponseItemsWotTopTanks = TypedDict(
    "CategoryWotResponseItemsWotTopTanks",
    {
        "00000": CategoryWotResponseItemsWotTopTanks00000,
    },
)


class CategoryWotResponseItemsSeller(TypedDict):
    user_id: int
    sold_items_count: int
    active_items_count: int
    restore_data: str
    username: str
    avatar_date: int
    is_banned: int
    display_style_group_id: int
    restore_percents: int


class CategoryWotResponseItems(TypedDict):
    item_id: int
    item_state: str
    category_id: int
    published_date: int
    title: str
    description: str
    price: int
    update_stat_date: int
    refreshed_date: int
    edit_date: int
    view_count: int
    is_sticky: int
    item_origin: str
    extended_guarantee: int
    nsb: int
    allow_ask_discount: int
    title_en: str
    description_en: str
    email_type: str
    email_provider: object
    item_domain: str
    resale_item_origin: str
    wot_item_id: int
    wot_last_activity: int
    wot_register_date: int
    wot_mobile: int
    wot_premium: int
    wot_premium_expires: int
    wot_gold: int
    wot_credits: int
    wot_battle_count: int
    wot_win_count: int
    wot_loss_count: int
    wot_win_count_percents: int
    wot_top_tanks: int
    wot_premium_tanks: int
    wot_top_premium_tanks: int
    wot_region: str
    wot_blitz: int
    feedback_data: str
    isIgnored: bool
    priceWithSellerFee: int
    guarantee: object
    canViewLoginData: bool
    canUpdateItemStats: bool
    canReportItem: bool
    canViewEmailLoginData: bool
    showGetEmailCodeButton: bool
    canOpenItem: bool
    canCloseItem: bool
    canEditItem: bool
    canDeleteItem: bool
    canStickItem: bool
    canUnstickItem: bool
    bumpSettings: CategoryWotResponseItemsBumpSettings
    canBumpItem: bool
    canBuyItem: bool
    rub_price: int
    price_currency: str
    canValidateAccount: bool
    canResellItemAfterPurchase: bool
    wotRegionPhrase: str
    isSmallExf: bool
    account_last_activity: int
    wotTopPremiumTanks: CategoryWotResponseItemsWotTopPremiumTanks
    wotTanks: CategoryWotResponseItemsWotTanks
    wotPremiumTanks: CategoryWotResponseItemsWotPremiumTanks
    wotTopTanks: CategoryWotResponseItemsWotTopTanks
    wotPremiumTankCount: int
    wotTankCount: int
    wotLauncherTitle: str
    wot_has_clan: bool
    canViewAccountLink: bool
    accountLinks: list[object]
    canChangePassword: bool
    itemOriginPhrase: str
    sold_items_category_count: int
    restore_items_category_count: int
    tags: list[object]
    note_text: object
    hasPendingAutoBuy: bool
    descriptionHtml: str
    descriptionEnHtml: str
    descriptionPlain: str
    descriptionEnPlain: str
    seller: CategoryWotResponseItemsSeller


class CategoryWotResponse(TypedDict):
    items: list[CategoryWotResponseItems]
    totalItems: int
    totalItemsPrice: object
    hasNextPage: bool
    perPage: int
    page: int
    wasCached: bool
    cacheTTL: int
    lastModified: int
    serverTime: int
    searchUrl: str
    stickyItems: list[object]
    system_info: Resp_SystemInfo


CategoryWotblitzParams = TypedDict(
    "CategoryWotblitzParams",
    {
        "page": int,
        "pmin": int,
        "pmax": int,
        "title": str,
        "order_by": Literal[
            "price_to_up",
            "price_to_down",
            "pdate_to_down",
            "pdate_to_up",
            "pdate_to_down_upload",
            "pdate_to_up_upload",
            "edate_to_up",
            "edate_to_down",
            "ddate_to_up",
            "ddate_to_down",
        ],
        "tag_id[]": list[int],
        "not_tag_id[]": list[int],
        "public_tag_id[]": list[int],
        "not_public_tag_id[]": list[int],
        "origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "not_origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "user_id": int,
        "nsb": bool,
        "sb": bool,
        "nsb_by_me": bool,
        "sb_by_me": bool,
        "currency": Literal[
            "rub", "uah", "kzt", "byn", "usd", "eur", "gbp", "cny", "try", "jpy", "brl"
        ],
        "email_login_data": bool,
        "email_provider[]": list[
            Literal["other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"]
        ],
        "not_email_provider[]": Literal[
            "other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"
        ],
        "parse_same_item_ids": bool,
        "email_type[]": list[Literal["autoreg", "native", "no"]],
        "item_domain": str,
        "tel": Literal["yes", "no", "nomatter"],
        "daybreak": int,
        "battles_min": int,
        "battles_max": int,
        "gold_min": int,
        "gold_max": int,
        "silver_min": int,
        "silver_max": int,
        "top_min": int,
        "top_max": int,
        "prem_min": int,
        "prem_max": int,
        "top_prem_min": int,
        "top_prem_max": int,
        "win_pmin": int,
        "win_pmax": int,
        "tank[]": list[int],
        "region[]": list[Literal["asia", "eu", "na", "ru"]],
        "not_region[]": list[Literal["asia", "eu", "na", "ru"]],
        "premium": Literal["yes", "no", "nomatter"],
        "premium_expiration": int,
        "premium_expiration_period": Literal["day", "month", "year"],
        "clan": Literal["yes", "no", "nomatter"],
        "clan_role[]": list[
            Literal[
                "commander",
                "executive_officer",
                "personnel_officer",
                "combat_officer",
                "intelligence_officer",
                "quartermaster",
                "recruitment_officer",
                "junior_officer",
                "private",
                "recruit",
                "reservist",
            ]
        ],
        "not_clan_role[]": list[
            Literal[
                "commander",
                "executive_officer",
                "personnel_officer",
                "combat_officer",
                "intelligence_officer",
                "quartermaster",
                "recruitment_officer",
                "junior_officer",
                "private",
                "recruit",
                "reservist",
            ]
        ],
        "clan_gold_min": int,
        "clan_gold_max": int,
        "clan_credits_min": int,
        "clan_credits_max": int,
        "clan_crystal_min": int,
        "clan_crystal_max": int,
        "country[]": list[str],
        "not_country[]": list[str],
    },
    total=False,
)


class CategoryWotblitzResponseItemsBumpSettings(TypedDict):
    canBumpItem: bool
    canBumpItemGlobally: bool
    shortErrorPhrase: object
    errorPhrase: object


class CategoryWotblitzResponseItemsWotTopPremiumTanks15697(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopPremiumTanks5681(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopPremiumTanks23313(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


CategoryWotblitzResponseItemsWotTopPremiumTanks = TypedDict(
    "CategoryWotblitzResponseItemsWotTopPremiumTanks",
    {
        "15697": CategoryWotblitzResponseItemsWotTopPremiumTanks15697,
        "5681": CategoryWotblitzResponseItemsWotTopPremiumTanks5681,
        "23313": CategoryWotblitzResponseItemsWotTopPremiumTanks23313,
    },
)


class CategoryWotblitzResponseItemsWotTanks12305(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks6753(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks18001(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks6449(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks15697(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks4481(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks13185(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks14337(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks3681(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks6145(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks5425(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks3649(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks7169(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks7249(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks7297(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks19537(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks5681(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks6209(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks58641(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks16897(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks10369(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks22817(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks9489(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks385(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks19217(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks9297(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks13825(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks5505(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks13089(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks12049(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks13569(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks4145(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks24321(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks23313(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks20257(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks14609(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks10289(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks14881(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks3937(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks10785(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks6929(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks16401(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks641(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks20001(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks12545(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks7953(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks25361(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks20481(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks62737(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks5137(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks18753(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks19025(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks13345(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks2945(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks16193(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks18209(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks19985(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks19489(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks20305(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks20737(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks21329(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks53025(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks18241(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks10881(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks21265(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks20513(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks12673(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks16705(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks6785(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks58881(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks18513(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks2849(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks9073(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks18769(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks15953(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks6257(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks6001(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks55297(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks23841(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks64529(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks21025(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks23057(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks7281(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks23825(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks8753(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks59137(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks10241(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks7793(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks5745(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks11553(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks625(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks20817(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks23297(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks2625(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks19713(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks24849(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks56097(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks57105(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks54785(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks2609(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks57361(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks1409(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks55889(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks5393(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks5489(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks53761(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks65377(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks54545(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks51473(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks10273(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks3121(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks4881(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks51729(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks4369(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTanks6993(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


CategoryWotblitzResponseItemsWotTanks = TypedDict(
    "CategoryWotblitzResponseItemsWotTanks",
    {
        "12305": CategoryWotblitzResponseItemsWotTanks12305,
        "6753": CategoryWotblitzResponseItemsWotTanks6753,
        "18001": CategoryWotblitzResponseItemsWotTanks18001,
        "6449": CategoryWotblitzResponseItemsWotTanks6449,
        "15697": CategoryWotblitzResponseItemsWotTanks15697,
        "4481": CategoryWotblitzResponseItemsWotTanks4481,
        "13185": CategoryWotblitzResponseItemsWotTanks13185,
        "14337": CategoryWotblitzResponseItemsWotTanks14337,
        "3681": CategoryWotblitzResponseItemsWotTanks3681,
        "6145": CategoryWotblitzResponseItemsWotTanks6145,
        "5425": CategoryWotblitzResponseItemsWotTanks5425,
        "3649": CategoryWotblitzResponseItemsWotTanks3649,
        "7169": CategoryWotblitzResponseItemsWotTanks7169,
        "7249": CategoryWotblitzResponseItemsWotTanks7249,
        "7297": CategoryWotblitzResponseItemsWotTanks7297,
        "19537": CategoryWotblitzResponseItemsWotTanks19537,
        "5681": CategoryWotblitzResponseItemsWotTanks5681,
        "6209": CategoryWotblitzResponseItemsWotTanks6209,
        "58641": CategoryWotblitzResponseItemsWotTanks58641,
        "16897": CategoryWotblitzResponseItemsWotTanks16897,
        "10369": CategoryWotblitzResponseItemsWotTanks10369,
        "22817": CategoryWotblitzResponseItemsWotTanks22817,
        "9489": CategoryWotblitzResponseItemsWotTanks9489,
        "385": CategoryWotblitzResponseItemsWotTanks385,
        "19217": CategoryWotblitzResponseItemsWotTanks19217,
        "9297": CategoryWotblitzResponseItemsWotTanks9297,
        "13825": CategoryWotblitzResponseItemsWotTanks13825,
        "5505": CategoryWotblitzResponseItemsWotTanks5505,
        "13089": CategoryWotblitzResponseItemsWotTanks13089,
        "12049": CategoryWotblitzResponseItemsWotTanks12049,
        "13569": CategoryWotblitzResponseItemsWotTanks13569,
        "4145": CategoryWotblitzResponseItemsWotTanks4145,
        "24321": CategoryWotblitzResponseItemsWotTanks24321,
        "23313": CategoryWotblitzResponseItemsWotTanks23313,
        "20257": CategoryWotblitzResponseItemsWotTanks20257,
        "14609": CategoryWotblitzResponseItemsWotTanks14609,
        "10289": CategoryWotblitzResponseItemsWotTanks10289,
        "14881": CategoryWotblitzResponseItemsWotTanks14881,
        "3937": CategoryWotblitzResponseItemsWotTanks3937,
        "10785": CategoryWotblitzResponseItemsWotTanks10785,
        "6929": CategoryWotblitzResponseItemsWotTanks6929,
        "16401": CategoryWotblitzResponseItemsWotTanks16401,
        "641": CategoryWotblitzResponseItemsWotTanks641,
        "20001": CategoryWotblitzResponseItemsWotTanks20001,
        "12545": CategoryWotblitzResponseItemsWotTanks12545,
        "7953": CategoryWotblitzResponseItemsWotTanks7953,
        "25361": CategoryWotblitzResponseItemsWotTanks25361,
        "20481": CategoryWotblitzResponseItemsWotTanks20481,
        "62737": CategoryWotblitzResponseItemsWotTanks62737,
        "5137": CategoryWotblitzResponseItemsWotTanks5137,
        "18753": CategoryWotblitzResponseItemsWotTanks18753,
        "19025": CategoryWotblitzResponseItemsWotTanks19025,
        "13345": CategoryWotblitzResponseItemsWotTanks13345,
        "2945": CategoryWotblitzResponseItemsWotTanks2945,
        "16193": CategoryWotblitzResponseItemsWotTanks16193,
        "18209": CategoryWotblitzResponseItemsWotTanks18209,
        "19985": CategoryWotblitzResponseItemsWotTanks19985,
        "19489": CategoryWotblitzResponseItemsWotTanks19489,
        "20305": CategoryWotblitzResponseItemsWotTanks20305,
        "20737": CategoryWotblitzResponseItemsWotTanks20737,
        "21329": CategoryWotblitzResponseItemsWotTanks21329,
        "53025": CategoryWotblitzResponseItemsWotTanks53025,
        "18241": CategoryWotblitzResponseItemsWotTanks18241,
        "10881": CategoryWotblitzResponseItemsWotTanks10881,
        "21265": CategoryWotblitzResponseItemsWotTanks21265,
        "20513": CategoryWotblitzResponseItemsWotTanks20513,
        "12673": CategoryWotblitzResponseItemsWotTanks12673,
        "16705": CategoryWotblitzResponseItemsWotTanks16705,
        "6785": CategoryWotblitzResponseItemsWotTanks6785,
        "58881": CategoryWotblitzResponseItemsWotTanks58881,
        "18513": CategoryWotblitzResponseItemsWotTanks18513,
        "2849": CategoryWotblitzResponseItemsWotTanks2849,
        "9073": CategoryWotblitzResponseItemsWotTanks9073,
        "18769": CategoryWotblitzResponseItemsWotTanks18769,
        "15953": CategoryWotblitzResponseItemsWotTanks15953,
        "6257": CategoryWotblitzResponseItemsWotTanks6257,
        "6001": CategoryWotblitzResponseItemsWotTanks6001,
        "55297": CategoryWotblitzResponseItemsWotTanks55297,
        "23841": CategoryWotblitzResponseItemsWotTanks23841,
        "64529": CategoryWotblitzResponseItemsWotTanks64529,
        "21025": CategoryWotblitzResponseItemsWotTanks21025,
        "23057": CategoryWotblitzResponseItemsWotTanks23057,
        "7281": CategoryWotblitzResponseItemsWotTanks7281,
        "23825": CategoryWotblitzResponseItemsWotTanks23825,
        "8753": CategoryWotblitzResponseItemsWotTanks8753,
        "59137": CategoryWotblitzResponseItemsWotTanks59137,
        "10241": CategoryWotblitzResponseItemsWotTanks10241,
        "7793": CategoryWotblitzResponseItemsWotTanks7793,
        "5745": CategoryWotblitzResponseItemsWotTanks5745,
        "11553": CategoryWotblitzResponseItemsWotTanks11553,
        "625": CategoryWotblitzResponseItemsWotTanks625,
        "20817": CategoryWotblitzResponseItemsWotTanks20817,
        "23297": CategoryWotblitzResponseItemsWotTanks23297,
        "2625": CategoryWotblitzResponseItemsWotTanks2625,
        "19713": CategoryWotblitzResponseItemsWotTanks19713,
        "24849": CategoryWotblitzResponseItemsWotTanks24849,
        "56097": CategoryWotblitzResponseItemsWotTanks56097,
        "57105": CategoryWotblitzResponseItemsWotTanks57105,
        "54785": CategoryWotblitzResponseItemsWotTanks54785,
        "2609": CategoryWotblitzResponseItemsWotTanks2609,
        "57361": CategoryWotblitzResponseItemsWotTanks57361,
        "1409": CategoryWotblitzResponseItemsWotTanks1409,
        "55889": CategoryWotblitzResponseItemsWotTanks55889,
        "5393": CategoryWotblitzResponseItemsWotTanks5393,
        "5489": CategoryWotblitzResponseItemsWotTanks5489,
        "53761": CategoryWotblitzResponseItemsWotTanks53761,
        "65377": CategoryWotblitzResponseItemsWotTanks65377,
        "54545": CategoryWotblitzResponseItemsWotTanks54545,
        "51473": CategoryWotblitzResponseItemsWotTanks51473,
        "10273": CategoryWotblitzResponseItemsWotTanks10273,
        "3121": CategoryWotblitzResponseItemsWotTanks3121,
        "4881": CategoryWotblitzResponseItemsWotTanks4881,
        "51729": CategoryWotblitzResponseItemsWotTanks51729,
        "4369": CategoryWotblitzResponseItemsWotTanks4369,
        "6993": CategoryWotblitzResponseItemsWotTanks6993,
    },
)


class CategoryWotblitzResponseItemsWotPremiumTanks5681(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks23313(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks15697(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks25361(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks12545(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks62737(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks18769(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks53025(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks20737(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks20481(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks18753(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks58881(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks19025(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks13345(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks2945(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks16193(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks19985(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks19489(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks20305(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks18241(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks21329(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks18513(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks16705(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks9073(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks12673(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks6785(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks21265(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks2849(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks20513(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks23057(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks64529(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks7793(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks23841(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks21025(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks6001(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks55297(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks6257(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks8753(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks23825(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks15953(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks59137(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks7281(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks20817(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks5745(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks625(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks19713(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks57105(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks23297(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks57361(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks54785(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks2609(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks55889(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks56097(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks51473(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks65377(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks5489(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks53761(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks54545(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks51729(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotPremiumTanks4881(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


CategoryWotblitzResponseItemsWotPremiumTanks = TypedDict(
    "CategoryWotblitzResponseItemsWotPremiumTanks",
    {
        "5681": CategoryWotblitzResponseItemsWotPremiumTanks5681,
        "23313": CategoryWotblitzResponseItemsWotPremiumTanks23313,
        "15697": CategoryWotblitzResponseItemsWotPremiumTanks15697,
        "25361": CategoryWotblitzResponseItemsWotPremiumTanks25361,
        "12545": CategoryWotblitzResponseItemsWotPremiumTanks12545,
        "62737": CategoryWotblitzResponseItemsWotPremiumTanks62737,
        "18769": CategoryWotblitzResponseItemsWotPremiumTanks18769,
        "53025": CategoryWotblitzResponseItemsWotPremiumTanks53025,
        "20737": CategoryWotblitzResponseItemsWotPremiumTanks20737,
        "20481": CategoryWotblitzResponseItemsWotPremiumTanks20481,
        "18753": CategoryWotblitzResponseItemsWotPremiumTanks18753,
        "58881": CategoryWotblitzResponseItemsWotPremiumTanks58881,
        "19025": CategoryWotblitzResponseItemsWotPremiumTanks19025,
        "13345": CategoryWotblitzResponseItemsWotPremiumTanks13345,
        "2945": CategoryWotblitzResponseItemsWotPremiumTanks2945,
        "16193": CategoryWotblitzResponseItemsWotPremiumTanks16193,
        "19985": CategoryWotblitzResponseItemsWotPremiumTanks19985,
        "19489": CategoryWotblitzResponseItemsWotPremiumTanks19489,
        "20305": CategoryWotblitzResponseItemsWotPremiumTanks20305,
        "18241": CategoryWotblitzResponseItemsWotPremiumTanks18241,
        "21329": CategoryWotblitzResponseItemsWotPremiumTanks21329,
        "18513": CategoryWotblitzResponseItemsWotPremiumTanks18513,
        "16705": CategoryWotblitzResponseItemsWotPremiumTanks16705,
        "9073": CategoryWotblitzResponseItemsWotPremiumTanks9073,
        "12673": CategoryWotblitzResponseItemsWotPremiumTanks12673,
        "6785": CategoryWotblitzResponseItemsWotPremiumTanks6785,
        "21265": CategoryWotblitzResponseItemsWotPremiumTanks21265,
        "2849": CategoryWotblitzResponseItemsWotPremiumTanks2849,
        "20513": CategoryWotblitzResponseItemsWotPremiumTanks20513,
        "23057": CategoryWotblitzResponseItemsWotPremiumTanks23057,
        "64529": CategoryWotblitzResponseItemsWotPremiumTanks64529,
        "7793": CategoryWotblitzResponseItemsWotPremiumTanks7793,
        "23841": CategoryWotblitzResponseItemsWotPremiumTanks23841,
        "21025": CategoryWotblitzResponseItemsWotPremiumTanks21025,
        "6001": CategoryWotblitzResponseItemsWotPremiumTanks6001,
        "55297": CategoryWotblitzResponseItemsWotPremiumTanks55297,
        "6257": CategoryWotblitzResponseItemsWotPremiumTanks6257,
        "8753": CategoryWotblitzResponseItemsWotPremiumTanks8753,
        "23825": CategoryWotblitzResponseItemsWotPremiumTanks23825,
        "15953": CategoryWotblitzResponseItemsWotPremiumTanks15953,
        "59137": CategoryWotblitzResponseItemsWotPremiumTanks59137,
        "7281": CategoryWotblitzResponseItemsWotPremiumTanks7281,
        "20817": CategoryWotblitzResponseItemsWotPremiumTanks20817,
        "5745": CategoryWotblitzResponseItemsWotPremiumTanks5745,
        "625": CategoryWotblitzResponseItemsWotPremiumTanks625,
        "19713": CategoryWotblitzResponseItemsWotPremiumTanks19713,
        "57105": CategoryWotblitzResponseItemsWotPremiumTanks57105,
        "23297": CategoryWotblitzResponseItemsWotPremiumTanks23297,
        "57361": CategoryWotblitzResponseItemsWotPremiumTanks57361,
        "54785": CategoryWotblitzResponseItemsWotPremiumTanks54785,
        "2609": CategoryWotblitzResponseItemsWotPremiumTanks2609,
        "55889": CategoryWotblitzResponseItemsWotPremiumTanks55889,
        "56097": CategoryWotblitzResponseItemsWotPremiumTanks56097,
        "51473": CategoryWotblitzResponseItemsWotPremiumTanks51473,
        "65377": CategoryWotblitzResponseItemsWotPremiumTanks65377,
        "5489": CategoryWotblitzResponseItemsWotPremiumTanks5489,
        "53761": CategoryWotblitzResponseItemsWotPremiumTanks53761,
        "54545": CategoryWotblitzResponseItemsWotPremiumTanks54545,
        "51729": CategoryWotblitzResponseItemsWotPremiumTanks51729,
        "4881": CategoryWotblitzResponseItemsWotPremiumTanks4881,
    },
)


class CategoryWotblitzResponseItemsWotTopTanks5505(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks13089(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks13569(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks4145(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks10289(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks3937(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks3649(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks18001(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks6449(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks15697(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks12305(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks4481(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks6145(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks7249(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks5681(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks58641(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks16897(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks14337(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks9489(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks385(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks10785(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks14609(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks23313(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks6929(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks6209(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks19537(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks7297(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks7169(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks5425(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks6753(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks3681(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks13185(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks10369(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks22817(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks14881(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks20257(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks24321(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks12049(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks13825(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks9297(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


class CategoryWotblitzResponseItemsWotTopTanks19217(TypedDict):
    tank_id: int
    name: str
    is_premium: int
    image_url: str
    tier: int
    short_name: str
    is_collectible: int


CategoryWotblitzResponseItemsWotTopTanks = TypedDict(
    "CategoryWotblitzResponseItemsWotTopTanks",
    {
        "5505": CategoryWotblitzResponseItemsWotTopTanks5505,
        "13089": CategoryWotblitzResponseItemsWotTopTanks13089,
        "13569": CategoryWotblitzResponseItemsWotTopTanks13569,
        "4145": CategoryWotblitzResponseItemsWotTopTanks4145,
        "10289": CategoryWotblitzResponseItemsWotTopTanks10289,
        "3937": CategoryWotblitzResponseItemsWotTopTanks3937,
        "3649": CategoryWotblitzResponseItemsWotTopTanks3649,
        "18001": CategoryWotblitzResponseItemsWotTopTanks18001,
        "6449": CategoryWotblitzResponseItemsWotTopTanks6449,
        "15697": CategoryWotblitzResponseItemsWotTopTanks15697,
        "12305": CategoryWotblitzResponseItemsWotTopTanks12305,
        "4481": CategoryWotblitzResponseItemsWotTopTanks4481,
        "6145": CategoryWotblitzResponseItemsWotTopTanks6145,
        "7249": CategoryWotblitzResponseItemsWotTopTanks7249,
        "5681": CategoryWotblitzResponseItemsWotTopTanks5681,
        "58641": CategoryWotblitzResponseItemsWotTopTanks58641,
        "16897": CategoryWotblitzResponseItemsWotTopTanks16897,
        "14337": CategoryWotblitzResponseItemsWotTopTanks14337,
        "9489": CategoryWotblitzResponseItemsWotTopTanks9489,
        "385": CategoryWotblitzResponseItemsWotTopTanks385,
        "10785": CategoryWotblitzResponseItemsWotTopTanks10785,
        "14609": CategoryWotblitzResponseItemsWotTopTanks14609,
        "23313": CategoryWotblitzResponseItemsWotTopTanks23313,
        "6929": CategoryWotblitzResponseItemsWotTopTanks6929,
        "6209": CategoryWotblitzResponseItemsWotTopTanks6209,
        "19537": CategoryWotblitzResponseItemsWotTopTanks19537,
        "7297": CategoryWotblitzResponseItemsWotTopTanks7297,
        "7169": CategoryWotblitzResponseItemsWotTopTanks7169,
        "5425": CategoryWotblitzResponseItemsWotTopTanks5425,
        "6753": CategoryWotblitzResponseItemsWotTopTanks6753,
        "3681": CategoryWotblitzResponseItemsWotTopTanks3681,
        "13185": CategoryWotblitzResponseItemsWotTopTanks13185,
        "10369": CategoryWotblitzResponseItemsWotTopTanks10369,
        "22817": CategoryWotblitzResponseItemsWotTopTanks22817,
        "14881": CategoryWotblitzResponseItemsWotTopTanks14881,
        "20257": CategoryWotblitzResponseItemsWotTopTanks20257,
        "24321": CategoryWotblitzResponseItemsWotTopTanks24321,
        "12049": CategoryWotblitzResponseItemsWotTopTanks12049,
        "13825": CategoryWotblitzResponseItemsWotTopTanks13825,
        "9297": CategoryWotblitzResponseItemsWotTopTanks9297,
        "19217": CategoryWotblitzResponseItemsWotTopTanks19217,
    },
)


class CategoryWotblitzResponseItemsSeller(TypedDict):
    user_id: int
    sold_items_count: int
    active_items_count: int
    restore_data: str
    username: str
    avatar_date: int
    is_banned: int
    display_style_group_id: int
    restore_percents: int


class CategoryWotblitzResponseItems(TypedDict):
    item_id: int
    item_state: str
    category_id: int
    published_date: int
    title: str
    description: str
    price: int
    update_stat_date: int
    refreshed_date: int
    edit_date: int
    view_count: int
    is_sticky: int
    item_origin: str
    extended_guarantee: int
    nsb: int
    allow_ask_discount: int
    title_en: str
    description_en: str
    email_type: str
    email_provider: object
    item_domain: str
    resale_item_origin: str
    wot_item_id: int
    wot_last_activity: int
    wot_register_date: int
    wot_mobile: int
    wot_premium: int
    wot_premium_expires: int
    wot_gold: int
    wot_credits: int
    wot_battle_count: int
    wot_win_count: int
    wot_loss_count: int
    wot_win_count_percents: int
    wot_top_tanks: int
    wot_premium_tanks: int
    wot_top_premium_tanks: int
    wot_region: str
    wot_blitz: int
    feedback_data: str
    isIgnored: bool
    priceWithSellerFee: int
    guarantee: object
    canViewLoginData: bool
    canUpdateItemStats: bool
    canReportItem: bool
    canViewEmailLoginData: bool
    showGetEmailCodeButton: bool
    canOpenItem: bool
    canCloseItem: bool
    canEditItem: bool
    canDeleteItem: bool
    canStickItem: bool
    canUnstickItem: bool
    bumpSettings: CategoryWotblitzResponseItemsBumpSettings
    canBumpItem: bool
    canBuyItem: bool
    rub_price: int
    price_currency: str
    canValidateAccount: bool
    canResellItemAfterPurchase: bool
    wotRegionPhrase: str
    isSmallExf: bool
    account_last_activity: int
    wotTopPremiumTanks: CategoryWotblitzResponseItemsWotTopPremiumTanks
    wotTanks: CategoryWotblitzResponseItemsWotTanks
    wotPremiumTanks: CategoryWotblitzResponseItemsWotPremiumTanks
    wotTopTanks: CategoryWotblitzResponseItemsWotTopTanks
    wotPremiumTankCount: int
    wotTankCount: int
    wotLauncherTitle: str
    wot_has_clan: bool
    canViewAccountLink: bool
    accountLinks: list[object]
    canChangePassword: bool
    itemOriginPhrase: str
    sold_items_category_count: int
    restore_items_category_count: int
    tags: list[object]
    note_text: object
    hasPendingAutoBuy: bool
    descriptionHtml: str
    descriptionEnHtml: str
    descriptionPlain: str
    descriptionEnPlain: str
    seller: CategoryWotblitzResponseItemsSeller


class CategoryWotblitzResponse(TypedDict):
    items: list[CategoryWotblitzResponseItems]
    totalItems: int
    totalItemsPrice: object
    hasNextPage: bool
    perPage: int
    page: int
    wasCached: bool
    cacheTTL: int
    lastModified: int
    serverTime: int
    searchUrl: str
    stickyItems: list[object]
    system_info: Resp_SystemInfo


CategoryGiftsParams = TypedDict(
    "CategoryGiftsParams",
    {
        "page": int,
        "pmin": int,
        "pmax": int,
        "title": str,
        "order_by": Literal[
            "price_to_up",
            "price_to_down",
            "pdate_to_down",
            "pdate_to_up",
            "pdate_to_down_upload",
            "pdate_to_up_upload",
            "edate_to_up",
            "edate_to_down",
            "ddate_to_up",
            "ddate_to_down",
        ],
        "tag_id[]": list[int],
        "not_tag_id[]": list[int],
        "public_tag_id[]": list[int],
        "not_public_tag_id[]": list[int],
        "origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "not_origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "user_id": int,
        "nsb": bool,
        "sb": bool,
        "nsb_by_me": bool,
        "sb_by_me": bool,
        "currency": Literal[
            "rub", "uah", "kzt", "byn", "usd", "eur", "gbp", "cny", "try", "jpy", "brl"
        ],
        "email_login_data": bool,
        "email_provider[]": list[
            Literal["other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"]
        ],
        "not_email_provider[]": Literal[
            "other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"
        ],
        "parse_same_item_ids": bool,
        "subscription": Literal[
            "discord_nitro", "discord_nitro_basic", "discord_nitro_trial", "telegram_premium"
        ],
        "subscription_length": int,
        "subscription_period": Literal["day", "month", "year"],
    },
    total=False,
)


class CategoryGiftsResponseItemsBumpSettings(TypedDict):
    canBumpItem: bool
    canBumpItemGlobally: bool
    shortErrorPhrase: object
    errorPhrase: object


class CategoryGiftsResponseItemsSeller(TypedDict):
    user_id: int
    sold_items_count: int
    active_items_count: int
    restore_data: str
    username: str
    avatar_date: int
    is_banned: int
    display_style_group_id: int
    restore_percents: object


class CategoryGiftsResponseItems(TypedDict):
    item_id: int
    item_state: str
    category_id: int
    published_date: int
    title: str
    description: str
    price: int
    update_stat_date: int
    refreshed_date: int
    edit_date: int
    view_count: int
    is_sticky: int
    item_origin: str
    extended_guarantee: int
    nsb: int
    allow_ask_discount: int
    title_en: str
    description_en: str
    email_type: str
    email_provider: object
    item_domain: str
    resale_item_origin: str
    gifts_item_id: int
    gifts_service: str
    gifts_duration: int
    gifts_type: str
    feedback_data: str
    isIgnored: bool
    priceWithSellerFee: int
    guarantee: object
    canViewLoginData: bool
    canUpdateItemStats: bool
    canReportItem: bool
    canViewEmailLoginData: bool
    showGetEmailCodeButton: bool
    canOpenItem: bool
    canCloseItem: bool
    canEditItem: bool
    canDeleteItem: bool
    canStickItem: bool
    canUnstickItem: bool
    bumpSettings: CategoryGiftsResponseItemsBumpSettings
    canBumpItem: bool
    canBuyItem: bool
    rub_price: int
    price_currency: str
    canValidateAccount: bool
    canResellItemAfterPurchase: bool
    giftsSubscriptionName: str
    giftsServiceName: str
    canViewAccountLink: bool
    canChangePassword: bool
    itemOriginPhrase: str
    tags: list[object]
    note_text: object
    hasPendingAutoBuy: bool
    descriptionHtml: str
    descriptionEnHtml: str
    descriptionPlain: str
    descriptionEnPlain: str
    seller: CategoryGiftsResponseItemsSeller


class CategoryGiftsResponse(TypedDict):
    items: list[CategoryGiftsResponseItems]
    totalItems: int
    totalItemsPrice: object
    hasNextPage: bool
    perPage: int
    page: int
    wasCached: bool
    cacheTTL: int
    lastModified: int
    serverTime: int
    searchUrl: str
    stickyItems: list[object]
    system_info: Resp_SystemInfo


CategoryEpicgamesParams = TypedDict(
    "CategoryEpicgamesParams",
    {
        "page": int,
        "pmin": int,
        "pmax": int,
        "title": str,
        "order_by": Literal[
            "price_to_up",
            "price_to_down",
            "pdate_to_down",
            "pdate_to_up",
            "pdate_to_down_upload",
            "pdate_to_up_upload",
            "edate_to_up",
            "edate_to_down",
            "ddate_to_up",
            "ddate_to_down",
        ],
        "tag_id[]": list[int],
        "not_tag_id[]": list[int],
        "public_tag_id[]": list[int],
        "not_public_tag_id[]": list[int],
        "origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "not_origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "user_id": int,
        "nsb": bool,
        "sb": bool,
        "nsb_by_me": bool,
        "sb_by_me": bool,
        "currency": Literal[
            "rub", "uah", "kzt", "byn", "usd", "eur", "gbp", "cny", "try", "jpy", "brl"
        ],
        "email_login_data": bool,
        "email_provider[]": list[
            Literal["other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"]
        ],
        "not_email_provider[]": Literal[
            "other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"
        ],
        "parse_same_item_ids": bool,
        "email_type[]": list[Literal["market", "autoreg", "native", "no"]],
        "item_domain": str,
        "eg": Literal[-1, 0, 1, 2],
        "game[]": list[str],
        "change_email": Literal["yes", "no", "nomatter"],
        "rl_purchases": bool,
        "balance_min": float,
        "balance_max": float,
        "rewards_balance_min": float,
        "rewards_balance_max": float,
        "gmin": int,
        "gmax": int,
        "country[]": list[str],
        "not_country[]": list[str],
        "daybreak": int,
        "hours_played": dict[str, int],
        "hours_played_max": dict[str, int],
    },
    total=False,
)


class CategoryEpicgamesResponseItemsEg_games0(TypedDict):
    internal_game_id: int
    app_id: str
    title: str
    abbr: str
    category_id: int
    img: str
    url: str
    ru: object
    hits_count: int
    link: str


CategoryEpicgamesResponseItemsEg_games = TypedDict(
    "CategoryEpicgamesResponseItemsEg_games",
    {
        "0": CategoryEpicgamesResponseItemsEg_games0,
    },
)


class CategoryEpicgamesResponseItemsBumpSettings(TypedDict):
    canBumpItem: bool
    canBumpItemGlobally: bool
    shortErrorPhrase: object
    errorPhrase: object


class CategoryEpicgamesResponseItemsEgTransactions(TypedDict):
    date: int
    title: str
    presentmentTotal: str
    orderType: str


class CategoryEpicgamesResponseItemsSeller(TypedDict):
    user_id: int
    sold_items_count: int
    active_items_count: int
    restore_data: str
    username: str
    avatar_date: int
    is_banned: int
    display_style_group_id: int
    restore_percents: int


class CategoryEpicgamesResponseItems(TypedDict):
    item_id: int
    item_state: str
    category_id: int
    published_date: int
    title: str
    description: str
    price: int
    update_stat_date: int
    refreshed_date: int
    edit_date: int
    view_count: int
    is_sticky: int
    item_origin: str
    extended_guarantee: int
    nsb: int
    allow_ask_discount: int
    title_en: str
    description_en: str
    email_type: str
    email_provider: str
    item_domain: str
    resale_item_origin: str
    eg_item_id: int
    eg_country: str
    eg_code_redemption_history: list[object]
    eg_coupons: list[object]
    eg_games: CategoryEpicgamesResponseItemsEg_games
    eg_change_email: int
    eg_can_update_display_name: int
    eg_last_activity: int
    eg_payment_methods: list[object]
    eg_rl_purchases: int
    eg_username: str
    eg_rewards_balance: int
    eg_rewards_expiration_date: int
    eg_next_change_email_date: int
    eg_game_count: int
    eg_balance: int
    feedback_data: str
    isIgnored: bool
    priceWithSellerFee: int
    guarantee: object
    canViewLoginData: bool
    canUpdateItemStats: bool
    canReportItem: bool
    canViewEmailLoginData: bool
    showGetEmailCodeButton: bool
    canOpenItem: bool
    canCloseItem: bool
    canEditItem: bool
    canDeleteItem: bool
    canStickItem: bool
    canUnstickItem: bool
    bumpSettings: CategoryEpicgamesResponseItemsBumpSettings
    canBumpItem: bool
    canBuyItem: bool
    rub_price: int
    price_currency: str
    canValidateAccount: bool
    canResellItemAfterPurchase: bool
    egBalance: str
    egGameCount: int
    egTransactions: list[CategoryEpicgamesResponseItemsEgTransactions]
    canViewAccountLink: bool
    accountLinks: list[object]
    emailLoginUrl: str
    canChangePassword: bool
    itemOriginPhrase: str
    sold_items_category_count: int
    restore_items_category_count: int
    tags: list[object]
    note_text: object
    hasPendingAutoBuy: bool
    descriptionHtml: str
    descriptionEnHtml: str
    descriptionPlain: str
    descriptionEnPlain: str
    seller: CategoryEpicgamesResponseItemsSeller


class CategoryEpicgamesResponse(TypedDict):
    items: list[CategoryEpicgamesResponseItems]
    totalItems: int
    totalItemsPrice: object
    hasNextPage: bool
    perPage: int
    page: int
    wasCached: bool
    cacheTTL: int
    lastModified: int
    serverTime: int
    searchUrl: str
    stickyItems: list[object]
    system_info: Resp_SystemInfo


CategoryEscapefromtarkovParams = TypedDict(
    "CategoryEscapefromtarkovParams",
    {
        "page": int,
        "pmin": int,
        "pmax": int,
        "title": str,
        "order_by": Literal[
            "price_to_up",
            "price_to_down",
            "pdate_to_down",
            "pdate_to_up",
            "pdate_to_down_upload",
            "pdate_to_up_upload",
            "edate_to_up",
            "edate_to_down",
            "ddate_to_up",
            "ddate_to_down",
        ],
        "tag_id[]": list[int],
        "not_tag_id[]": list[int],
        "public_tag_id[]": list[int],
        "not_public_tag_id[]": list[int],
        "origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "not_origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "user_id": int,
        "nsb": bool,
        "sb": bool,
        "nsb_by_me": bool,
        "sb_by_me": bool,
        "currency": Literal[
            "rub", "uah", "kzt", "byn", "usd", "eur", "gbp", "cny", "try", "jpy", "brl"
        ],
        "email_login_data": bool,
        "email_provider[]": list[
            Literal["other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"]
        ],
        "not_email_provider[]": Literal[
            "other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"
        ],
        "parse_same_item_ids": bool,
        "email_type[]": list[Literal["autoreg", "native", "no"]],
        "item_domain": str,
        "region": Literal["af", "as", "cis", "eu", "me", "oc", "us"],
        "version[]": list[
            Literal[
                "edge_of_darkness",
                "left_behind",
                "prepare_for_escape",
                "standard",
                "unheard_edition",
            ]
        ],
        "reg": int,
        "reg_period": Literal["day", "month", "year"],
        "level_min": int,
        "level_max": int,
        "pve": YesNoNoMatterScheme,
        "side": Literal["Bear", "Savage"],
    },
    total=False,
)


class CategoryEscapefromtarkovResponseItemsBumpSettings(TypedDict):
    canBumpItem: bool
    canBumpItemGlobally: bool
    shortErrorPhrase: object
    errorPhrase: object


class CategoryEscapefromtarkovResponseItemsSeller(TypedDict):
    user_id: int
    sold_items_count: int
    active_items_count: int
    restore_data: str
    username: str
    avatar_date: int
    is_banned: int
    display_style_group_id: int
    restore_percents: int


class CategoryEscapefromtarkovResponseItems(TypedDict):
    item_id: int
    item_state: str
    category_id: int
    published_date: int
    title: str
    description: str
    price: int
    update_stat_date: int
    refreshed_date: int
    edit_date: int
    view_count: int
    is_sticky: int
    item_origin: str
    extended_guarantee: int
    nsb: int
    allow_ask_discount: int
    title_en: str
    description_en: str
    email_type: str
    email_provider: str
    item_domain: str
    resale_item_origin: str
    tarkov_item_id: int
    tarkov_game_version: str
    tarkov_register_date: int
    tarkov_level: int
    tarkov_exp: int
    tarkov_last_activity: int
    tarkov_side: str
    tarkov_rubles: int
    tarkov_secured_container: str
    tarkov_euros: int
    tarkov_dollars: int
    tarkov_kd: int
    tarkov_deaths: int
    tarkov_kills: int
    tarkov_sessions: int
    tarkov_region: str
    tarkov_total_in_game: int
    tarkov_mail_forwarding: int
    tarkov_username: str
    tarkov_purchase_date: int
    feedback_data: str
    isIgnored: bool
    priceWithSellerFee: int
    guarantee: object
    canViewLoginData: bool
    canUpdateItemStats: bool
    canReportItem: bool
    canViewEmailLoginData: bool
    showGetEmailCodeButton: bool
    canOpenItem: bool
    canCloseItem: bool
    canEditItem: bool
    canDeleteItem: bool
    canStickItem: bool
    canUnstickItem: bool
    bumpSettings: CategoryEscapefromtarkovResponseItemsBumpSettings
    canBumpItem: bool
    canBuyItem: bool
    rub_price: int
    price_currency: str
    canValidateAccount: bool
    canResellItemAfterPurchase: bool
    tarkovRegionPhrase: str
    tarkovGameVersionPhrase: str
    tarkovSecuredContainer: str
    tarkovKd: int
    accountDomain: str
    canViewAccountLink: bool
    emailLoginUrl: str
    canChangePassword: bool
    itemOriginPhrase: str
    sold_items_category_count: int
    restore_items_category_count: int
    tags: list[object]
    note_text: object
    hasPendingAutoBuy: bool
    descriptionHtml: str
    descriptionEnHtml: str
    descriptionPlain: str
    descriptionEnPlain: str
    seller: CategoryEscapefromtarkovResponseItemsSeller


class CategoryEscapefromtarkovResponse(TypedDict):
    items: list[CategoryEscapefromtarkovResponseItems]
    totalItems: int
    totalItemsPrice: object
    hasNextPage: bool
    perPage: int
    page: int
    wasCached: bool
    cacheTTL: int
    lastModified: int
    serverTime: int
    searchUrl: str
    stickyItems: list[object]
    system_info: Resp_SystemInfo


CategorySocialclubParams = TypedDict(
    "CategorySocialclubParams",
    {
        "page": int,
        "pmin": int,
        "pmax": int,
        "title": str,
        "order_by": Literal[
            "price_to_up",
            "price_to_down",
            "pdate_to_down",
            "pdate_to_up",
            "pdate_to_down_upload",
            "pdate_to_up_upload",
            "edate_to_up",
            "edate_to_down",
            "ddate_to_up",
            "ddate_to_down",
        ],
        "tag_id[]": list[int],
        "not_tag_id[]": list[int],
        "public_tag_id[]": list[int],
        "not_public_tag_id[]": list[int],
        "origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "not_origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "user_id": int,
        "nsb": bool,
        "sb": bool,
        "nsb_by_me": bool,
        "sb_by_me": bool,
        "currency": Literal[
            "rub", "uah", "kzt", "byn", "usd", "eur", "gbp", "cny", "try", "jpy", "brl"
        ],
        "email_login_data": bool,
        "email_provider[]": list[
            Literal["other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"]
        ],
        "not_email_provider[]": Literal[
            "other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"
        ],
        "parse_same_item_ids": bool,
        "daybreak": int,
        "level_min": int,
        "level_max": int,
        "cash_min": int,
        "cash_max": int,
        "bank_cash_min": int,
        "bank_cash_max": int,
        "game[]": list[str],
    },
    total=False,
)


class CategorySocialclubResponseItemsSocialclub_games(TypedDict):
    id: int
    name: str
    defaultPlatform: str
    platform: str
    lastSeen: str
    internal_game_id: int
    app_id: str
    title: str
    abbr: str
    category_id: int
    img: str
    url: str
    ru: object


class CategorySocialclubResponseItemsBumpSettings(TypedDict):
    canBumpItem: bool
    canBumpItemGlobally: bool
    shortErrorPhrase: object
    errorPhrase: object


class CategorySocialclubResponseItemsSeller(TypedDict):
    user_id: int
    sold_items_count: int
    active_items_count: int
    restore_data: str
    username: str
    avatar_date: int
    is_banned: int
    display_style_group_id: int
    restore_percents: object


class CategorySocialclubResponseItems(TypedDict):
    item_id: int
    item_state: str
    category_id: int
    published_date: int
    title: str
    description: str
    price: int
    update_stat_date: int
    refreshed_date: int
    edit_date: int
    view_count: int
    is_sticky: int
    item_origin: str
    extended_guarantee: int
    nsb: int
    allow_ask_discount: int
    title_en: str
    description_en: str
    email_type: str
    email_provider: str
    item_domain: str
    resale_item_origin: str
    socialclub_item_id: int
    socialclub_level: int
    socialclub_cash: int
    socialclub_bank_cash: int
    socialclub_games: list[CategorySocialclubResponseItemsSocialclub_games]
    socialclub_last_activity: int
    socialclub_has_gtav: int
    socialclub_has_rdr2: int
    feedback_data: str
    isIgnored: bool
    priceWithSellerFee: int
    guarantee: object
    canViewLoginData: bool
    canUpdateItemStats: bool
    canReportItem: bool
    canViewEmailLoginData: bool
    showGetEmailCodeButton: bool
    canOpenItem: bool
    canCloseItem: bool
    canEditItem: bool
    canDeleteItem: bool
    canStickItem: bool
    canUnstickItem: bool
    bumpSettings: CategorySocialclubResponseItemsBumpSettings
    canBumpItem: bool
    canBuyItem: bool
    rub_price: int
    price_currency: str
    canValidateAccount: bool
    canResellItemAfterPurchase: bool
    isSmallExf: bool
    account_last_activity: int
    canViewAccountLink: bool
    accountLinks: list[object]
    emailLoginUrl: str
    canChangePassword: bool
    itemOriginPhrase: str
    tags: list[object]
    note_text: object
    hasPendingAutoBuy: bool
    descriptionHtml: str
    descriptionEnHtml: str
    descriptionPlain: str
    descriptionEnPlain: str
    seller: CategorySocialclubResponseItemsSeller


class CategorySocialclubResponse(TypedDict):
    items: list[CategorySocialclubResponseItems]
    totalItems: int
    totalItemsPrice: object
    hasNextPage: bool
    perPage: int
    page: int
    wasCached: bool
    cacheTTL: int
    lastModified: int
    serverTime: int
    searchUrl: str
    stickyItems: list[object]
    system_info: Resp_SystemInfo


CategoryUplayParams = TypedDict(
    "CategoryUplayParams",
    {
        "page": int,
        "pmin": int,
        "pmax": int,
        "title": str,
        "order_by": Literal[
            "price_to_up",
            "price_to_down",
            "pdate_to_down",
            "pdate_to_up",
            "pdate_to_down_upload",
            "pdate_to_up_upload",
            "edate_to_up",
            "edate_to_down",
            "ddate_to_up",
            "ddate_to_down",
        ],
        "tag_id[]": list[int],
        "not_tag_id[]": list[int],
        "public_tag_id[]": list[int],
        "not_public_tag_id[]": list[int],
        "origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "not_origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "user_id": int,
        "nsb": bool,
        "sb": bool,
        "nsb_by_me": bool,
        "sb_by_me": bool,
        "currency": Literal[
            "rub", "uah", "kzt", "byn", "usd", "eur", "gbp", "cny", "try", "jpy", "brl"
        ],
        "email_login_data": bool,
        "email_provider[]": list[
            Literal["other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"]
        ],
        "not_email_provider[]": Literal[
            "other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"
        ],
        "parse_same_item_ids": bool,
        "email_type[]": list[Literal["autoreg", "native", "no"]],
        "item_domain": str,
        "game[]": list[str],
        "country[]": list[str],
        "not_country[]": list[str],
        "daybreak": int,
        "gmin": int,
        "gmax": int,
        "subscription": Literal["basic", "premium", "premiumAnywhere"],
        "subscription_length": int,
        "subscription_period": Literal["day", "month", "year"],
        "r6_level_min": int,
        "r6_level_max": int,
        "r6_rank_min": int,
        "r6_rank_max": int,
        "r6_operators_min": int,
        "r6_operators_max": int,
        "r6_ban": YesNoNoMatterScheme,
        "r6_smin": int,
        "r6_smax": int,
        "r6_skin[]": list[str],
        "r6_operator[]": list[str],
        "xbox_connected": YesNoNoMatterScheme,
        "psn_connected": YesNoNoMatterScheme,
        "steam_connected": YesNoNoMatterScheme,
        "balance_min": float,
        "balance_max": float,
        "transactions": YesNoNoMatterScheme,
        "reg": int,
        "reg_period": Literal["day", "month", "year"],
    },
    total=False,
)


class CategoryUplayResponseItemsUplay_gamesFfffffffFfffFfffFfffFfffffffffff(TypedDict):
    title: str
    img: str
    pvpTimePlayed: int
    pveTimePlayed: int
    abbr: str
    gameId: str


CategoryUplayResponseItemsUplay_games = TypedDict(
    "CategoryUplayResponseItemsUplay_games",
    {
        "ffffffff-ffff-ffff-ffff-ffffffffffff": CategoryUplayResponseItemsUplay_gamesFfffffffFfffFfffFfffFfffffffffff,
    },
)


class CategoryUplayResponseItemsBumpSettings(TypedDict):
    canBumpItem: bool
    canBumpItemGlobally: bool
    shortErrorPhrase: object
    errorPhrase: object


class CategoryUplayResponseItemsR6Operators(TypedDict):
    img: str
    name: str
    url: str


class CategoryUplayResponseItemsSeller(TypedDict):
    user_id: int
    sold_items_count: int
    active_items_count: int
    restore_data: str
    username: str
    avatar_date: int
    is_banned: int
    display_style_group_id: int
    restore_percents: int


class CategoryUplayResponseItems(TypedDict):
    item_id: int
    item_state: str
    category_id: int
    published_date: int
    title: str
    description: str
    price: int
    update_stat_date: int
    refreshed_date: int
    edit_date: int
    view_count: int
    is_sticky: int
    item_origin: str
    extended_guarantee: int
    nsb: int
    allow_ask_discount: int
    title_en: str
    description_en: str
    email_type: str
    email_provider: str
    item_domain: str
    resale_item_origin: str
    uplay_item_id: int
    uplay_last_activity: int
    uplay_country: str
    uplay_created_date: int
    uplay_games: CategoryUplayResponseItemsUplay_games
    uplay_game_count: int
    uplay_r6_level: int
    uplay_r6_ban: int
    uplay_r6_operators: str
    uplay_r6_operators_count: int
    uplay_r6_skins: str
    uplay_r6_skins_count: int
    uplay_subscription: str
    uplay_subscription_end_date: int
    uplay_xbox_connected: int
    uplay_psn_connected: int
    uplay_steam_connected: int
    uplay_r6_rank: int
    feedback_data: str
    isIgnored: bool
    priceWithSellerFee: int
    guarantee: object
    canViewLoginData: bool
    canUpdateItemStats: bool
    canReportItem: bool
    canViewEmailLoginData: bool
    showGetEmailCodeButton: bool
    canOpenItem: bool
    canCloseItem: bool
    canEditItem: bool
    canDeleteItem: bool
    canStickItem: bool
    canUnstickItem: bool
    bumpSettings: CategoryUplayResponseItemsBumpSettings
    canBumpItem: bool
    canBuyItem: bool
    rub_price: int
    price_currency: str
    canValidateAccount: bool
    canResellItemAfterPurchase: bool
    uplayLinkedAccounts: str
    uplayR6Rank: str
    uplay_r6_steam_warning: bool
    uplay_r6_external_warning: bool
    uplay_r6: bool
    uplay_r6_ban_active: bool
    isSmallExf: bool
    account_last_activity: int
    r6Skins: list[object]
    r6Operators: list[CategoryUplayResponseItemsR6Operators]
    canViewAccountLink: bool
    emailLoginUrl: str
    canChangePassword: bool
    itemOriginPhrase: str
    sold_items_category_count: int
    restore_items_category_count: int
    tags: list[object]
    note_text: object
    hasPendingAutoBuy: bool
    descriptionHtml: str
    descriptionEnHtml: str
    descriptionPlain: str
    descriptionEnPlain: str
    seller: CategoryUplayResponseItemsSeller


class CategoryUplayResponse(TypedDict):
    items: list[CategoryUplayResponseItems]
    totalItems: int
    totalItemsPrice: object
    hasNextPage: bool
    perPage: int
    page: int
    wasCached: bool
    cacheTTL: int
    lastModified: int
    serverTime: int
    searchUrl: str
    stickyItems: list[object]
    system_info: Resp_SystemInfo


CategoryDiscordParams = TypedDict(
    "CategoryDiscordParams",
    {
        "page": int,
        "pmin": int,
        "pmax": int,
        "title": str,
        "order_by": Literal[
            "price_to_up",
            "price_to_down",
            "pdate_to_down",
            "pdate_to_up",
            "pdate_to_down_upload",
            "pdate_to_up_upload",
            "edate_to_up",
            "edate_to_down",
            "ddate_to_up",
            "ddate_to_down",
        ],
        "tag_id[]": list[int],
        "not_tag_id[]": list[int],
        "public_tag_id[]": list[int],
        "not_public_tag_id[]": list[int],
        "origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "not_origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "user_id": int,
        "nsb": bool,
        "sb": bool,
        "nsb_by_me": bool,
        "sb_by_me": bool,
        "currency": Literal[
            "rub", "uah", "kzt", "byn", "usd", "eur", "gbp", "cny", "try", "jpy", "brl"
        ],
        "email_login_data": bool,
        "email_provider[]": list[
            Literal["other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"]
        ],
        "not_email_provider[]": Literal[
            "other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"
        ],
        "parse_same_item_ids": bool,
        "email_type[]": list[Literal["autoreg", "native", "no"]],
        "item_domain": str,
        "tel": Literal["yes", "no", "nomatter"],
        "nitro": YesNoNoMatterScheme,
        "nitro_type[]": list[Literal["basic", "classic", "full", "none", "trial"]],
        "nitro_length": int,
        "nitro_period": Literal["day", "month", "year"],
        "boosts_min": int,
        "boosts_max": int,
        "billing": YesNoNoMatterScheme,
        "gifts": YesNoNoMatterScheme,
        "transactions": YesNoNoMatterScheme,
        "badge[]": list[
            Literal[
                "bug_hunter",
                "bug_hunter_level_2",
                "certificated_moderator",
                "early_supporter",
                "hypesquad",
                "partner",
                "staff",
                "verified_developer",
            ]
        ],
        "condition[]": list[Literal["cleaned", "empty", "nospam", "spam"]],
        "chat_min": int,
        "chat_max": int,
        "min_admin_members": int,
        "max_admin_members": int,
        "min_admin": int,
        "max_admin": int,
        "reg": int,
        "reg_period": Literal["day", "month", "year"],
        "language[]": list[str],
        "not_language[]": list[str],
        "clans": YesNoNoMatterScheme,
        "min_admin_clans": int,
        "max_admin_clans": int,
        "min_owner_clans": int,
        "max_owner_clans": int,
        "country[]": list[str],
        "not_country[]": list[str],
        "min_servers": int,
        "max_servers": int,
        "2fa": YesNoNoMatterScheme,
        "min_full_credits": int,
        "max_full_credits": int,
        "min_basic_credits": int,
        "max_basic_credits": int,
        "min_orbs": int,
        "max_orbs": int,
    },
    total=False,
)


class CategoryDiscordResponseItemsBumpSettings(TypedDict):
    canBumpItem: bool
    canBumpItemGlobally: bool
    shortErrorPhrase: object
    errorPhrase: object


class CategoryDiscordResponseItemsSeller(TypedDict):
    user_id: int
    sold_items_count: int
    active_items_count: int
    restore_data: str
    username: str
    avatar_date: int
    is_banned: int
    display_style_group_id: int
    restore_percents: object


class CategoryDiscordResponseItems(TypedDict):
    item_id: int
    item_state: str
    category_id: int
    published_date: int
    title: str
    description: str
    price: int
    update_stat_date: int
    refreshed_date: int
    edit_date: int
    view_count: int
    is_sticky: int
    item_origin: str
    extended_guarantee: int
    nsb: int
    allow_ask_discount: int
    title_en: str
    description_en: str
    email_type: str
    email_provider: str
    item_domain: str
    resale_item_origin: str
    discord_item_id: int
    discord_chat_count: int
    discord_verified: int
    discord_condition: str
    discord_gifts: int
    discord_billing: int
    discord_register_date: int
    discord_locale: str
    discord_nitro_end_date: int
    discord_available_boosts: int
    discord_nitro_type: int
    discord_admin_members_count: int
    discord_admin_servers_count: int
    discord_admin_servers: str
    feedback_data: str
    isIgnored: bool
    priceWithSellerFee: int
    guarantee: object
    canViewLoginData: bool
    canUpdateItemStats: bool
    canReportItem: bool
    canViewEmailLoginData: bool
    showGetEmailCodeButton: bool
    canOpenItem: bool
    canCloseItem: bool
    canEditItem: bool
    canDeleteItem: bool
    canStickItem: bool
    canUnstickItem: bool
    bumpSettings: CategoryDiscordResponseItemsBumpSettings
    canBumpItem: bool
    canBuyItem: bool
    rub_price: int
    price_currency: str
    canValidateAccount: bool
    canResellItemAfterPurchase: bool
    discordAccountConditionLabel: str
    discordLocaleTitle: str
    discordNitroType: str
    canViewAccountLink: bool
    emailLoginUrl: str
    canChangePassword: bool
    itemOriginPhrase: str
    tags: list[object]
    note_text: object
    hasPendingAutoBuy: bool
    descriptionHtml: str
    descriptionEnHtml: str
    descriptionPlain: str
    descriptionEnPlain: str
    seller: CategoryDiscordResponseItemsSeller


class CategoryDiscordResponse(TypedDict):
    items: list[CategoryDiscordResponseItems]
    totalItems: int
    totalItemsPrice: object
    hasNextPage: bool
    perPage: int
    page: int
    wasCached: bool
    cacheTTL: int
    lastModified: int
    serverTime: int
    searchUrl: str
    stickyItems: list[object]
    system_info: Resp_SystemInfo


CategoryTiktokParams = TypedDict(
    "CategoryTiktokParams",
    {
        "page": int,
        "pmin": int,
        "pmax": int,
        "title": str,
        "order_by": Literal[
            "price_to_up",
            "price_to_down",
            "pdate_to_down",
            "pdate_to_up",
            "pdate_to_down_upload",
            "pdate_to_up_upload",
            "edate_to_up",
            "edate_to_down",
            "ddate_to_up",
            "ddate_to_down",
        ],
        "tag_id[]": list[int],
        "not_tag_id[]": list[int],
        "public_tag_id[]": list[int],
        "not_public_tag_id[]": list[int],
        "origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "not_origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "user_id": int,
        "nsb": bool,
        "sb": bool,
        "nsb_by_me": bool,
        "sb_by_me": bool,
        "currency": Literal[
            "rub", "uah", "kzt", "byn", "usd", "eur", "gbp", "cny", "try", "jpy", "brl"
        ],
        "email_login_data": bool,
        "email_provider[]": list[
            Literal["other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"]
        ],
        "not_email_provider[]": Literal[
            "other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"
        ],
        "parse_same_item_ids": bool,
        "email_type[]": list[Literal["autoreg", "native", "no"]],
        "item_domain": str,
        "tel": Literal["yes", "no", "nomatter"],
        "reg": int,
        "reg_period": Literal["day", "month", "year"],
        "followers_min": int,
        "followers_max": int,
        "post_min": int,
        "post_max": int,
        "like_min": int,
        "like_max": int,
        "coins_min": int,
        "coins_max": int,
        "cookie_login": YesNoNoMatterScheme,
        "verified": Literal["yes", "no", "nomatter"],
        "email": Literal["yes", "no", "nomatter"],
    },
    total=False,
)


class CategoryTiktokResponseItemsBumpSettings(TypedDict):
    canBumpItem: bool
    canBumpItemGlobally: bool
    shortErrorPhrase: object
    errorPhrase: object


class CategoryTiktokResponseItemsAccountLinks(TypedDict):
    link: str
    text: str
    iconClass: str


class CategoryTiktokResponseItemsSeller(TypedDict):
    user_id: int
    sold_items_count: int
    active_items_count: int
    restore_data: str
    username: str
    avatar_date: int
    is_banned: int
    display_style_group_id: int
    restore_percents: int


class CategoryTiktokResponseItems(TypedDict):
    item_id: int
    item_state: str
    category_id: int
    published_date: int
    title: str
    description: str
    price: int
    update_stat_date: int
    refreshed_date: int
    edit_date: int
    view_count: int
    is_sticky: int
    item_origin: str
    extended_guarantee: int
    nsb: int
    allow_ask_discount: int
    title_en: str
    description_en: str
    email_type: str
    email_provider: object
    item_domain: str
    resale_item_origin: str
    tt_item_id: int
    tt_id: int
    tt_permalink: str
    tt_uniqueId: str
    tt_verified: int
    tt_createTime: int
    tt_privateAccount: int
    tt_followers: int
    tt_following: int
    tt_likes: int
    tt_videos: int
    tt_screen_name: str
    tt_hasEmail: int
    tt_hasMobile: int
    tt_top_country: str
    tt_countries: str
    tt_coins: int
    tt_hasLivePermission: int
    tt_cookie_login: int
    feedback_data: str
    isIgnored: bool
    priceWithSellerFee: int
    guarantee: object
    canViewLoginData: bool
    canUpdateItemStats: bool
    canReportItem: bool
    canViewEmailLoginData: bool
    showGetEmailCodeButton: bool
    canOpenItem: bool
    canCloseItem: bool
    canEditItem: bool
    canDeleteItem: bool
    canStickItem: bool
    canUnstickItem: bool
    bumpSettings: CategoryTiktokResponseItemsBumpSettings
    canBumpItem: bool
    canBuyItem: bool
    rub_price: int
    price_currency: str
    canValidateAccount: bool
    canResellItemAfterPurchase: bool
    canViewAccountLink: bool
    accountLinks: list[CategoryTiktokResponseItemsAccountLinks]
    accountLink: str
    canChangePassword: bool
    itemOriginPhrase: str
    sold_items_category_count: int
    restore_items_category_count: int
    tags: list[object]
    note_text: object
    hasPendingAutoBuy: bool
    descriptionHtml: str
    descriptionEnHtml: str
    descriptionPlain: str
    descriptionEnPlain: str
    seller: CategoryTiktokResponseItemsSeller


class CategoryTiktokResponse(TypedDict):
    items: list[CategoryTiktokResponseItems]
    totalItems: int
    totalItemsPrice: object
    hasNextPage: bool
    perPage: int
    page: int
    wasCached: bool
    cacheTTL: int
    lastModified: int
    serverTime: int
    searchUrl: str
    stickyItems: list[object]
    system_info: Resp_SystemInfo


CategoryInstagramParams = TypedDict(
    "CategoryInstagramParams",
    {
        "page": int,
        "pmin": int,
        "pmax": int,
        "title": str,
        "order_by": Literal[
            "price_to_up",
            "price_to_down",
            "pdate_to_down",
            "pdate_to_up",
            "pdate_to_down_upload",
            "pdate_to_up_upload",
            "edate_to_up",
            "edate_to_down",
            "ddate_to_up",
            "ddate_to_down",
        ],
        "tag_id[]": list[int],
        "not_tag_id[]": list[int],
        "public_tag_id[]": list[int],
        "not_public_tag_id[]": list[int],
        "origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "not_origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "user_id": int,
        "nsb": bool,
        "sb": bool,
        "nsb_by_me": bool,
        "sb_by_me": bool,
        "currency": Literal[
            "rub", "uah", "kzt", "byn", "usd", "eur", "gbp", "cny", "try", "jpy", "brl"
        ],
        "email_login_data": bool,
        "email_provider[]": list[
            Literal["other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"]
        ],
        "not_email_provider[]": Literal[
            "other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"
        ],
        "parse_same_item_ids": bool,
        "email_type[]": list[Literal["autoreg", "native", "no"]],
        "item_domain": str,
        "tel": Literal["yes", "no", "nomatter"],
        "country[]": list[str],
        "not_country[]": list[str],
        "cookies": Literal["yes", "no", "nomatter"],
        "login_without_cookies": YesNoNoMatterScheme,
        "followers_min": int,
        "followers_max": int,
        "post_min": int,
        "post_max": int,
        "reg": int,
        "reg_period": Literal["day", "month", "year"],
    },
    total=False,
)


class CategoryInstagramResponseItemsBumpSettings(TypedDict):
    canBumpItem: bool
    canBumpItemGlobally: bool
    shortErrorPhrase: object
    errorPhrase: object


class CategoryInstagramResponseItemsAccountLinks(TypedDict):
    link: str
    text: str
    iconClass: str


class CategoryInstagramResponseItemsSeller(TypedDict):
    user_id: int
    sold_items_count: int
    active_items_count: int
    restore_data: str
    username: str
    avatar_date: int
    is_banned: int
    display_style_group_id: int
    restore_percents: object


class CategoryInstagramResponseItems(TypedDict):
    item_id: int
    item_state: str
    category_id: int
    published_date: int
    title: str
    description: str
    price: int
    update_stat_date: int
    refreshed_date: int
    edit_date: int
    view_count: int
    is_sticky: int
    item_origin: str
    extended_guarantee: int
    nsb: int
    allow_ask_discount: int
    title_en: str
    description_en: str
    email_type: str
    email_provider: str
    item_domain: str
    resale_item_origin: str
    instagram_item_id: int
    instagram_id: str
    instagram_follower_count: int
    instagram_follow_count: int
    instagram_post_count: int
    instagram_country: str
    instagram_username: str
    instagram_mobile: int
    instagram_register_date: int
    instagram_has_cookies: int
    instagram_login_without_cookies: int
    feedback_data: str
    isIgnored: bool
    priceWithSellerFee: int
    guarantee: object
    canViewLoginData: bool
    canUpdateItemStats: bool
    canReportItem: bool
    canViewEmailLoginData: bool
    showGetEmailCodeButton: bool
    canOpenItem: bool
    canCloseItem: bool
    canEditItem: bool
    canDeleteItem: bool
    canStickItem: bool
    canUnstickItem: bool
    bumpSettings: CategoryInstagramResponseItemsBumpSettings
    canBumpItem: bool
    canBuyItem: bool
    rub_price: int
    price_currency: str
    canValidateAccount: bool
    canResellItemAfterPurchase: bool
    canViewAccountLink: bool
    accountLinks: list[CategoryInstagramResponseItemsAccountLinks]
    accountLink: str
    emailLoginUrl: str
    canChangePassword: bool
    itemOriginPhrase: str
    tags: list[object]
    note_text: object
    hasPendingAutoBuy: bool
    descriptionHtml: str
    descriptionEnHtml: str
    descriptionPlain: str
    descriptionEnPlain: str
    seller: CategoryInstagramResponseItemsSeller


class CategoryInstagramResponse(TypedDict):
    items: list[CategoryInstagramResponseItems]
    totalItems: int
    totalItemsPrice: object
    hasNextPage: bool
    perPage: int
    page: int
    wasCached: bool
    cacheTTL: int
    lastModified: int
    serverTime: int
    searchUrl: str
    stickyItems: list[object]
    system_info: Resp_SystemInfo


CategoryBattlenetParams = TypedDict(
    "CategoryBattlenetParams",
    {
        "page": int,
        "pmin": int,
        "pmax": int,
        "title": str,
        "order_by": Literal[
            "price_to_up",
            "price_to_down",
            "pdate_to_down",
            "pdate_to_up",
            "pdate_to_down_upload",
            "pdate_to_up_upload",
            "edate_to_up",
            "edate_to_down",
            "ddate_to_up",
            "ddate_to_down",
        ],
        "tag_id[]": list[int],
        "not_tag_id[]": list[int],
        "public_tag_id[]": list[int],
        "not_public_tag_id[]": list[int],
        "origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "not_origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "user_id": int,
        "nsb": bool,
        "sb": bool,
        "nsb_by_me": bool,
        "sb_by_me": bool,
        "currency": Literal[
            "rub", "uah", "kzt", "byn", "usd", "eur", "gbp", "cny", "try", "jpy", "brl"
        ],
        "email_login_data": bool,
        "email_provider[]": list[
            Literal["other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"]
        ],
        "not_email_provider[]": Literal[
            "other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"
        ],
        "parse_same_item_ids": bool,
        "email_type[]": list[Literal["native", "no"]],
        "item_domain": str,
        "eg": Literal[0, 1],
        "game[]": list[int],
        "daybreak": int,
        "country[]": list[str],
        "not_country[]": list[str],
        "tel": Literal["yes", "no", "nomatter"],
        "edit_btag": YesNoNoMatterScheme,
        "changeable_fn": YesNoNoMatterScheme,
        "real_id": YesNoNoMatterScheme,
        "parent_control": YesNoNoMatterScheme,
        "no_bans": YesNoNoMatterScheme,
        "balance_min": int,
        "balance_max": int,
    },
    total=False,
)


CategoryBattlenetResponseItemsGuarantee = TypedDict(
    "CategoryBattlenetResponseItemsGuarantee",
    {
        "duration": int,
        "class": str,
        "durationPhrase": str,
        "endDate": object,
        "active": object,
        "cancelled": object,
        "remainingTime": object,
    },
)


class CategoryBattlenetResponseItemsBumpSettings(TypedDict):
    canBumpItem: bool
    canBumpItemGlobally: bool
    shortErrorPhrase: object
    errorPhrase: object


class CategoryBattlenetResponseItemsBattlenetGames17459(TypedDict):
    internal_game_id: int
    app_id: str
    title: str
    abbr: str
    category_id: int
    img: str
    url: str
    ru: object


CategoryBattlenetResponseItemsBattlenetGames = TypedDict(
    "CategoryBattlenetResponseItemsBattlenetGames",
    {
        "17459": CategoryBattlenetResponseItemsBattlenetGames17459,
    },
)


class CategoryBattlenetResponseItemsBattlenetTransactions(TypedDict):
    date: int
    productTitle: str
    formattedTotal: str
    total: str


class CategoryBattlenetResponseItemsSeller(TypedDict):
    user_id: int
    sold_items_count: int
    active_items_count: int
    restore_data: str
    username: str
    avatar_date: int
    is_banned: int
    display_style_group_id: int
    restore_percents: int


class CategoryBattlenetResponseItems(TypedDict):
    item_id: int
    item_state: str
    category_id: int
    published_date: int
    title: str
    description: str
    price: int
    update_stat_date: int
    refreshed_date: int
    edit_date: int
    view_count: int
    is_sticky: int
    item_origin: str
    extended_guarantee: int
    nsb: int
    allow_ask_discount: int
    title_en: str
    description_en: str
    email_type: str
    email_provider: str
    item_domain: str
    resale_item_origin: str
    battlenet_item_id: int
    battlenet_balance: str
    battlenet_country: str
    battlenet_last_activity: int
    battlenet_mobile: int
    battlenet_bans: str
    battlenet_can_change_tag: int
    battlenet_real_id_enabled: int
    battlenet_change_full_name: int
    battlenet_parent_control: int
    battlenet_converted_balance: int
    feedback_data: str
    isIgnored: bool
    priceWithSellerFee: int
    guarantee: CategoryBattlenetResponseItemsGuarantee
    canViewLoginData: bool
    canUpdateItemStats: bool
    canReportItem: bool
    canViewEmailLoginData: bool
    showGetEmailCodeButton: bool
    canOpenItem: bool
    canCloseItem: bool
    canEditItem: bool
    canDeleteItem: bool
    canStickItem: bool
    canUnstickItem: bool
    bumpSettings: CategoryBattlenetResponseItemsBumpSettings
    canBumpItem: bool
    canBuyItem: bool
    rub_price: int
    price_currency: str
    canValidateAccount: bool
    canResellItemAfterPurchase: bool
    isSmallExf: bool
    account_last_activity: int
    battlenetBans: str
    battlenetGames: CategoryBattlenetResponseItemsBattlenetGames
    hasOverwatch: bool
    battlenetTransactions: list[CategoryBattlenetResponseItemsBattlenetTransactions]
    displayConvertedBalance: bool
    canViewAccountLink: bool
    accountLinks: list[object]
    emailLoginUrl: str
    canChangePassword: bool
    itemOriginPhrase: str
    sold_items_category_count: int
    restore_items_category_count: int
    tags: list[object]
    note_text: object
    hasPendingAutoBuy: bool
    descriptionHtml: str
    descriptionEnHtml: str
    descriptionPlain: str
    descriptionEnPlain: str
    seller: CategoryBattlenetResponseItemsSeller


class CategoryBattlenetResponse(TypedDict):
    items: list[CategoryBattlenetResponseItems]
    totalItems: int
    totalItemsPrice: object
    hasNextPage: bool
    perPage: int
    page: int
    wasCached: bool
    cacheTTL: int
    lastModified: int
    serverTime: int
    searchUrl: str
    stickyItems: list[object]
    system_info: Resp_SystemInfo


CategoryChatgptParams = TypedDict(
    "CategoryChatgptParams",
    {
        "page": int,
        "pmin": int,
        "pmax": int,
        "title": str,
        "order_by": Literal[
            "price_to_up",
            "price_to_down",
            "pdate_to_down",
            "pdate_to_up",
            "pdate_to_down_upload",
            "pdate_to_up_upload",
            "edate_to_up",
            "edate_to_down",
            "ddate_to_up",
            "ddate_to_down",
        ],
        "tag_id[]": list[int],
        "not_tag_id[]": list[int],
        "public_tag_id[]": list[int],
        "not_public_tag_id[]": list[int],
        "origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "not_origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "user_id": int,
        "nsb": bool,
        "sb": bool,
        "nsb_by_me": bool,
        "sb_by_me": bool,
        "currency": Literal[
            "rub", "uah", "kzt", "byn", "usd", "eur", "gbp", "cny", "try", "jpy", "brl"
        ],
        "email_login_data": bool,
        "email_provider[]": list[
            Literal["other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"]
        ],
        "not_email_provider[]": Literal[
            "other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"
        ],
        "parse_same_item_ids": bool,
        "email_type[]": list[Literal["native", "no"]],
        "item_domain": str,
        "subscription[]": list[
            Literal[
                "chatgptplusplan",
                "chatgptpro",
                "chatgptenterpriseplan",
                "chatgptteamplan",
                "chatgpteduplan",
                "chatgptquorumplan",
            ]
        ],
        "subscription_length": int,
        "subscription_period": Literal["day", "month", "year"],
        "autorenewal": Literal["yes", "no", "nomatter"],
        "tel": Literal["yes", "no", "nomatter"],
        "transactions": YesNoNoMatterScheme,
        "reg": int,
        "reg_period": Literal["day", "month", "year"],
        "openai_tier[]": list[Literal["tier1", "tier2", "tier3", "tier4", "tier5"]],
        "openai_balance_min": int,
        "openai_balance_max": int,
    },
    total=False,
)


class CategoryChatgptResponseItemsCopyFormatData(TypedDict):
    title_link: str


class CategoryChatgptResponseItemsBumpSettings(TypedDict):
    canBumpItem: bool
    canBumpItemGlobally: bool
    shortErrorPhrase: object
    errorPhrase: object


class CategoryChatgptResponseItemsSeller(TypedDict):
    user_id: int
    sold_items_count: int
    active_items_count: int
    restore_data: str
    username: str
    avatar_date: int
    is_banned: int
    display_style_group_id: int
    restore_percents: object


class CategoryChatgptResponseItems(TypedDict):
    item_id: int
    item_state: str
    category_id: int
    published_date: int
    title: str
    description: str
    price: int
    update_stat_date: int
    refreshed_date: int
    edit_date: int
    view_count: int
    is_sticky: int
    item_origin: str
    extended_guarantee: int
    nsb: int
    allow_ask_discount: int
    title_en: str
    description_en: str
    email_type: str
    email_provider: str
    item_domain: str
    resale_item_origin: str
    chatgpt_item_id: int
    chatgpt_country: str
    chatgpt_register_date: int
    chatgpt_phone: int
    chatgpt_subscription: str
    chatgpt_subscription_ends: int
    chatgpt_subscription_auto_renew: int
    feedback_data: str
    isIgnored: bool
    priceWithSellerFee: float
    guarantee: object
    canViewLoginData: bool
    canUpdateItemStats: bool
    canReportItem: bool
    canViewItemViews: bool
    canViewEmailLoginData: bool
    copyFormatData: CategoryChatgptResponseItemsCopyFormatData
    showGetEmailCodeButton: bool
    canOpenItem: bool
    canCloseItem: bool
    canEditItem: bool
    canDeleteItem: bool
    canStickItem: bool
    canUnstickItem: bool
    bumpSettings: CategoryChatgptResponseItemsBumpSettings
    isPersonalAccount: bool
    canBumpItem: bool
    canBuyItem: bool
    rub_price: int
    price_currency: str
    priceWithSellerFeeLabel: str
    canValidateAccount: bool
    canResellItemAfterPurchase: bool
    gptSubType: str
    canViewAccountLink: bool
    emailLoginUrl: str
    canChangePassword: bool
    canChangeEmailPassword: bool
    uniqueKeyExists: bool
    itemOriginPhrase: str
    tags: list[object]
    note_text: object
    hasPendingAutoBuy: bool
    descriptionHtml: str
    descriptionEnHtml: str
    descriptionPlain: str
    descriptionEnPlain: str
    seller: CategoryChatgptResponseItemsSeller


class CategoryChatgptResponse(TypedDict):
    items: list[CategoryChatgptResponseItems]
    totalItems: int
    totalItemsPrice: object
    hasNextPage: bool
    perPage: int
    page: int
    wasCached: bool
    cacheTTL: int
    lastModified: int
    serverTime: int
    searchUrl: str
    stickyItems: list[object]
    system_info: Resp_SystemInfo


CategoryVpnParams = TypedDict(
    "CategoryVpnParams",
    {
        "page": int,
        "pmin": int,
        "pmax": int,
        "title": str,
        "order_by": Literal[
            "price_to_up",
            "price_to_down",
            "pdate_to_down",
            "pdate_to_up",
            "pdate_to_down_upload",
            "pdate_to_up_upload",
            "edate_to_up",
            "edate_to_down",
            "ddate_to_up",
            "ddate_to_down",
        ],
        "tag_id[]": list[int],
        "not_tag_id[]": list[int],
        "public_tag_id[]": list[int],
        "not_public_tag_id[]": list[int],
        "origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "not_origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "user_id": int,
        "nsb": bool,
        "sb": bool,
        "nsb_by_me": bool,
        "sb_by_me": bool,
        "currency": Literal[
            "rub", "uah", "kzt", "byn", "usd", "eur", "gbp", "cny", "try", "jpy", "brl"
        ],
        "email_login_data": bool,
        "email_provider[]": list[
            Literal["other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"]
        ],
        "not_email_provider[]": Literal[
            "other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"
        ],
        "parse_same_item_ids": bool,
        "service[]": list[
            Literal[
                "AdguardVPN",
                "PIAVPN",
                "cyberghostVPN",
                "hotspotShieldVPN",
                "mullvadVPN",
                "planetVPN",
                "pureVPN",
                "tunnelbearVPN",
                "ultraVPN",
                "vanishVPN",
                "vyprVPN",
                "windscribeVPN",
            ]
        ],
        "subscription_length": int,
        "subscription_period": Literal["day", "month", "year"],
        "autorenewal": Literal["yes", "no", "nomatter"],
    },
    total=False,
)


class CategoryVpnResponseItemsBumpSettings(TypedDict):
    canBumpItem: bool
    canBumpItemGlobally: bool
    shortErrorPhrase: object
    errorPhrase: object


class CategoryVpnResponseItemsSeller(TypedDict):
    user_id: int
    sold_items_count: int
    active_items_count: int
    restore_data: str
    username: str
    avatar_date: int
    is_banned: int
    display_style_group_id: int
    restore_percents: int


class CategoryVpnResponseItems(TypedDict):
    item_id: int
    item_state: str
    category_id: int
    published_date: int
    title: str
    description: str
    price: int
    update_stat_date: int
    refreshed_date: int
    edit_date: int
    view_count: int
    is_sticky: int
    item_origin: str
    extended_guarantee: int
    nsb: int
    allow_ask_discount: int
    title_en: str
    description_en: str
    email_type: str
    email_provider: object
    item_domain: str
    resale_item_origin: str
    vpn_item_id: int
    vpn_service: str
    vpn_expire_date: int
    vpn_renewable: int
    feedback_data: str
    isIgnored: bool
    priceWithSellerFee: int
    guarantee: object
    canViewLoginData: bool
    canUpdateItemStats: bool
    canReportItem: bool
    canViewEmailLoginData: bool
    showGetEmailCodeButton: bool
    canOpenItem: bool
    canCloseItem: bool
    canEditItem: bool
    canDeleteItem: bool
    canStickItem: bool
    canUnstickItem: bool
    bumpSettings: CategoryVpnResponseItemsBumpSettings
    canBumpItem: bool
    canBuyItem: bool
    rub_price: int
    price_currency: str
    canValidateAccount: bool
    canResellItemAfterPurchase: bool
    vpnProductTitle: str
    canViewAccountLink: bool
    canChangePassword: bool
    itemOriginPhrase: str
    sold_items_category_count: int
    restore_items_category_count: int
    tags: list[object]
    note_text: object
    hasPendingAutoBuy: bool
    descriptionHtml: str
    descriptionEnHtml: str
    descriptionPlain: str
    descriptionEnPlain: str
    seller: CategoryVpnResponseItemsSeller


class CategoryVpnResponse(TypedDict):
    items: list[CategoryVpnResponseItems]
    totalItems: int
    totalItemsPrice: object
    hasNextPage: bool
    perPage: int
    page: int
    wasCached: bool
    cacheTTL: int
    lastModified: int
    serverTime: int
    searchUrl: str
    stickyItems: list[object]
    system_info: Resp_SystemInfo


CategoryRobloxParams = TypedDict(
    "CategoryRobloxParams",
    {
        "page": int,
        "pmin": int,
        "pmax": int,
        "title": str,
        "order_by": Literal[
            "price_to_up",
            "price_to_down",
            "pdate_to_down",
            "pdate_to_up",
            "pdate_to_down_upload",
            "pdate_to_up_upload",
            "edate_to_up",
            "edate_to_down",
            "ddate_to_up",
            "ddate_to_down",
        ],
        "tag_id[]": list[int],
        "not_tag_id[]": list[int],
        "public_tag_id[]": list[int],
        "not_public_tag_id[]": list[int],
        "origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "not_origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "user_id": int,
        "nsb": bool,
        "sb": bool,
        "nsb_by_me": bool,
        "sb_by_me": bool,
        "currency": Literal[
            "rub", "uah", "kzt", "byn", "usd", "eur", "gbp", "cny", "try", "jpy", "brl"
        ],
        "email_login_data": bool,
        "email_provider[]": list[
            Literal["other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"]
        ],
        "not_email_provider[]": Literal[
            "other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"
        ],
        "parse_same_item_ids": bool,
        "email": YesNoNoMatterScheme,
        "robux_min": int,
        "robux_max": int,
        "friends_min": int,
        "friends_max": int,
        "followers_min": int,
        "followers_max": int,
        "country": list[str],
        "not_country": list[str],
        "reg": int,
        "reg_period": Literal["day", "month", "year"],
        "subscription": Literal[
            "RobloxPremium1000",
            "RobloxPremium100012Months",
            "RobloxPremium1000OneMonth",
            "RobloxPremium2200",
            "RobloxPremium2200OneMonth",
            "RobloxPremium450",
            "RobloxPremium450OneMonth",
        ],
        "subscription_length": int,
        "subscription_period": Literal["day", "month", "year"],
        "autorenewal": Literal["yes", "no", "nomatter"],
        "xbox_connected": YesNoNoMatterScheme,
        "psn_connected": YesNoNoMatterScheme,
        "verified": Literal["yes", "no", "nomatter"],
        "age_verified": YesNoNoMatterScheme,
        "incoming_robux_total_min": int,
        "incoming_robux_total_max": int,
        "limited_price_min": int,
        "limited_price_max": int,
        "gamepass_min": int,
        "gamepass_max": int,
        "game_donations": YesNoNoMatterScheme,
        "inv_min": int,
        "inv_max": int,
        "ugc_limited_price_min": int,
        "ugc_limited_price_max": int,
        "credit_balance_min": int,
        "credit_balance_max": int,
        "offsale_min": int,
        "offsale_max": int,
        "voice": YesNoNoMatterScheme,
        "age_group[]": list[str],
        "not_age_group[]": list[str],
    },
    total=False,
)


class CategoryRobloxResponseItemsBumpSettings(TypedDict):
    canBumpItem: bool
    canBumpItemGlobally: bool
    shortErrorPhrase: object
    errorPhrase: object


class CategoryRobloxResponseItemsRobloxGameDonations(TypedDict):
    id: int
    title: str
    amount: int


class CategoryRobloxResponseItemsRobloxGameDonationsDetails(TypedDict):
    product: str
    amount: int
    type: str


class CategoryRobloxResponseItemsAccountLinks(TypedDict):
    link: str
    text: str
    iconClass: str


class CategoryRobloxResponseItemsSeller(TypedDict):
    user_id: int
    sold_items_count: int
    active_items_count: int
    restore_data: str
    username: str
    avatar_date: int
    is_banned: int
    display_style_group_id: int
    restore_percents: int


class CategoryRobloxResponseItems(TypedDict):
    item_id: int
    item_state: str
    category_id: int
    published_date: int
    title: str
    description: str
    price: int
    update_stat_date: int
    refreshed_date: int
    edit_date: int
    view_count: int
    is_sticky: int
    item_origin: str
    extended_guarantee: int
    nsb: int
    allow_ask_discount: int
    title_en: str
    description_en: str
    email_type: str
    email_provider: str
    item_domain: str
    resale_item_origin: str
    roblox_item_id: int
    roblox_id: int
    roblox_email_verified: int
    roblox_robux: int
    roblox_username: str
    roblox_country: str
    roblox_register_date: int
    roblox_friends: int
    roblox_followers: int
    roblox_subscription: str
    roblox_subscription_end_date: int
    roblox_xbox_connected: int
    roblox_incoming_robux_total: int
    roblox_limited_price: int
    roblox_verified: int
    roblox_age_verified: int
    roblox_psn_connected: int
    roblox_subscription_auto_renew: int
    roblox_game_pass_total_robux: int
    roblox_game_donations: str
    roblox_inventory_price: int
    roblox_ugc_limited_price: int
    roblox_credit_balance: int
    feedback_data: str
    isIgnored: bool
    priceWithSellerFee: int
    guarantee: object
    canViewLoginData: bool
    canUpdateItemStats: bool
    canReportItem: bool
    canViewEmailLoginData: bool
    showGetEmailCodeButton: bool
    canOpenItem: bool
    canCloseItem: bool
    canEditItem: bool
    canDeleteItem: bool
    canStickItem: bool
    canUnstickItem: bool
    bumpSettings: CategoryRobloxResponseItemsBumpSettings
    canBumpItem: bool
    canBuyItem: bool
    rub_price: int
    price_currency: str
    canValidateAccount: bool
    canResellItemAfterPurchase: bool
    robloxLinkedAccounts: str
    creditBalance: str
    robloxGameDonations: list[CategoryRobloxResponseItemsRobloxGameDonations]
    robloxGameDonationsDetails: list[CategoryRobloxResponseItemsRobloxGameDonationsDetails]
    canViewAccountLink: bool
    accountLinks: list[CategoryRobloxResponseItemsAccountLinks]
    accountLink: str
    emailLoginUrl: str
    canChangePassword: bool
    itemOriginPhrase: str
    sold_items_category_count: int
    restore_items_category_count: int
    tags: list[object]
    note_text: object
    hasPendingAutoBuy: bool
    descriptionHtml: str
    descriptionEnHtml: str
    descriptionPlain: str
    descriptionEnPlain: str
    seller: CategoryRobloxResponseItemsSeller


class CategoryRobloxResponse(TypedDict):
    items: list[CategoryRobloxResponseItems]
    totalItems: int
    totalItemsPrice: object
    hasNextPage: bool
    perPage: int
    page: int
    wasCached: bool
    cacheTTL: int
    lastModified: int
    serverTime: int
    searchUrl: str
    stickyItems: list[object]
    system_info: Resp_SystemInfo


CategoryWarfaceParams = TypedDict(
    "CategoryWarfaceParams",
    {
        "page": int,
        "pmin": int,
        "pmax": int,
        "title": str,
        "order_by": Literal[
            "price_to_up",
            "price_to_down",
            "pdate_to_down",
            "pdate_to_up",
            "pdate_to_down_upload",
            "pdate_to_up_upload",
            "edate_to_up",
            "edate_to_down",
            "ddate_to_up",
            "ddate_to_down",
        ],
        "tag_id[]": list[int],
        "not_tag_id[]": list[int],
        "public_tag_id[]": list[int],
        "not_public_tag_id[]": list[int],
        "origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "not_origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "user_id": int,
        "nsb": bool,
        "sb": bool,
        "nsb_by_me": bool,
        "sb_by_me": bool,
        "currency": Literal[
            "rub", "uah", "kzt", "byn", "usd", "eur", "gbp", "cny", "try", "jpy", "brl"
        ],
        "email_login_data": bool,
        "email_provider[]": list[
            Literal["other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"]
        ],
        "not_email_provider[]": Literal[
            "other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"
        ],
        "parse_same_item_ids": bool,
        "rank_min": int,
        "rank_max": int,
        "bonus_rank_min": int,
        "bonus_rank_max": int,
        "tel": Literal["yes", "no", "nomatter"],
        "daybreak": int,
        "kredits_min": int,
        "kredits_max": int,
        "total_kredits_min": int,
        "total_kredits_max": int,
    },
    total=False,
)


class CategoryWarfaceResponseItemsBumpSettings(TypedDict):
    canBumpItem: bool
    canBumpItemGlobally: bool
    shortErrorPhrase: object
    errorPhrase: object


class CategoryWarfaceResponseItemsWf_servers(TypedDict):
    id: int
    rank: int
    title: str


class CategoryWarfaceResponseItemsSeller(TypedDict):
    user_id: int
    sold_items_count: int
    active_items_count: int
    restore_data: str
    username: str
    avatar_date: int
    is_banned: int
    display_style_group_id: int
    restore_percents: int


class CategoryWarfaceResponseItems(TypedDict):
    item_id: int
    item_state: str
    category_id: int
    published_date: int
    title: str
    description: str
    price: int
    update_stat_date: int
    refreshed_date: int
    edit_date: int
    view_count: int
    is_sticky: int
    item_origin: str
    extended_guarantee: int
    nsb: int
    allow_ask_discount: int
    title_en: str
    description_en: str
    email_type: str
    email_provider: object
    item_domain: str
    resale_item_origin: str
    wf_item_id: int
    wf_players: bool
    wf_server_1: int
    wf_server_2: int
    wf_server_3: int
    wf_mobile: int
    wf_bonus_rank: int
    wf_mail_mobile: int
    wf_last_game_date: int
    wf_loan: bool
    wf_active_loan: int
    wf_rank: int
    feedback_data: str
    isIgnored: bool
    priceWithSellerFee: int
    guarantee: object
    canViewLoginData: bool
    canUpdateItemStats: bool
    canReportItem: bool
    canViewEmailLoginData: bool
    showGetEmailCodeButton: bool
    canOpenItem: bool
    canCloseItem: bool
    canEditItem: bool
    canDeleteItem: bool
    canStickItem: bool
    canUnstickItem: bool
    bumpSettings: CategoryWarfaceResponseItemsBumpSettings
    canBumpItem: bool
    canBuyItem: bool
    rub_price: int
    price_currency: str
    canValidateAccount: bool
    canResellItemAfterPurchase: bool
    isSmallExf: bool
    account_last_activity: int
    wf_servers: list[CategoryWarfaceResponseItemsWf_servers]
    domain: str
    canViewAccountLink: bool
    canChangePassword: bool
    itemOriginPhrase: str
    sold_items_category_count: int
    restore_items_category_count: int
    tags: list[object]
    note_text: object
    hasPendingAutoBuy: bool
    descriptionHtml: str
    descriptionEnHtml: str
    descriptionPlain: str
    descriptionEnPlain: str
    seller: CategoryWarfaceResponseItemsSeller


class CategoryWarfaceResponse(TypedDict):
    items: list[CategoryWarfaceResponseItems]
    totalItems: int
    totalItemsPrice: object
    hasNextPage: bool
    perPage: int
    page: int
    wasCached: bool
    cacheTTL: int
    lastModified: int
    serverTime: int
    searchUrl: str
    stickyItems: list[object]
    system_info: Resp_SystemInfo


CategoryMinecraftParams = TypedDict(
    "CategoryMinecraftParams",
    {
        "page": int,
        "pmin": int,
        "pmax": int,
        "title": str,
        "order_by": Literal[
            "price_to_up",
            "price_to_down",
            "pdate_to_down",
            "pdate_to_up",
            "pdate_to_down_upload",
            "pdate_to_up_upload",
            "edate_to_up",
            "edate_to_down",
            "ddate_to_up",
            "ddate_to_down",
        ],
        "tag_id[]": list[int],
        "not_tag_id[]": list[int],
        "public_tag_id[]": list[int],
        "not_public_tag_id[]": list[int],
        "origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "not_origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "user_id": int,
        "nsb": bool,
        "sb": bool,
        "nsb_by_me": bool,
        "sb_by_me": bool,
        "currency": Literal[
            "rub", "uah", "kzt", "byn", "usd", "eur", "gbp", "cny", "try", "jpy", "brl"
        ],
        "email_login_data": bool,
        "email_provider[]": list[
            Literal["other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"]
        ],
        "not_email_provider[]": Literal[
            "other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"
        ],
        "parse_same_item_ids": bool,
        "subscription": Literal["PC Game Pass", "Xbox Game Pass Ultimate"],
        "subscription_length": int,
        "subscription_period": Literal["day", "month", "year"],
        "autorenewal": Literal["yes", "no", "nomatter"],
        "java": YesNoNoMatterScheme,
        "bedrock": YesNoNoMatterScheme,
        "dungeons": YesNoNoMatterScheme,
        "legends": YesNoNoMatterScheme,
        "change_nickname": YesNoNoMatterScheme,
        "capes[]": list[str],
        "capes_min": int,
        "capes_max": int,
        "country[]": list[str],
        "not_country[]": list[str],
        "hypixel_ban": YesNoNoMatterScheme,
        "hypixel_skyblock_api_enabled": YesNoNoMatterScheme,
        "rank_hypixel[]": list[Literal["MVP", "MVP+", "MVP++", "VIP", "VIP+", "YOUTUBE"]],
        "level_hypixel_min": int,
        "level_hypixel_max": int,
        "achievement_hypixel_min": int,
        "achievement_hypixel_max": int,
        "level_hypixel_skyblock_min": int,
        "level_hypixel_skyblock_max": int,
        "net_worth_hypixel_skyblock_min": int,
        "net_worth_hypixel_skyblock_max": int,
        "reg": int,
        "reg_period": Literal["day", "month", "year"],
        "last_login_hypixel": int,
        "last_login_hypixel_period": Literal["day", "month", "year"],
        "can_change_details": YesNoNoMatterScheme,
        "nickname_length_min": int,
        "nickname_length_max": int,
        "hypixel_ban_parsed": YesNoNoMatterScheme,
        "minecoins_min": int,
        "minecoins_max": int,
    },
    total=False,
)


class CategoryMinecraftResponseItemsBumpSettings(TypedDict):
    canBumpItem: bool
    canBumpItemGlobally: bool
    shortErrorPhrase: object
    errorPhrase: object


class CategoryMinecraftResponseItemsAccountLinks(TypedDict):
    link: str
    text: str
    iconClass: str


class CategoryMinecraftResponseItemsSeller(TypedDict):
    user_id: int
    sold_items_count: int
    active_items_count: int
    restore_data: str
    username: str
    avatar_date: int
    is_banned: int
    display_style_group_id: int
    restore_percents: object


class CategoryMinecraftResponseItems(TypedDict):
    item_id: int
    item_state: str
    category_id: int
    published_date: int
    title: str
    description: str
    price: int
    update_stat_date: int
    refreshed_date: int
    edit_date: int
    view_count: int
    is_sticky: int
    item_origin: str
    extended_guarantee: int
    nsb: int
    allow_ask_discount: int
    title_en: str
    description_en: str
    email_type: str
    email_provider: str
    item_domain: str
    resale_item_origin: str
    minecraft_item_id: int
    minecraft_id: str
    minecraft_nickname: str
    minecraft_country: str
    minecraft_skin: str
    minecraft_java: int
    minecraft_bedrock: int
    minecraft_can_change_nickname: int
    minecraft_created_at: int
    minecraft_hypixel_rank: str
    minecraft_hypixel_level: int
    minecraft_hypixel_achievement: int
    minecraft_hypixel_last_login: int
    minecraft_hypixel_ban: int
    minecraft_hypixel_ban_reason: str
    minecraft_hypixel_skyblock_level: int
    minecraft_hypixel_skyblock_net_worth: int
    minecraft_dungeons: int
    minecraft_legends: int
    minecraft_capes_count: int
    minecraft_capes: list[object]
    minecraft_subscription_name: str
    minecraft_subscription_ends: int
    minecraft_subscription_auto_renew: int
    minecraft_email_reset_date: int
    feedback_data: str
    isIgnored: bool
    priceWithSellerFee: int
    guarantee: object
    canViewLoginData: bool
    canUpdateItemStats: bool
    canReportItem: bool
    canViewEmailLoginData: bool
    showGetEmailCodeButton: bool
    canOpenItem: bool
    canCloseItem: bool
    canEditItem: bool
    canDeleteItem: bool
    canStickItem: bool
    canUnstickItem: bool
    bumpSettings: CategoryMinecraftResponseItemsBumpSettings
    canBumpItem: bool
    canBuyItem: bool
    rub_price: int
    price_currency: str
    canValidateAccount: bool
    canResellItemAfterPurchase: bool
    minecraftHasPaidLicense: bool
    canViewAccountLink: bool
    accountLinks: list[CategoryMinecraftResponseItemsAccountLinks]
    accountLink: str
    emailLoginUrl: str
    canChangePassword: bool
    itemOriginPhrase: str
    tags: list[object]
    note_text: object
    hasPendingAutoBuy: bool
    descriptionHtml: str
    descriptionEnHtml: str
    descriptionPlain: str
    descriptionEnPlain: str
    seller: CategoryMinecraftResponseItemsSeller


class CategoryMinecraftResponse(TypedDict):
    items: list[CategoryMinecraftResponseItems]
    totalItems: int
    totalItemsPrice: object
    hasNextPage: bool
    perPage: int
    page: int
    wasCached: bool
    cacheTTL: int
    lastModified: int
    serverTime: int
    searchUrl: str
    stickyItems: list[object]
    system_info: Resp_SystemInfo


CategoryHytaleParams = TypedDict(
    "CategoryHytaleParams",
    {
        "page": int,
        "pmin": int,
        "pmax": int,
        "title": str,
        "order_by": Literal[
            "price_to_up",
            "price_to_down",
            "pdate_to_down",
            "pdate_to_up",
            "pdate_to_down_upload",
            "pdate_to_up_upload",
            "edate_to_up",
            "edate_to_down",
            "ddate_to_up",
            "ddate_to_down",
        ],
        "tag_id[]": list[int],
        "not_tag_id[]": list[int],
        "public_tag_id[]": list[int],
        "not_public_tag_id[]": list[int],
        "origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "not_origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "user_id": int,
        "nsb": bool,
        "sb": bool,
        "nsb_by_me": bool,
        "sb_by_me": bool,
        "currency": Literal[
            "rub", "uah", "kzt", "byn", "usd", "eur", "gbp", "cny", "try", "jpy", "brl"
        ],
        "email_login_data": bool,
        "email_provider[]": list[
            Literal["other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"]
        ],
        "not_email_provider[]": Literal[
            "other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"
        ],
        "parse_same_item_ids": bool,
        "edition[]": list[Literal["base", "deluxe", "founder"]],
        "profiles_min": int,
        "profiles_max": int,
    },
    total=False,
)


class CategoryHytaleResponseItemsCategory(TypedDict):
    category_id: int
    category_title: str
    category_name: str
    category_url: str


class CategoryHytaleResponseItemsCopyFormatData(TypedDict):
    title_link: str


class CategoryHytaleResponseItemsSeller(TypedDict):
    user_id: int
    sold_items_count: int
    active_items_count: int
    restore_data: str
    username: str
    avatar_date: int
    is_banned: int
    display_style_group_id: int
    restore_percents: object


class CategoryHytaleResponseItems(TypedDict):
    item_id: int
    item_state: str
    category_id: int
    published_date: int
    title: str
    description: str
    price: int
    update_stat_date: int
    refreshed_date: int
    edit_date: int
    pending_deletion_date: int
    view_count: int
    is_sticky: int
    item_origin: str
    extended_guarantee: int
    nsb: int
    allow_ask_discount: int
    title_en: str
    description_en: str
    email_type: str
    email_provider: str
    item_domain: str
    resale_item_origin: str
    auto_bump_period: int
    rub_price: int
    discount: bool
    hytale_item_id: int
    hytale_profiles: int
    hytale_edition: str
    feedback_data: str
    max_discount_percent: int
    isIgnored: bool
    priceWithSellerFee: float
    category: CategoryHytaleResponseItemsCategory
    guarantee: object
    canViewLoginData: bool
    canViewTempEmail: bool
    canUpdateItemStats: bool
    canReportItem: bool
    canViewItemViews: bool
    canManagePublicTag: bool
    canViewEmailLoginData: bool
    copyFormatData: CategoryHytaleResponseItemsCopyFormatData
    showGetEmailCodeButton: bool
    canOpenItem: bool
    canCloseItem: bool
    canEditItem: bool
    canDeleteItem: bool
    canStickItem: bool
    canUnstickItem: bool
    canBumpItem: bool
    canNotBumpItemReason: str
    buyer: object
    isPersonalAccount: bool
    canBuyItem: bool
    price_currency: str
    priceWithSellerFeeLabel: str
    canValidateAccount: bool
    canResellItem: bool
    canViewAccountLink: bool
    imagePreviewLinks: list[object]
    emailLoginUrl: str
    canChangePassword: bool
    canChangeEmailPassword: bool
    uniqueKeyExists: bool
    itemOriginPhrase: str
    tags: list[object]
    public_tag: object
    note_text: object
    hasPendingAutoBuy: bool
    descriptionHtml: str
    descriptionEnHtml: str
    descriptionPlain: str
    descriptionEnPlain: str
    seller: CategoryHytaleResponseItemsSeller


class CategoryHytaleResponse(TypedDict):
    items: list[CategoryHytaleResponseItems]
    totalItems: int
    totalItemsPrice: object
    hasNextPage: bool
    perPage: int
    page: int
    wasCached: bool
    cacheTTL: int
    lastModified: int
    serverTime: int
    searchUrl: str
    stickyItems: list[object]
    system_info: Resp_SystemInfo


class CategoryListParams(TypedDict, total=False):
    top_queries: bool


CategoryListResponseCategoryLinks = TypedDict(
    "CategoryListResponseCategoryLinks",
    {
        "permalink": str,
        "detail": str,
        "sub-categories": str,
        "sub-forums": str,
    },
)


class CategoryListResponseCategory(TypedDict):
    category_id: int
    category_title: str
    category_description: str
    links: CategoryListResponseCategoryLinks


class CategoryListResponse(TypedDict):
    category: CategoryListResponseCategory
    system_info: Resp_SystemInfo


class CategoryParamsResponseCategory(TypedDict):
    category_id: int
    sub_category_id: int
    category_order: int
    category_title: str
    category_name: str
    category_url: str
    category_description_html: str
    category_login_url: str
    add_item_available: int
    mass_upload_item_available: int
    has_guarantee: int
    has_account_link: int
    require_temp_email: int
    recovery_link: str
    check_button_enabled: int
    checker_enabled: int
    support_personal_proxy: int
    support_email_login_data: int
    require_email_login_data: int
    display_in_list: int
    category_description_html_en: str
    category_h1_html_en: str
    account_price_min: int
    require_video_recording: int
    top_queries: str
    require_eld_for_native_accs: int
    can_be_resold: int
    support_temp_email: int
    cookies: str
    login_type: str
    guest_hidden: int
    available_temp_email: int
    resale_duration_limit_days: int
    buy_without_validation: int
    max_invalid_upload_tries: int


class CategoryParamsResponseParams(TypedDict):
    name: str
    input: str
    description: str
    values: list[str]


class CategoryParamsResponseBase_params0(TypedDict):
    name: str
    input: str
    description: str


CategoryParamsResponseBase_params = TypedDict(
    "CategoryParamsResponseBase_params",
    {
        "0": CategoryParamsResponseBase_params0,
    },
)


class CategoryParamsResponse(TypedDict, total=False):
    category: CategoryParamsResponseCategory
    params: list[CategoryParamsResponseParams]
    base_params: CategoryParamsResponseBase_params
    system_info: Resp_SystemInfo


class CategoryGamesResponseGames(TypedDict):
    app_id: str
    title: str
    abbr: str
    category_id: int
    img: str
    url: str
    ru: str


class CategoryGamesResponse(TypedDict, total=False):
    games: list[CategoryGamesResponseGames]
    system_info: Resp_SystemInfo


# ─── ListApi Types ────────────────────────────────────────


ListUserParams = TypedDict(
    "ListUserParams",
    {
        "user_id": int,
        "category_id": CategoryIDModel,
        "page": int,
        "show": Literal[
            "active",
            "paid",
            "deleted",
            "awaiting",
            "closed",
            "discount_request",
            "stickied",
            "pre_active",
        ],
        "delete_reason": str,
        "title": str,
        "pmin": int,
        "pmax": int,
        "login": str,
        "origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "not_origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "order_by": Literal[
            "price_to_up",
            "price_to_down",
            "pdate_to_down",
            "pdate_to_up",
            "pdate_to_down_upload",
            "pdate_to_up_upload",
            "edate_to_up",
            "edate_to_down",
            "ddate_to_up",
            "ddate_to_down",
        ],
        "sb": bool,
        "sb_by_me": bool,
        "nsb": bool,
        "nsb_by_me": bool,
        "username": str,
        "published_startDate": str,
        "published_endDate": str,
        "filter_by_published_date": bool,
        "paid_startDate": str,
        "paid_endDate": str,
        "filter_by_buyer_operation_date": bool,
        "delete_startDate": str,
        "delete_endDate": str,
        "filter_by_delete_date": bool,
    },
    total=False,
)


class ListUserResponse(TypedDict):
    items: list[ItemFromListModel]
    totalItems: int
    totalItemsPrice: object
    hasNextPage: bool
    perPage: int
    page: int
    searchUrl: str
    stickyItems: list[ItemFromListModel]
    system_info: Resp_SystemInfo


ListOrdersParams = TypedDict(
    "ListOrdersParams",
    {
        "user_id": int,
        "category_id": CategoryIDModel,
        "page": int,
        "show": Literal[
            "active",
            "paid",
            "deleted",
            "awaiting",
            "closed",
            "discount_request",
            "stickied",
            "pre_active",
        ],
        "title": str,
        "pmin": int,
        "pmax": int,
        "login": str,
        "origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "not_origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "order_by": Literal[
            "price_to_up",
            "price_to_down",
            "pdate_to_down",
            "pdate_to_up",
            "pdate_to_down_upload",
            "pdate_to_up_upload",
            "edate_to_up",
            "edate_to_down",
            "ddate_to_up",
            "ddate_to_down",
        ],
        "sb": bool,
        "sb_by_me": bool,
        "nsb": bool,
        "nsb_by_me": bool,
    },
    total=False,
)


class ListOrdersResponse(TypedDict):
    items: list[ItemFromListModel]
    totalItems: int
    totalItemsPrice: object
    hasNextPage: bool
    perPage: int
    page: int
    searchUrl: str
    stickyItems: list[ItemFromListModel]
    system_info: Resp_SystemInfo


class ListStatesParams(TypedDict, total=False):
    user_id: int | str


class ListStatesResponseUserItemStatesStickied(TypedDict):
    item_state: str
    item_count: int
    title: str
    stickyLimit: int


class ListStatesResponseUserItemStatesDiscount_request(TypedDict):
    item_state: str
    item_count: int
    title: str


class ListStatesResponseUserItemStatesIn_buyers_favorites(TypedDict):
    item_state: str
    item_count: int
    title: str


class ListStatesResponseUserItemStatesActive(TypedDict):
    item_count: int
    item_state: str
    title: str


class ListStatesResponseUserItemStatesPaid(TypedDict):
    item_count: int
    item_state: str
    title: str


class ListStatesResponseUserItemStatesClosed(TypedDict):
    item_state: str
    item_count: int
    title: str


class ListStatesResponseUserItemStatesDeleted(TypedDict):
    item_count: int
    item_state: str
    title: str


class ListStatesResponseUserItemStatesAwaiting(TypedDict):
    item_count: int
    item_state: str
    title: str


class ListStatesResponseUserItemStatesPre_active(TypedDict):
    item_state: str
    item_count: int
    title: str


class ListStatesResponseUserItemStatesPre_upload(TypedDict):
    item_state: str
    item_count: int
    title: str


class ListStatesResponseUserItemStatesPending_deletion(TypedDict):
    item_state: str
    item_count: int
    title: str


class ListStatesResponseUserItemStatesClosed_inactive(TypedDict):
    item_count: int
    item_state: str
    title: str


class ListStatesResponseUserItemStatesAuto_bump(TypedDict):
    item_state: str
    item_count: int
    title: str


class ListStatesResponseUserItemStates(TypedDict):
    stickied: ListStatesResponseUserItemStatesStickied
    discount_request: ListStatesResponseUserItemStatesDiscount_request
    in_buyers_favorites: ListStatesResponseUserItemStatesIn_buyers_favorites
    active: ListStatesResponseUserItemStatesActive
    paid: ListStatesResponseUserItemStatesPaid
    closed: ListStatesResponseUserItemStatesClosed
    deleted: ListStatesResponseUserItemStatesDeleted
    awaiting: ListStatesResponseUserItemStatesAwaiting
    pre_active: ListStatesResponseUserItemStatesPre_active
    pre_upload: ListStatesResponseUserItemStatesPre_upload
    pending_deletion: ListStatesResponseUserItemStatesPending_deletion
    closed_inactive: ListStatesResponseUserItemStatesClosed_inactive
    auto_bump: ListStatesResponseUserItemStatesAuto_bump


class ListStatesResponse(TypedDict):
    userItemStates: ListStatesResponseUserItemStates
    system_info: Resp_SystemInfo


ListDownloadParams = TypedDict(
    "ListDownloadParams",
    {
        "format": Literal["short", "custom", "mfa_file_steam_id", "mfa_file_login"],
        "custom_format": str,
        "category_id": CategoryIDModel,
        "page": int,
        "show": Literal[
            "active",
            "paid",
            "deleted",
            "awaiting",
            "closed",
            "discount_request",
            "stickied",
            "pre_active",
        ],
        "delete_reason": str,
        "title": str,
        "pmin": int,
        "pmax": int,
        "origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "not_origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "order_by": Literal[
            "price_to_up",
            "price_to_down",
            "pdate_to_down",
            "pdate_to_up",
            "pdate_to_down_upload",
            "pdate_to_up_upload",
            "edate_to_up",
            "edate_to_down",
            "ddate_to_up",
            "ddate_to_down",
        ],
        "sb": bool,
        "sb_by_me": bool,
        "nsb": bool,
        "nsb_by_me": bool,
        "username": str,
        "published_startDate": str,
        "published_endDate": str,
        "filter_by_published_date": bool,
        "paid_startDate": str,
        "paid_endDate": str,
        "filter_by_buyer_operation_date": bool,
        "delete_startDate": str,
        "delete_endDate": str,
        "filter_by_delete_date": bool,
    },
    total=False,
)


ListDownloadResponse = object


ListFavoritesParams = TypedDict(
    "ListFavoritesParams",
    {
        "page": int,
        "show": Literal[
            "active",
            "paid",
            "deleted",
            "awaiting",
            "closed",
            "discount_request",
            "stickied",
            "pre_active",
        ],
        "title": str,
        "pmin": int,
        "pmax": int,
        "origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "not_origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "order_by": Literal[
            "price_to_up",
            "price_to_down",
            "pdate_to_down",
            "pdate_to_up",
            "pdate_to_down_upload",
            "pdate_to_up_upload",
            "edate_to_up",
            "edate_to_down",
            "ddate_to_up",
            "ddate_to_down",
        ],
        "sb": bool,
        "sb_by_me": bool,
        "nsb": bool,
        "nsb_by_me": bool,
    },
    total=False,
)


class ListFavoritesResponse(TypedDict):
    items: list[ItemFromListModel]
    totalItems: int
    totalItemsPrice: object
    hasNextPage: bool
    perPage: int
    page: int
    searchUrl: str
    stickyItems: list[ItemFromListModel]
    system_info: Resp_SystemInfo


ListViewedParams = TypedDict(
    "ListViewedParams",
    {
        "page": int,
        "show": Literal[
            "active",
            "paid",
            "deleted",
            "awaiting",
            "closed",
            "discount_request",
            "stickied",
            "pre_active",
        ],
        "title": str,
        "pmin": int,
        "pmax": int,
        "origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "not_origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "order_by": Literal[
            "price_to_up",
            "price_to_down",
            "pdate_to_down",
            "pdate_to_up",
            "pdate_to_down_upload",
            "pdate_to_up_upload",
            "edate_to_up",
            "edate_to_down",
            "ddate_to_up",
            "ddate_to_down",
        ],
        "sb": bool,
        "sb_by_me": bool,
        "nsb": bool,
        "nsb_by_me": bool,
    },
    total=False,
)


class ListViewedResponse(TypedDict):
    items: list[ItemFromListModel]
    totalItems: int
    totalItemsPrice: object
    hasNextPage: bool
    perPage: int
    page: int
    searchUrl: str
    stickyItems: list[ItemFromListModel]
    system_info: Resp_SystemInfo


# ─── ManagingApi Types ────────────────────────────────────────


class ManagingGetParams(TypedDict, total=False):
    parse_same_item_ids: bool


class ManagingGetResponse(TypedDict):
    item: ItemModel
    canStickItem: bool
    canUnstickItem: bool
    canBuyItem: bool
    cannotBuyItemError: str
    canCloseItem: bool
    canOpenItem: bool
    canReportItem: bool
    canEditItem: bool
    canDeleteItem: bool
    canCancelConfirmedBuy: bool
    canViewItemHistory: bool
    faveCount: bool
    isVisibleItem: bool
    canViewLoginData: bool
    showToFavouritesButton: bool
    itemLink: str
    canChangeOwner: bool
    sameItemsIds: list[int]
    sameItemsCount: int
    system_info: Resp_SystemInfo


class ManagingDeleteBody(TypedDict):
    reason: str


class ManagingDeleteResponse(TypedDict):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ManagingCreateclaimBody(TypedDict):
    item_id: ItemIDModel
    post_body: str


class _ManagingCreateclaimResponseThreadFirst_postLike_usersRequired(TypedDict):
    user_id: int
    username: str


class ManagingCreateclaimResponseThreadFirst_postLike_users(
    _ManagingCreateclaimResponseThreadFirst_postLike_usersRequired, total=False
):
    display_style_group_id: int
    is_banned: int
    uniq_username_css: str


class ManagingCreateclaimResponseThreadFirst_postLinks(TypedDict):
    permalink: str
    detail: str
    thread: str
    poster: str
    likes: str
    report: str
    attachments: str
    poster_avatar: str


class ManagingCreateclaimResponseThreadFirst_postPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    reply: bool
    like: bool
    report: bool
    upload_attachment: bool


class ManagingCreateclaimResponseThreadFirst_post(TypedDict):
    post_id: int
    thread_id: int
    poster_user_id: int
    poster_username: str
    post_create_date: int
    post_body: str
    post_body_html: str
    post_body_plain_text: str
    signature: str
    signature_html: str
    signature_plain_text: str
    post_like_count: int
    post_attachment_count: int
    like_users: list[ManagingCreateclaimResponseThreadFirst_postLike_users]
    user_is_ignored: bool
    post_is_published: bool
    post_is_deleted: bool
    post_update_date: int
    post_is_first_post: bool
    links: ManagingCreateclaimResponseThreadFirst_postLinks
    permissions: ManagingCreateclaimResponseThreadFirst_postPermissions


class ManagingCreateclaimResponseThreadLinks(TypedDict):
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


class ManagingCreateclaimResponseThreadPermissions(TypedDict):
    view: bool
    delete: bool
    follow: bool
    post: bool
    upload_attachment: bool
    edit: bool


class ManagingCreateclaimResponseThreadForumForum_prefixesGroup_prefixes(TypedDict):
    prefix_id: int
    prefix_title: str


class ManagingCreateclaimResponseThreadForumForum_prefixes(TypedDict):
    group_title: str
    group_prefixes: list[ManagingCreateclaimResponseThreadForumForum_prefixesGroup_prefixes]


ManagingCreateclaimResponseThreadForumLinks = TypedDict(
    "ManagingCreateclaimResponseThreadForumLinks",
    {
        "permalink": str,
        "detail": str,
        "sub-categories": str,
        "sub-forums": str,
        "threads": str,
        "followers": str,
    },
)


class ManagingCreateclaimResponseThreadForumPermissions(TypedDict):
    view: bool
    edit: bool
    delete: bool
    create_thread: bool
    upload_attachment: bool
    tag_thread: bool
    follow: bool


class ManagingCreateclaimResponseThreadForum(TypedDict):
    forum_id: int
    forum_title: str
    forum_description: str
    forum_thread_count: int
    forum_post_count: int
    forum_prefixes: list[ManagingCreateclaimResponseThreadForumForum_prefixes]
    thread_default_prefix_id: int
    thread_prefix_is_required: bool
    links: ManagingCreateclaimResponseThreadForumLinks
    permissions: ManagingCreateclaimResponseThreadForumPermissions
    forum_is_followed: bool


class ManagingCreateclaimResponseThread(TypedDict):
    thread_id: int
    forum_id: int
    thread_title: str
    thread_view_count: int
    creator_user_id: int
    creator_username: str
    thread_create_date: int
    thread_update_date: int
    user_is_ignored: bool
    thread_post_count: int
    thread_is_published: bool
    thread_is_deleted: bool
    thread_is_sticky: bool
    thread_is_followed: bool
    first_post: ManagingCreateclaimResponseThreadFirst_post
    thread_prefixes: list[object]
    thread_tags: list[object]
    links: ManagingCreateclaimResponseThreadLinks
    permissions: ManagingCreateclaimResponseThreadPermissions
    forum: ManagingCreateclaimResponseThreadForum


class ManagingCreateclaimResponseSystem_info(TypedDict):
    visitor_id: int
    time: int


class ManagingCreateclaimResponse(TypedDict):
    thread: ManagingCreateclaimResponseThread
    system_info: ManagingCreateclaimResponseSystem_info


class ManagingBulkgetBody(TypedDict, total=False):
    item_id: list[ItemIDModel]
    parse_same_item_ids: bool


ManagingBulkgetResponseItems = TypedDict(
    "ManagingBulkgetResponseItems",
    {
        "0": ItemModel,
    },
    total=False,
)


class ManagingBulkgetResponse(TypedDict):
    items: list[ManagingBulkgetResponseItems]
    left_item_id: list[int]
    system_info: Resp_SystemInfo


class ManagingSteaminventoryvalueParams(TypedDict, total=False):
    app_id: Literal[730, 578080, 753, 570, 440, 252490, 304930, 232090, 322330]
    currency: CurrencyModel
    ignore_cache: bool


class ManagingSteaminventoryvalueResponseDataItems0Stickers(TypedDict):
    stickerCount: int
    count: int
    images: list[str]
    title: str


class ManagingSteaminventoryvalueResponseDataItems0(TypedDict):
    classid: str
    tradable: int
    marketable: int
    image_url: str
    title: str
    price: float
    count: int
    type: str
    market_hash_name: str
    fraudwarnings: object
    stickers: ManagingSteaminventoryvalueResponseDataItems0Stickers


ManagingSteaminventoryvalueResponseDataItems = TypedDict(
    "ManagingSteaminventoryvalueResponseDataItems",
    {
        "0": ManagingSteaminventoryvalueResponseDataItems0,
    },
    total=False,
)


class ManagingSteaminventoryvalueResponseData(TypedDict):
    items: ManagingSteaminventoryvalueResponseDataItems
    steam_id: str
    appId: int
    appTitle: str
    totalValue: float
    itemCount: int
    marketableItemCount: int
    currency: str
    currencyIcon: str
    language: str
    time: int


class ManagingSteaminventoryvalueResponse(TypedDict, total=False):
    query: str
    data: ManagingSteaminventoryvalueResponseData
    appId: int
    system_info: Resp_SystemInfo


class _ManagingSteamvalueParamsRequired(TypedDict):
    link: str


class ManagingSteamvalueParams(_ManagingSteamvalueParamsRequired, total=False):
    app_id: Literal[730, 578080, 753, 570, 440, 252490, 304930, 232090, 322330]
    currency: CurrencyModel
    ignore_cache: bool


class ManagingSteamvalueResponseDataItems0Stickers(TypedDict):
    stickerCount: int
    count: int
    images: list[str]
    title: str


class ManagingSteamvalueResponseDataItems0(TypedDict):
    classid: str
    tradable: int
    marketable: int
    image_url: str
    title: str
    price: float
    count: int
    type: str
    market_hash_name: str
    fraudwarnings: object
    stickers: ManagingSteamvalueResponseDataItems0Stickers


ManagingSteamvalueResponseDataItems = TypedDict(
    "ManagingSteamvalueResponseDataItems",
    {
        "0": ManagingSteamvalueResponseDataItems0,
    },
    total=False,
)


class ManagingSteamvalueResponseData(TypedDict):
    items: ManagingSteamvalueResponseDataItems
    steam_id: str
    appId: int
    appTitle: str
    totalValue: float
    itemCount: int
    marketableItemCount: int
    currency: str
    currencyIcon: str
    language: str
    time: int


class ManagingSteamvalueResponse(TypedDict, total=False):
    query: str
    data: ManagingSteamvalueResponseData
    appId: int
    system_info: Resp_SystemInfo


class ManagingSteampreviewParams(TypedDict, total=False):
    type: Literal["profiles", "games"]


ManagingSteampreviewResponse = object


class ManagingEditBody(TypedDict, total=False):
    title: str
    title_en: str
    price: int
    currency: CurrencyModel
    item_origin: Literal["brute", "phishing", "stealer", "personal", "resale", "autoreg", "dummy"]
    email_login_data: str
    email_type: Literal["native", "autoreg"]
    allow_ask_discount: bool
    proxy_id: int
    description: str
    information: str


class ManagingEditResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ManagingAipriceResponse(TypedDict):
    price: int
    system_info: Resp_SystemInfo


class ManagingAutobuypriceResponse(TypedDict):
    price: int
    system_info: Resp_SystemInfo


class ManagingNoteBody(TypedDict, total=False):
    text: str


class ManagingNoteResponse(TypedDict):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ManagingSteamupdatevalueBody(TypedDict, total=False):
    all: bool
    app_id: Literal[730, 578080, 753, 570, 440, 252490, 304930, 232090, 322330]
    authorize: bool


class ManagingSteamupdatevalueResponse(TypedDict):
    status: str
    item: ItemModel
    system_info: Resp_SystemInfo


class ManagingBumpResponse(TypedDict):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ManagingAutobumpBody(TypedDict):
    hour: int


class ManagingAutobumpResponse(TypedDict):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ManagingAutobumpdisableResponse(TypedDict):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ManagingOpenResponse(TypedDict):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ManagingCloseResponse(TypedDict):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ManagingImageParams(TypedDict):
    type: Literal["skins", "pickaxes", "dances", "gliders", "weapons", "agents", "buddies"]


class ManagingImageResponse(TypedDict):
    base64: str
    system_info: Resp_SystemInfo


class ManagingEmailcodeResponseCodeData(TypedDict):
    code: str
    date: int
    textPlain: str


class ManagingEmailcodeResponse(TypedDict):
    item: ItemModel
    codeData: ManagingEmailcodeResponseCodeData


class ManagingGetletters2Params(TypedDict, total=False):
    email_password: str
    email: str
    password: str
    limit: int


ManagingGetletters2ResponseLetters = TypedDict(
    "ManagingGetletters2ResponseLetters",
    {
        "textHtml": str,
        "textPlain": str,
        "from": str,
        "date": int,
    },
)


class ManagingGetletters2Response(TypedDict):
    email: str
    letters: list[ManagingGetletters2ResponseLetters]
    system_info: Resp_SystemInfo


class ManagingSteamGetmafileResponseMaFileSession(TypedDict):
    SessionID: str
    AccessToken: str
    RefreshToken: str
    SteamID: str
    SteamLoginSecure: str


class ManagingSteamGetmafileResponseMaFile(TypedDict):
    shared_secret: str
    serial_number: int
    revocation_code: str
    uri: str
    account_name: str
    token_gid: str
    identity_secret: str
    secret_1: str
    device_id: str
    fully_enrolled: bool
    Session: ManagingSteamGetmafileResponseMaFileSession


class ManagingSteamGetmafileResponse(TypedDict):
    maFile: ManagingSteamGetmafileResponseMaFile
    system_info: Resp_SystemInfo


class ManagingSteamAddmafileResponse(TypedDict):
    status: str
    message: str
    item: ItemModel
    system_info: Resp_SystemInfo


class ManagingSteamRemovemafileResponse(TypedDict):
    status: str
    message: str
    item: ItemModel
    system_info: Resp_SystemInfo


class ManagingSteammafilecodeResponseCodeData(TypedDict):
    code: str
    date: int
    textPlain: str


class ManagingSteammafilecodeResponse(TypedDict):
    item: ItemModel
    codeData: ManagingSteammafilecodeResponseCodeData


class ManagingSteamsdaBody(TypedDict, total=False):
    id: int
    nonce: int


class ManagingSteamsdaResponse(TypedDict):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ManagingTelegramcodeResponseCodes(TypedDict, total=False):
    code: str
    date: int


class ManagingTelegramcodeResponse(TypedDict):
    item: ItemModel
    codes: ManagingTelegramcodeResponseCodes


class ManagingTelegramresetauthResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ManagingRefuseguaranteeResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ManagingDeclinevideorecordingBody(TypedDict):
    i_voluntarily_and_with_full_awareness_of_my_actions_waive_any_claims_regarding_this_item: bool


class ManagingDeclinevideorecordingResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ManagingCheckguaranteeResponse(TypedDict):
    message: str
    system_info: Resp_SystemInfo


class ManagingChangepasswordBody(TypedDict, total=False):
    _cancel: Literal[1]


class _ManagingChangepasswordResponseRequired(TypedDict):
    new_password: str


class ManagingChangepasswordResponse(_ManagingChangepasswordResponseRequired, total=False):
    status: str
    message: str


class ManagingTempemailpasswordResponseItem(TypedDict):
    account: str


class ManagingTempemailpasswordResponse(TypedDict):
    item: ManagingTempemailpasswordResponseItem


class ManagingTagBody(TypedDict):
    tag_id: int


class ManagingTagResponseTag(TypedDict):
    tag_id: int
    title: str
    isDefault: bool
    forOwnedAccountsOnly: bool
    bc: str


class ManagingTagResponse(TypedDict):
    itemId: int
    tag: ManagingTagResponseTag
    addedTagId: int
    deleteTags: list[int]
    system_info: Resp_SystemInfo


class ManagingUntagBody(TypedDict):
    tag_id: int


class ManagingUntagResponseTag(TypedDict):
    tag_id: int
    title: str
    isDefault: bool
    forOwnedAccountsOnly: bool
    bc: str


class ManagingUntagResponse(TypedDict):
    itemId: int
    tag: ManagingUntagResponseTag
    addedTagId: int
    deleteTags: list[int]
    system_info: Resp_SystemInfo


class ManagingPublictagBody(TypedDict):
    tag_id: int


class ManagingPublictagResponseTag(TypedDict):
    tag_id: int
    title: str
    isDefault: bool
    forOwnedAccountsOnly: bool
    bc: str


class ManagingPublictagResponse(TypedDict):
    itemId: int
    tag: ManagingPublictagResponseTag
    addedTagId: int
    deleteTags: list[int]
    system_info: Resp_SystemInfo


class ManagingPublicuntagBody(TypedDict):
    tag_id: int


class ManagingPublicuntagResponseTag(TypedDict):
    tag_id: int
    title: str
    isDefault: bool
    forOwnedAccountsOnly: bool
    bc: str


class ManagingPublicuntagResponse(TypedDict):
    itemId: int
    tag: ManagingPublicuntagResponseTag
    addedTagId: int
    deleteTags: list[int]
    system_info: Resp_SystemInfo


class ManagingFavoriteResponse(TypedDict):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ManagingUnfavoriteResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ManagingStickResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ManagingUnstickResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ManagingTransferBody(TypedDict):
    username: str
    secret_answer: str


class ManagingTransferResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


# ─── ProfileApi Types ────────────────────────────────────────


class ProfileClaimsParams(TypedDict, total=False):
    type: Literal["market", "nomarket"]
    claim_state: Literal["active", "solved", "rejected", "settled"]


class ProfileClaimsResponseClaimsAuthorLinks(TypedDict):
    permalink: str
    detail: str
    avatar: str
    avatar_big: str
    avatar_small: str
    followers: str
    followings: str
    ignore: str
    timeline: str


class ProfileClaimsResponseClaimsAuthorPermissions(TypedDict):
    edit: bool
    follow: bool
    ignore: bool


class ProfileClaimsResponseClaimsAuthorFields(TypedDict):
    id: str
    title: str
    description: str
    position: str
    is_required: bool


class ProfileClaimsResponseClaimsAuthor(TypedDict):
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
    links: ProfileClaimsResponseClaimsAuthorLinks
    permissions: ProfileClaimsResponseClaimsAuthorPermissions
    user_is_ignored: bool
    user_is_visitor: bool
    user_group_id: int
    ban_reason: str
    fields: list[ProfileClaimsResponseClaimsAuthorFields]


class ProfileClaimsResponseClaims(TypedDict):
    thread_id: int
    claim_date: int
    claim_state: str
    message_body: str
    amount_formatted: str
    author: ProfileClaimsResponseClaimsAuthor


class ProfileClaimsResponseStatsMarket(TypedDict):
    total: int
    solved: int
    settled: int
    rejected: int


class ProfileClaimsResponseStatsNoMarket(TypedDict):
    total: int
    solved: int
    settled: int
    rejected: int


class ProfileClaimsResponseStats(TypedDict):
    market: ProfileClaimsResponseStatsMarket
    noMarket: ProfileClaimsResponseStatsNoMarket


class ProfileClaimsResponse(TypedDict):
    claims: list[ProfileClaimsResponseClaims]
    stats: ProfileClaimsResponseStats
    system_info: Resp_SystemInfo


class ProfileGetParams(TypedDict, total=False):
    fields_include: list[Literal["*", "searchHistory", "savedSearch"]]


class ProfileGetResponse(TypedDict):
    user: UserModel
    system_info: Resp_SystemInfo


class ProfileEditBody(TypedDict, total=False):
    user: dict[str, object]
    option: dict[str, object]
    allow_accept_accounts: list[str]
    telegram_api_id: str
    telegram_api_hash: str
    telegram_device_model: str
    telegram_system_version: str
    telegram_app_version: str
    telegram_lang_pack: str
    telegram_lang_code: str
    telegram_system_lang_code: str
    clear_telegram_client: bool


class ProfileEditResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


# ─── CartApi Types ────────────────────────────────────────


CartGetParams = TypedDict(
    "CartGetParams",
    {
        "category_id": CategoryIDModel,
        "page": int,
        "pmin": int,
        "pmax": int,
        "title": str,
        "order_by": Literal[
            "price_to_up",
            "price_to_down",
            "pdate_to_down",
            "pdate_to_up",
            "pdate_to_down_upload",
            "pdate_to_up_upload",
            "edate_to_up",
            "edate_to_down",
            "ddate_to_up",
            "ddate_to_down",
        ],
        "tag_id[]": list[int],
        "not_tag_id[]": list[int],
        "public_tag_id[]": list[int],
        "not_public_tag_id[]": list[int],
        "origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "not_origin[]": list[
            Literal[
                "brute",
                "phishing",
                "stealer",
                "personal",
                "resale",
                "autoreg",
                "self_registration",
                "retrieve",
                "retrieve_via_support",
                "dummy",
            ]
        ],
        "user_id": int,
        "nsb": bool,
        "sb": bool,
        "nsb_by_me": bool,
        "sb_by_me": bool,
        "currency": Literal[
            "rub", "uah", "kzt", "byn", "usd", "eur", "gbp", "cny", "try", "jpy", "brl"
        ],
        "email_login_data": bool,
        "email_provider[]": list[
            Literal["other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"]
        ],
        "not_email_provider[]": Literal[
            "other", "rambler", "outlook", "firstmail", "notletters", "mail_ru"
        ],
        "parse_same_item_ids": bool,
    },
    total=False,
)


class CartGetResponse(TypedDict):
    items: list[ItemFromListModel]
    totalItems: int
    totalItemsPrice: object
    hasNextPage: bool
    perPage: int
    page: int
    searchUrl: str
    stickyItems: list[ItemFromListModel]
    system_info: Resp_SystemInfo


class CartAddBody(TypedDict):
    item_id: ItemIDModel


class CartAddResponse(TypedDict):
    success: bool
    system_info: Resp_SystemInfo


class CartDeleteBody(TypedDict, total=False):
    item_id: ItemIDModel


class CartDeleteResponse(TypedDict):
    success: bool
    system_info: Resp_SystemInfo


# ─── PurchasingApi Types ────────────────────────────────────────


class PurchasingFastbuyBody(TypedDict, total=False):
    price: float
    balance_id: int


PurchasingFastbuyResponseItemGuarantee = TypedDict(
    "PurchasingFastbuyResponseItemGuarantee",
    {
        "duration": int,
        "class": str,
        "durationPhrase": str,
        "endDate": int,
        "active": bool,
        "cancelled": bool,
        "remainingTime": int,
        "remainingTimePhrase": str,
    },
)


class PurchasingFastbuyResponseItemLoginData(TypedDict):
    raw: str
    encodedRaw: str
    login: str
    password: str
    encodedPassword: str
    oldPassword: str
    encodedOldPassword: object


class PurchasingFastbuyResponseItemEmailLoginData(TypedDict):
    raw: str
    encodedRaw: str
    login: str
    password: str
    encodedPassword: str
    oldPassword: str
    encodedOldPassword: str


class PurchasingFastbuyResponseItemBuyer(TypedDict):
    user_id: int
    operation_date: int
    visitorIsBuyer: bool
    username: str
    is_banned: int
    display_style_group_id: int
    uniq_username_css: str
    user_group_id: int


class PurchasingFastbuyResponseItemAccountLinks(TypedDict):
    link: str
    text: str
    iconClass: str


class PurchasingFastbuyResponseItemTags1(TypedDict):
    tag_id: int
    title: str
    isDefault: bool
    forOwnedAccountsOnly: bool
    bc: str


PurchasingFastbuyResponseItemTags = TypedDict(
    "PurchasingFastbuyResponseItemTags",
    {
        "1": PurchasingFastbuyResponseItemTags1,
    },
)


class PurchasingFastbuyResponseItemExtraPrices(TypedDict):
    currency: str
    price: str


class PurchasingFastbuyResponseItemBumpSettings(TypedDict):
    canBumpItem: bool
    canBumpItemGlobally: bool
    shortErrorPhrase: object
    errorPhrase: object


class PurchasingFastbuyResponseItemSeller(TypedDict):
    user_id: int
    username: str
    avatar_date: int
    is_banned: int
    display_style_group_id: int
    joined_date: int
    sold_items_count: int
    active_items_count: int
    restore_data: str
    restore_percents: int
    isOnline: bool


class PurchasingFastbuyResponseItem(TypedDict):
    item_id: int
    item_state: str
    category_id: int
    published_date: int
    title: str
    description: str
    price: int
    update_stat_date: int
    refreshed_date: int
    edit_date: int
    login: str
    temp_email: str
    view_count: int
    is_sticky: int
    information: str
    item_origin: str
    extended_guarantee: int
    nsb: int
    allow_ask_discount: int
    title_en: str
    description_en: str
    information_en: str
    email_type: str
    email_provider: str
    item_domain: str
    resale_item_origin: str
    user_allow_ask_discount: int
    max_discount_percent: int
    market_custom_title: str
    feedback_data: str
    buyer_avatar_date: int
    buyer_user_group_id: int
    priceWithSellerFee: int
    guarantee: PurchasingFastbuyResponseItemGuarantee
    canViewLoginData: bool
    canUpdateItemStats: bool
    canReportItem: bool
    loginData: PurchasingFastbuyResponseItemLoginData
    canViewEmailLoginData: bool
    emailLoginData: PurchasingFastbuyResponseItemEmailLoginData
    showGetEmailCodeButton: bool
    getEmailCodeDisplayLogin: str
    buyer: PurchasingFastbuyResponseItemBuyer
    isPersonalAccount: bool
    sold_items_category_count: int
    restore_items_category_count: int
    rub_price: int
    price_currency: str
    canValidateAccount: bool
    canResellItemAfterPurchase: bool
    account_last_activity: int
    displayConvertedBalance: bool
    canViewAccountLink: bool
    accountLinks: list[PurchasingFastbuyResponseItemAccountLinks]
    accountLink: str
    emailLoginUrl: str
    canChangePassword: bool
    itemOriginPhrase: str
    visitorIsAuthor: bool
    canAskDiscount: bool
    tags: PurchasingFastbuyResponseItemTags
    customFields: list[object]
    externalAuth: list[object]
    isTrusted: bool
    isBirthdayToday: bool
    isIgnored: bool
    deposit: int
    extraPrices: list[PurchasingFastbuyResponseItemExtraPrices]
    canViewAccountLoginAndTempEmail: bool
    bumpSettings: PurchasingFastbuyResponseItemBumpSettings
    canCheckGuarantee: bool
    needToRequireVideoToViewLoginData: bool
    descriptionHtml: str
    descriptionEnHtml: str
    descriptionPlain: str
    descriptionEnPlain: str
    seller: PurchasingFastbuyResponseItemSeller


class PurchasingFastbuyResponse(TypedDict):
    status: str
    item: PurchasingFastbuyResponseItem
    system_info: Resp_SystemInfo


PurchasingCheckResponseItemGuarantee = TypedDict(
    "PurchasingCheckResponseItemGuarantee",
    {
        "duration": int,
        "class": str,
        "durationPhrase": str,
        "endDate": object,
        "active": object,
        "cancelled": object,
        "remainingTime": object,
    },
)


class PurchasingCheckResponseItemAccountLinks(TypedDict):
    link: str
    text: str
    iconClass: str


class PurchasingCheckResponseItemExtraPrices(TypedDict):
    currency: str
    price: str


class PurchasingCheckResponseItemBumpSettings(TypedDict):
    canBumpItem: bool
    canBumpItemGlobally: bool
    shortErrorPhrase: object
    errorPhrase: object


class PurchasingCheckResponseItemSeller(TypedDict):
    user_id: int
    username: str
    avatar_date: int
    is_banned: int
    display_style_group_id: int
    joined_date: int
    sold_items_count: int
    active_items_count: int
    restore_data: str
    restore_percents: object
    isOnline: bool


class PurchasingCheckResponseItem(TypedDict):
    item_id: int
    item_state: str
    category_id: int
    published_date: int
    title: str
    description: str
    price: int
    update_stat_date: int
    refreshed_date: int
    edit_date: int
    view_count: int
    is_sticky: int
    item_origin: str
    extended_guarantee: int
    nsb: int
    allow_ask_discount: int
    title_en: str
    description_en: str
    email_type: str
    email_provider: str
    item_domain: str
    resale_item_origin: str
    user_allow_ask_discount: int
    max_discount_percent: int
    market_custom_title: str
    feedback_data: str
    category_title: str
    category_url: str
    require_temp_email: int
    available_temp_email: int
    check_button_enabled: int
    checker_enabled: int
    buy_without_validation: int
    has_guarantee: int
    require_video_recording: int
    can_be_resold: int
    login_type: str
    require_email_login_data: int
    category_prefix_id: int
    ask_user_id: object
    ask_item_id: object
    ask_date: object
    discount_price: object
    discount_accepted: object
    user_alerted: object
    message: object
    min_price: int
    priceWithSellerFee: int
    guarantee: PurchasingCheckResponseItemGuarantee
    canViewLoginData: bool
    canUpdateItemStats: bool
    canReportItem: bool
    canViewEmailLoginData: bool
    showGetEmailCodeButton: bool
    isPersonalAccount: bool
    rub_price: int
    price_currency: str
    canValidateAccount: bool
    canResellItemAfterPurchase: bool
    isSmallExf: bool
    account_last_activity: int
    canViewAccountLink: bool
    accountLinks: list[PurchasingCheckResponseItemAccountLinks]
    accountLink: str
    emailLoginUrl: str
    canChangePassword: bool
    itemOriginPhrase: str
    visitorIsAuthor: bool
    canAskDiscount: bool
    tags: list[object]
    customFields: list[object]
    externalAuth: list[object]
    isTrusted: bool
    isBirthdayToday: bool
    isIgnored: bool
    deposit: int
    extraPrices: list[PurchasingCheckResponseItemExtraPrices]
    canViewAccountLoginAndTempEmail: bool
    bumpSettings: PurchasingCheckResponseItemBumpSettings
    canCheckGuarantee: bool
    needToRequireVideoToViewLoginData: bool
    descriptionHtml: str
    descriptionEnHtml: str
    descriptionPlain: str
    descriptionEnPlain: str
    seller: PurchasingCheckResponseItemSeller


class PurchasingCheckResponse(TypedDict):
    status: str
    item: PurchasingCheckResponseItem
    requireVideoRecording: bool
    system_info: Resp_SystemInfo


class PurchasingConfirmBody(TypedDict, total=False):
    price: int
    balance_id: int


class PurchasingConfirmResponseItemLoginData(TypedDict):
    raw: str
    encodedRaw: str
    login: str
    password: str
    encodedPassword: str
    oldPassword: str
    encodedOldPassword: str
    adviceToChangePassword: bool


class PurchasingConfirmResponseItem(TypedDict):
    loginData: PurchasingConfirmResponseItemLoginData


class _PurchasingConfirmResponseRequired(TypedDict):
    item: PurchasingConfirmResponseItem
    system_info: Resp_SystemInfo


class PurchasingConfirmResponse(_PurchasingConfirmResponseRequired, total=False):
    status: str


class _PurchasingDiscountrequestBodyRequired(TypedDict):
    discount_price: float


class PurchasingDiscountrequestBody(_PurchasingDiscountrequestBodyRequired, total=False):
    message: str


class PurchasingDiscountrequestResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class PurchasingDiscountcancelResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


# ─── CustomDiscountsApi Types ────────────────────────────────────────


class CustomDiscountsGetResponse(TypedDict):
    discounts: list[DiscountModel]
    total: int
    system_info: Resp_SystemInfo


class _CustomDiscountsCreateBodyRequired(TypedDict):
    user_id: int
    category_id: CategoryIDModel
    discount_percent: float
    min_price: float


class CustomDiscountsCreateBody(_CustomDiscountsCreateBodyRequired, total=False):
    max_price: float
    currency: CurrencyModel


class CustomDiscountsCreateResponse(TypedDict):
    discount: DiscountModel
    total: int
    system_info: Resp_SystemInfo


class _CustomDiscountsEditBodyRequired(TypedDict):
    discount_id: int


class CustomDiscountsEditBody(_CustomDiscountsEditBodyRequired, total=False):
    discount_percent: float
    min_price: float
    max_price: float


class CustomDiscountsEditResponse(TypedDict):
    discounts: list[DiscountModel]
    total: int
    system_info: Resp_SystemInfo


class CustomDiscountsDeleteBody(TypedDict):
    discount_id: int


class CustomDiscountsDeleteResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


# ─── PublishingApi Types ────────────────────────────────────────


class _PublishingFastsellBodyRequired(TypedDict):
    price: float
    category_id: Literal[
        1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 28, 30, 31
    ]
    currency: CurrencyModel
    item_origin: Literal[
        "brute",
        "phishing",
        "stealer",
        "personal",
        "resale",
        "autoreg",
        "dummy",
        "self_registration",
    ]


class PublishingFastsellBody(_PublishingFastsellBodyRequired, total=False):
    title: str
    title_en: str
    extended_guarantee: Literal[-1, 0, 1]
    allow_ask_discount: bool
    proxy_id: int
    random_proxy: bool
    description: str
    information: str
    login: str
    password: str
    login_password: str
    has_email_login_data: bool
    email_login_data: str
    email_type: Literal["native", "autoreg"]
    extra: ExtraModel


class PublishingFastsellResponse(TypedDict):
    item: ItemModel
    itemLink: str
    system_info: Resp_SystemInfo


class _PublishingAddBodyRequired(TypedDict):
    price: float
    category_id: Literal[
        1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 28, 30, 31
    ]
    currency: CurrencyModel
    item_origin: Literal[
        "brute",
        "phishing",
        "stealer",
        "personal",
        "resale",
        "autoreg",
        "dummy",
        "self_registration",
    ]


class PublishingAddBody(_PublishingAddBodyRequired, total=False):
    title: str
    title_en: str
    extended_guarantee: Literal[-1, 0, 1]
    description: str
    information: str
    forceTempEmail: bool
    resell_item_id: int
    has_email_login_data: bool
    email_login_data: str
    email_type: Literal["native", "autoreg"]
    allow_ask_discount: bool
    proxy_id: int
    random_proxy: bool


class PublishingAddResponse(TypedDict):
    status: str
    item: ItemModel
    system_info: Resp_SystemInfo


class PublishingCheckBody(TypedDict, total=False):
    resell_item_id: int
    random_proxy: bool
    login: str
    password: str
    login_password: str
    has_email_login_data: bool
    email_login_data: str
    email_type: Literal["native", "autoreg"]
    extra: ExtraModel


PublishingCheckResponseItemGuarantee = TypedDict(
    "PublishingCheckResponseItemGuarantee",
    {
        "duration": int,
        "class": str,
        "durationPhrase": str,
        "endDate": int,
        "active": bool,
        "cancelled": bool,
        "remainingTime": int,
        "remainingTimePhrase": str,
    },
)


class PublishingCheckResponseItemLoginData(TypedDict):
    raw: str
    encodedRaw: str
    login: str
    password: str
    encodedPassword: str
    oldPassword: str
    encodedOldPassword: object


class PublishingCheckResponseItemEmailLoginData(TypedDict):
    raw: str
    encodedRaw: str
    login: str
    password: str
    encodedPassword: str
    oldPassword: str
    encodedOldPassword: str


class PublishingCheckResponseItemBuyer(TypedDict):
    user_id: int
    operation_date: int
    visitorIsBuyer: bool
    username: str
    is_banned: int
    display_style_group_id: int
    uniq_username_css: str
    user_group_id: int


class PublishingCheckResponseItemAccountLinks(TypedDict):
    link: str
    text: str
    iconClass: str


class PublishingCheckResponseItemTags1(TypedDict):
    tag_id: int
    title: str
    isDefault: bool
    forOwnedAccountsOnly: bool
    bc: str


PublishingCheckResponseItemTags = TypedDict(
    "PublishingCheckResponseItemTags",
    {
        "1": PublishingCheckResponseItemTags1,
    },
)


class PublishingCheckResponseItemExtraPrices(TypedDict):
    currency: str
    price: str


class PublishingCheckResponseItemBumpSettings(TypedDict):
    canBumpItem: bool
    canBumpItemGlobally: bool
    shortErrorPhrase: object
    errorPhrase: object


class PublishingCheckResponseItemSeller(TypedDict):
    user_id: int
    username: str
    avatar_date: int
    is_banned: int
    display_style_group_id: int
    joined_date: int
    sold_items_count: int
    active_items_count: int
    restore_data: str
    restore_percents: int
    isOnline: bool


class PublishingCheckResponseItem(TypedDict):
    item_id: int
    item_state: str
    category_id: int
    published_date: int
    title: str
    description: str
    price: int
    update_stat_date: int
    refreshed_date: int
    edit_date: int
    login: str
    temp_email: str
    view_count: int
    is_sticky: int
    information: str
    item_origin: str
    extended_guarantee: int
    nsb: int
    allow_ask_discount: int
    title_en: str
    description_en: str
    information_en: str
    email_type: str
    email_provider: str
    item_domain: str
    resale_item_origin: str
    user_allow_ask_discount: int
    max_discount_percent: int
    market_custom_title: str
    feedback_data: str
    buyer_avatar_date: int
    buyer_user_group_id: int
    priceWithSellerFee: int
    guarantee: PublishingCheckResponseItemGuarantee
    canViewLoginData: bool
    canUpdateItemStats: bool
    canReportItem: bool
    loginData: PublishingCheckResponseItemLoginData
    canViewEmailLoginData: bool
    emailLoginData: PublishingCheckResponseItemEmailLoginData
    showGetEmailCodeButton: bool
    getEmailCodeDisplayLogin: str
    buyer: PublishingCheckResponseItemBuyer
    isPersonalAccount: bool
    sold_items_category_count: int
    restore_items_category_count: int
    rub_price: int
    price_currency: str
    canValidateAccount: bool
    canResellItemAfterPurchase: bool
    account_last_activity: int
    displayConvertedBalance: bool
    canViewAccountLink: bool
    accountLinks: list[PublishingCheckResponseItemAccountLinks]
    accountLink: str
    emailLoginUrl: str
    canChangePassword: bool
    itemOriginPhrase: str
    visitorIsAuthor: bool
    canAskDiscount: bool
    tags: PublishingCheckResponseItemTags
    customFields: list[object]
    externalAuth: list[object]
    isTrusted: bool
    isBirthdayToday: bool
    isIgnored: bool
    deposit: int
    extraPrices: list[PublishingCheckResponseItemExtraPrices]
    canViewAccountLoginAndTempEmail: bool
    bumpSettings: PublishingCheckResponseItemBumpSettings
    canCheckGuarantee: bool
    needToRequireVideoToViewLoginData: bool
    descriptionHtml: str
    descriptionEnHtml: str
    descriptionPlain: str
    descriptionEnPlain: str
    seller: PublishingCheckResponseItemSeller


class PublishingCheckResponse(TypedDict):
    status: str
    item: PublishingCheckResponseItem
    system_info: Resp_SystemInfo


class _PublishingExternalBodyRequired(TypedDict):
    type: Literal["socialclub"]


class PublishingExternalBody(_PublishingExternalBodyRequired, total=False):
    login: str
    email_login_data: str
    cookies: str


class PublishingExternalResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


# ─── PaymentsApi Types ────────────────────────────────────────


class PaymentsInvoiceGetParams(TypedDict, total=False):
    invoice_id: int
    payment_id: str


class PaymentsInvoiceGetResponse(TypedDict):
    invoice: InvoiceModel
    system_info: Resp_SystemInfo


class _PaymentsInvoiceCreateBodyRequired(TypedDict):
    currency: CurrencyModel
    amount: float
    payment_id: str
    comment: str
    url_success: str
    merchant_id: int


class PaymentsInvoiceCreateBody(_PaymentsInvoiceCreateBodyRequired, total=False):
    url_callback: str
    required_telegram_id: int
    required_telegram_username: str
    lifetime: float
    additional_data: str
    is_test: bool


class PaymentsInvoiceCreateResponse(TypedDict):
    invoice: InvoiceModel
    system_info: Resp_SystemInfo


class PaymentsInvoiceListParams(TypedDict, total=False):
    page: int
    currency: CurrencyModel
    status: Literal["paid", "not_paid"]
    amount: float
    merchant_id: int


class PaymentsInvoiceListResponse(TypedDict):
    invoices: list[InvoiceModel]
    count: int
    page: int
    perPage: int
    system_info: Resp_SystemInfo


class PaymentsCurrencyResponseCurrencyListBTC(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListETH(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListBNB(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListBCH(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListXMR(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListSOL(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListLTC(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListDASH(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListTON(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListUSDT(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListMATIC(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListTRX(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListDOGE(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListKWD(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListGBP(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListCHF(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListEUR(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListUSD(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListSGD(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListCAD(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListAUD(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListNZD(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListBGN(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListGEL(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListILS(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListQAR(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListPEN(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListAED(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListSAR(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListPLN(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListMYR(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListRON(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListBRL(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListDKK(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListCNY(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListHKD(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListSEK(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListNOK(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListZAR(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListMXN(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListCZK(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListTWD(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListTHB(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListTRY(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListUAH(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListUYU(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListPHP(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListINR(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListRUB(TypedDict):
    title: str
    rate: int
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListRSD(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListJPY(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListHUF(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListKZT(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListCRC(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListCLP(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListARS(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListKRW(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListCOP(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListIDR(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyListVND(TypedDict):
    title: str
    rate: float
    formattedRate: str
    symbol: str


class PaymentsCurrencyResponseCurrencyList(TypedDict):
    BTC: PaymentsCurrencyResponseCurrencyListBTC
    ETH: PaymentsCurrencyResponseCurrencyListETH
    BNB: PaymentsCurrencyResponseCurrencyListBNB
    BCH: PaymentsCurrencyResponseCurrencyListBCH
    XMR: PaymentsCurrencyResponseCurrencyListXMR
    SOL: PaymentsCurrencyResponseCurrencyListSOL
    LTC: PaymentsCurrencyResponseCurrencyListLTC
    DASH: PaymentsCurrencyResponseCurrencyListDASH
    TON: PaymentsCurrencyResponseCurrencyListTON
    USDT: PaymentsCurrencyResponseCurrencyListUSDT
    MATIC: PaymentsCurrencyResponseCurrencyListMATIC
    TRX: PaymentsCurrencyResponseCurrencyListTRX
    DOGE: PaymentsCurrencyResponseCurrencyListDOGE
    KWD: PaymentsCurrencyResponseCurrencyListKWD
    GBP: PaymentsCurrencyResponseCurrencyListGBP
    CHF: PaymentsCurrencyResponseCurrencyListCHF
    EUR: PaymentsCurrencyResponseCurrencyListEUR
    USD: PaymentsCurrencyResponseCurrencyListUSD
    SGD: PaymentsCurrencyResponseCurrencyListSGD
    CAD: PaymentsCurrencyResponseCurrencyListCAD
    AUD: PaymentsCurrencyResponseCurrencyListAUD
    NZD: PaymentsCurrencyResponseCurrencyListNZD
    BGN: PaymentsCurrencyResponseCurrencyListBGN
    GEL: PaymentsCurrencyResponseCurrencyListGEL
    ILS: PaymentsCurrencyResponseCurrencyListILS
    QAR: PaymentsCurrencyResponseCurrencyListQAR
    PEN: PaymentsCurrencyResponseCurrencyListPEN
    AED: PaymentsCurrencyResponseCurrencyListAED
    SAR: PaymentsCurrencyResponseCurrencyListSAR
    PLN: PaymentsCurrencyResponseCurrencyListPLN
    MYR: PaymentsCurrencyResponseCurrencyListMYR
    RON: PaymentsCurrencyResponseCurrencyListRON
    BRL: PaymentsCurrencyResponseCurrencyListBRL
    DKK: PaymentsCurrencyResponseCurrencyListDKK
    CNY: PaymentsCurrencyResponseCurrencyListCNY
    HKD: PaymentsCurrencyResponseCurrencyListHKD
    SEK: PaymentsCurrencyResponseCurrencyListSEK
    NOK: PaymentsCurrencyResponseCurrencyListNOK
    ZAR: PaymentsCurrencyResponseCurrencyListZAR
    MXN: PaymentsCurrencyResponseCurrencyListMXN
    CZK: PaymentsCurrencyResponseCurrencyListCZK
    TWD: PaymentsCurrencyResponseCurrencyListTWD
    THB: PaymentsCurrencyResponseCurrencyListTHB
    TRY: PaymentsCurrencyResponseCurrencyListTRY
    UAH: PaymentsCurrencyResponseCurrencyListUAH
    UYU: PaymentsCurrencyResponseCurrencyListUYU
    PHP: PaymentsCurrencyResponseCurrencyListPHP
    INR: PaymentsCurrencyResponseCurrencyListINR
    RUB: PaymentsCurrencyResponseCurrencyListRUB
    RSD: PaymentsCurrencyResponseCurrencyListRSD
    JPY: PaymentsCurrencyResponseCurrencyListJPY
    HUF: PaymentsCurrencyResponseCurrencyListHUF
    KZT: PaymentsCurrencyResponseCurrencyListKZT
    CRC: PaymentsCurrencyResponseCurrencyListCRC
    CLP: PaymentsCurrencyResponseCurrencyListCLP
    ARS: PaymentsCurrencyResponseCurrencyListARS
    KRW: PaymentsCurrencyResponseCurrencyListKRW
    COP: PaymentsCurrencyResponseCurrencyListCOP
    IDR: PaymentsCurrencyResponseCurrencyListIDR
    VND: PaymentsCurrencyResponseCurrencyListVND


class PaymentsCurrencyResponse(TypedDict):
    currencyList: PaymentsCurrencyResponseCurrencyList
    lastUpdate: int
    visitorCurrency: str
    system_info: Resp_SystemInfo


class PaymentsBalanceListResponseFromBalance(TypedDict):
    balance: str
    convertedBalance: int
    fullTitle: str
    title: str
    type: str


PaymentsBalanceListResponseFrom = TypedDict(
    "PaymentsBalanceListResponseFrom",
    {
        "balance": PaymentsBalanceListResponseFromBalance,
        "12345": BalanceModel,
    },
)


class PaymentsBalanceListResponseTo(TypedDict):
    balance: UserModel


PaymentsBalanceListResponse = TypedDict(
    "PaymentsBalanceListResponse",
    {
        "from": PaymentsBalanceListResponseFrom,
        "to": PaymentsBalanceListResponseTo,
        "system_info": Resp_SystemInfo,
    },
)


class PaymentsBalanceexchangeBody(TypedDict):
    from_balance: str
    to_balance: str
    amount: int


class PaymentsBalanceexchangeResponseFromBalance(TypedDict):
    balance: str
    convertedBalance: int
    fullTitle: str
    title: str
    type: str


PaymentsBalanceexchangeResponseFrom = TypedDict(
    "PaymentsBalanceexchangeResponseFrom",
    {
        "balance": PaymentsBalanceexchangeResponseFromBalance,
        "12345": BalanceModel,
    },
)


class PaymentsBalanceexchangeResponseTo(TypedDict):
    balance: UserModel


PaymentsBalanceexchangeResponse = TypedDict(
    "PaymentsBalanceexchangeResponse",
    {
        "from": PaymentsBalanceexchangeResponseFrom,
        "to": PaymentsBalanceexchangeResponseTo,
        "system_info": Resp_SystemInfo,
    },
)


class _PaymentsTransferBodyRequired(TypedDict):
    amount: int
    currency: CurrencyModel


class PaymentsTransferBody(_PaymentsTransferBodyRequired, total=False):
    user_id: int
    username: str
    comment: str
    telegram_deal: bool
    telegram_username: str
    transfer_hold: bool
    hold_length_value: int
    hold_length_option: Literal["hour", "day", "week", "month", "year"]


class PaymentsTransferResponse(TypedDict):
    status: str
    message: str
    system_info: Resp_SystemInfo


class PaymentsFeeParams(TypedDict, total=False):
    amount: float


class PaymentsFeeResponseCalculator(TypedDict):
    inputAmount: int
    commissionAmount: int
    totalOutputAmount: int


class PaymentsFeeResponse(TypedDict):
    commission_percentage: int
    spentCurrentMonth: int
    calculator: PaymentsFeeResponseCalculator
    system_info: Resp_SystemInfo


class PaymentsCancelBody(TypedDict):
    payment_id: int


class PaymentsCancelResponse(TypedDict):
    status: str
    message: str
    system_info: Resp_SystemInfo


class PaymentsHistoryParams(TypedDict, total=False):
    type: Literal[
        "paid_item",
        "sold_item",
        "withdrawal_balance",
        "refilled_balance",
        "internal_purchase",
        "money_transfer",
        "receiving_money",
        "claim_hold",
        "insurance_deposit",
        "paid_mail",
        "contest",
        "invoice",
        "balance_exchange",
    ]
    pmin: int
    pmax: int
    currency: CurrencyModel
    page: int
    operation_id_lt: int
    receiver: str
    sender: str
    is_api: bool
    startDate: str
    endDate: str
    wallet: str
    comment: str
    is_hold: bool
    show_payment_stats: bool


class PaymentsHistoryResponsePayments1234567890Data(TypedDict):
    user_id: int
    username: str
    comment: str
    fee: int
    invoice_id: int
    is_test: bool
    payment_id: str
    commentPlain: str
    is_banned: int
    display_style_group_id: int
    uniq_username_css: str
    uniq_banner: str
    avatar_date: int
    user_group_id: int
    username_html: str
    avatar: str


class PaymentsHistoryResponsePayments1234567890Label(TypedDict):
    title: str


class PaymentsHistoryResponsePayments1234567890Merchant(TypedDict):
    merchant_id: int
    name: str
    user_id: int
    created_date: int
    secret_key: str
    avatar_data: str
    url: str


class PaymentsHistoryResponsePayments1234567890User(TypedDict):
    user_id: int
    user_balance: str
    user_hold: str
    user_balance_with_hold: float


class PaymentsHistoryResponsePayments1234567890(TypedDict):
    operation_id: int
    operation_date: int
    operation_type: str
    outgoing_sum: str
    incoming_sum: str
    item_id: int
    wallet: str
    is_finished: int
    is_hold: int
    payment_system: str
    data: PaymentsHistoryResponsePayments1234567890Data
    hold_end_date: int
    operation_end_date: int
    api: int
    sum: str
    payment_status: str
    supportLink: object
    paymentSystemIcons: list[object]
    canCancelPaidMailPayment: bool
    canCancelBalanceTransfer: bool
    canCancelBalancePayout: bool
    canCancelBalanceHold: bool
    canFinishBalanceTransfer: bool
    canFinishBalancePayout: bool
    canFinishBalanceHold: bool
    label: PaymentsHistoryResponsePayments1234567890Label
    merchant: PaymentsHistoryResponsePayments1234567890Merchant
    user: PaymentsHistoryResponsePayments1234567890User


PaymentsHistoryResponsePayments = TypedDict(
    "PaymentsHistoryResponsePayments",
    {
        "1234567890": PaymentsHistoryResponsePayments1234567890,
    },
)


class PaymentsHistoryResponsePageNavParams(TypedDict):
    type: str
    startDate: str
    endDate: str


class PaymentsHistoryResponseInput(TypedDict):
    user_id: int
    type: str
    startDate: str
    endDate: str
    page: int
    period_label: str
    receiver: str
    sender: str
    comment: str
    pmin: str
    pmax: str
    category_id: int
    wallet: str
    is_hold: bool
    currency: str
    operation_id_lt: int


class PaymentsHistoryResponse(TypedDict):
    payments: PaymentsHistoryResponsePayments
    perPage: str
    page: int
    pageNavLink: str
    pageNavParams: PaymentsHistoryResponsePageNavParams
    periodLabel: str
    periodLabelPhrase: str
    filterDatesDefault: bool
    input: PaymentsHistoryResponseInput
    paymentStats: object
    hasNextPage: bool
    lastOperationId: int
    nextPageHref: str
    system_info: Resp_SystemInfo


class PaymentsPayoutservicesResponseSystemsProvidersBEP20(TypedDict):
    title: str
    isUnavailable: bool


class PaymentsPayoutservicesResponseSystemsProvidersTRC20(TypedDict):
    title: str
    isUnavailable: bool


class PaymentsPayoutservicesResponseSystemsProvidersERC20(TypedDict):
    title: str
    isUnavailable: bool


class PaymentsPayoutservicesResponseSystemsProvidersTRX(TypedDict):
    title: str
    isUnavailable: bool


class PaymentsPayoutservicesResponseSystemsProvidersBTC(TypedDict):
    title: str
    isUnavailable: bool


class PaymentsPayoutservicesResponseSystemsProvidersTON(TypedDict):
    title: str
    isUnavailable: bool


class PaymentsPayoutservicesResponseSystemsProvidersETH(TypedDict):
    title: str
    isUnavailable: bool


class PaymentsPayoutservicesResponseSystemsProvidersLTC(TypedDict):
    title: str
    isUnavailable: bool


class PaymentsPayoutservicesResponseSystemsProvidersBNB(TypedDict):
    title: str
    isUnavailable: bool


class PaymentsPayoutservicesResponseSystemsProvidersDASH(TypedDict):
    title: str
    isUnavailable: bool


class PaymentsPayoutservicesResponseSystemsProvidersDOGE(TypedDict):
    title: str
    isUnavailable: bool


class PaymentsPayoutservicesResponseSystemsProvidersXMR(TypedDict):
    title: str
    isUnavailable: bool


class PaymentsPayoutservicesResponseSystemsProvidersSOL(TypedDict):
    title: str
    isUnavailable: bool


class PaymentsPayoutservicesResponseSystemsProvidersBCH(TypedDict):
    title: str
    isUnavailable: bool


class PaymentsPayoutservicesResponseSystemsProviders(TypedDict):
    BEP20: PaymentsPayoutservicesResponseSystemsProvidersBEP20
    TRC20: PaymentsPayoutservicesResponseSystemsProvidersTRC20
    ERC20: PaymentsPayoutservicesResponseSystemsProvidersERC20
    TRX: PaymentsPayoutservicesResponseSystemsProvidersTRX
    BTC: PaymentsPayoutservicesResponseSystemsProvidersBTC
    TON: PaymentsPayoutservicesResponseSystemsProvidersTON
    ETH: PaymentsPayoutservicesResponseSystemsProvidersETH
    LTC: PaymentsPayoutservicesResponseSystemsProvidersLTC
    BNB: PaymentsPayoutservicesResponseSystemsProvidersBNB
    DASH: PaymentsPayoutservicesResponseSystemsProvidersDASH
    DOGE: PaymentsPayoutservicesResponseSystemsProvidersDOGE
    XMR: PaymentsPayoutservicesResponseSystemsProvidersXMR
    SOL: PaymentsPayoutservicesResponseSystemsProvidersSOL
    BCH: PaymentsPayoutservicesResponseSystemsProvidersBCH


class PaymentsPayoutservicesResponseSystems(TypedDict):
    system: str
    commission: str
    min: int
    max: int
    instant_payout: bool
    problematic_payout: bool
    is_unavailable: bool
    p2p: bool
    has_wallet: bool
    providers: PaymentsPayoutservicesResponseSystemsProviders


class PaymentsPayoutservicesResponse(TypedDict):
    systems: list[PaymentsPayoutservicesResponseSystems]
    system_info: Resp_SystemInfo


class _PaymentsPayoutBodyRequired(TypedDict):
    payment_system: str
    wallet: str
    amount: float
    currency: CurrencyModel


class PaymentsPayoutBody(_PaymentsPayoutBodyRequired, total=False):
    include_fee: bool
    extra: dict[str, object]


class PaymentsPayoutResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


# ─── AutoPaymentsApi Types ────────────────────────────────────────


class AutoPaymentsListResponsePayments1234567890ReceiverLinks(TypedDict):
    permalink: str
    detail: str
    avatar: str
    avatar_big: str
    avatar_small: str
    followers: str
    followings: str
    ignore: str
    timeline: str


class AutoPaymentsListResponsePayments1234567890ReceiverPermissions(TypedDict):
    edit: bool
    follow: bool
    ignore: bool
    profile_post: bool


class AutoPaymentsListResponsePayments1234567890ReceiverFields(TypedDict):
    id: str
    title: str
    description: str
    position: str
    is_required: bool
    value: str


class AutoPaymentsListResponsePayments1234567890Receiver(TypedDict):
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
    links: AutoPaymentsListResponsePayments1234567890ReceiverLinks
    permissions: AutoPaymentsListResponsePayments1234567890ReceiverPermissions
    user_is_ignored: bool
    user_is_visitor: bool
    user_group_id: int
    fields: list[AutoPaymentsListResponsePayments1234567890ReceiverFields]


class AutoPaymentsListResponsePayments1234567890(TypedDict):
    user_id: int
    receiver_id: int
    amount: str
    description: str
    next_payment: int
    next_alert_date: int
    auto_payment_id: int
    day: str
    receiver: AutoPaymentsListResponsePayments1234567890Receiver


AutoPaymentsListResponsePayments = TypedDict(
    "AutoPaymentsListResponsePayments",
    {
        "1234567890": AutoPaymentsListResponsePayments1234567890,
    },
)


class AutoPaymentsListResponse(TypedDict):
    payments: AutoPaymentsListResponsePayments
    system_info: Resp_SystemInfo


class _AutoPaymentsCreateBodyRequired(TypedDict):
    username_receiver: str
    day: Literal[
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
    ]
    amount: float


class AutoPaymentsCreateBody(_AutoPaymentsCreateBodyRequired, total=False):
    secret_answer: str
    currency: CurrencyModel
    description: str


class AutoPaymentsCreateResponse(TypedDict):
    status: str
    message: str
    auto_payment_id: int
    system_info: Resp_SystemInfo


class AutoPaymentsDeleteBody(TypedDict):
    auto_payment_id: int


class AutoPaymentsDeleteResponse(TypedDict):
    status: str
    message: str
    system_info: Resp_SystemInfo


# ─── ProxyApi Types ────────────────────────────────────────


class ProxyGetResponseProxiesProxy(TypedDict):
    proxy_id: int
    user_id: int
    proxy_ip: str
    proxy_port: int
    proxy_user: str
    proxy_pass: str
    proxyString: str


class ProxyGetResponseProxies(TypedDict):
    proxy: ProxyGetResponseProxiesProxy


class ProxyGetResponse(TypedDict):
    proxies: list[ProxyGetResponseProxies]
    system_info: Resp_SystemInfo


class ProxyAddBody(TypedDict, total=False):
    proxy_ip: str
    proxy_port: int
    proxy_user: str
    proxy_pass: str
    proxy_row: str


class ProxyAddResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ProxyDeleteBody(TypedDict, total=False):
    proxy_id: int
    delete_all: bool


class ProxyDeleteResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


# ─── ImapApi Types ────────────────────────────────────────


class ImapCreateBody(TypedDict):
    domain: str
    imap_server: str
    port: int
    secure: bool


class ImapCreateResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ImapDeleteBody(TypedDict):
    domain: str


class ImapDeleteResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


# ─── BatchApi Types ────────────────────────────────────────


BatchBatchBody = list[dict[str, object]]


class BatchBatchResponseJobsJob_id(TypedDict, total=False):
    _job_result: str
    _job_error: str


class BatchBatchResponseJobs(TypedDict):
    job_id: BatchBatchResponseJobsJob_id


class _BatchBatchResponseRequired(TypedDict):
    jobs: BatchBatchResponseJobs


class BatchBatchResponse(_BatchBatchResponseRequired, total=False):
    system_info: Resp_SystemInfo
