# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING

from lolzteam.runtime.types import RequestOptions

if TYPE_CHECKING:
    from lolzteam.runtime.async_http_client import AsyncHttpClient
    from lolzteam.runtime.http_client import HttpClient

    from .types import OAuthTokenBody, OAuthTokenResponse


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
        )


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
        )
