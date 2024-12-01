from enum import Enum

from pydantic import BaseModel, Field


class OrderStatus(str, Enum):
    """Enumeration for order statuses."""

    OPEN = "open"
    PENDING = "pending"
    OVERDUE = "overdue"
    CANCELED = "canceled"
    COMPLETED = "completed"


class PatchOrderStatus(BaseModel):
    """Model for updating the status of an order."""

    status: OrderStatus = Field(..., description="The new status of the order.")
