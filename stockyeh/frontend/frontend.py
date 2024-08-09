from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="", tags=["frontend"])
templates = Jinja2Templates(directory=r"stockyeh\frontend")


@router.get("/signin", response_class=HTMLResponse)
async def signin(request: Request) -> HTMLResponse:
    """Signin page."""
    return templates.TemplateResponse("auth.html", {"request": request})
