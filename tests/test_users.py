from typing import Any

import allure
import pytest
from pydantic_core import ValidationError

from services.users.models.user_models import UserResponse, UsersResponse
from services.users.user_api_client import UserAPIClient
from utils.helpers import UserAPITestHelpers


@allure.epic("User Management")
@allure.feature("User API Operations")
class TestUsersAPI:
    """Tests for the Users API."""

    @allure.title("Test get users list")
    @allure.description("Verify retrieving users list with different task IDs")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("task_id", ["api-21", "api-6"])
    def test_get_users(self, user_api_client: UserAPIClient, task_id: str) -> None:
        """
        Getting a list of users with a Task-Id.

        :param user_api_client: Instance of UserAPIClient
        :param task_id: Task ID to be tested
        """
        with allure.step(f"Retrieving users list for Task-Id {task_id}"):
            response_data = user_api_client.get_users(task_id, offset=0, limit=10)

            try:
                validated_response: UsersResponse = UsersResponse.model_validate(
                    response_data
                )
            except ValidationError as e:
                msg = f"Response validation failed for Task-Id {task_id}: {e}"
                raise AssertionError(msg) from e

            assert (
                validated_response.meta.total > 0
            ), f"Meta 'total' should be greater than 0 for Task-Id {task_id}, "
            f"but got {validated_response.meta.total}"
            assert (
                len(validated_response.users) > 0
            ), f"Users list should not be empty for Task-Id {task_id}"

            UserAPITestHelpers.validate_offset(
                user_api_client, task_id, validated_response
            )

    @allure.title("Test get single user details")
    @allure.description("Verify retrieving details for a specific user")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_user(self, user_api_client: UserAPIClient, new_user: dict) -> None:
        """
        Test getting user details by UUID.

        :param user_api_client: Instance of UserAPIClient
        :param new_user: Fixture with a newly created user
        """
        task_id = "api-23"
        user_uuid = new_user["uuid"]

        with allure.step(f"Retrieving user details for UUID {user_uuid}"):
            user_data: dict[str, Any] = user_api_client.get_user(user_uuid, task_id)

            expected_keys = ["avatar_url", "email", "name", "nickname", "uuid"]
            assert len(user_data) == len(
                expected_keys
            ), f"Expected {len(expected_keys)} keys, but got {len(user_data)}"
            assert user_data["uuid"] == user_uuid, "UUIDs don't match"

            try:
                UserResponse.model_validate(user_data)
            except ValidationError as e:
                msg = f"User data validation failed: {e}"
                raise AssertionError(msg) from e

    @allure.title("Test delete user")
    @allure.description("Verify deleting a single user by UUID")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_user(self, user_api_client: UserAPIClient, new_user: dict) -> None:
        """
        Test deleting a single user by UUID.

        :param user_api_client: Instance of UserAPIClient
        :param new_user: Fixture with a newly created user
        """
        task_id = "api-1"
        user_uuid = new_user["uuid"]

        with allure.step(f"Deleting user with UUID {user_uuid}"):
            response_data = user_api_client.delete_user(user_uuid, task_id)

            assert (
                response_data["uuid"] == user_uuid
            ), "Deleted UUID should match the created user"

    @allure.title("Test create user")
    @allure.description("Verify user creation and data validation")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user(self, new_user: dict) -> None:
        """
        Test creating a new user.

        :param new_user: Fixture with a newly created user
        """
        with allure.step("Validating newly created user data"):
            user = new_user

            try:
                UserResponse.model_validate(user)
            except ValidationError as e:
                msg = f"User data validation failed: {e}"
                raise AssertionError(msg) from e

    @allure.title("Test update user")
    @allure.description("Verify updating an existing user by UUID")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("task_id", ["api-4", "api-24"])
    def test_update_user(
        self, user_api_client: UserAPIClient, new_user: dict, task_id: str
    ) -> None:
        """
        Test updating a single user by UUID.

        :param user_api_client: Instance of UserAPIClient
        :param new_user: Fixture with a newly created user
        :param task_id: Task ID to be tested
        """
        user_uuid = new_user["uuid"]

        with allure.step(f"Updating user with UUID {user_uuid} for Task-Id {task_id}"):
            updated_user_data = user_api_client.update_user(user_uuid, task_id)

            assert (
                "uuid" in updated_user_data
            ), "UUID field should be present in response"
            assert (
                updated_user_data["uuid"] == user_uuid
            ), "UUID should remain unchanged after update"

            assert (
                updated_user_data["name"] != new_user["name"]
            ), "Name should be different after update"
            assert (
                updated_user_data["email"] != new_user["email"]
            ), "Email should be different after update"
            assert (
                updated_user_data["nickname"] != new_user["nickname"]
            ), "Nickname should be different after update"

            try:
                UserResponse.model_validate(updated_user_data)
            except ValidationError as e:
                msg = f"Updated user data validation failed: {e}"
                raise AssertionError(msg) from e
