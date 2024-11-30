from typing import Any

from playwright.sync_api import APIRequestContext

from services.http_client import HTTPClient


class UserAPIClient(HTTPClient):
    """User API client class."""

    def __init__(self, api_context: APIRequestContext) -> None:
        """
        Initializing the UserAPIClient with the passed APIRequestContext.

        :param api_context: Context for executing API requests
        """
        super().__init__(api_context)

    def get_users(
        self, task_id: str, offset: int = 0, limit: int = 10
    ) -> dict[str, Any]:
        """
        Getting a list of users with a Task-Id.

        :param task_id: Task ID
        :return: Response from the API
        """
        headers = {"X-Task-Id": task_id}
        params = {"offset": offset, "limit": limit}
        response = self.get("users", headers=headers, params=params)
        return response.json()

    def get_user(self, user_uuid: str, task_id: str) -> dict[str, Any]:
        """Getting user details by UUID."""
        headers = {"X-Task-Id": task_id}
        endpoint = f"users/{user_uuid}"
        response = self.get(endpoint, headers=headers)

        # Явная проверка статуса
        if not response.ok:
            msg = f"Request failed with status {response.status}"
            raise ValueError(msg)

        return response.json()
