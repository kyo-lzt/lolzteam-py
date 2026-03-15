from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest

from lolzteam import AsyncForumClient, AsyncMarketClient, ForumClient, MarketClient
from lolzteam.runtime.errors import (
    AuthError,
    ConfigError,
    NetworkError,
    NotFoundError,
    RateLimitError,
    ServerError,
)


def _mock_response(
    status_code: int = 200,
    json_data: object = None,
    headers: dict[str, str] | None = None,
) -> MagicMock:
    resp = MagicMock(spec=httpx.Response)
    resp.status_code = status_code
    resp.is_success = 200 <= status_code < 300
    resp.json.return_value = json_data if json_data is not None else {}
    resp.headers = httpx.Headers(headers or {})
    return resp


# ---------------------------------------------------------------------------
# ForumClient
# ---------------------------------------------------------------------------
FORUM_API_GROUPS = [
    "o_auth",
    "assets",
    "categories",
    "forums",
    "links",
    "pages",
    "navigation",
    "threads",
    "posts",
    "users",
    "profile_posts",
    "conversations",
    "notifications",
    "tags",
    "search",
    "batch",
    "chatbox",
    "forms",
]


class TestForumClient:
    def test_instantiation_defaults(self) -> None:
        client = ForumClient(token="test-token")
        assert client._http._token == "test-token"
        assert client._http._base_url == "https://prod-api.lolz.live"
        client.close()

    def test_instantiation_custom_base_url(self) -> None:
        client = ForumClient(token="t", base_url="https://custom.api")
        assert client._http._base_url == "https://custom.api"
        client.close()

    @pytest.mark.parametrize("group", FORUM_API_GROUPS)
    def test_api_group_accessible(self, group: str) -> None:
        client = ForumClient(token="t")
        assert hasattr(client, group)
        assert getattr(client, group) is not None
        client.close()

    def test_proxy_config(self) -> None:
        with patch("lolzteam.runtime.http_client.httpx.Client") as mock_cls:
            ForumClient(token="t", proxy="http://proxy:8080")
            mock_cls.assert_called_once_with(proxy="http://proxy:8080", timeout=None)

    def test_proxy_none_by_default(self) -> None:
        with patch("lolzteam.runtime.http_client.httpx.Client") as mock_cls:
            ForumClient(token="t")
            mock_cls.assert_called_once_with(proxy=None, timeout=None)

    def test_context_manager(self) -> None:
        with patch("lolzteam.runtime.http_client.httpx.Client"), ForumClient(token="t") as client:
            assert isinstance(client, ForumClient)

    @patch("lolzteam.runtime.http_client.httpx.Client")
    def test_threads_list_makes_get_request(self, mock_cls: MagicMock) -> None:
        mock_http = MagicMock()
        mock_http.request.return_value = _mock_response(json_data={"threads": []})
        mock_cls.return_value = mock_http

        client = ForumClient(token="t", max_retries=0)
        client._http._client = mock_http
        result = client.threads.list()
        assert result == {"threads": []}
        mock_http.request.assert_called_once()
        call_kwargs = mock_http.request.call_args
        assert call_kwargs.kwargs["method"] == "GET"
        assert "/threads" in call_kwargs.kwargs["url"]
        client.close()

    @patch("lolzteam.runtime.http_client.httpx.Client")
    def test_request_includes_auth_header(self, mock_cls: MagicMock) -> None:
        mock_http = MagicMock()
        mock_http.request.return_value = _mock_response(json_data={})
        mock_cls.return_value = mock_http

        client = ForumClient(token="secret-token", max_retries=0)
        client._http._client = mock_http
        client.threads.list()
        call_kwargs = mock_http.request.call_args
        headers = call_kwargs.kwargs["headers"]
        assert headers["Authorization"] == "Bearer secret-token"
        client.close()

    @patch("lolzteam.runtime.http_client.httpx.Client")
    def test_error_401_raises_auth_error(self, mock_cls: MagicMock) -> None:
        mock_http = MagicMock()
        mock_http.request.return_value = _mock_response(
            status_code=401, json_data={"error": "unauthorized"}
        )
        mock_cls.return_value = mock_http

        client = ForumClient(token="t", max_retries=0)
        client._http._client = mock_http
        with pytest.raises(AuthError) as exc_info:
            client.threads.list()
        assert exc_info.value.status == 401
        client.close()

    @patch("lolzteam.runtime.http_client.httpx.Client")
    def test_error_404_raises_not_found_error(self, mock_cls: MagicMock) -> None:
        mock_http = MagicMock()
        mock_http.request.return_value = _mock_response(status_code=404)
        mock_cls.return_value = mock_http

        client = ForumClient(token="t", max_retries=0)
        client._http._client = mock_http
        with pytest.raises(NotFoundError) as exc_info:
            client.threads.get(999)
        assert exc_info.value.status == 404
        client.close()

    @patch("lolzteam.runtime.http_client.httpx.Client")
    def test_error_429_raises_rate_limit_error(self, mock_cls: MagicMock) -> None:
        mock_http = MagicMock()
        mock_http.request.return_value = _mock_response(
            status_code=429, headers={"retry-after": "5"}
        )
        mock_cls.return_value = mock_http

        client = ForumClient(token="t", max_retries=0)
        client._http._client = mock_http
        with pytest.raises(RateLimitError) as exc_info:
            client.threads.list()
        assert exc_info.value.retry_after == 5.0
        client.close()

    @patch("lolzteam.runtime.http_client.httpx.Client")
    def test_error_502_raises_server_error(self, mock_cls: MagicMock) -> None:
        mock_http = MagicMock()
        mock_http.request.return_value = _mock_response(status_code=502)
        mock_cls.return_value = mock_http

        client = ForumClient(token="t", max_retries=0)
        client._http._client = mock_http
        with pytest.raises(ServerError) as exc_info:
            client.threads.list()
        assert exc_info.value.status == 502
        client.close()

    @patch("lolzteam.runtime.http_client.httpx.Client")
    def test_network_error_on_connection_failure(self, mock_cls: MagicMock) -> None:
        mock_http = MagicMock()
        mock_http.request.side_effect = httpx.ConnectError("connection refused")
        mock_cls.return_value = mock_http

        client = ForumClient(token="t", max_retries=0)
        client._http._client = mock_http
        with pytest.raises(NetworkError):
            client.threads.list()
        client.close()

    def test_retry_config_passed(self) -> None:
        with patch("lolzteam.runtime.http_client.httpx.Client"):
            client = ForumClient(token="t", max_retries=5, base_delay=2.0, max_delay=60.0)
            assert client._http._retry_config.max_retries == 5
            assert client._http._retry_config.base_delay == 2.0
            assert client._http._retry_config.max_delay == 60.0
            client.close()

    def test_rate_limit_config_passed(self) -> None:
        with patch("lolzteam.runtime.http_client.httpx.Client"):
            client = ForumClient(token="t", requests_per_minute=100)
            assert client._http._rate_limiter is not None
            client.close()


# ---------------------------------------------------------------------------
# AsyncForumClient
# ---------------------------------------------------------------------------
class TestAsyncForumClient:
    def test_instantiation(self) -> None:
        with patch("lolzteam.runtime.async_http_client.httpx.AsyncClient"):
            client = AsyncForumClient(token="test-token")
            assert client._http._token == "test-token"
            assert client._http._base_url == "https://prod-api.lolz.live"

    @pytest.mark.parametrize("group", FORUM_API_GROUPS)
    def test_api_group_accessible(self, group: str) -> None:
        with patch("lolzteam.runtime.async_http_client.httpx.AsyncClient"):
            client = AsyncForumClient(token="t")
            assert hasattr(client, group)
            assert getattr(client, group) is not None

    def test_proxy_config(self) -> None:
        with patch("lolzteam.runtime.async_http_client.httpx.AsyncClient") as mock_cls:
            AsyncForumClient(token="t", proxy="http://proxy:8080")
            mock_cls.assert_called_once_with(proxy="http://proxy:8080", timeout=None)

    async def test_context_manager(self) -> None:
        mock_async_client = AsyncMock()
        with patch(
            "lolzteam.runtime.async_http_client.httpx.AsyncClient",
            return_value=mock_async_client,
        ):
            async with AsyncForumClient(token="t") as client:
                assert isinstance(client, AsyncForumClient)

    async def test_threads_list_makes_get_request(self) -> None:
        with patch("lolzteam.runtime.async_http_client.httpx.AsyncClient"):
            client = AsyncForumClient(token="t", max_retries=0)
            mock_http = AsyncMock()
            mock_http.request.return_value = _mock_response(json_data={"threads": []})
            client._http._client = mock_http

            result = await client.threads.list()
            assert result == {"threads": []}
            mock_http.request.assert_called_once()

    async def test_error_401_raises_auth_error(self) -> None:
        with patch("lolzteam.runtime.async_http_client.httpx.AsyncClient"):
            client = AsyncForumClient(token="t", max_retries=0)
            mock_http = AsyncMock()
            mock_http.request.return_value = _mock_response(status_code=401)
            client._http._client = mock_http

            with pytest.raises(AuthError):
                await client.threads.list()

    async def test_error_429_raises_rate_limit_error(self) -> None:
        with patch("lolzteam.runtime.async_http_client.httpx.AsyncClient"):
            client = AsyncForumClient(token="t", max_retries=0)
            mock_http = AsyncMock()
            mock_http.request.return_value = _mock_response(
                status_code=429, headers={"retry-after": "3"}
            )
            client._http._client = mock_http

            with pytest.raises(RateLimitError):
                await client.threads.list()

    async def test_network_error_on_connection_failure(self) -> None:
        with patch("lolzteam.runtime.async_http_client.httpx.AsyncClient"):
            client = AsyncForumClient(token="t", max_retries=0)
            mock_http = AsyncMock()
            mock_http.request.side_effect = httpx.ConnectError("fail")
            client._http._client = mock_http

            with pytest.raises(NetworkError):
                await client.threads.list()

    async def test_request_includes_auth_header(self) -> None:
        with patch("lolzteam.runtime.async_http_client.httpx.AsyncClient"):
            client = AsyncForumClient(token="my-token", max_retries=0)
            mock_http = AsyncMock()
            mock_http.request.return_value = _mock_response(json_data={})
            client._http._client = mock_http

            await client.threads.list()
            call_kwargs = mock_http.request.call_args
            assert call_kwargs.kwargs["headers"]["Authorization"] == "Bearer my-token"


# ---------------------------------------------------------------------------
# MarketClient
# ---------------------------------------------------------------------------
MARKET_API_GROUPS = [
    "category",
    "list",
    "managing",
    "profile",
    "cart",
    "purchasing",
    "custom_discounts",
    "publishing",
    "payments",
    "auto_payments",
    "proxy",
    "imap",
    "batch",
]


class TestMarketClient:
    def test_instantiation_defaults(self) -> None:
        client = MarketClient(token="test-token")
        assert client._http._token == "test-token"
        assert client._http._base_url == "https://prod-api.lzt.market"
        client.close()

    @pytest.mark.parametrize("group", MARKET_API_GROUPS)
    def test_api_group_accessible(self, group: str) -> None:
        client = MarketClient(token="t")
        assert hasattr(client, group)
        assert getattr(client, group) is not None
        client.close()

    def test_proxy_config(self) -> None:
        with patch("lolzteam.runtime.http_client.httpx.Client") as mock_cls:
            MarketClient(token="t", proxy="socks5://proxy:1080")
            mock_cls.assert_called_once_with(proxy="socks5://proxy:1080", timeout=None)

    def test_context_manager(self) -> None:
        with patch("lolzteam.runtime.http_client.httpx.Client"), MarketClient(token="t") as client:
            assert isinstance(client, MarketClient)

    @patch("lolzteam.runtime.http_client.httpx.Client")
    def test_error_401_raises_auth_error(self, mock_cls: MagicMock) -> None:
        mock_http = MagicMock()
        mock_http.request.return_value = _mock_response(status_code=401)
        mock_cls.return_value = mock_http

        client = MarketClient(token="t", max_retries=0)
        client._http._client = mock_http
        with pytest.raises(AuthError):
            client.category.list()
        client.close()

    @patch("lolzteam.runtime.http_client.httpx.Client")
    def test_error_404_raises_not_found_error(self, mock_cls: MagicMock) -> None:
        mock_http = MagicMock()
        mock_http.request.return_value = _mock_response(status_code=404)
        mock_cls.return_value = mock_http

        client = MarketClient(token="t", max_retries=0)
        client._http._client = mock_http
        with pytest.raises(NotFoundError):
            client.category.list()
        client.close()

    @patch("lolzteam.runtime.http_client.httpx.Client")
    def test_error_429_raises_rate_limit_error(self, mock_cls: MagicMock) -> None:
        mock_http = MagicMock()
        mock_http.request.return_value = _mock_response(
            status_code=429, headers={"retry-after": "10"}
        )
        mock_cls.return_value = mock_http

        client = MarketClient(token="t", max_retries=0)
        client._http._client = mock_http
        with pytest.raises(RateLimitError) as exc_info:
            client.category.list()
        assert exc_info.value.retry_after == 10.0
        client.close()

    @patch("lolzteam.runtime.http_client.httpx.Client")
    def test_error_502_raises_server_error(self, mock_cls: MagicMock) -> None:
        mock_http = MagicMock()
        mock_http.request.return_value = _mock_response(status_code=502)
        mock_cls.return_value = mock_http

        client = MarketClient(token="t", max_retries=0)
        client._http._client = mock_http
        with pytest.raises(ServerError):
            client.category.list()
        client.close()

    def test_default_rate_limit_120(self) -> None:
        with patch("lolzteam.runtime.http_client.httpx.Client"):
            client = MarketClient(token="t")
            assert client._http._rate_limiter is not None
            client.close()

    def test_retry_config(self) -> None:
        with patch("lolzteam.runtime.http_client.httpx.Client"):
            client = MarketClient(token="t", max_retries=2, base_delay=0.5, max_delay=10.0)
            assert client._http._retry_config.max_retries == 2
            assert client._http._retry_config.base_delay == 0.5
            assert client._http._retry_config.max_delay == 10.0
            client.close()


# ---------------------------------------------------------------------------
# AsyncMarketClient
# ---------------------------------------------------------------------------
class TestAsyncMarketClient:
    def test_instantiation(self) -> None:
        with patch("lolzteam.runtime.async_http_client.httpx.AsyncClient"):
            client = AsyncMarketClient(token="test-token")
            assert client._http._token == "test-token"
            assert client._http._base_url == "https://prod-api.lzt.market"

    @pytest.mark.parametrize("group", MARKET_API_GROUPS)
    def test_api_group_accessible(self, group: str) -> None:
        with patch("lolzteam.runtime.async_http_client.httpx.AsyncClient"):
            client = AsyncMarketClient(token="t")
            assert hasattr(client, group)
            assert getattr(client, group) is not None

    def test_proxy_config(self) -> None:
        with patch("lolzteam.runtime.async_http_client.httpx.AsyncClient") as mock_cls:
            AsyncMarketClient(token="t", proxy="http://proxy:3128")
            mock_cls.assert_called_once_with(proxy="http://proxy:3128", timeout=None)

    async def test_context_manager(self) -> None:
        mock_async_client = AsyncMock()
        with patch(
            "lolzteam.runtime.async_http_client.httpx.AsyncClient",
            return_value=mock_async_client,
        ):
            async with AsyncMarketClient(token="t") as client:
                assert isinstance(client, AsyncMarketClient)

    async def test_error_401_raises_auth_error(self) -> None:
        with patch("lolzteam.runtime.async_http_client.httpx.AsyncClient"):
            client = AsyncMarketClient(token="t", max_retries=0)
            mock_http = AsyncMock()
            mock_http.request.return_value = _mock_response(status_code=401)
            client._http._client = mock_http

            with pytest.raises(AuthError):
                await client.category.list()

    async def test_error_429_raises_rate_limit_error(self) -> None:
        with patch("lolzteam.runtime.async_http_client.httpx.AsyncClient"):
            client = AsyncMarketClient(token="t", max_retries=0)
            mock_http = AsyncMock()
            mock_http.request.return_value = _mock_response(
                status_code=429, headers={"retry-after": "7"}
            )
            client._http._client = mock_http

            with pytest.raises(RateLimitError):
                await client.category.list()

    async def test_network_error(self) -> None:
        with patch("lolzteam.runtime.async_http_client.httpx.AsyncClient"):
            client = AsyncMarketClient(token="t", max_retries=0)
            mock_http = AsyncMock()
            mock_http.request.side_effect = httpx.ConnectError("timeout")
            client._http._client = mock_http

            with pytest.raises(NetworkError):
                await client.category.list()

    async def test_request_includes_auth_header(self) -> None:
        with patch("lolzteam.runtime.async_http_client.httpx.AsyncClient"):
            client = AsyncMarketClient(token="market-key", max_retries=0)
            mock_http = AsyncMock()
            mock_http.request.return_value = _mock_response(json_data={})
            client._http._client = mock_http

            await client.category.list()
            call_kwargs = mock_http.request.call_args
            assert call_kwargs.kwargs["headers"]["Authorization"] == "Bearer market-key"


# ---------------------------------------------------------------------------
# Config edge cases
# ---------------------------------------------------------------------------
class TestConfig:
    def test_no_proxy_by_default(self) -> None:
        with patch("lolzteam.runtime.http_client.httpx.Client") as mock_cls:
            ForumClient(token="t")
            mock_cls.assert_called_once_with(proxy=None, timeout=None)

    def test_retry_defaults(self) -> None:
        with patch("lolzteam.runtime.http_client.httpx.Client"):
            client = ForumClient(token="t")
            assert client._http._retry_config.max_retries == 3
            assert client._http._retry_config.base_delay == 1.0
            assert client._http._retry_config.max_delay == 30.0
            client.close()

    def test_forum_default_rate_limit_300(self) -> None:
        with patch("lolzteam.runtime.http_client.httpx.Client"):
            client = ForumClient(token="t")
            assert client._http._rate_limiter is not None
            client.close()

    def test_market_default_rate_limit_120(self) -> None:
        with patch("lolzteam.runtime.http_client.httpx.Client"):
            client = MarketClient(token="t")
            assert client._http._rate_limiter is not None
            client.close()

    def test_custom_base_url_trailing_slash_stripped(self) -> None:
        with patch("lolzteam.runtime.http_client.httpx.Client"):
            client = ForumClient(token="t", base_url="https://example.com/")
            assert client._http._base_url == "https://example.com"
            client.close()

    def test_proxy_rejects_unsupported_scheme(self) -> None:
        with pytest.raises(ConfigError, match="unsupported proxy scheme"):
            ForumClient(token="t", proxy="ftp://proxy:8080")

    def test_proxy_rejects_no_scheme(self) -> None:
        with pytest.raises(ConfigError, match="unsupported proxy scheme"):
            ForumClient(token="t", proxy="just-a-host:8080")

    def test_proxy_rejects_no_host(self) -> None:
        with pytest.raises(ConfigError, match="proxy URL has no host"):
            ForumClient(token="t", proxy="http://")

    def test_proxy_accepts_valid_http(self) -> None:
        with patch("lolzteam.runtime.http_client.httpx.Client"):
            client = ForumClient(token="t", proxy="http://proxy:8080")
            client.close()

    def test_proxy_accepts_valid_socks5(self) -> None:
        with patch("lolzteam.runtime.http_client.httpx.Client"):
            client = ForumClient(token="t", proxy="socks5://proxy:1080")
            client.close()
