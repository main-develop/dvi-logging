from fastapi import APIRouter, Header, Request
from models.page_navigation_log import PageNavigationLog
from typing import Annotated
from utils.verify_signature import verify_signature
from loggers.log_handler import process_and_send_log

page_navigation_router = APIRouter(
    tags=["Page navigation logs"],
    prefix="/dvi-logging/page-navigation"
)


@page_navigation_router.post("/send-page-navigation-log")
async def send_page_navigation_log(
        request: Request,
        x_signature: Annotated[str, Header()],
        log: PageNavigationLog
):
    await verify_signature(log.dict(), x_signature, request)

    return await process_and_send_log(log)
