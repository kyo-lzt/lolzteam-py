# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING, Literal

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
        AutoPaymentsCreateBody,
        AutoPaymentsCreateResponse,
        AutoPaymentsDeleteBody,
        AutoPaymentsDeleteResponse,
        AutoPaymentsListResponse,
        BatchBatchBody,
        BatchBatchResponse,
        CartAddBody,
        CartAddResponse,
        CartDeleteBody,
        CartDeleteResponse,
        CartGetParams,
        CartGetResponse,
        CategoryAllParams,
        CategoryAllResponse,
        CategoryBattlenetParams,
        CategoryBattlenetResponse,
        CategoryChatgptParams,
        CategoryChatgptResponse,
        CategoryDiscordParams,
        CategoryDiscordResponse,
        CategoryEaParams,
        CategoryEaResponse,
        CategoryEpicgamesParams,
        CategoryEpicgamesResponse,
        CategoryEscapefromtarkovParams,
        CategoryEscapefromtarkovResponse,
        CategoryFortniteParams,
        CategoryFortniteResponse,
        CategoryGamesResponse,
        CategoryGiftsParams,
        CategoryGiftsResponse,
        CategoryHytaleParams,
        CategoryHytaleResponse,
        CategoryInstagramParams,
        CategoryInstagramResponse,
        CategoryListParams,
        CategoryListResponse,
        CategoryMihoyoParams,
        CategoryMihoyoResponse,
        CategoryMinecraftParams,
        CategoryMinecraftResponse,
        CategoryParamsResponse,
        CategoryRiotParams,
        CategoryRiotResponse,
        CategoryRobloxParams,
        CategoryRobloxResponse,
        CategorySocialclubParams,
        CategorySocialclubResponse,
        CategorySteamParams,
        CategorySteamResponse,
        CategorySupercellParams,
        CategorySupercellResponse,
        CategoryTelegramParams,
        CategoryTelegramResponse,
        CategoryTiktokParams,
        CategoryTiktokResponse,
        CategoryUplayParams,
        CategoryUplayResponse,
        CategoryVpnParams,
        CategoryVpnResponse,
        CategoryWarfaceParams,
        CategoryWarfaceResponse,
        CategoryWotblitzParams,
        CategoryWotblitzResponse,
        CategoryWotParams,
        CategoryWotResponse,
        CustomDiscountsCreateBody,
        CustomDiscountsCreateResponse,
        CustomDiscountsDeleteBody,
        CustomDiscountsDeleteResponse,
        CustomDiscountsEditBody,
        CustomDiscountsEditResponse,
        CustomDiscountsGetResponse,
        ImapCreateBody,
        ImapCreateResponse,
        ImapDeleteBody,
        ImapDeleteResponse,
        ListDownloadParams,
        ListDownloadResponse,
        ListFavoritesParams,
        ListFavoritesResponse,
        ListOrdersParams,
        ListOrdersResponse,
        ListStatesParams,
        ListStatesResponse,
        ListUserParams,
        ListUserResponse,
        ListViewedParams,
        ListViewedResponse,
        ManagingAipriceResponse,
        ManagingAutobumpBody,
        ManagingAutobumpdisableResponse,
        ManagingAutobumpResponse,
        ManagingAutobuypriceResponse,
        ManagingBulkgetBody,
        ManagingBulkgetResponse,
        ManagingBumpResponse,
        ManagingChangepasswordBody,
        ManagingChangepasswordResponse,
        ManagingCheckguaranteeResponse,
        ManagingCloseResponse,
        ManagingCreateclaimBody,
        ManagingCreateclaimResponse,
        ManagingDeclinevideorecordingBody,
        ManagingDeclinevideorecordingResponse,
        ManagingDeleteBody,
        ManagingDeleteResponse,
        ManagingEditBody,
        ManagingEditResponse,
        ManagingEmailcodeResponse,
        ManagingFavoriteResponse,
        ManagingGetletters2Params,
        ManagingGetletters2Response,
        ManagingGetParams,
        ManagingGetResponse,
        ManagingImageParams,
        ManagingImageResponse,
        ManagingNoteBody,
        ManagingNoteResponse,
        ManagingOpenResponse,
        ManagingPublictagBody,
        ManagingPublictagResponse,
        ManagingPublicuntagBody,
        ManagingPublicuntagResponse,
        ManagingRefuseguaranteeResponse,
        ManagingSteamAddmafileResponse,
        ManagingSteamGetmafileResponse,
        ManagingSteaminventoryvalueParams,
        ManagingSteaminventoryvalueResponse,
        ManagingSteammafilecodeResponse,
        ManagingSteampreviewParams,
        ManagingSteampreviewResponse,
        ManagingSteamRemovemafileResponse,
        ManagingSteamsdaBody,
        ManagingSteamsdaResponse,
        ManagingSteamupdatevalueBody,
        ManagingSteamupdatevalueResponse,
        ManagingSteamvalueParams,
        ManagingSteamvalueResponse,
        ManagingStickResponse,
        ManagingTagBody,
        ManagingTagResponse,
        ManagingTelegramcodeResponse,
        ManagingTelegramresetauthResponse,
        ManagingTempemailpasswordResponse,
        ManagingTransferBody,
        ManagingTransferResponse,
        ManagingUnfavoriteResponse,
        ManagingUnstickResponse,
        ManagingUntagBody,
        ManagingUntagResponse,
        PaymentsBalanceexchangeBody,
        PaymentsBalanceexchangeResponse,
        PaymentsBalanceListResponse,
        PaymentsCancelBody,
        PaymentsCancelResponse,
        PaymentsCurrencyResponse,
        PaymentsFeeParams,
        PaymentsFeeResponse,
        PaymentsHistoryParams,
        PaymentsHistoryResponse,
        PaymentsInvoiceCreateBody,
        PaymentsInvoiceCreateResponse,
        PaymentsInvoiceGetParams,
        PaymentsInvoiceGetResponse,
        PaymentsInvoiceListParams,
        PaymentsInvoiceListResponse,
        PaymentsPayoutBody,
        PaymentsPayoutResponse,
        PaymentsPayoutservicesResponse,
        PaymentsTransferBody,
        PaymentsTransferResponse,
        ProfileClaimsParams,
        ProfileClaimsResponse,
        ProfileEditBody,
        ProfileEditResponse,
        ProfileGetParams,
        ProfileGetResponse,
        ProxyAddBody,
        ProxyAddResponse,
        ProxyDeleteBody,
        ProxyDeleteResponse,
        ProxyGetResponse,
        PublishingAddBody,
        PublishingAddResponse,
        PublishingCheckBody,
        PublishingCheckResponse,
        PublishingExternalBody,
        PublishingExternalResponse,
        PublishingFastsellBody,
        PublishingFastsellResponse,
        PurchasingCheckResponse,
        PurchasingConfirmBody,
        PurchasingConfirmResponse,
        PurchasingDiscountcancelResponse,
        PurchasingDiscountrequestBody,
        PurchasingDiscountrequestResponse,
        PurchasingFastbuyBody,
        PurchasingFastbuyResponse,
    )


class CategoryApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def all(self, *, params: CategoryAllParams | None = None) -> CategoryAllResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    def steam(self, *, params: CategorySteamParams | None = None) -> CategorySteamResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/steam",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    def fortnite(self, *, params: CategoryFortniteParams | None = None) -> CategoryFortniteResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/fortnite",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    def mihoyo(self, *, params: CategoryMihoyoParams | None = None) -> CategoryMihoyoResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/mihoyo",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    def riot(self, *, params: CategoryRiotParams | None = None) -> CategoryRiotResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/riot",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    def telegram(self, *, params: CategoryTelegramParams | None = None) -> CategoryTelegramResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/telegram",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    def supercell(
        self, *, params: CategorySupercellParams | None = None
    ) -> CategorySupercellResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/supercell",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    def ea(self, *, params: CategoryEaParams | None = None) -> CategoryEaResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/ea",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    def wot(self, *, params: CategoryWotParams | None = None) -> CategoryWotResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/world-of-tanks",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    def wotblitz(self, *, params: CategoryWotblitzParams | None = None) -> CategoryWotblitzResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/wot-blitz",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    def gifts(self, *, params: CategoryGiftsParams | None = None) -> CategoryGiftsResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/gifts",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    def epicgames(
        self, *, params: CategoryEpicgamesParams | None = None
    ) -> CategoryEpicgamesResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/epicgames",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    def escapefromtarkov(
        self, *, params: CategoryEscapefromtarkovParams | None = None
    ) -> CategoryEscapefromtarkovResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/escape-from-tarkov",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    def socialclub(
        self, *, params: CategorySocialclubParams | None = None
    ) -> CategorySocialclubResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/socialclub",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    def uplay(self, *, params: CategoryUplayParams | None = None) -> CategoryUplayResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/uplay",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    def discord(self, *, params: CategoryDiscordParams | None = None) -> CategoryDiscordResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/discord",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    def tiktok(self, *, params: CategoryTiktokParams | None = None) -> CategoryTiktokResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/tiktok",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    def instagram(
        self, *, params: CategoryInstagramParams | None = None
    ) -> CategoryInstagramResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/instagram",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    def battlenet(
        self, *, params: CategoryBattlenetParams | None = None
    ) -> CategoryBattlenetResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/battlenet",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    def chatgpt(self, *, params: CategoryChatgptParams | None = None) -> CategoryChatgptResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/chatgpt",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    def vpn(self, *, params: CategoryVpnParams | None = None) -> CategoryVpnResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/vpn",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    def roblox(self, *, params: CategoryRobloxParams | None = None) -> CategoryRobloxResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/roblox",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    def warface(self, *, params: CategoryWarfaceParams | None = None) -> CategoryWarfaceResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/warface",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    def minecraft(
        self, *, params: CategoryMinecraftParams | None = None
    ) -> CategoryMinecraftResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/minecraft",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    def hytale(self, *, params: CategoryHytaleParams | None = None) -> CategoryHytaleResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/hytale",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    def list(self, *, params: CategoryListParams | None = None) -> CategoryListResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/category",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    def params(
        self,
        categoryName: Literal[
            "steam",
            "fortnite",
            "mihoyo",
            "riot",
            "telegram",
            "supercell",
            "ea",
            "world-of-tanks",
            "wot-blitz",
            "epicgames",
            "gifts",
            "minecraft",
            "escape-from-tarkov",
            "socialclub",
            "uplay",
            "discord",
            "tiktok",
            "instagram",
            "chatgpt",
            "battlenet",
            "vpn",
            "roblox",
            "warface",
            "hytale",
        ],
    ) -> CategoryParamsResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/{categoryName}/params",
                is_search=True,
            )
        )  # type: ignore[return-value]

    def games(
        self,
        categoryName: Literal[
            "steam",
            "fortnite",
            "mihoyo",
            "riot",
            "telegram",
            "supercell",
            "ea",
            "world-of-tanks",
            "wot-blitz",
            "epicgames",
            "gifts",
            "minecraft",
            "escape-from-tarkov",
            "socialclub",
            "uplay",
            "discord",
            "tiktok",
            "instagram",
            "chatgpt",
            "battlenet",
            "vpn",
            "roblox",
            "warface",
            "hytale",
        ],
    ) -> CategoryGamesResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/{categoryName}/games",
                is_search=True,
            )
        )  # type: ignore[return-value]


class AsyncCategoryApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def all(self, *, params: CategoryAllParams | None = None) -> CategoryAllResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    async def steam(self, *, params: CategorySteamParams | None = None) -> CategorySteamResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/steam",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    async def fortnite(
        self, *, params: CategoryFortniteParams | None = None
    ) -> CategoryFortniteResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/fortnite",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    async def mihoyo(self, *, params: CategoryMihoyoParams | None = None) -> CategoryMihoyoResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/mihoyo",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    async def riot(self, *, params: CategoryRiotParams | None = None) -> CategoryRiotResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/riot",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    async def telegram(
        self, *, params: CategoryTelegramParams | None = None
    ) -> CategoryTelegramResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/telegram",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    async def supercell(
        self, *, params: CategorySupercellParams | None = None
    ) -> CategorySupercellResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/supercell",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    async def ea(self, *, params: CategoryEaParams | None = None) -> CategoryEaResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/ea",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    async def wot(self, *, params: CategoryWotParams | None = None) -> CategoryWotResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/world-of-tanks",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    async def wotblitz(
        self, *, params: CategoryWotblitzParams | None = None
    ) -> CategoryWotblitzResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/wot-blitz",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    async def gifts(self, *, params: CategoryGiftsParams | None = None) -> CategoryGiftsResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/gifts",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    async def epicgames(
        self, *, params: CategoryEpicgamesParams | None = None
    ) -> CategoryEpicgamesResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/epicgames",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    async def escapefromtarkov(
        self, *, params: CategoryEscapefromtarkovParams | None = None
    ) -> CategoryEscapefromtarkovResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/escape-from-tarkov",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    async def socialclub(
        self, *, params: CategorySocialclubParams | None = None
    ) -> CategorySocialclubResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/socialclub",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    async def uplay(self, *, params: CategoryUplayParams | None = None) -> CategoryUplayResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/uplay",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    async def discord(
        self, *, params: CategoryDiscordParams | None = None
    ) -> CategoryDiscordResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/discord",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    async def tiktok(self, *, params: CategoryTiktokParams | None = None) -> CategoryTiktokResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/tiktok",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    async def instagram(
        self, *, params: CategoryInstagramParams | None = None
    ) -> CategoryInstagramResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/instagram",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    async def battlenet(
        self, *, params: CategoryBattlenetParams | None = None
    ) -> CategoryBattlenetResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/battlenet",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    async def chatgpt(
        self, *, params: CategoryChatgptParams | None = None
    ) -> CategoryChatgptResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/chatgpt",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    async def vpn(self, *, params: CategoryVpnParams | None = None) -> CategoryVpnResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/vpn",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    async def roblox(self, *, params: CategoryRobloxParams | None = None) -> CategoryRobloxResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/roblox",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    async def warface(
        self, *, params: CategoryWarfaceParams | None = None
    ) -> CategoryWarfaceResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/warface",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    async def minecraft(
        self, *, params: CategoryMinecraftParams | None = None
    ) -> CategoryMinecraftResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/minecraft",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    async def hytale(self, *, params: CategoryHytaleParams | None = None) -> CategoryHytaleResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/hytale",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    async def list(self, *, params: CategoryListParams | None = None) -> CategoryListResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/category",
                query=params,
                is_search=True,
            )
        )  # type: ignore[return-value]

    async def params(
        self,
        categoryName: Literal[
            "steam",
            "fortnite",
            "mihoyo",
            "riot",
            "telegram",
            "supercell",
            "ea",
            "world-of-tanks",
            "wot-blitz",
            "epicgames",
            "gifts",
            "minecraft",
            "escape-from-tarkov",
            "socialclub",
            "uplay",
            "discord",
            "tiktok",
            "instagram",
            "chatgpt",
            "battlenet",
            "vpn",
            "roblox",
            "warface",
            "hytale",
        ],
    ) -> CategoryParamsResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/{categoryName}/params",
                is_search=True,
            )
        )  # type: ignore[return-value]

    async def games(
        self,
        categoryName: Literal[
            "steam",
            "fortnite",
            "mihoyo",
            "riot",
            "telegram",
            "supercell",
            "ea",
            "world-of-tanks",
            "wot-blitz",
            "epicgames",
            "gifts",
            "minecraft",
            "escape-from-tarkov",
            "socialclub",
            "uplay",
            "discord",
            "tiktok",
            "instagram",
            "chatgpt",
            "battlenet",
            "vpn",
            "roblox",
            "warface",
            "hytale",
        ],
    ) -> CategoryGamesResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/{categoryName}/games",
                is_search=True,
            )
        )  # type: ignore[return-value]


class ListApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def user(self, *, params: ListUserParams | None = None) -> ListUserResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/user/items",
                query=params,
            )
        )  # type: ignore[return-value]

    def orders(self, *, params: ListOrdersParams | None = None) -> ListOrdersResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/user/orders",
                query=params,
            )
        )  # type: ignore[return-value]

    def states(self, *, params: ListStatesParams | None = None) -> ListStatesResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/user/item-states",
                query=params,
            )
        )  # type: ignore[return-value]

    def download(
        self, type: Literal["items", "orders"], *, params: ListDownloadParams | None = None
    ) -> ListDownloadResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/user/{type}/download",
                query=params,
            )
        )  # type: ignore[return-value]

    def favorites(self, *, params: ListFavoritesParams | None = None) -> ListFavoritesResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/fave",
                query=params,
            )
        )  # type: ignore[return-value]

    def viewed(self, *, params: ListViewedParams | None = None) -> ListViewedResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/viewed",
                query=params,
            )
        )  # type: ignore[return-value]


class AsyncListApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def user(self, *, params: ListUserParams | None = None) -> ListUserResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/user/items",
                query=params,
            )
        )  # type: ignore[return-value]

    async def orders(self, *, params: ListOrdersParams | None = None) -> ListOrdersResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/user/orders",
                query=params,
            )
        )  # type: ignore[return-value]

    async def states(self, *, params: ListStatesParams | None = None) -> ListStatesResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/user/item-states",
                query=params,
            )
        )  # type: ignore[return-value]

    async def download(
        self, type: Literal["items", "orders"], *, params: ListDownloadParams | None = None
    ) -> ListDownloadResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/user/{type}/download",
                query=params,
            )
        )  # type: ignore[return-value]

    async def favorites(
        self, *, params: ListFavoritesParams | None = None
    ) -> ListFavoritesResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/fave",
                query=params,
            )
        )  # type: ignore[return-value]

    async def viewed(self, *, params: ListViewedParams | None = None) -> ListViewedResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/viewed",
                query=params,
            )
        )  # type: ignore[return-value]


class ManagingApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def get(self, item_id: int, *, params: ManagingGetParams | None = None) -> ManagingGetResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/{item_id}",
                query=params,
            )
        )  # type: ignore[return-value]

    def delete(self, item_id: int, *, body: ManagingDeleteBody) -> ManagingDeleteResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/{item_id}",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def createclaim(self, *, body: ManagingCreateclaimBody) -> ManagingCreateclaimResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/claims",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def bulkget(self, *, body: ManagingBulkgetBody) -> ManagingBulkgetResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/bulk/items",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def steaminventoryvalue(
        self, item_id: int, *, params: ManagingSteaminventoryvalueParams | None = None
    ) -> ManagingSteaminventoryvalueResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/{item_id}/inventory-value",
                query=params,
            )
        )  # type: ignore[return-value]

    def steamvalue(self, *, params: ManagingSteamvalueParams) -> ManagingSteamvalueResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/steam-value",
                query=params,
            )
        )  # type: ignore[return-value]

    def steampreview(
        self, item_id: int, *, params: ManagingSteampreviewParams | None = None
    ) -> ManagingSteampreviewResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/{item_id}/steam-preview",
                query=params,
            )
        )  # type: ignore[return-value]

    def edit(self, item_id: int, *, body: ManagingEditBody | None = None) -> ManagingEditResponse:
        return self._http.request(
            RequestOptions(
                method="PUT",
                path=f"/{item_id}/edit",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def aiprice(self, item_id: int) -> ManagingAipriceResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/{item_id}/ai-price",
            )
        )  # type: ignore[return-value]

    def autobuyprice(self, item_id: int) -> ManagingAutobuypriceResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/{item_id}/auto-buy-price",
            )
        )  # type: ignore[return-value]

    def note(self, item_id: int, *, body: ManagingNoteBody | None = None) -> ManagingNoteResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/note-save",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def steamupdatevalue(
        self, item_id: int, *, body: ManagingSteamupdatevalueBody | None = None
    ) -> ManagingSteamupdatevalueResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/update-inventory",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def bump(self, item_id: int) -> ManagingBumpResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/bump",
            )
        )  # type: ignore[return-value]

    def autobump(self, item_id: int, *, body: ManagingAutobumpBody) -> ManagingAutobumpResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/auto-bump",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def autobumpdisable(self, item_id: int) -> ManagingAutobumpdisableResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/{item_id}/auto-bump",
            )
        )  # type: ignore[return-value]

    def open(self, item_id: int) -> ManagingOpenResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/open",
            )
        )  # type: ignore[return-value]

    def close(self, item_id: int) -> ManagingCloseResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/close",
            )
        )  # type: ignore[return-value]

    def image(self, item_id: int, *, params: ManagingImageParams) -> ManagingImageResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/{item_id}/image",
                query=params,
            )
        )  # type: ignore[return-value]

    def emailcode(self, item_id: int) -> ManagingEmailcodeResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/{item_id}/email-code",
            )
        )  # type: ignore[return-value]

    def getletters2(
        self, *, params: ManagingGetletters2Params | None = None
    ) -> ManagingGetletters2Response:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/letters2",
                query=params,
            )
        )  # type: ignore[return-value]

    def steam_getmafile(self, item_id: int) -> ManagingSteamGetmafileResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/{item_id}/mafile",
            )
        )  # type: ignore[return-value]

    def steam_addmafile(self, item_id: int) -> ManagingSteamAddmafileResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/mafile",
            )
        )  # type: ignore[return-value]

    def steam_removemafile(self, item_id: int) -> ManagingSteamRemovemafileResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/{item_id}/mafile",
            )
        )  # type: ignore[return-value]

    def steammafilecode(self, item_id: int) -> ManagingSteammafilecodeResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/{item_id}/guard-code",
            )
        )  # type: ignore[return-value]

    def steamsda(
        self, item_id: int, *, body: ManagingSteamsdaBody | None = None
    ) -> ManagingSteamsdaResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/confirm-sda",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def telegramcode(self, item_id: int) -> ManagingTelegramcodeResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/{item_id}/telegram-login-code",
            )
        )  # type: ignore[return-value]

    def telegramresetauth(self, item_id: int) -> ManagingTelegramresetauthResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/telegram-reset-authorizations",
            )
        )  # type: ignore[return-value]

    def refuseguarantee(self, item_id: int) -> ManagingRefuseguaranteeResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/refuse-guarantee",
            )
        )  # type: ignore[return-value]

    def declinevideorecording(
        self, item_id: int, *, body: ManagingDeclinevideorecordingBody
    ) -> ManagingDeclinevideorecordingResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/decline-video-recording",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def checkguarantee(self, item_id: int) -> ManagingCheckguaranteeResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/check-guarantee",
            )
        )  # type: ignore[return-value]

    def changepassword(
        self, item_id: int, *, body: ManagingChangepasswordBody | None = None
    ) -> ManagingChangepasswordResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/change-password",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def tempemailpassword(self, item_id: int) -> ManagingTempemailpasswordResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/{item_id}/temp-email-password",
            )
        )  # type: ignore[return-value]

    def tag(self, item_id: int, *, body: ManagingTagBody) -> ManagingTagResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/tag",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def untag(self, item_id: int, *, body: ManagingUntagBody) -> ManagingUntagResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/{item_id}/tag",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def publictag(self, item_id: int, *, body: ManagingPublictagBody) -> ManagingPublictagResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/public-tag",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def publicuntag(
        self, item_id: int, *, body: ManagingPublicuntagBody
    ) -> ManagingPublicuntagResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/{item_id}/public-tag",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def favorite(self, item_id: int) -> ManagingFavoriteResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/star",
            )
        )  # type: ignore[return-value]

    def unfavorite(self, item_id: int) -> ManagingUnfavoriteResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/{item_id}/star",
            )
        )  # type: ignore[return-value]

    def stick(self, item_id: int) -> ManagingStickResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/stick",
            )
        )  # type: ignore[return-value]

    def unstick(self, item_id: int) -> ManagingUnstickResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/{item_id}/stick",
            )
        )  # type: ignore[return-value]

    def transfer(self, item_id: int, *, body: ManagingTransferBody) -> ManagingTransferResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/change-owner",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


class AsyncManagingApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def get(
        self, item_id: int, *, params: ManagingGetParams | None = None
    ) -> ManagingGetResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/{item_id}",
                query=params,
            )
        )  # type: ignore[return-value]

    async def delete(self, item_id: int, *, body: ManagingDeleteBody) -> ManagingDeleteResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/{item_id}",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def createclaim(self, *, body: ManagingCreateclaimBody) -> ManagingCreateclaimResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/claims",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def bulkget(self, *, body: ManagingBulkgetBody) -> ManagingBulkgetResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/bulk/items",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def steaminventoryvalue(
        self, item_id: int, *, params: ManagingSteaminventoryvalueParams | None = None
    ) -> ManagingSteaminventoryvalueResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/{item_id}/inventory-value",
                query=params,
            )
        )  # type: ignore[return-value]

    async def steamvalue(self, *, params: ManagingSteamvalueParams) -> ManagingSteamvalueResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/steam-value",
                query=params,
            )
        )  # type: ignore[return-value]

    async def steampreview(
        self, item_id: int, *, params: ManagingSteampreviewParams | None = None
    ) -> ManagingSteampreviewResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/{item_id}/steam-preview",
                query=params,
            )
        )  # type: ignore[return-value]

    async def edit(
        self, item_id: int, *, body: ManagingEditBody | None = None
    ) -> ManagingEditResponse:
        return await self._http.request(
            RequestOptions(
                method="PUT",
                path=f"/{item_id}/edit",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def aiprice(self, item_id: int) -> ManagingAipriceResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/{item_id}/ai-price",
            )
        )  # type: ignore[return-value]

    async def autobuyprice(self, item_id: int) -> ManagingAutobuypriceResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/{item_id}/auto-buy-price",
            )
        )  # type: ignore[return-value]

    async def note(
        self, item_id: int, *, body: ManagingNoteBody | None = None
    ) -> ManagingNoteResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/note-save",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def steamupdatevalue(
        self, item_id: int, *, body: ManagingSteamupdatevalueBody | None = None
    ) -> ManagingSteamupdatevalueResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/update-inventory",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def bump(self, item_id: int) -> ManagingBumpResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/bump",
            )
        )  # type: ignore[return-value]

    async def autobump(
        self, item_id: int, *, body: ManagingAutobumpBody
    ) -> ManagingAutobumpResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/auto-bump",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def autobumpdisable(self, item_id: int) -> ManagingAutobumpdisableResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/{item_id}/auto-bump",
            )
        )  # type: ignore[return-value]

    async def open(self, item_id: int) -> ManagingOpenResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/open",
            )
        )  # type: ignore[return-value]

    async def close(self, item_id: int) -> ManagingCloseResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/close",
            )
        )  # type: ignore[return-value]

    async def image(self, item_id: int, *, params: ManagingImageParams) -> ManagingImageResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/{item_id}/image",
                query=params,
            )
        )  # type: ignore[return-value]

    async def emailcode(self, item_id: int) -> ManagingEmailcodeResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/{item_id}/email-code",
            )
        )  # type: ignore[return-value]

    async def getletters2(
        self, *, params: ManagingGetletters2Params | None = None
    ) -> ManagingGetletters2Response:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/letters2",
                query=params,
            )
        )  # type: ignore[return-value]

    async def steam_getmafile(self, item_id: int) -> ManagingSteamGetmafileResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/{item_id}/mafile",
            )
        )  # type: ignore[return-value]

    async def steam_addmafile(self, item_id: int) -> ManagingSteamAddmafileResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/mafile",
            )
        )  # type: ignore[return-value]

    async def steam_removemafile(self, item_id: int) -> ManagingSteamRemovemafileResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/{item_id}/mafile",
            )
        )  # type: ignore[return-value]

    async def steammafilecode(self, item_id: int) -> ManagingSteammafilecodeResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/{item_id}/guard-code",
            )
        )  # type: ignore[return-value]

    async def steamsda(
        self, item_id: int, *, body: ManagingSteamsdaBody | None = None
    ) -> ManagingSteamsdaResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/confirm-sda",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def telegramcode(self, item_id: int) -> ManagingTelegramcodeResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/{item_id}/telegram-login-code",
            )
        )  # type: ignore[return-value]

    async def telegramresetauth(self, item_id: int) -> ManagingTelegramresetauthResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/telegram-reset-authorizations",
            )
        )  # type: ignore[return-value]

    async def refuseguarantee(self, item_id: int) -> ManagingRefuseguaranteeResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/refuse-guarantee",
            )
        )  # type: ignore[return-value]

    async def declinevideorecording(
        self, item_id: int, *, body: ManagingDeclinevideorecordingBody
    ) -> ManagingDeclinevideorecordingResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/decline-video-recording",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def checkguarantee(self, item_id: int) -> ManagingCheckguaranteeResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/check-guarantee",
            )
        )  # type: ignore[return-value]

    async def changepassword(
        self, item_id: int, *, body: ManagingChangepasswordBody | None = None
    ) -> ManagingChangepasswordResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/change-password",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def tempemailpassword(self, item_id: int) -> ManagingTempemailpasswordResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path=f"/{item_id}/temp-email-password",
            )
        )  # type: ignore[return-value]

    async def tag(self, item_id: int, *, body: ManagingTagBody) -> ManagingTagResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/tag",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def untag(self, item_id: int, *, body: ManagingUntagBody) -> ManagingUntagResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/{item_id}/tag",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def publictag(
        self, item_id: int, *, body: ManagingPublictagBody
    ) -> ManagingPublictagResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/public-tag",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def publicuntag(
        self, item_id: int, *, body: ManagingPublicuntagBody
    ) -> ManagingPublicuntagResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/{item_id}/public-tag",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def favorite(self, item_id: int) -> ManagingFavoriteResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/star",
            )
        )  # type: ignore[return-value]

    async def unfavorite(self, item_id: int) -> ManagingUnfavoriteResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/{item_id}/star",
            )
        )  # type: ignore[return-value]

    async def stick(self, item_id: int) -> ManagingStickResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/stick",
            )
        )  # type: ignore[return-value]

    async def unstick(self, item_id: int) -> ManagingUnstickResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/{item_id}/stick",
            )
        )  # type: ignore[return-value]

    async def transfer(
        self, item_id: int, *, body: ManagingTransferBody
    ) -> ManagingTransferResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/change-owner",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


class ProfileApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def claims(self, *, params: ProfileClaimsParams | None = None) -> ProfileClaimsResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/claims",
                query=params,
            )
        )  # type: ignore[return-value]

    def get(self, *, params: ProfileGetParams | None = None) -> ProfileGetResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/me",
                query=params,
            )
        )  # type: ignore[return-value]

    def edit(self, *, body: ProfileEditBody | None = None) -> ProfileEditResponse:
        return self._http.request(
            RequestOptions(
                method="PUT",
                path="/me",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


class AsyncProfileApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def claims(self, *, params: ProfileClaimsParams | None = None) -> ProfileClaimsResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/claims",
                query=params,
            )
        )  # type: ignore[return-value]

    async def get(self, *, params: ProfileGetParams | None = None) -> ProfileGetResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/me",
                query=params,
            )
        )  # type: ignore[return-value]

    async def edit(self, *, body: ProfileEditBody | None = None) -> ProfileEditResponse:
        return await self._http.request(
            RequestOptions(
                method="PUT",
                path="/me",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


class CartApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def get(self, *, params: CartGetParams | None = None) -> CartGetResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/cart",
                query=params,
            )
        )  # type: ignore[return-value]

    def add(self, *, body: CartAddBody) -> CartAddResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/cart",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def delete(self, *, body: CartDeleteBody | None = None) -> CartDeleteResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path="/cart",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


class AsyncCartApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def get(self, *, params: CartGetParams | None = None) -> CartGetResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/cart",
                query=params,
            )
        )  # type: ignore[return-value]

    async def add(self, *, body: CartAddBody) -> CartAddResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/cart",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def delete(self, *, body: CartDeleteBody | None = None) -> CartDeleteResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path="/cart",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


class PurchasingApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def fastbuy(
        self, item_id: int, *, body: PurchasingFastbuyBody | None = None
    ) -> PurchasingFastbuyResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/fast-buy",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def check(self, item_id: int) -> PurchasingCheckResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/check-account",
            )
        )  # type: ignore[return-value]

    def confirm(
        self, item_id: int, *, body: PurchasingConfirmBody | None = None
    ) -> PurchasingConfirmResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/confirm-buy",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def discountrequest(
        self, item_id: int, *, body: PurchasingDiscountrequestBody
    ) -> PurchasingDiscountrequestResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/discount",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def discountcancel(self, item_id: int) -> PurchasingDiscountcancelResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/{item_id}/discount",
            )
        )  # type: ignore[return-value]


class AsyncPurchasingApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def fastbuy(
        self, item_id: int, *, body: PurchasingFastbuyBody | None = None
    ) -> PurchasingFastbuyResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/fast-buy",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def check(self, item_id: int) -> PurchasingCheckResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/check-account",
            )
        )  # type: ignore[return-value]

    async def confirm(
        self, item_id: int, *, body: PurchasingConfirmBody | None = None
    ) -> PurchasingConfirmResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/confirm-buy",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def discountrequest(
        self, item_id: int, *, body: PurchasingDiscountrequestBody
    ) -> PurchasingDiscountrequestResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/discount",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def discountcancel(self, item_id: int) -> PurchasingDiscountcancelResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path=f"/{item_id}/discount",
            )
        )  # type: ignore[return-value]


class CustomDiscountsApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def get(self) -> CustomDiscountsGetResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/custom-discounts",
            )
        )  # type: ignore[return-value]

    def create(self, *, body: CustomDiscountsCreateBody) -> CustomDiscountsCreateResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/custom-discounts",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def edit(self, *, body: CustomDiscountsEditBody) -> CustomDiscountsEditResponse:
        return self._http.request(
            RequestOptions(
                method="PUT",
                path="/custom-discounts",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def delete(self, *, body: CustomDiscountsDeleteBody) -> CustomDiscountsDeleteResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path="/custom-discounts",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


class AsyncCustomDiscountsApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def get(self) -> CustomDiscountsGetResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/custom-discounts",
            )
        )  # type: ignore[return-value]

    async def create(self, *, body: CustomDiscountsCreateBody) -> CustomDiscountsCreateResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/custom-discounts",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def edit(self, *, body: CustomDiscountsEditBody) -> CustomDiscountsEditResponse:
        return await self._http.request(
            RequestOptions(
                method="PUT",
                path="/custom-discounts",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def delete(self, *, body: CustomDiscountsDeleteBody) -> CustomDiscountsDeleteResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path="/custom-discounts",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


class PublishingApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def fastsell(self, *, body: PublishingFastsellBody) -> PublishingFastsellResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/item/fast-sell",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def add(self, *, body: PublishingAddBody) -> PublishingAddResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/item/add",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def check(
        self, item_id: int, *, body: PublishingCheckBody | None = None
    ) -> PublishingCheckResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/goods/check",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def external(self, item_id: int, *, body: PublishingExternalBody) -> PublishingExternalResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/external-account",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


class AsyncPublishingApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def fastsell(self, *, body: PublishingFastsellBody) -> PublishingFastsellResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/item/fast-sell",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def add(self, *, body: PublishingAddBody) -> PublishingAddResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/item/add",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def check(
        self, item_id: int, *, body: PublishingCheckBody | None = None
    ) -> PublishingCheckResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/goods/check",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def external(
        self, item_id: int, *, body: PublishingExternalBody
    ) -> PublishingExternalResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path=f"/{item_id}/external-account",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


class PaymentsApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def invoice_get(
        self, *, params: PaymentsInvoiceGetParams | None = None
    ) -> PaymentsInvoiceGetResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/invoice",
                query=params,
            )
        )  # type: ignore[return-value]

    def invoice_create(self, *, body: PaymentsInvoiceCreateBody) -> PaymentsInvoiceCreateResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/invoice",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def invoice_list(
        self, *, params: PaymentsInvoiceListParams | None = None
    ) -> PaymentsInvoiceListResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/invoice/list",
                query=params,
            )
        )  # type: ignore[return-value]

    def currency(self) -> PaymentsCurrencyResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/currency",
            )
        )  # type: ignore[return-value]

    def balance_list(self) -> PaymentsBalanceListResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/balance/exchange",
            )
        )  # type: ignore[return-value]

    def balanceexchange(
        self, *, body: PaymentsBalanceexchangeBody
    ) -> PaymentsBalanceexchangeResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/balance/exchange",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def transfer(self, *, body: PaymentsTransferBody) -> PaymentsTransferResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/balance/transfer",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def fee(self, *, params: PaymentsFeeParams | None = None) -> PaymentsFeeResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/balance/transfer/fee",
                query=params,
            )
        )  # type: ignore[return-value]

    def cancel(self, *, body: PaymentsCancelBody) -> PaymentsCancelResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/balance/transfer/cancel",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def history(self, *, params: PaymentsHistoryParams | None = None) -> PaymentsHistoryResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/user/payments",
                query=params,
            )
        )  # type: ignore[return-value]

    def payoutservices(self) -> PaymentsPayoutservicesResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/balance/payout/services",
            )
        )  # type: ignore[return-value]

    def payout(self, *, body: PaymentsPayoutBody) -> PaymentsPayoutResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/balance/payout",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


class AsyncPaymentsApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def invoice_get(
        self, *, params: PaymentsInvoiceGetParams | None = None
    ) -> PaymentsInvoiceGetResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/invoice",
                query=params,
            )
        )  # type: ignore[return-value]

    async def invoice_create(
        self, *, body: PaymentsInvoiceCreateBody
    ) -> PaymentsInvoiceCreateResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/invoice",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def invoice_list(
        self, *, params: PaymentsInvoiceListParams | None = None
    ) -> PaymentsInvoiceListResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/invoice/list",
                query=params,
            )
        )  # type: ignore[return-value]

    async def currency(self) -> PaymentsCurrencyResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/currency",
            )
        )  # type: ignore[return-value]

    async def balance_list(self) -> PaymentsBalanceListResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/balance/exchange",
            )
        )  # type: ignore[return-value]

    async def balanceexchange(
        self, *, body: PaymentsBalanceexchangeBody
    ) -> PaymentsBalanceexchangeResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/balance/exchange",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def transfer(self, *, body: PaymentsTransferBody) -> PaymentsTransferResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/balance/transfer",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def fee(self, *, params: PaymentsFeeParams | None = None) -> PaymentsFeeResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/balance/transfer/fee",
                query=params,
            )
        )  # type: ignore[return-value]

    async def cancel(self, *, body: PaymentsCancelBody) -> PaymentsCancelResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/balance/transfer/cancel",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def history(
        self, *, params: PaymentsHistoryParams | None = None
    ) -> PaymentsHistoryResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/user/payments",
                query=params,
            )
        )  # type: ignore[return-value]

    async def payoutservices(self) -> PaymentsPayoutservicesResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/balance/payout/services",
            )
        )  # type: ignore[return-value]

    async def payout(self, *, body: PaymentsPayoutBody) -> PaymentsPayoutResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/balance/payout",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


class AutoPaymentsApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def list(self) -> AutoPaymentsListResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/auto-payments",
            )
        )  # type: ignore[return-value]

    def create(self, *, body: AutoPaymentsCreateBody) -> AutoPaymentsCreateResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/auto-payment",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def delete(self, *, body: AutoPaymentsDeleteBody) -> AutoPaymentsDeleteResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path="/auto-payment",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


class AsyncAutoPaymentsApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def list(self) -> AutoPaymentsListResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/auto-payments",
            )
        )  # type: ignore[return-value]

    async def create(self, *, body: AutoPaymentsCreateBody) -> AutoPaymentsCreateResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/auto-payment",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def delete(self, *, body: AutoPaymentsDeleteBody) -> AutoPaymentsDeleteResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path="/auto-payment",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


class ProxyApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def get(self) -> ProxyGetResponse:
        return self._http.request(
            RequestOptions(
                method="GET",
                path="/proxy",
            )
        )  # type: ignore[return-value]

    def add(self, *, body: ProxyAddBody) -> ProxyAddResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/proxy",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def delete(self, *, body: ProxyDeleteBody | None = None) -> ProxyDeleteResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path="/proxy",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


class AsyncProxyApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def get(self) -> ProxyGetResponse:
        return await self._http.request(
            RequestOptions(
                method="GET",
                path="/proxy",
            )
        )  # type: ignore[return-value]

    async def add(self, *, body: ProxyAddBody) -> ProxyAddResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/proxy",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def delete(self, *, body: ProxyDeleteBody | None = None) -> ProxyDeleteResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path="/proxy",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


class ImapApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def create(self, *, body: ImapCreateBody) -> ImapCreateResponse:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/imap",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    def delete(self, *, body: ImapDeleteBody) -> ImapDeleteResponse:
        return self._http.request(
            RequestOptions(
                method="DELETE",
                path="/imap",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


class AsyncImapApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def create(self, *, body: ImapCreateBody) -> ImapCreateResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/imap",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]

    async def delete(self, *, body: ImapDeleteBody) -> ImapDeleteResponse:
        return await self._http.request(
            RequestOptions(
                method="DELETE",
                path="/imap",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


class BatchApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def batch(self, *, body: BatchBatchBody) -> BatchBatchResponse:
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

    async def batch(self, *, body: BatchBatchBody) -> BatchBatchResponse:
        return await self._http.request(
            RequestOptions(
                method="POST",
                path="/batch",
                body=body,
                content_type="json",
            )
        )  # type: ignore[return-value]


class MarketClient:
    def __init__(
        self,
        config: ClientConfig | None = None,
        *,
        token: str | None = None,
        base_url: str = "https://prod-api.lzt.market",
        proxy: str | None = None,
        max_retries: int = 3,
        base_delay: float = 1.0,
        max_delay: float = 30.0,
        requests_per_minute: int = 120,
        search_requests_per_minute: int = 20,
        on_retry: OnRetryCallback | None = None,
    ) -> None:
        if config is None:
            if token is None:
                raise ConfigError("either config or token must be provided")
            import warnings

            warnings.warn(
                "MarketClient(token=...) is deprecated, "
                "use MarketClient(ClientConfig(token=..., ...)) instead",
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
                search_rate_limit=RateLimitConfig(requests_per_minute=search_requests_per_minute),
                on_retry=on_retry,
            )
        self._http = HttpClient(config)
        self.category = CategoryApi(self._http)
        self.list = ListApi(self._http)
        self.managing = ManagingApi(self._http)
        self.profile = ProfileApi(self._http)
        self.cart = CartApi(self._http)
        self.purchasing = PurchasingApi(self._http)
        self.custom_discounts = CustomDiscountsApi(self._http)
        self.publishing = PublishingApi(self._http)
        self.payments = PaymentsApi(self._http)
        self.auto_payments = AutoPaymentsApi(self._http)
        self.proxy = ProxyApi(self._http)
        self.imap = ImapApi(self._http)
        self.batch = BatchApi(self._http)

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> MarketClient:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()


class AsyncMarketClient:
    def __init__(
        self,
        config: ClientConfig | None = None,
        *,
        token: str | None = None,
        base_url: str = "https://prod-api.lzt.market",
        proxy: str | None = None,
        max_retries: int = 3,
        base_delay: float = 1.0,
        max_delay: float = 30.0,
        requests_per_minute: int = 120,
        search_requests_per_minute: int = 20,
        on_retry: OnRetryCallback | None = None,
    ) -> None:
        if config is None:
            if token is None:
                raise ConfigError("either config or token must be provided")
            import warnings

            warnings.warn(
                "AsyncMarketClient(token=...) is deprecated, "
                "use AsyncMarketClient(ClientConfig(token=..., ...)) instead",
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
                search_rate_limit=RateLimitConfig(requests_per_minute=search_requests_per_minute),
                on_retry=on_retry,
            )
        self._http = AsyncHttpClient(config)
        self.category = AsyncCategoryApi(self._http)
        self.list = AsyncListApi(self._http)
        self.managing = AsyncManagingApi(self._http)
        self.profile = AsyncProfileApi(self._http)
        self.cart = AsyncCartApi(self._http)
        self.purchasing = AsyncPurchasingApi(self._http)
        self.custom_discounts = AsyncCustomDiscountsApi(self._http)
        self.publishing = AsyncPublishingApi(self._http)
        self.payments = AsyncPaymentsApi(self._http)
        self.auto_payments = AsyncAutoPaymentsApi(self._http)
        self.proxy = AsyncProxyApi(self._http)
        self.imap = AsyncImapApi(self._http)
        self.batch = AsyncBatchApi(self._http)

    async def close(self) -> None:
        await self._http.close()

    async def __aenter__(self) -> AsyncMarketClient:
        return self

    async def __aexit__(self, *args: object) -> None:
        await self.close()
