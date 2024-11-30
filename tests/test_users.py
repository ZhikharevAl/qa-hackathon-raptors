import pytest

from services.users.models.user_models import UsersResponse
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

        from pydantic import ValidationError

        try:
            validated_response = UsersResponse.model_validate(response_data)
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
