import allure

from services.games.games_api_client import GamesAPIClient
from services.games.models.games_models import GamesResponse


@allure.epic("Game Management")
@allure.feature("Game Search API")
class TestGamesAPI:
    """Tests for the Games API."""

    @allure.title("Test search games with specific title")
    @allure.description(
        "Verify retrieving games with the same title (case-insensitive)"
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_games(self, game_api_client: GamesAPIClient) -> None:
        """
        Test getting a list of games with the same title (case-insensitive).

        :param game_api_client: Instance of GamesAPIClient
        """
        task_id = "api-2"
        specific_game_name = "Elden Ring"

        with allure.step(f"Searching for games with title '{specific_game_name}'"):
            response_data = game_api_client.search_games(
                task_id=task_id, query=specific_game_name
            )

            try:
                validated_response = GamesResponse.model_validate(response_data)
            except Exception as e:
                msg = f"Response validation failed: {e}"
                raise AssertionError(msg) from e

            with allure.step("Checking game titles consistency"):
                game_titles = {game.title.lower() for game in validated_response.games}
                assert len(game_titles) == 1, (
                    f"Expected all games to have the same title (case-insensitive) "
                    f"{specific_game_name}",
                    f"but found different titles: {game_titles}",
                )

            with allure.step("Validating individual game details"):
                for game in validated_response.games:
                    allure.attach(
                        (
                            f"Game Title: {game.title}\n"
                            f"Game Price: {game.price}\n"
                            f"Game UUID: {game.uuid}"
                        ),
                        name="Game Details",
                        attachment_type=allure.attachment_type.TEXT,
                    )

                    assert (
                        game.title.lower() == specific_game_name.lower()
                    ), "Game title doesn't match. Expected "
                    f"{specific_game_name}, got {game.title}"
                    assert (
                        game.price >= 0
                    ), f"Game price should be non-negative but got {game.price}"
                    assert game.uuid, "Game UUID should not be empty"
