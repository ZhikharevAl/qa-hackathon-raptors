from typing import Any

from playwright.sync_api import APIRequestContext

from services.api_endpoints import APIEndpoints
from services.http_client import HTTPClient
from services.users.payloads import Payloads

USERS_ENDPOINT = APIEndpoints.USERS_ENDPOINT


class UserAPIClient(HTTPClient):
    """User API client class."""

    def __init__(self, api_context: APIRequestContext) -> None:
        """
        Initializing the UserAPIClient with the passed APIRequestContext.

        :param api_context: Context for executing API requests
        """
        super().__init__(api_context)
        self.payloads = Payloads()

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
        response = self.get(USERS_ENDPOINT, headers=headers, params=params)

        if not response.ok:
            msg = f"Request failed with status {response.status}"
            raise ValueError(msg)

        return response.json()

    def get_user(self, user_uuid: str, task_id: str) -> dict[str, Any]:
        """Getting user details by UUID."""
        headers = {"X-Task-Id": task_id}
        endpoint = f"{USERS_ENDPOINT}/{user_uuid}"
        response = self.get(endpoint, headers=headers)

        if not response.ok:
            msg = f"Request failed with status {response.status}"
            raise ValueError(msg)

        return response.json()

    def delete_user(self, user_uuid: str, task_id: str) -> dict[str, Any]:
        """
        Deleting a single user by UUID.

        :param user_uuid: The UUID of the user to delete
        :param task_id: Task ID
        :return: Full API Response
        """
        headers = {"X-Task-Id": task_id}
        endpoint = f"{USERS_ENDPOINT}/{user_uuid}"
        response = self.delete(endpoint, headers=headers)

        if not response.ok:
            msg = f"Request failed with status {response.status}"
            raise ValueError(msg)

        return {"uuid": user_uuid}

    def create_user(self, task_id: str) -> dict[str, Any]:
        """
        Creating a new user.

        :param task_id: Task ID
        :return: Full API Response
        """
        headers = {"X-Task-Id": task_id}
        response = self.post(
            USERS_ENDPOINT, headers=headers, json=self.payloads.create_user
        )

        if not response.ok:
            msg = f"Request failed with status {response.status}"
            raise ValueError(msg)

        return response.json()

    def update_user(self, user_uuid: str, task_id: str) -> dict[str, Any]:
        """
        Updating an existing user by UUID.

        :param user_uuid: The UUID of the user to update
        :param task_id: Task ID
        :return: Full API Response
        """
        headers = {"X-Task-Id": task_id}
        response = self.patch(
            f"{USERS_ENDPOINT}/{user_uuid}",
            headers=headers,
            json=self.payloads.update_user,
        )

        if not response.ok:
            msg = f"Request failed with status {response.status}"
            raise ValueError(msg)

        return response.json()
