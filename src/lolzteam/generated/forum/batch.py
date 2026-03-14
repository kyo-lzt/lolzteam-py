# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import TYPE_CHECKING

from lolzteam.runtime.types import RequestOptions

if TYPE_CHECKING:
    from lolzteam.runtime.async_http_client import AsyncHttpClient
    from lolzteam.runtime.http_client import HttpClient

    from .types import BatchExecuteBody, BatchExecuteResponse


class BatchApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def execute(self, *, body: BatchExecuteBody | None = None) -> BatchExecuteResponse:
        return self._http.request(RequestOptions(
            method="POST",
            path="/batch",
            body=body,
        ))


class AsyncBatchApi:
    def __init__(self, http: AsyncHttpClient) -> None:
        self._http = http

    async def execute(self, *, body: BatchExecuteBody | None = None) -> BatchExecuteResponse:
        return await self._http.request(RequestOptions(
            method="POST",
            path="/batch",
            body=body,
        ))
