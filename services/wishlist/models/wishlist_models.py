from pydantic import UUID4, BaseModel, Field


class Game(BaseModel):
    """Game model."""

    category_uuids: list[UUID4] = Field(..., max_items=10)
    price: int = Field(..., ge=0, description="Price of the game in cents")
    title: str = Field(..., min_length=1, max_length=100)
    uuid: UUID4 = Field(..., description="Unique identifier for the game")


class Wishlist(BaseModel):
    """Wishlist model."""

    items: list[Game] = Field(
        ..., max_items=10, description="List of games in the wishlist"
    )
    user_uuid: UUID4 = Field(..., description="Unique identifier for the user")
