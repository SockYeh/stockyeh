from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from stockyeh.backend.utils.config import env
from stockyeh.backend.database import CurrentSession, create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.add_middleware(SessionMiddleware, secret_key=env.AUTH_SECRET)


@app.get("/")
async def root(db: CurrentSession):
    print(db)
    return {"message": "Hello World"}
