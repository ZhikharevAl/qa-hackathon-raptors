from services.games.games_api_client import GamesAPIClient
from services.games.models.games_models import GamesResponse


class TestGamesAPI:
    """Tests for the Games API."""

    def test_get_games(self, game_api_client: GamesAPIClient) -> None:
        """
        Test getting a list of games for a specific Task ID.

        :param user_api_client: Instance of UserAPIClient
        """
        task_id = "api-2"
        offset = 0
        limit = 10
        response_data = game_api_client.get_games(
            task_id=task_id, offset=offset, limit=limit
        )

        try:
            validated_response = GamesResponse.model_validate(response_data)
        except Exception as e:  # noqa: BLE001
            msg = f"Response validation failed: {e}"
            raise AssertionError(msg)  # noqa: B904

        assert validated_response.meta.total >= 0, "Meta 'total' should be non-negative"
        assert (
            len(validated_response.games) <= limit
        ), f"Expected at most {limit} games, but got more"
        for game in validated_response.games:
            assert (
                game.price >= 0
            ), f"Game price should be non-negative but got {game.price}"
            assert game.title, "Game title should not be empty"
            assert game.uuid, "Game UUID should not be empty"
