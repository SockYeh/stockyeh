from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Depends
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

from stockyeh.backend.utils.config import env


class DatabaseError(Exception):
    """Error raised due to unhandeled database exception."""

    def __init__(self, message: str) -> None:
        super().__init__(message)


def create_engine_and_session(url: str | URL) -> tuple:
    """Create an async engine and session."""
    try:
        engine = create_async_engine(url, future=True, pool_pre_ping=True)
    except Exception as e:
        raise DatabaseError(e) from e
    else:
        db_session = async_sessionmaker(
            bind=engine,
            autoflush=False,
            expire_on_commit=False,
            class_=AsyncSession,
        )
        return engine, db_session


SQLALCHEMY_DATABASE_URL = env.DATABASE_URL

async_engine, async_db_session = create_engine_and_session(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Get an async database session."""
    session: AsyncSession = async_db_session()
    try:
        yield session
    except Exception as se:
        await session.rollback()
        raise DatabaseError(se) from se
    finally:
        await session.close()


CurrentSession = Annotated[AsyncSession, Depends(get_db)]


async def create_tables() -> None:
    """Create database tables."""
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
