from typing import Any

from playwright.sync_api import APIRequestContext

from services.api_endpoints import APIEndpoints
from services.games.games_api_client import GAMES_ENDPOINT
from services.http_client import HTTPClient

CATEGORIES_ENDPOINT = APIEndpoints.CATEGORIES_ENDPOINT


class CategoriesAPIClient(HTTPClient):
    """Categories API client class."""

    def __init__(self, api_context: APIRequestContext) -> None:
        """Initializing the CategoriesAPIClient with the passed APIRequestContext."""
        super().__init__(api_context)

    def get_games(
        self, task_id: str, offset: int = 0, limit: int = 10, categories_uuid: str = ""
    ) -> dict[str, Any]:
        """Getting a list of games with a categories_uuid."""
        headers = {"X-Task-Id": task_id}
        params = {"offset": offset, "limit": limit}
        endpoint = f"{CATEGORIES_ENDPOINT}/{categories_uuid}/{GAMES_ENDPOINT}"
        response = self.get(endpoint, headers=headers, params=params)

        if not response.ok:
            msg = f"Request failed with status {response.status}"
            raise ValueError(msg)

        return response.json()
