from pydantic import BaseModel, Field


class Meta(BaseModel):
    """Model for Meta information in the API response."""

    total: int = Field(..., ge=0, description="Total number of users.")
