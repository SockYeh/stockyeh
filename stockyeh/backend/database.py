import os
from typing import AsyncGenerator

from dotenv import find_dotenv, load_dotenv
from fastapi import Depends
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from typing_extensions import Annotated

load_dotenv(find_dotenv())


def create_engine_and_session(url: str | URL):
    try:
        engine = create_async_engine(url, future=True, pool_pre_ping=True)
    except Exception as e:
        raise e
    else:
        db_session = async_sessionmaker(
            bind=engine, autoflush=False, expire_on_commit=False
        )
        return engine, db_session


SQLALCHEMY_DATABASE_URL = os.environ["DATABASE_URL"]

async_engine, async_db_session = create_engine_and_session(SQLALCHEMY_DATABASE_URL)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    session: AsyncSession = async_db_session()
    try:
        yield session
    except Exception as se:
        await session.rollback()
        raise se
    finally:
        await session.close()


CurrentSession = Annotated[AsyncSession, Depends(get_db)]
