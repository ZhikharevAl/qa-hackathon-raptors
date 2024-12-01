from pydantic import BaseModel, Field


class ErrorResponse(BaseModel):
    """Model for receiving error responses."""

    code: int = Field(..., description="The error code.")
    message: str = Field(..., description="The error message.")
