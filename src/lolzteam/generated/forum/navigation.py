# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING

from lolzteam.runtime.types import RequestOptions

if TYPE_CHECKING:
    from lolzteam.runtime.async_http_client import AsyncHttpClient
    from lolzteam.runtime.http_client import HttpClient

    from .types import NavigationListParams, NavigationListResponse


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
        )


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
        )
