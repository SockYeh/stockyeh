from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    """Schema for user."""

    id: int
    username: str
    email: str
    joined_at: datetime


class UserLogin(BaseModel):
    """Schema for user login."""

    email: str
