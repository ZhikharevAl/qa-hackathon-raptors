from datetime import datetime
from enum import Enum
from uuid import UUID

from pydantic import BaseModel, Field


class PaymentType(str, Enum):
    """Enumeration for payment methods."""

    CARD = "card"
    PAYPAL = "paypal"
    WECHAT_PAY = "wechat_pay"
    MIR_PAY = "mir_pay"


class PaymentStatus(str, Enum):
    """Enumeration for payment statuses."""

    PROCESSING = "processing"
    SUCCEEDED = "succeeded"
    CANCELED = "canceled"


class Payment(BaseModel):
    """Model representing a payment response."""

    order_uuid: UUID = Field(
        ..., description="The UUID of the order associated with the payment."
    )
    payment_method: PaymentType = Field(
        default=PaymentType.CARD, description="The payment method used."
    )
    amount: int = Field(..., ge=0, description="The amount paid in cents.")
    created_at: datetime = Field(
        ..., description="The timestamp when the payment was created.", readOnly=True
    )
    status: PaymentStatus = Field(
        default=PaymentStatus.SUCCEEDED, description="The status of the payment."
    )
    updated_at: datetime = Field(
        ...,
        description="The timestamp when the payment was last updated.",
        readOnly=True,
    )
    user_uuid: UUID = Field(
        ..., description="The UUID of the user who made the payment."
    )
    uuid: UUID = Field(..., description="The UUID of the payment transaction.")
