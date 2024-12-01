from pydantic import BaseModel, Field


class PaginationParams(BaseModel):
    """Model for pagination parameters (limit and offset)."""

    limit: int = Field(
        default=10,
        ge=1,
        le=100,
        description="The maximum number of results to return (1-100).",
    )

    offset: int = Field(
        default=0,
        ge=0,
        description="The offset (starting point) for the results.",
    )
