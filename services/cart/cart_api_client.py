from typing import Any

from playwright.sync_api import APIRequestContext

from services.api_endpoints import APIEndpoints
from services.http_client import HTTPClient

CART_ENDPOINT = APIEndpoints.CART_ENDPOINT


class CartAPIClient(HTTPClient):
    """Cart API client."""

    def __init__(self, api_context: APIRequestContext) -> None:
        """
        Initializing the UserAPIClient with the passed APIRequestContext.

        :param api_context: Context for executing API requests
        """
        super().__init__(api_context)

    def get_a_cart(self, task_id: str, user_uuid: str) -> dict[str, Any]:
        """
        Getting a list of users with a Task-Id.

        :param task_id: Task ID
        :return: Response from the API
        """
        headers = {"X-Task-Id": task_id}
        endpoint = f"{APIEndpoints.USERS_ENDPOINT}/{user_uuid}/{CART_ENDPOINT}"
        response = self.get(endpoint, headers=headers)

        if not response.ok:
            msg = f"Request failed with status {response.status}: {response.text}"
            raise ValueError(msg)

        return response.json()

    def add_an_item_to_cart(
        self, task_id: str, user_uuid: str, item_uuid: str
    ) -> dict[str, Any]:
        """
        Adding an item to the user's cart.

        :param task_id: Task ID
        :param user_uuid: UUID of the user
        :param item_uuid: UUID of the item to add to the cart
        """
        headers = {"X-Task-Id": task_id}
        endpoint = f"{APIEndpoints.USERS_ENDPOINT}/{user_uuid}/{CART_ENDPOINT}/add"
        data = {"item_uuid": item_uuid}
        response = self.post(endpoint, headers=headers, json=data)

        if not response.ok:
            msg = f"Request failed with status {response.status}: {response.text}"
            raise ValueError(msg)

        return response.json()

    def change_item_quantity(
        self, task_id: str, user_uuid: str, item_uuid: str, quantity: int
    ) -> dict[str, Any]:
        """
        Changing the quantity of an item in the user's cart.

        :param task_id: Task ID
        :param user_uuid: UUID of the user
        :param item_uuid: UUID of the item to change the quantity of
        :param quantity: New quantity of the item
        """
        headers = {"X-Task-Id": task_id}
        endpoint = f"{APIEndpoints.USERS_ENDPOINT}/{user_uuid}/{CART_ENDPOINT}/change"
        data = {"item_uuid": item_uuid, "quantity": quantity}
        response = self.post(endpoint, headers=headers, json=data)

        if not response.ok:
            msg = f"Request failed with status {response.status}: {response.text}"
            raise ValueError(msg)

        return response.json()

    def clear_cart(self, task_id: str, user_uuid: str) -> dict[str, Any]:
        """
        Clearing the user's cart.

        :param task_id: Task ID
        :param user_uuid: UUID of the user
        """
        headers = {"X-Task-Id": task_id}
        endpoint = f"{APIEndpoints.USERS_ENDPOINT}/{user_uuid}/{CART_ENDPOINT}/clear"
        response = self.post(endpoint, headers=headers)

        if not response.ok:
            msg = f"Request failed with status {response.status}: {response.text}"
            raise ValueError(msg)

        return response.json()

    def remove_an_item_from_cart(
        self, task_id: str, user_uuid: str, item_uuid: str
    ) -> dict[str, Any]:
        """
        Removing an item from the user's cart.

        :param task_id: Task ID
        :param user_uuid: UUID of the user
        :param item_uuid: UUID of the item to remove from the cart
        """
        headers = {"X-Task-Id": task_id}
        endpoint = f"{APIEndpoints.USERS_ENDPOINT}/{user_uuid}/{CART_ENDPOINT}/remove"
        data = {"item_uuid": item_uuid}
        response = self.post(endpoint, headers=headers, json=data)

        if not response.ok:
            msg = f"Request failed with status {response.status}: {response.text}"
            raise ValueError(msg)

        return response.json()
