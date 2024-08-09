from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from stockyeh.backend.database import create_tables
from stockyeh.backend.routers import auth
from stockyeh.backend.utils.config import env
from stockyeh.frontend import frontend


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:  # noqa: ARG001
    """Context manager for application lifespan."""
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.add_middleware(SessionMiddleware, secret_key=env.AUTH_SECRET)


routers = [auth.router, frontend.router]
for router in routers:
    app.include_router(router)
