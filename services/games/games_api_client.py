import urllib.parse
from typing import Any

from playwright.sync_api import APIRequestContext

from services.api_endpoints import APIEndpoints
from services.http_client import HTTPClient

GAMES_ENDPOINT = APIEndpoints.GAMES_ENDPOINT


class GamesAPIClient(HTTPClient):
    """Games API client class."""

    def __init__(self, api_context: APIRequestContext) -> None:
        """
        Initializing the UserAPIClient with the passed APIRequestContext.

        :param api_context: Context for executing API requests
        """
        super().__init__(api_context)

    def search_games(
        self, task_id: str, query: str = "", offset: int = 0, limit: int = 10
    ) -> dict[str, Any]:
        """
        Getting a list of games with a Task-Id and optional search query.

        :param task_id: Task ID
        :param query: Search query for game names
        :param offset: Offset for pagination
        :param limit: Limit of results per page
        :return: Response from the API
        """
        headers = {"X-Task-Id": task_id}

        encoded_query = urllib.parse.quote(query)

        if query:
            endpoint = (
                f"{GAMES_ENDPOINT}/search/"
                f"?query={encoded_query}&offset={offset}&limit={limit}"
            )
        else:
            endpoint = f"{GAMES_ENDPOINT}/search/" f"?offset={offset}&limit={limit}"

        response = self.get(endpoint, headers=headers)

        if not response.ok:
            msg = f"Request failed with status {response.status}"
            raise ValueError(msg)

        return response.json()
