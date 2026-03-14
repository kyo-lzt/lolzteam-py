# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING

from lolzteam.runtime.types import RequestOptions

if TYPE_CHECKING:
    from lolzteam.runtime.async_http_client import AsyncHttpClient
    from lolzteam.runtime.http_client import HttpClient

    from .types import (
        ManagingAipriceResponse,
        ManagingAutobumpBody,
        ManagingAutobumpResponse,
        ManagingAutobumpdisableResponse,
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
        ManagingGetParams,
        ManagingGetResponse,
        ManagingGetletters2Params,
        ManagingGetletters2Response,
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
        ManagingSteamRemovemafileResponse,
        ManagingSteaminventoryvalueParams,
        ManagingSteaminventoryvalueResponse,
        ManagingSteammafilecodeResponse,
        ManagingSteampreviewParams,
        ManagingSteampreviewResponse,
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
    )


class ManagingApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def get(self, item_id: int, *, params: ManagingGetParams | None = None) -> ManagingGetResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path=f"/{item_id}",
            query=params,
        ))

    def delete(self, item_id: int, *, body: ManagingDeleteBody) -> ManagingDeleteResponse:
        return self._http.request(RequestOptions(
            method="DELETE",
            path=f"/{item_id}",
            body=body,
        ))

    def createclaim(self, *, body: ManagingCreateclaimBody) -> ManagingCreateclaimResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path="/claims",
            body=body,
        ))

    def bulkget(self, *, body: ManagingBulkgetBody) -> ManagingBulkgetResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path="/bulk/items",
            body=body,
        ))

    def steaminventoryvalue(self, item_id: int, *, params: ManagingSteaminventoryvalueParams | None = None) -> ManagingSteaminventoryvalueResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path=f"/{item_id}/inventory-value",
            query=params,
        ))

    def steamvalue(self, *, params: ManagingSteamvalueParams) -> ManagingSteamvalueResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path="/steam-value",
            query=params,
        ))

    def steampreview(self, item_id: int, *, params: ManagingSteampreviewParams | None = None) -> ManagingSteampreviewResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path=f"/{item_id}/steam-preview",
            query=params,
        ))

    def edit(self, item_id: int, *, body: ManagingEditBody | None = None) -> ManagingEditResponse:
        return self._http.request(RequestOptions(
            method="PUT",
            path=f"/{item_id}/edit",
            body=body,
        ))

    def aiprice(self, item_id: int) -> ManagingAipriceResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path=f"/{item_id}/ai-price",
        ))

    def autobuyprice(self, item_id: int) -> ManagingAutobuypriceResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path=f"/{item_id}/auto-buy-price",
        ))

    def note(self, item_id: int, *, body: ManagingNoteBody | None = None) -> ManagingNoteResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/note-save",
            body=body,
        ))

    def steamupdatevalue(self, item_id: int, *, body: ManagingSteamupdatevalueBody | None = None) -> ManagingSteamupdatevalueResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/update-inventory",
            body=body,
        ))

    def bump(self, item_id: int) -> ManagingBumpResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/bump",
        ))

    def autobump(self, item_id: int, *, body: ManagingAutobumpBody) -> ManagingAutobumpResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/auto-bump",
            body=body,
        ))

    def autobumpdisable(self, item_id: int) -> ManagingAutobumpdisableResponse:
        return self._http.request(RequestOptions(
            method="DELETE",
            path=f"/{item_id}/auto-bump",
        ))

    def open(self, item_id: int) -> ManagingOpenResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/open",
        ))

    def close(self, item_id: int) -> ManagingCloseResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/close",
        ))

    def image(self, item_id: int, *, params: ManagingImageParams) -> ManagingImageResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path=f"/{item_id}/image",
            query=params,
        ))

    def emailcode(self, item_id: int) -> ManagingEmailcodeResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path=f"/{item_id}/email-code",
        ))

    def getletters2(self, *, params: ManagingGetletters2Params | None = None) -> ManagingGetletters2Response:
        return self._http.request(RequestOptions(
            method="GET",
            path="/letters2",
            query=params,
        ))

    def steam_getmafile(self, item_id: int) -> ManagingSteamGetmafileResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path=f"/{item_id}/mafile",
        ))

    def steam_addmafile(self, item_id: int) -> ManagingSteamAddmafileResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/mafile",
        ))

    def steam_removemafile(self, item_id: int) -> ManagingSteamRemovemafileResponse:
        return self._http.request(RequestOptions(
            method="DELETE",
            path=f"/{item_id}/mafile",
        ))

    def steammafilecode(self, item_id: int) -> ManagingSteammafilecodeResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path=f"/{item_id}/guard-code",
        ))

    def steamsda(self, item_id: int, *, body: ManagingSteamsdaBody | None = None) -> ManagingSteamsdaResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/confirm-sda",
            body=body,
        ))

    def telegramcode(self, item_id: int) -> ManagingTelegramcodeResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path=f"/{item_id}/telegram-login-code",
        ))

    def telegramresetauth(self, item_id: int) -> ManagingTelegramresetauthResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/telegram-reset-authorizations",
        ))

    def refuseguarantee(self, item_id: int) -> ManagingRefuseguaranteeResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/refuse-guarantee",
        ))

    def declinevideorecording(self, item_id: int, *, body: ManagingDeclinevideorecordingBody) -> ManagingDeclinevideorecordingResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/decline-video-recording",
            body=body,
        ))

    def checkguarantee(self, item_id: int) -> ManagingCheckguaranteeResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/check-guarantee",
        ))

    def changepassword(self, item_id: int, *, body: ManagingChangepasswordBody | None = None) -> ManagingChangepasswordResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/change-password",
            body=body,
        ))

    def tempemailpassword(self, item_id: int) -> ManagingTempemailpasswordResponse:
        return self._http.request(RequestOptions(
            method="GET",
            path=f"/{item_id}/temp-email-password",
        ))

    def tag(self, item_id: int, *, body: ManagingTagBody) -> ManagingTagResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/tag",
            body=body,
        ))

    def untag(self, item_id: int, *, body: ManagingUntagBody) -> ManagingUntagResponse:
        return self._http.request(RequestOptions(
            method="DELETE",
            path=f"/{item_id}/tag",
            body=body,
        ))

    def publictag(self, item_id: int, *, body: ManagingPublictagBody) -> ManagingPublictagResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/public-tag",
            body=body,
        ))

    def publicuntag(self, item_id: int, *, body: ManagingPublicuntagBody) -> ManagingPublicuntagResponse:
        return self._http.request(RequestOptions(
            method="DELETE",
            path=f"/{item_id}/public-tag",
            body=body,
        ))

    def favorite(self, item_id: int) -> ManagingFavoriteResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/star",
        ))

    def unfavorite(self, item_id: int) -> ManagingUnfavoriteResponse:
        return self._http.request(RequestOptions(
            method="DELETE",
            path=f"/{item_id}/star",
        ))

    def stick(self, item_id: int) -> ManagingStickResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/stick",
        ))

    def unstick(self, item_id: int) -> ManagingUnstickResponse:
        return self._http.request(RequestOptions(
            method="DELETE",
            path=f"/{item_id}/stick",
        ))

    def transfer(self, item_id: int, *, body: ManagingTransferBody) -> ManagingTransferResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/change-owner",
            body=body,
        ))


class AsyncManagingApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def get(self, item_id: int, *, params: ManagingGetParams | None = None) -> ManagingGetResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path=f"/{item_id}",
            query=params,
        ))

    async def delete(self, item_id: int, *, body: ManagingDeleteBody) -> ManagingDeleteResponse:
        return await self._http.request(RequestOptions(
            method="DELETE",
            path=f"/{item_id}",
            body=body,
        ))

    async def createclaim(self, *, body: ManagingCreateclaimBody) -> ManagingCreateclaimResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path="/claims",
            body=body,
        ))

    async def bulkget(self, *, body: ManagingBulkgetBody) -> ManagingBulkgetResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path="/bulk/items",
            body=body,
        ))

    async def steaminventoryvalue(self, item_id: int, *, params: ManagingSteaminventoryvalueParams | None = None) -> ManagingSteaminventoryvalueResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path=f"/{item_id}/inventory-value",
            query=params,
        ))

    async def steamvalue(self, *, params: ManagingSteamvalueParams) -> ManagingSteamvalueResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/steam-value",
            query=params,
        ))

    async def steampreview(self, item_id: int, *, params: ManagingSteampreviewParams | None = None) -> ManagingSteampreviewResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path=f"/{item_id}/steam-preview",
            query=params,
        ))

    async def edit(self, item_id: int, *, body: ManagingEditBody | None = None) -> ManagingEditResponse:
        return await self._http.request(RequestOptions(
            method="PUT",
            path=f"/{item_id}/edit",
            body=body,
        ))

    async def aiprice(self, item_id: int) -> ManagingAipriceResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path=f"/{item_id}/ai-price",
        ))

    async def autobuyprice(self, item_id: int) -> ManagingAutobuypriceResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path=f"/{item_id}/auto-buy-price",
        ))

    async def note(self, item_id: int, *, body: ManagingNoteBody | None = None) -> ManagingNoteResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/note-save",
            body=body,
        ))

    async def steamupdatevalue(self, item_id: int, *, body: ManagingSteamupdatevalueBody | None = None) -> ManagingSteamupdatevalueResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/update-inventory",
            body=body,
        ))

    async def bump(self, item_id: int) -> ManagingBumpResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/bump",
        ))

    async def autobump(self, item_id: int, *, body: ManagingAutobumpBody) -> ManagingAutobumpResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/auto-bump",
            body=body,
        ))

    async def autobumpdisable(self, item_id: int) -> ManagingAutobumpdisableResponse:
        return await self._http.request(RequestOptions(
            method="DELETE",
            path=f"/{item_id}/auto-bump",
        ))

    async def open(self, item_id: int) -> ManagingOpenResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/open",
        ))

    async def close(self, item_id: int) -> ManagingCloseResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/close",
        ))

    async def image(self, item_id: int, *, params: ManagingImageParams) -> ManagingImageResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path=f"/{item_id}/image",
            query=params,
        ))

    async def emailcode(self, item_id: int) -> ManagingEmailcodeResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path=f"/{item_id}/email-code",
        ))

    async def getletters2(self, *, params: ManagingGetletters2Params | None = None) -> ManagingGetletters2Response:
        return await self._http.request(RequestOptions(
            method="GET",
            path="/letters2",
            query=params,
        ))

    async def steam_getmafile(self, item_id: int) -> ManagingSteamGetmafileResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path=f"/{item_id}/mafile",
        ))

    async def steam_addmafile(self, item_id: int) -> ManagingSteamAddmafileResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/mafile",
        ))

    async def steam_removemafile(self, item_id: int) -> ManagingSteamRemovemafileResponse:
        return await self._http.request(RequestOptions(
            method="DELETE",
            path=f"/{item_id}/mafile",
        ))

    async def steammafilecode(self, item_id: int) -> ManagingSteammafilecodeResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path=f"/{item_id}/guard-code",
        ))

    async def steamsda(self, item_id: int, *, body: ManagingSteamsdaBody | None = None) -> ManagingSteamsdaResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/confirm-sda",
            body=body,
        ))

    async def telegramcode(self, item_id: int) -> ManagingTelegramcodeResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path=f"/{item_id}/telegram-login-code",
        ))

    async def telegramresetauth(self, item_id: int) -> ManagingTelegramresetauthResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/telegram-reset-authorizations",
        ))

    async def refuseguarantee(self, item_id: int) -> ManagingRefuseguaranteeResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/refuse-guarantee",
        ))

    async def declinevideorecording(self, item_id: int, *, body: ManagingDeclinevideorecordingBody) -> ManagingDeclinevideorecordingResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/decline-video-recording",
            body=body,
        ))

    async def checkguarantee(self, item_id: int) -> ManagingCheckguaranteeResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/check-guarantee",
        ))

    async def changepassword(self, item_id: int, *, body: ManagingChangepasswordBody | None = None) -> ManagingChangepasswordResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/change-password",
            body=body,
        ))

    async def tempemailpassword(self, item_id: int) -> ManagingTempemailpasswordResponse:
        return await self._http.request(RequestOptions(
            method="GET",
            path=f"/{item_id}/temp-email-password",
        ))

    async def tag(self, item_id: int, *, body: ManagingTagBody) -> ManagingTagResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/tag",
            body=body,
        ))

    async def untag(self, item_id: int, *, body: ManagingUntagBody) -> ManagingUntagResponse:
        return await self._http.request(RequestOptions(
            method="DELETE",
            path=f"/{item_id}/tag",
            body=body,
        ))

    async def publictag(self, item_id: int, *, body: ManagingPublictagBody) -> ManagingPublictagResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/public-tag",
            body=body,
        ))

    async def publicuntag(self, item_id: int, *, body: ManagingPublicuntagBody) -> ManagingPublicuntagResponse:
        return await self._http.request(RequestOptions(
            method="DELETE",
            path=f"/{item_id}/public-tag",
            body=body,
        ))

    async def favorite(self, item_id: int) -> ManagingFavoriteResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/star",
        ))

    async def unfavorite(self, item_id: int) -> ManagingUnfavoriteResponse:
        return await self._http.request(RequestOptions(
            method="DELETE",
            path=f"/{item_id}/star",
        ))

    async def stick(self, item_id: int) -> ManagingStickResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/stick",
        ))

    async def unstick(self, item_id: int) -> ManagingUnstickResponse:
        return await self._http.request(RequestOptions(
            method="DELETE",
            path=f"/{item_id}/stick",
        ))

    async def transfer(self, item_id: int, *, body: ManagingTransferBody) -> ManagingTransferResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path=f"/{item_id}/change-owner",
            body=body,
        ))
