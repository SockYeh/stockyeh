import time
from secrets import token_hex

import jwt
from config import env


class MagicLinkExpiredError(Exception):
    """Magic link expired error."""


class MagicLinkIPMismatchError(Exception):
    """Magic link ip mismatch error."""


class MagicLinkInvalidError(Exception):
    """Magic link invalid error."""


def encode_magiclink_jwt(email: str, ip: str) -> str:
    """Encode magic link jwt."""
    payload = {
        "email": email,
        "ip": ip,
        "expires": time.time() + 60 * 60,
        "random_gibberish": token_hex(32),
    }
    return jwt.encode(payload, env.AUTH_SECRET, algorithm="HS256")


def decode_magiclink_jwt(token: str, ip: str) -> dict:
    """Decode magic link jwt."""
    try:
        decoded = jwt.decode(token, env.AUTH_SECRET, algorithms=["HS256"])
    except jwt.InvalidTokenError as e:
        raise MagicLinkExpiredError from e

    if decoded["ip"] != ip:
        raise MagicLinkIPMismatchError
    if decoded["expires"] < time.time():
        raise MagicLinkExpiredError

    del decoded["random_gibberish"]
    del decoded["ip"]

    return decoded
