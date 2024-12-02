from typing import Any

from playwright.sync_api import APIRequestContext

from services.api_endpoints import APIEndpoints
from services.http_client import HTTPClient
from services.users.user_api_client import USERS_ENDPOINT

ORDERS_ENDPOINT = APIEndpoints.ORDERS_ENDPOINT


class OrdersAPIClient(HTTPClient):
    """Orders API client class."""

    def __init__(self, api_context: APIRequestContext) -> None:
        """
        Initializing the UserAPIClient with the passed APIRequestContext.

        :param api_context: Context for executing API requests
        """
        super().__init__(api_context)

    def get_a_payment(self, task_id: str, order_uuid: str) -> dict[str, Any]:
        """
        Getting payment details by UUID.

        :param task_id: Task ID for the payment
        :param uuid: UUID of the payment
        :return: Response from the API
        """
        headers = {"X-Task-Id": task_id}
        endpoint = f"{ORDERS_ENDPOINT}/{order_uuid}"
        response = self.get(endpoint, headers=headers)

        if not response.ok:
            msg = f"Request failed with status {response.status}"
            raise ValueError(msg)

        return response.json()

    def get_all_orders(
        self, task_id: str, user_uuid: str, offset: int = 0, limit: int = 10
    ) -> dict[str, Any]:
        """
        Getting a list of orders with a Task-Id.

        :param task_id: Task ID
        :param user_uuid: UUID of the user
        :return: Response from the API
        """
        headers = {"X-Task-Id": task_id}
        params = {"offset": offset, "limit": limit}
        endpoint = f"{USERS_ENDPOINT}/{user_uuid}/{ORDERS_ENDPOINT}"
        response = self.get(endpoint, headers=headers, params=params)

        if not response.ok:
            msg = f"Request failed with status {response.status}"
            raise ValueError(msg)

        return response.json()

    def create_new_order(self, task_id: str, user_uuid: str) -> dict[str, Any]:
        """
        Creating a new order.

        :param task_id: Task ID
        :param user_uuid: UUID of the user
        :return: Response from the API
        """
        headers = {"X-Task-Id": task_id}
        endpoint = f"{USERS_ENDPOINT}/{user_uuid}/{ORDERS_ENDPOINT}"
        response = self.post(endpoint, headers=headers)

        if not response.ok:
            msg = f"Request failed with status {response.status}"
            raise ValueError(msg)

        return response.json()

    def update_order(self, order_uuid: str, task_id: str) -> dict[str, Any]:
        """
        Updating an existing order by UUID.

        :param order_uuid: The UUID of the order to update
        :param task_id: Task ID
        :return: Response from the API
        """
        headers = {"X-Task-Id": task_id}
        endpoint = f"{ORDERS_ENDPOINT}/{order_uuid}/status"
        response = self.patch(endpoint, headers=headers)

        if not response.ok:
            msg = f"Request failed with status {response.status}"
            raise ValueError(msg)

        return response.json()
