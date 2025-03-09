from fastapi import APIRouter, Header, Request
from models.authentication_action_log import SignUpLog, LogInLog, LogOutLog
from typing import Annotated
from utils.verify_signature import verify_signature
from loggers.log_handler import process_and_send_log

authentication_router = APIRouter(
    tags=["Authentication logs"],
    prefix="/dvi-logging/authentication"
)


@authentication_router.post("/send-sign-up-log")
async def send_sign_up_log(
        request: Request,
        x_signature: Annotated[str, Header()],
        log: SignUpLog
):
    await verify_signature(log.dict(), x_signature, request)

    return await process_and_send_log(log)


@authentication_router.post("/send-log-in-log")
async def send_log_in_log(
        request: Request,
        x_signature: Annotated[str, Header()],
        log: LogInLog
):
    await verify_signature(log.dict(), x_signature, request)

    return await process_and_send_log(log)


@authentication_router.post("/send-log-out-log")
async def send_log_out_log(
        request: Request,
        x_signature: Annotated[str, Header()],
        log: LogOutLog
):
    await verify_signature(log.dict(), x_signature, request)

    return await process_and_send_log(log)
