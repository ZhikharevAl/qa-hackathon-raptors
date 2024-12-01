from uuid import UUID

from pydantic import BaseModel, Field


class CartItem(BaseModel):
    """Model representing a single item in the cart."""

    item_uuid: UUID = Field(..., description="The UUID of the item in the cart.")
    quantity: int = Field(
        ..., description="The quantity of the item in the cart.", ge=1, le=100
    )
    total_price: int = Field(
        ..., description="The total price of the item in cents.", ge=0
    )


class Cart(BaseModel):
    """Model representing the cart with items."""

    items: list[CartItem] = Field(
        ..., description="List of items in the cart.", max_items=10
    )
    total_price: int = Field(
        ..., description="The total price of the cart in cents.", ge=0
    )
    user_uuid: UUID = Field(..., description="The UUID of the user who owns the cart.")
