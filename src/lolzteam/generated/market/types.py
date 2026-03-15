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


class UserModel(TypedDict):
    active_items_count: int
    activity_visible: bool
    age: int
    balance: str
    balances: list[dict[str, object]]
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
    custom_fields: dict[str, object]
    custom_title: str
    deposit: int
    dob: dict[str, object]
    feedback_data: dict[str, object]
    hold: str
    homepage: str
    imap_data: dict[str, object]
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
    public_tags: list[dict[str, object]]
    register_date: int
    rendered: dict[str, object]
    restore_count: int
    restore_data: dict[str, object]
    short_link: str
    sold_items_count: int
    tags: list[dict[str, object]]
    telegram_client: dict[str, object]
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


class ConfirmationCodeModel(TypedDict):
    item: ItemModel
    codeData: dict[str, object]


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
    bumpSettings: dict[str, object]
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
    seller: dict[str, object]


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
    priceWithSellerFee: int | float
    guarantee: dict[str, object]
    canViewLoginData: bool
    canUpdateItemStats: bool
    canReportItem: bool
    canViewItemViews: bool
    loginData: dict[str, object]
    canViewEmailLoginData: bool
    copyFormatData: dict[str, object]
    showGetEmailCodeButton: bool
    getEmailCodeDisplayLogin: object
    buyer: dict[str, object]
    isPersonalAccount: bool
    rub_price: int
    price_currency: str
    priceWithSellerFeeLabel: str
    canValidateAccount: bool
    canResellItemAfterPurchase: bool
    isSmallExf: bool
    account_last_activity: int
    canViewAccountLink: bool
    accountLinks: list[dict[str, object]]
    accountLink: str
    imagePreviewLinks: list[str]
    canChangePassword: bool
    canChangeEmailPassword: bool
    uniqueKeyExists: bool
    itemOriginPhrase: str
    visitorIsAuthor: bool
    canAskDiscount: bool
    tags: dict[str, object]
    customFields: dict[str, object]
    externalAuth: list[object]
    isTrusted: bool
    isBirthdayToday: bool
    isIgnored: bool
    deposit: int
    extraPrices: list[dict[str, object]]
    canViewAccountLoginAndTempEmail: bool
    bumpSettings: dict[str, object]
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
    seller: dict[str, object]


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
        "inv_min": int | float,
        "inv_max": int | float,
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
        "gifts_purchase_min": int | float,
        "gifts_purchase_max": int | float,
        "refunds_purchase_min": int | float,
        "refunds_purchase_max": int | float,
        "ingame_purchase_min": int | float,
        "ingame_purchase_max": int | float,
        "games_purchase_min": int | float,
        "games_purchase_max": int | float,
        "purchase_min": int | float,
        "purchase_max": int | float,
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


class CategorySteamResponse(TypedDict):
    items: list[dict[str, object]]
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


class CategoryFortniteResponse(TypedDict):
    items: list[dict[str, object]]
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


class CategoryMihoyoResponse(TypedDict):
    items: list[dict[str, object]]
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


class CategoryRiotResponse(TypedDict):
    items: list[dict[str, object]]
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


class CategoryTelegramResponse(TypedDict):
    items: list[dict[str, object]]
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


class CategorySupercellResponse(TypedDict):
    items: list[dict[str, object]]
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


class CategoryEaResponse(TypedDict):
    items: list[dict[str, object]]
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


class CategoryWotResponse(TypedDict):
    items: list[dict[str, object]]
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


class CategoryWotblitzResponse(TypedDict):
    items: list[dict[str, object]]
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


class CategoryGiftsResponse(TypedDict):
    items: list[dict[str, object]]
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
        "balance_min": int | float,
        "balance_max": int | float,
        "rewards_balance_min": int | float,
        "rewards_balance_max": int | float,
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


class CategoryEpicgamesResponse(TypedDict):
    items: list[dict[str, object]]
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


class CategoryEscapefromtarkovResponse(TypedDict):
    items: list[dict[str, object]]
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


class CategorySocialclubResponse(TypedDict):
    items: list[dict[str, object]]
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
        "balance_min": int | float,
        "balance_max": int | float,
        "transactions": YesNoNoMatterScheme,
        "reg": int,
        "reg_period": Literal["day", "month", "year"],
    },
    total=False,
)


class CategoryUplayResponse(TypedDict):
    items: list[dict[str, object]]
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


class CategoryDiscordResponse(TypedDict):
    items: list[dict[str, object]]
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


class CategoryTiktokResponse(TypedDict):
    items: list[dict[str, object]]
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


class CategoryInstagramResponse(TypedDict):
    items: list[dict[str, object]]
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


class CategoryBattlenetResponse(TypedDict):
    items: list[dict[str, object]]
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


class CategoryChatgptResponse(TypedDict):
    items: list[dict[str, object]]
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


class CategoryVpnResponse(TypedDict):
    items: list[dict[str, object]]
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


class CategoryRobloxResponse(TypedDict):
    items: list[dict[str, object]]
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


class CategoryWarfaceResponse(TypedDict):
    items: list[dict[str, object]]
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


class CategoryMinecraftResponse(TypedDict):
    items: list[dict[str, object]]
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


class CategoryHytaleResponse(TypedDict):
    items: list[dict[str, object]]
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


class CategoryListResponse(TypedDict):
    category: dict[str, object]
    system_info: Resp_SystemInfo


class CategoryParamsResponse(TypedDict, total=False):
    category: dict[str, object]
    params: list[dict[str, object]]
    base_params: dict[str, object]
    system_info: Resp_SystemInfo


class CategoryGamesResponse(TypedDict, total=False):
    games: list[dict[str, object]]
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


class ListStatesResponse(TypedDict):
    userItemStates: dict[str, object]
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


class ManagingCreateclaimResponse(TypedDict):
    thread: dict[str, object]
    system_info: dict[str, object]


class ManagingBulkgetBody(TypedDict, total=False):
    item_id: list[ItemIDModel]
    parse_same_item_ids: bool


class ManagingBulkgetResponse(TypedDict):
    items: list[dict[str, object]]
    left_item_id: list[int]
    system_info: Resp_SystemInfo


class ManagingSteaminventoryvalueParams(TypedDict, total=False):
    app_id: Literal[730, 578080, 753, 570, 440, 252490, 304930, 232090, 322330]
    currency: CurrencyModel
    ignore_cache: bool


class ManagingSteaminventoryvalueResponse(TypedDict, total=False):
    query: str
    data: dict[str, object]
    appId: int
    system_info: Resp_SystemInfo


class _ManagingSteamvalueParamsRequired(TypedDict):
    link: str


class ManagingSteamvalueParams(_ManagingSteamvalueParamsRequired, total=False):
    app_id: Literal[730, 578080, 753, 570, 440, 252490, 304930, 232090, 322330]
    currency: CurrencyModel
    ignore_cache: bool


class ManagingSteamvalueResponse(TypedDict, total=False):
    query: str
    data: dict[str, object]
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


class ManagingEmailcodeResponse(TypedDict):
    item: ItemModel
    codeData: dict[str, object]


class ManagingGetletters2Params(TypedDict, total=False):
    email_password: str
    email: str
    password: str
    limit: int


class ManagingGetletters2Response(TypedDict):
    email: str
    letters: list[dict[str, object]]
    system_info: Resp_SystemInfo


class ManagingSteamGetmafileResponse(TypedDict):
    maFile: dict[str, object]
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


class ManagingSteammafilecodeResponse(TypedDict):
    item: ItemModel
    codeData: dict[str, object]


class ManagingSteamsdaBody(TypedDict, total=False):
    id: int
    nonce: int


class ManagingSteamsdaResponse(TypedDict):
    status: str
    message: str
    system_info: Resp_SystemInfo


class ManagingTelegramcodeResponse(TypedDict):
    item: ItemModel
    codes: dict[str, object]


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


class ManagingTempemailpasswordResponse(TypedDict):
    item: dict[str, object]


class ManagingTagBody(TypedDict):
    tag_id: int


class ManagingTagResponse(TypedDict):
    itemId: int
    tag: dict[str, object]
    addedTagId: int
    deleteTags: list[int]
    system_info: Resp_SystemInfo


class ManagingUntagBody(TypedDict):
    tag_id: int


class ManagingUntagResponse(TypedDict):
    itemId: int
    tag: dict[str, object]
    addedTagId: int
    deleteTags: list[int]
    system_info: Resp_SystemInfo


class ManagingPublictagBody(TypedDict):
    tag_id: int


class ManagingPublictagResponse(TypedDict):
    itemId: int
    tag: dict[str, object]
    addedTagId: int
    deleteTags: list[int]
    system_info: Resp_SystemInfo


class ManagingPublicuntagBody(TypedDict):
    tag_id: int


class ManagingPublicuntagResponse(TypedDict):
    itemId: int
    tag: dict[str, object]
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


class ProfileClaimsResponse(TypedDict):
    claims: list[dict[str, object]]
    stats: dict[str, object]
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
    price: int | float
    balance_id: int


class PurchasingFastbuyResponse(TypedDict):
    status: str
    item: dict[str, object]
    system_info: Resp_SystemInfo


class PurchasingCheckResponse(TypedDict):
    status: str
    item: dict[str, object]
    requireVideoRecording: bool
    system_info: Resp_SystemInfo


class PurchasingConfirmBody(TypedDict, total=False):
    price: int
    balance_id: int


class _PurchasingConfirmResponseRequired(TypedDict):
    item: dict[str, object]
    system_info: Resp_SystemInfo


class PurchasingConfirmResponse(_PurchasingConfirmResponseRequired, total=False):
    status: str


class _PurchasingDiscountrequestBodyRequired(TypedDict):
    discount_price: int | float


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
    discount_percent: int | float
    min_price: int | float


class CustomDiscountsCreateBody(_CustomDiscountsCreateBodyRequired, total=False):
    max_price: int | float
    currency: CurrencyModel


class CustomDiscountsCreateResponse(TypedDict):
    discount: DiscountModel
    total: int
    system_info: Resp_SystemInfo


class _CustomDiscountsEditBodyRequired(TypedDict):
    discount_id: int


class CustomDiscountsEditBody(_CustomDiscountsEditBodyRequired, total=False):
    discount_percent: int | float
    min_price: int | float
    max_price: int | float


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
    price: int | float
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
    price: int | float
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


class PublishingCheckResponse(TypedDict):
    status: str
    item: dict[str, object]
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
    amount: int | float
    payment_id: str
    comment: str
    url_success: str
    merchant_id: int


class PaymentsInvoiceCreateBody(_PaymentsInvoiceCreateBodyRequired, total=False):
    url_callback: str
    required_telegram_id: int
    required_telegram_username: str
    lifetime: int | float
    additional_data: str
    is_test: bool


class PaymentsInvoiceCreateResponse(TypedDict):
    invoice: InvoiceModel
    system_info: Resp_SystemInfo


class PaymentsInvoiceListParams(TypedDict, total=False):
    page: int
    currency: CurrencyModel
    status: Literal["paid", "not_paid"]
    amount: int | float
    merchant_id: int


class PaymentsInvoiceListResponse(TypedDict):
    invoices: list[InvoiceModel]
    count: int
    page: int
    perPage: int
    system_info: Resp_SystemInfo


class PaymentsCurrencyResponse(TypedDict):
    currencyList: dict[str, object]
    lastUpdate: int
    visitorCurrency: str
    system_info: Resp_SystemInfo


PaymentsBalanceListResponse = TypedDict(
    "PaymentsBalanceListResponse",
    {
        "from": dict[str, object],
        "to": dict[str, object],
        "system_info": Resp_SystemInfo,
    },
)


class PaymentsBalanceexchangeBody(TypedDict):
    from_balance: str
    to_balance: str
    amount: int


PaymentsBalanceexchangeResponse = TypedDict(
    "PaymentsBalanceexchangeResponse",
    {
        "from": dict[str, object],
        "to": dict[str, object],
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
    amount: int | float


class PaymentsFeeResponse(TypedDict):
    commission_percentage: int
    spentCurrentMonth: int
    calculator: dict[str, object]
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


class PaymentsHistoryResponse(TypedDict):
    payments: dict[str, object]
    perPage: str
    page: int
    pageNavLink: str
    pageNavParams: dict[str, object]
    periodLabel: str
    periodLabelPhrase: str
    filterDatesDefault: bool
    input: dict[str, object]
    paymentStats: object
    hasNextPage: bool
    lastOperationId: int
    nextPageHref: str
    system_info: Resp_SystemInfo


class PaymentsPayoutservicesResponse(TypedDict):
    systems: list[dict[str, object]]
    system_info: Resp_SystemInfo


class _PaymentsPayoutBodyRequired(TypedDict):
    payment_system: str
    wallet: str
    amount: int | float
    currency: CurrencyModel


class PaymentsPayoutBody(_PaymentsPayoutBodyRequired, total=False):
    include_fee: bool
    extra: dict[str, object]


class PaymentsPayoutResponse(TypedDict, total=False):
    status: str
    message: str
    system_info: Resp_SystemInfo


# ─── AutoPaymentsApi Types ────────────────────────────────────────


class AutoPaymentsListResponse(TypedDict):
    payments: dict[str, object]
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
    amount: int | float


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


class ProxyGetResponse(TypedDict):
    proxies: list[dict[str, object]]
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


class _BatchBatchResponseRequired(TypedDict):
    jobs: dict[str, object]


class BatchBatchResponse(_BatchBatchResponseRequired, total=False):
    system_info: Resp_SystemInfo
