from uuid import UUID

import allure
import pytest
from pydantic_core import ValidationError

from services.wishlist.api_client_wishlist import WishlistAPIClient
from services.wishlist.models.wishlist_models import Wishlist


@allure.epic("Wishlist Management")
@allure.feature("Add Game to Wishlist")
@allure.title("Test adding a game to the wishlist")
@allure.description("Verify adding a game to the user's wishlist")
@pytest.mark.parametrize("task_id", ["api-5", "api-25"])
def test_add_game_to_wishlist(
    wishlist_api_client: WishlistAPIClient, new_user: dict, task_id: str
) -> None:
    """
    Test adding a game to the user's wishlist.

    :param wishlist_api_client: Instance of WishlistAPIClient
    :param new_user: Fixture with a newly created user
    :param task_id: Task ID
    """
    user_uuid = UUID(new_user["uuid"])
    item_uuid = "03dbad48-ad81-433d-9901-dd5332f5d9ee"

    with allure.step("Adding a game to the wishlist"):
        response_data = wishlist_api_client.add_an_item_to_wishlist(
            task_id=task_id, user_uuid=str(user_uuid), item_uuid=item_uuid
        )

    with allure.step("Checking response data"):
        try:
            validated_response: Wishlist = Wishlist.model_validate(response_data)
        except ValidationError as e:
            msg = f"Response validation failed for Task-Id {task_id}: {e}"
            raise AssertionError(msg) from e

    with allure.step("Checking response data"):
        assert str(validated_response.user_uuid) == str(
            user_uuid
        ), "UUID users don't match"

        assert (
            len(validated_response.items) == 1
        ), "There should be exactly one item in the wishlist"

        assert any(
            item.uuid == UUID(item_uuid) for item in validated_response.items
        ), "Item UUIDs don't match."

        with allure.step("Adding a game to the wishlist"):
            response_data = wishlist_api_client.add_an_item_to_wishlist(
                task_id=task_id, user_uuid=str(user_uuid), item_uuid=item_uuid
            )
