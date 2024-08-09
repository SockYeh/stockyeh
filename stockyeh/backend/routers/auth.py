import re

from fastapi import APIRouter, HTTPException, Request, status
from sqlalchemy import select

from stockyeh.backend.database import CurrentSession
from stockyeh.backend.models.user import User
from stockyeh.backend.schemas.auth import UserLogin
from stockyeh.backend.utils.magic_link import (
    MLErrors,
    decode_magiclink_jwt,
    encode_magiclink_jwt,
    send_verification_email,
)

router = APIRouter(
    prefix="/api/auth",
    tags=["auth"],
)


@router.post("/login", status_code=status.HTTP_204_NO_CONTENT)
async def login(
    request: Request,
    payload: UserLogin,
) -> None:
    """Login user."""
    email = payload.email
    ip = request.client.host

    if not re.match(r"\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*", email):
        raise HTTPException(status_code=400, detail="Invalid email")

    token = encode_magiclink_jwt(email, ip)
    try:
        await send_verification_email(
            email,
            token,
            f"{request.base_url}api/auth/verify",
        )
    except MLErrors.EmailError as e:
        raise HTTPException(status_code=500, detail="Email error") from e


@router.get("/verify", status_code=status.HTTP_204_NO_CONTENT)
async def verify(
    request: Request,
    db: CurrentSession,
    token: str,
) -> None:
    """Verify user."""
    ip = request.client.host
    try:
        decoded = decode_magiclink_jwt(token, ip)
    except MLErrors.ExpiredError as e:
        raise HTTPException(status_code=400, detail="Expired token") from e
    except MLErrors.IPMismatchError as e:
        raise HTTPException(status_code=400, detail="IP mismatch") from e
    except MLErrors.InvalidError as e:
        raise HTTPException(status_code=400, detail="Invalid token") from e

    email = decoded["email"]

    async with db as session:
        stmt = select(User).where(User.email == email)
        user = (await session.execute(stmt)).first().User

        if not user:
            user = User(email=email, username=email.split("@")[0])
            session.add(user)
            await session.commit()
            user = (await session.execute(stmt)).first().User

        request.session["userid"] = str(user.id)
        print(request.session["userid"])
        await session.commit()
