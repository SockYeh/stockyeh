from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.sql import func
from stockyeh.backend.database import Base


class User(Base):
    """Database model for users."""

    __tablename__ = "user"

    id: Column[int] = Column(Integer, primary_key=True, index=True)
    username: Column[str] = Column(String(20), unique=True, index=True, nullable=False)
    email: Column[str] = Column(String(50), unique=True, index=True, nullable=False)
    joined_at: Column = Column(DateTime(timezone=True), server_default=func.now())


class Portfolio(Base):
    """Database model for user portfolio."""

    __tablename__ = "portfolio"

    user_id: Column[int] = Column(
        Integer,
        ForeignKey("user.id", ondelete="CASCADE"),
        nullable=False,
    )
    asset_id: Column[int] = Column(
        Integer,
        ForeignKey("asset.id", ondelete="CASCADE"),
        primary_key=True,
    )
    amount: Column[int] = Column(Integer, nullable=False)
    bought_at: Column = Column(DateTime(timezone=True), server_default=func.now())
