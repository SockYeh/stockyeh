from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.sql import func


class Assets(DeclarativeBase):
    __tablename__ = "assets"

    id: Column[int] = Column(Integer, primary_key=True, index=True)
    symbol: Column[str] = Column(String(10), unique=True, index=True, nullable=False)
    name: Column[str] = Column(String(50), nullable=False)
    current_price: Column[float] = Column(Float, nullable=False)
    last_updated: Column = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    created_at: Column = Column(DateTime(timezone=True), server_default=func.now())
    company_id: Column[int] = Column(
        Integer, ForeignKey("companies.id", ondelete="CASCADE")
    )


class AssetHistory(DeclarativeBase):
    __tablename__ = "asset_history"

    asset_id: Column[int] = Column(Integer, ForeignKey("assets.id", ondelete="CASCADE"))
    price: Column[float] = Column(Float, nullable=False)
    timestamp: Column = Column(DateTime(timezone=True), server_default=func.now())
