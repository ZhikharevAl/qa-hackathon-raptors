from uuid import UUID

from pydantic import BaseModel, Field

from services.users.models.meta_models import Meta


class Game(BaseModel):
    """Model for a single game."""

    category_uuids: list[UUID] = Field(
        ...,
        description="List of category UUIDs associated with the game.",
    )
    price: int = Field(
        ..., description="Price of the game in cents.", example=5999, ge=0
    )
    title: str = Field(
        ...,
        description="Title of the game.",
        max_length=100,
        min_length=1,
    )
    uuid: UUID = Field(
        ...,
        description="Unique identifier for the game.",
    )


class GamesResponse(BaseModel):
    """Model for the API response containing games."""

    games: list[Game] = Field(..., description="List of games.")
    meta: Meta = Field(..., description="Metadata about the games response.")
