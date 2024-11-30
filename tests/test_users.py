from typing import Any

import pytest
from pydantic_core import ValidationError

from services.users.models.user_models import UserResponse, UsersResponse
from services.users.user_api_client import UserAPIClient
from utils.helpers import UserAPITestHelpers


class TestUsersAPI:
    """Tests for the Users API."""

    @pytest.mark.parametrize("task_id", ["api-21", "api-6"])
    def test_get_users(self, user_api_client: UserAPIClient, task_id: str) -> None:
        """
        Getting a list of users with a Task-Id.

        :param user_api_client: Instance of UserAPIClient
        :param task_id: Task ID to be tested
        """
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

        UserAPITestHelpers.validate_offset(user_api_client, task_id, validated_response)

    def test_get_user(self, user_api_client: UserAPIClient) -> None:
        """
        Test getting user details by UUID.

        :param user_api_client: Instance of UserAPIClient
        """
        task_id = "api-23"
        user_uuid = "23403afa-483c-4803-8af1-2d1316f1460f"
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
