from typing import Any

from playwright.sync_api import APIRequestContext

from services.api_endpoints import APIEndpoints
from services.http_client import HTTPClient
from services.users.user_api_client import USERS_ENDPOINT

PAYMENTS_ENDPOINT = APIEndpoints.PAYMENTS_ENDPOINT


class PaymentAPIClient(HTTPClient):
    """Payment API client."""

    def __init__(self, api_context: APIRequestContext) -> None:
        """
        Initializing the PaymentAPIClient with the passed APIRequestContext.

        :param api_context: Context for executing API requests
        """
        super().__init__(api_context)

    def get_payments(self, task_id: str, uuid: str) -> dict[str, Any]:
        """
         Getting payment details by UUID.

        :param task_id: Task ID for the payment
        param uuid: UUID of the payment
        :return: Response from the API
        """
        headers = {"X-Task-Id": task_id}
        endpoint = f"{PAYMENTS_ENDPOINT}/{uuid}"
        response = self.get(endpoint, headers=headers)

        if not response.ok:
            msg = f"Request failed with status {response.status}"
            raise ValueError(msg)

        return response.json()

    def get_all_payments(self, task_id: str, user_uuid: str) -> dict[str, Any]:
        """
        Getting a list of payments with a Task-Id.

        :param task_id: Task ID
        :param user_uuid: UUID of the user
        :return: Response from the API
        """
        headers = {"X-Task-Id": task_id}
        endpoint = f"{USERS_ENDPOINT}/{user_uuid}/{PAYMENTS_ENDPOINT}"
        response = self.get(endpoint, headers=headers)

        if not response.ok:
            msg = f"Request failed with status {response.status}"
            raise ValueError(msg)

        return response.json()
