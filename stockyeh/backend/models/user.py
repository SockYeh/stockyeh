from stockyeh.backend.models.model import MappedBase
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func


class User(MappedBase):

    id: Column[int] = Column(Integer, primary_key=True, index=True)
    username: Column[str] = Column(String(20), unique=True, index=True, nullable=False)
    email: Column[str] = Column(String(50), unique=True, index=True, nullable=False)
    joined_at: Column = Column(DateTime(timezone=True), server_default=func.now())


class Portfolio(MappedBase):

    user_id: Column[int] = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    asset_id: Column[int] = Column(Integer, ForeignKey("asset.id", ondelete="CASCADE"))
    amount: Column[int] = Column(Integer, nullable=False)
    bought_at: Column = Column(DateTime(timezone=True), server_default=func.now())
