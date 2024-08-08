from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.sql import func
from stockyeh.backend.database import Base


class Company(Base):
    """Database model for companies."""

    __tablename__ = "company"

    id: Column[int] = Column(Integer, primary_key=True, index=True)
    name: Column[str] = Column(String(50), unique=True, index=True, nullable=False)
    symbol: Column[str] = Column(String(10), unique=True, index=True, nullable=False)
    description: Column[str] = Column(String(500), nullable=False)
    founded: Column[str] = Column(String(20), nullable=False)
    employee_count: Column[int] = Column(Integer, nullable=False)
    headquarters: Column[str] = Column(String(100), nullable=False)
    industry: Column[str] = Column(String(50), nullable=False)
    last_updated: Column = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
    created_at: Column = Column(DateTime(timezone=True), server_default=func.now())


class CompanyHistory(Base):
    """Database model for company history."""

    __tablename__ = "company_history"

    company_id: Column[int] = Column(
        Integer,
        ForeignKey("company.id", ondelete="CASCADE"),
    )
    revenue: Column[float] = Column(Float, nullable=False)
    market_cap: Column[float] = Column(Float, nullable=False)
    timestamp: Column = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        primary_key=True,
    )


class CompanyRoles(Base):
    """Database model for company roles."""

    __tablename__ = "company_roles"

    company_id: Column[int] = Column(
        Integer,
        ForeignKey("company.id", ondelete="CASCADE"),
    )
    CEO: Column[str] = Column(String(50), nullable=False)
    CMO: Column[str] = Column(String(50), nullable=False)
    CTO: Column[str] = Column(String(50), nullable=False)
    CFO: Column[str] = Column(String(50), nullable=False)
    CIO: Column[str] = Column(String(50), nullable=False)
    COO: Column[str] = Column(String(50), nullable=False)
    timestamp: Column = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        primary_key=True,
    )


class CompanyProjects(Base):
    """Database model for company projects."""

    __tablename__ = "company_projects"

    company_id: Column[int] = Column(
        Integer,
        ForeignKey("company.id", ondelete="CASCADE"),
    )
    project_name: Column[str] = Column(String(50), nullable=False)
    project_description: Column[str] = Column(String(500), nullable=False)
    project_status: Column[str] = Column(String(50), nullable=False)
    project_completion_at: Column = Column(DateTime(timezone=True), nullable=False)
    timestamp: Column = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        primary_key=True,
    )
