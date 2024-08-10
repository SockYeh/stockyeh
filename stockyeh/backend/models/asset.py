from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.sql import func

from stockyeh.backend.database import Base


class Assets(Base):
    """Database model for assets."""

    __tablename__ = "asset"

    id: Column[int] = Column(Integer, primary_key=True, index=True)
    symbol: Column[str] = Column(String(10), unique=True, index=True, nullable=False)
    name: Column[str] = Column(String(50), nullable=False)
    current_price: Column[float] = Column(Float, nullable=False)
    last_updated: Column = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
    created_at: Column = Column(DateTime(timezone=True), server_default=func.now())
    company_id: Column[int] = Column(
        Integer,
        ForeignKey("company.id", ondelete="CASCADE"),
    )


class AssetHistory(Base):
    """Database model for asset history."""

    __tablename__ = "asset_history"

    asset_id: Column[int] = Column(Integer, ForeignKey("asset.id", ondelete="CASCADE"))
    price: Column[float] = Column(Float, nullable=False)
    timestamp: Column = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        primary_key=True,
    )
