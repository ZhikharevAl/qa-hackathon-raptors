from pydantic import BaseModel, Field

from services.orders.models.order_models import Order


class Meta(BaseModel):
    """Model representing metadata for a collection of orders."""

    total: int = Field(..., description="Total number of orders.")
    orders: list[Order] = Field(..., description="List of orders.")
