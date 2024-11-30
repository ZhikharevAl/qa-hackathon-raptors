from typing import TYPE_CHECKING

import faker
from pydantic_core import ValidationError

from services.users.models.user_models import UsersResponse
from services.users.user_api_client import UserAPIClient

if TYPE_CHECKING:
    from uuid import UUID


class UserAPITestHelpers:
    """Helpers for testing Users API functionality."""

    @staticmethod
    def validate_offset(
        user_api_client: UserAPIClient,
        task_id: str,
        first_validated_response: UsersResponse,
    ) -> None:
        """
        Validate that offset works correctly.

        :param user_api_client: Instance of UserAPIClient
        :param task_id: Task ID to be tested
        :param first_validated_response: First page of users response
        """
        random_offset: int = faker.Faker().random_int(min=1, max=10)
        second_response_data = user_api_client.get_users(
            task_id, offset=random_offset, limit=10
        )

        try:
            second_validated_response = UsersResponse.model_validate(
                second_response_data
            )
        except ValidationError as e:
            msg = (
                f"Response validation failed for Task-Id {task_id} "
                f"with offset={random_offset}: {e}"
            )
            raise AssertionError(msg) from e

        first_user_uuid: UUID = first_validated_response.users[0].uuid

        second_list_uuids: list[UUID] = [
            user.uuid for user in second_validated_response.users
        ]
        assert first_user_uuid not in second_list_uuids, (
            f"First user UUID {first_user_uuid} from initial list "
            f"should not be present in the second list with offset=10"
        )
        assert (
            len(second_validated_response.users) > 0
        ), "Users list should not be empty with offset=10"
        assert (
            second_validated_response.meta.total > 10
        ), "Total users should be more than 10"
