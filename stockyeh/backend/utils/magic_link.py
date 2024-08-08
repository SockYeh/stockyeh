import time
from email.mime.text import MIMEText
from secrets import token_hex

import aiosmtplib
import jwt
from config import env

SMTP_EMAIL = env.SMTP_EMAIL
SMTP_PASSWORD = env.SMTP_PASSWORD
SMTP_HOST = env.SMTP_HOST
SMTP_PORT = env.SMTP_PORT


class MLErrors:
    """Errors for magic link."""

    class ExpiredError(Exception):
        """Magic link expired error."""

    class IPMismatchError(Exception):
        """Magic link ip mismatch error."""

    class InvalidError(Exception):
        """Magic link invalid error."""

    class EmailError(Exception):
        """Magic link email error."""


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
        raise MLErrors.ExpiredError from e

    if decoded["ip"] != ip:
        raise MLErrors.IPMismatchError

    if decoded["expires"] < time.time():
        raise MLErrors.ExpiredError

    del decoded["random_gibberish"]
    del decoded["ip"]

    return decoded


async def send_verification_email(email: str, token: str, url: str) -> bool:
    """Send verification email."""
    email_body = f'<pre> <a href="{url}?token={token}">click here</a> </pre>'

    msg = MIMEText(email_body, "html")
    msg["Subject"] = "StockYeh Magic link"
    msg["From"] = SMTP_EMAIL
    msg["To"] = email

    try:
        async with aiosmtplib.SMTP(SMTP_HOST, SMTP_PORT) as smtp:
            await smtp.ehlo()
            await smtp.login(SMTP_EMAIL, SMTP_PASSWORD)
            await smtp.send_message(msg)
            await smtp.quit()

            return True
    except aiosmtplib.errors.SMTPResponseException as e:
        raise MLErrors.EmailError from e
