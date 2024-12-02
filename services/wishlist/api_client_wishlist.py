from playwright.sync_api import APIRequestContext

from services.api_endpoints import APIEndpoints
from services.http_client import HTTPClient
from services.users.user_api_client import USERS_ENDPOINT

WISHLIST_ENDPOINT = APIEndpoints.WISHLIST_ENDPOINT


class WishlistAPIClient(HTTPClient):
    """Wishlist API client class."""

    def __init__(self, api_context: APIRequestContext) -> None:
        """
        Initializing the UserAPIClient with the passed APIRequestContext.

        :param api_context: Context for executing API requests
        """
        super().__init__(api_context)

    def add_an_item_to_wishlist(
        self, task_id: str, user_uuid: str, item_uuid: str
    ) -> dict:
        """
        Adding an item to the user's wishlist.

        :param task_id: Task ID
        :param user_uuid: UUID of the user
        :param item_uuid: UUID of the item to add to the wishlist
        """
        headers = {"X-Task-Id": task_id}
        endpoint = f"{USERS_ENDPOINT}/{user_uuid}/{WISHLIST_ENDPOINT}/add"
        data = {"item_uuid": item_uuid}
        response = self.post(endpoint, headers=headers, json=data)

        if not response.ok:
            msg = f"Request failed with status {response.status}: {response.text}"
            raise ValueError(msg)

        return response.json()
