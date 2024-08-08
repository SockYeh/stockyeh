from pydantic import BaseModel


class UserLogin(BaseModel):
    """Schema for user login."""

    email: str
