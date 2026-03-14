# Auto-generated. Do not edit manually.
from __future__ import annotations

from lolzteam.runtime.async_http_client import AsyncHttpClient
from lolzteam.runtime.http_client import HttpClient
from lolzteam.runtime.types import ClientConfig, ProxyConfig, RateLimitConfig, RetryConfig

from .assets import AssetsApi, AsyncAssetsApi
from .batch import AsyncBatchApi, BatchApi
from .categories import AsyncCategoriesApi, CategoriesApi
from .chatbox import AsyncChatboxApi, ChatboxApi
from .conversations import AsyncConversationsApi, ConversationsApi
from .forms import AsyncFormsApi, FormsApi
from .forums import AsyncForumsApi, ForumsApi
from .links import AsyncLinksApi, LinksApi
from .navigation import AsyncNavigationApi, NavigationApi
from .notifications import AsyncNotificationsApi, NotificationsApi
from .o_auth import AsyncOAuthApi, OAuthApi
from .pages import AsyncPagesApi, PagesApi
from .posts import AsyncPostsApi, PostsApi
from .profile_posts import AsyncProfilePostsApi, ProfilePostsApi
from .search import AsyncSearchApi, SearchApi
from .tags import AsyncTagsApi, TagsApi
from .threads import AsyncThreadsApi, ThreadsApi
from .users import AsyncUsersApi, UsersApi


class ForumClient:
    def __init__(
        self,
        token: str,
        *,
        base_url: str = "https://api.lolz.live",
        proxy: str | None = None,
        max_retries: int = 3,
        base_delay: float = 1.0,
        max_delay: float = 30.0,
        requests_per_minute: int = 300,
    ) -> None:
        config = ClientConfig(
            token=token,
            base_url=base_url,
            proxy=ProxyConfig(url=proxy) if proxy else None,
            retry=RetryConfig(max_retries=max_retries, base_delay=base_delay, max_delay=max_delay),
            rate_limit=RateLimitConfig(requests_per_minute=requests_per_minute),
        )
        self._http = HttpClient(config)
        self.o_auth = OAuthApi(self._http)
        self.assets = AssetsApi(self._http)
        self.categories = CategoriesApi(self._http)
        self.forums = ForumsApi(self._http)
        self.links = LinksApi(self._http)
        self.pages = PagesApi(self._http)
        self.navigation = NavigationApi(self._http)
        self.threads = ThreadsApi(self._http)
        self.posts = PostsApi(self._http)
        self.users = UsersApi(self._http)
        self.profile_posts = ProfilePostsApi(self._http)
        self.conversations = ConversationsApi(self._http)
        self.notifications = NotificationsApi(self._http)
        self.tags = TagsApi(self._http)
        self.search = SearchApi(self._http)
        self.batch = BatchApi(self._http)
        self.chatbox = ChatboxApi(self._http)
        self.forms = FormsApi(self._http)

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> ForumClient:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()


class AsyncForumClient:
    def __init__(
        self,
        token: str,
        *,
        base_url: str = "https://api.lolz.live",
        proxy: str | None = None,
        max_retries: int = 3,
        base_delay: float = 1.0,
        max_delay: float = 30.0,
        requests_per_minute: int = 300,
    ) -> None:
        config = ClientConfig(
            token=token,
            base_url=base_url,
            proxy=ProxyConfig(url=proxy) if proxy else None,
            retry=RetryConfig(max_retries=max_retries, base_delay=base_delay, max_delay=max_delay),
            rate_limit=RateLimitConfig(requests_per_minute=requests_per_minute),
        )
        self._http = AsyncHttpClient(config)
        self.o_auth = AsyncOAuthApi(self._http)
        self.assets = AsyncAssetsApi(self._http)
        self.categories = AsyncCategoriesApi(self._http)
        self.forums = AsyncForumsApi(self._http)
        self.links = AsyncLinksApi(self._http)
        self.pages = AsyncPagesApi(self._http)
        self.navigation = AsyncNavigationApi(self._http)
        self.threads = AsyncThreadsApi(self._http)
        self.posts = AsyncPostsApi(self._http)
        self.users = AsyncUsersApi(self._http)
        self.profile_posts = AsyncProfilePostsApi(self._http)
        self.conversations = AsyncConversationsApi(self._http)
        self.notifications = AsyncNotificationsApi(self._http)
        self.tags = AsyncTagsApi(self._http)
        self.search = AsyncSearchApi(self._http)
        self.batch = AsyncBatchApi(self._http)
        self.chatbox = AsyncChatboxApi(self._http)
        self.forms = AsyncFormsApi(self._http)

    async def close(self) -> None:
        await self._http.close()

    async def __aenter__(self) -> AsyncForumClient:
        return self

    async def __aexit__(self, *args: object) -> None:
        await self.close()
