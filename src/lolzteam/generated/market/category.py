# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from lolzteam.runtime.types import RequestOptions

if TYPE_CHECKING:
    from lolzteam.runtime.async_http_client import AsyncHttpClient
    from lolzteam.runtime.http_client import HttpClient

    from .types import (
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
        CategoryWotParams,
        CategoryWotResponse,
        CategoryWotblitzParams,
        CategoryWotblitzResponse,
    )


class CategoryApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def all(self, *, params: CategoryAllParams | None = None) -> CategoryAllResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/",
            query=params,
        ))

    def steam(self, *, params: CategorySteamParams | None = None) -> CategorySteamResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/steam",
            query=params,
        ))

    def fortnite(self, *, params: CategoryFortniteParams | None = None) -> CategoryFortniteResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/fortnite",
            query=params,
        ))

    def mihoyo(self, *, params: CategoryMihoyoParams | None = None) -> CategoryMihoyoResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/mihoyo",
            query=params,
        ))

    def riot(self, *, params: CategoryRiotParams | None = None) -> CategoryRiotResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/riot",
            query=params,
        ))

    def telegram(self, *, params: CategoryTelegramParams | None = None) -> CategoryTelegramResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/telegram",
            query=params,
        ))

    def supercell(self, *, params: CategorySupercellParams | None = None) -> CategorySupercellResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/supercell",
            query=params,
        ))

    def ea(self, *, params: CategoryEaParams | None = None) -> CategoryEaResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/ea",
            query=params,
        ))

    def wot(self, *, params: CategoryWotParams | None = None) -> CategoryWotResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/world-of-tanks",
            query=params,
        ))

    def wotblitz(self, *, params: CategoryWotblitzParams | None = None) -> CategoryWotblitzResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/wot-blitz",
            query=params,
        ))

    def gifts(self, *, params: CategoryGiftsParams | None = None) -> CategoryGiftsResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/gifts",
            query=params,
        ))

    def epicgames(self, *, params: CategoryEpicgamesParams | None = None) -> CategoryEpicgamesResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/epicgames",
            query=params,
        ))

    def escapefromtarkov(self, *, params: CategoryEscapefromtarkovParams | None = None) -> CategoryEscapefromtarkovResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/escape-from-tarkov",
            query=params,
        ))

    def socialclub(self, *, params: CategorySocialclubParams | None = None) -> CategorySocialclubResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/socialclub",
            query=params,
        ))

    def uplay(self, *, params: CategoryUplayParams | None = None) -> CategoryUplayResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/uplay",
            query=params,
        ))

    def discord(self, *, params: CategoryDiscordParams | None = None) -> CategoryDiscordResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/discord",
            query=params,
        ))

    def tiktok(self, *, params: CategoryTiktokParams | None = None) -> CategoryTiktokResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/tiktok",
            query=params,
        ))

    def instagram(self, *, params: CategoryInstagramParams | None = None) -> CategoryInstagramResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/instagram",
            query=params,
        ))

    def battlenet(self, *, params: CategoryBattlenetParams | None = None) -> CategoryBattlenetResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/battlenet",
            query=params,
        ))

    def chatgpt(self, *, params: CategoryChatgptParams | None = None) -> CategoryChatgptResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/chatgpt",
            query=params,
        ))

    def vpn(self, *, params: CategoryVpnParams | None = None) -> CategoryVpnResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/vpn",
            query=params,
        ))

    def roblox(self, *, params: CategoryRobloxParams | None = None) -> CategoryRobloxResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/roblox",
            query=params,
        ))

    def warface(self, *, params: CategoryWarfaceParams | None = None) -> CategoryWarfaceResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/warface",
            query=params,
        ))

    def minecraft(self, *, params: CategoryMinecraftParams | None = None) -> CategoryMinecraftResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/minecraft",
            query=params,
        ))

    def hytale(self, *, params: CategoryHytaleParams | None = None) -> CategoryHytaleResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/hytale",
            query=params,
        ))

    def list(self, *, params: CategoryListParams | None = None) -> CategoryListResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/category",
            query=params,
        ))

    def params(self, categoryName: Literal["steam", "fortnite", "mihoyo", "riot", "telegram", "supercell", "ea", "world-of-tanks", "wot-blitz", "epicgames", "gifts", "minecraft", "escape-from-tarkov", "socialclub", "uplay", "discord", "tiktok", "instagram", "chatgpt", "battlenet", "vpn", "roblox", "warface", "hytale"]) -> CategoryParamsResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path=f"/{categoryName}/params",
        ))

    def games(self, categoryName: Literal["steam", "fortnite", "mihoyo", "riot", "telegram", "supercell", "ea", "world-of-tanks", "wot-blitz", "epicgames", "gifts", "minecraft", "escape-from-tarkov", "socialclub", "uplay", "discord", "tiktok", "instagram", "chatgpt", "battlenet", "vpn", "roblox", "warface", "hytale"]) -> CategoryGamesResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path=f"/{categoryName}/games",
        ))


class AsyncCategoryApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def all(self, *, params: CategoryAllParams | None = None) -> CategoryAllResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/",
            query=params,
        ))

    async def steam(self, *, params: CategorySteamParams | None = None) -> CategorySteamResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/steam",
            query=params,
        ))

    async def fortnite(self, *, params: CategoryFortniteParams | None = None) -> CategoryFortniteResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/fortnite",
            query=params,
        ))

    async def mihoyo(self, *, params: CategoryMihoyoParams | None = None) -> CategoryMihoyoResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/mihoyo",
            query=params,
        ))

    async def riot(self, *, params: CategoryRiotParams | None = None) -> CategoryRiotResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/riot",
            query=params,
        ))

    async def telegram(self, *, params: CategoryTelegramParams | None = None) -> CategoryTelegramResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/telegram",
            query=params,
        ))

    async def supercell(self, *, params: CategorySupercellParams | None = None) -> CategorySupercellResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/supercell",
            query=params,
        ))

    async def ea(self, *, params: CategoryEaParams | None = None) -> CategoryEaResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/ea",
            query=params,
        ))

    async def wot(self, *, params: CategoryWotParams | None = None) -> CategoryWotResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/world-of-tanks",
            query=params,
        ))

    async def wotblitz(self, *, params: CategoryWotblitzParams | None = None) -> CategoryWotblitzResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/wot-blitz",
            query=params,
        ))

    async def gifts(self, *, params: CategoryGiftsParams | None = None) -> CategoryGiftsResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/gifts",
            query=params,
        ))

    async def epicgames(self, *, params: CategoryEpicgamesParams | None = None) -> CategoryEpicgamesResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/epicgames",
            query=params,
        ))

    async def escapefromtarkov(self, *, params: CategoryEscapefromtarkovParams | None = None) -> CategoryEscapefromtarkovResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/escape-from-tarkov",
            query=params,
        ))

    async def socialclub(self, *, params: CategorySocialclubParams | None = None) -> CategorySocialclubResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/socialclub",
            query=params,
        ))

    async def uplay(self, *, params: CategoryUplayParams | None = None) -> CategoryUplayResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/uplay",
            query=params,
        ))

    async def discord(self, *, params: CategoryDiscordParams | None = None) -> CategoryDiscordResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/discord",
            query=params,
        ))

    async def tiktok(self, *, params: CategoryTiktokParams | None = None) -> CategoryTiktokResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/tiktok",
            query=params,
        ))

    async def instagram(self, *, params: CategoryInstagramParams | None = None) -> CategoryInstagramResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/instagram",
            query=params,
        ))

    async def battlenet(self, *, params: CategoryBattlenetParams | None = None) -> CategoryBattlenetResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/battlenet",
            query=params,
        ))

    async def chatgpt(self, *, params: CategoryChatgptParams | None = None) -> CategoryChatgptResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/chatgpt",
            query=params,
        ))

    async def vpn(self, *, params: CategoryVpnParams | None = None) -> CategoryVpnResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/vpn",
            query=params,
        ))

    async def roblox(self, *, params: CategoryRobloxParams | None = None) -> CategoryRobloxResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/roblox",
            query=params,
        ))

    async def warface(self, *, params: CategoryWarfaceParams | None = None) -> CategoryWarfaceResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/warface",
            query=params,
        ))

    async def minecraft(self, *, params: CategoryMinecraftParams | None = None) -> CategoryMinecraftResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/minecraft",
            query=params,
        ))

    async def hytale(self, *, params: CategoryHytaleParams | None = None) -> CategoryHytaleResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/hytale",
            query=params,
        ))

    async def list(self, *, params: CategoryListParams | None = None) -> CategoryListResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/category",
            query=params,
        ))

    async def params(self, categoryName: Literal["steam", "fortnite", "mihoyo", "riot", "telegram", "supercell", "ea", "world-of-tanks", "wot-blitz", "epicgames", "gifts", "minecraft", "escape-from-tarkov", "socialclub", "uplay", "discord", "tiktok", "instagram", "chatgpt", "battlenet", "vpn", "roblox", "warface", "hytale"]) -> CategoryParamsResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path=f"/{categoryName}/params",
        ))

    async def games(self, categoryName: Literal["steam", "fortnite", "mihoyo", "riot", "telegram", "supercell", "ea", "world-of-tanks", "wot-blitz", "epicgames", "gifts", "minecraft", "escape-from-tarkov", "socialclub", "uplay", "discord", "tiktok", "instagram", "chatgpt", "battlenet", "vpn", "roblox", "warface", "hytale"]) -> CategoryGamesResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path=f"/{categoryName}/games",
        ))
