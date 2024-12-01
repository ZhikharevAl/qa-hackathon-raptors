from datetime import datetime
from enum import Enum
from uuid import UUID

from pydantic import BaseModel, Field


class OrderStatus(str, Enum):
    """Enumeration for order statuses."""

    OPEN = "open"
    PENDING = "pending"
    OVERDUE = "overdue"
    CANCELED = "canceled"
    COMPLETED = "completed"


class CartItem(BaseModel):
    """Model representing an item in the order."""

    item_uuid: UUID = Field(..., description="The UUID of the item.")
    quantity: int = Field(..., description="The quantity of the item.", ge=1, le=100)
    total_price: int = Field(
        ..., description="The total price of the item in cents.", ge=0
    )


class Order(BaseModel):
    """Model representing an order."""

    created_at: datetime = Field(
        ..., description="The timestamp when the order was created.", readOnly=True
    )
    updated_at: datetime = Field(
        ..., description="The timestamp when the order was last updated.", readOnly=True
    )
    items: list[CartItem] = Field(
        ..., description="List of items in the order.", min_items=1, max_items=10
    )
    status: OrderStatus = Field(
        default=OrderStatus.OPEN, description="The current status of the order."
    )
    total_price: int = Field(
        ..., description="The total price of the order in cents.", ge=0
    )
    user_uuid: UUID = Field(
        ..., description="The UUID of the user who placed the order."
    )
    uuid: UUID = Field(..., description="The UUID of the order.")
