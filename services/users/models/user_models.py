from uuid import UUID

from pydantic import BaseModel, Field

from services.users.models.meta_models import Meta


class UserRequest(BaseModel):
    """Model for sending user data in a request."""

    email: str = Field(
        ...,
        max_length=100,
        min_length=5,
        pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
        description="The email of the user.",
    )
    password: str = Field(
        ...,
        max_length=100,
        min_length=6,
        pattern=r"^\S.+$",
        description="The password of the user (write-only).",
    )
    name: str = Field(
        ...,
        max_length=100,
        min_length=1,
        pattern=r"^\S.+$",
        description="The name of the user.",
    )
    nickname: str = Field(
        ...,
        max_length=100,
        min_length=2,
        pattern=r"^[a-zA-Z0-9_.+-]+$",
        description="The nickname of the user.",
    )
    avatar_url: str = Field(..., description="The URL of the user's avatar.")


class UserResponse(BaseModel):
    """Model for receiving user data in a response."""

    uuid: UUID = Field(
        ...,
        description="The UUID of the user.",
    )
    email: str = Field(
        ...,
        max_length=100,
        min_length=5,
        pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
        description="The email of the user.",
    )
    name: str = Field(
        ...,
        max_length=100,
        min_length=1,
        pattern=r"^\S.+$",
        description="The name of the user.",
    )
    nickname: str = Field(
        ...,
        max_length=100,
        min_length=2,
        pattern=r"^[a-zA-Z0-9_.+-]+$",
        description="The nickname of the user.",
    )
    avatar_url: str = Field(..., description="The URL of the user's avatar.")


class UsersResponse(BaseModel):
    """Model for the entire API response."""

    meta: Meta
    users: list[UserResponse]
