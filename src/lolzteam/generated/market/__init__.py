# Auto-generated. Do not edit manually.
from __future__ import annotations

from lolzteam.runtime.async_http_client import AsyncHttpClient
from lolzteam.runtime.http_client import HttpClient
from lolzteam.runtime.types import ClientConfig, ProxyConfig, RateLimitConfig, RetryConfig

from .auto_payments import AsyncAutoPaymentsApi, AutoPaymentsApi
from .batch import AsyncBatchApi, BatchApi
from .cart import AsyncCartApi, CartApi
from .category import AsyncCategoryApi, CategoryApi
from .custom_discounts import AsyncCustomDiscountsApi, CustomDiscountsApi
from .imap import AsyncImapApi, ImapApi
from .list import AsyncListApi, ListApi
from .managing import AsyncManagingApi, ManagingApi
from .payments import AsyncPaymentsApi, PaymentsApi
from .profile import AsyncProfileApi, ProfileApi
from .proxy import AsyncProxyApi, ProxyApi
from .publishing import AsyncPublishingApi, PublishingApi
from .purchasing import AsyncPurchasingApi, PurchasingApi


class MarketClient:
    def __init__(
        self,
        token: str,
        *,
        base_url: str = "https://prod-api.lzt.market",
        proxy: str | None = None,
        max_retries: int = 3,
        base_delay: float = 1.0,
        max_delay: float = 30.0,
        requests_per_minute: int = 120,
    ) -> None:
        config = ClientConfig(
            token=token,
            base_url=base_url,
            proxy=ProxyConfig(url=proxy) if proxy else None,
            retry=RetryConfig(max_retries=max_retries, base_delay=base_delay, max_delay=max_delay),
            rate_limit=RateLimitConfig(requests_per_minute=requests_per_minute),
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
        token: str,
        *,
        base_url: str = "https://prod-api.lzt.market",
        proxy: str | None = None,
        max_retries: int = 3,
        base_delay: float = 1.0,
        max_delay: float = 30.0,
        requests_per_minute: int = 120,
    ) -> None:
        config = ClientConfig(
            token=token,
            base_url=base_url,
            proxy=ProxyConfig(url=proxy) if proxy else None,
            retry=RetryConfig(max_retries=max_retries, base_delay=base_delay, max_delay=max_delay),
            rate_limit=RateLimitConfig(requests_per_minute=requests_per_minute),
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
