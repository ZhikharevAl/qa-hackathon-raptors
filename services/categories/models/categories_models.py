from uuid import UUID

from pydantic import BaseModel, Field


class Category(BaseModel):
    """Model representing a category."""

    name: str = Field(
        ..., description="The name of the category.", max_length=100, min_length=1
    )
    uuid: UUID = Field(..., description="The UUID of the category.")
