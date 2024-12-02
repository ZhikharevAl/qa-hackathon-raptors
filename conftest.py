import logging
import os
from collections.abc import Generator
from typing import Any

import pytest
from dotenv import load_dotenv
from playwright.sync_api import APIRequestContext, Playwright

from services.games.games_api_client import GamesAPIClient
from services.users.user_api_client import UserAPIClient
from services.wishlist.api_client_wishlist import WishlistAPIClient

load_dotenv()


@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    """Context for executing API requests."""
    headers = {
        "Authorization": "Bearer {os.getenv('API_TOKEN'),
        "Content-Type": "application/json",
    }
    base_url = os.getenv("BASE_URL", "https://default-url.com/api/v1/")

    request_context: APIRequestContext = playwright.request.new_context(
        base_url=base_url,
        extra_http_headers=headers,
    )
    yield request_context
    request_context.dispose()


@pytest.fixture
def user_api_client(api_request_context: APIRequestContext) -> UserAPIClient:
    """User API client."""
    return UserAPIClient(api_request_context)


@pytest.fixture
def game_api_client(api_request_context: APIRequestContext) -> GamesAPIClient:
    """Games API client."""
    return GamesAPIClient(api_request_context)


@pytest.fixture
def wishlist_api_client(api_request_context: APIRequestContext) -> WishlistAPIClient:
    """Wishlist API client."""
    return WishlistAPIClient(api_request_context)


@pytest.fixture(params=["api-3", "api-22"])
def new_user(
    user_api_client: UserAPIClient, request: pytest.FixtureRequest
) -> Generator[dict[str, Any], Any, None]:
    """
    A fixture for creating a new user that will be automatically deleted after the test.

    :param user_api_client: A client for working with the user API
    :param request: Fixture request object, used for parametrization
    """
    task_id = request.param
    user: dict[str, Any] = user_api_client.create_user(task_id)

    yield user

    try:
        user_api_client.delete_user(str(user["uuid"]), task_id)
    except Exception as e:
        error_message = f"The user could not be deleted {user['uuid']}: {e}"
        logging.exception(error_message)


def pytest_configure() -> None:
    """Log configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logging.getLogger("faker").setLevel(logging.WARNING)
