from fastapi import APIRouter, Header, Request
from models.settings_action_log import (
    ChangePersonalInformationLog,
    ChangeEmailLog,
    ChangePasswordLog,
    DeleteAccountLog
)
from typing import Annotated
from utils.verify_signature import verify_signature
from loggers.log_handler import process_and_send_log

settings_action_router = APIRouter(
    tags=["Settings action logs"],
    prefix="/dvi-logging/settings-action"
)


@settings_action_router.post("/send-change-personal-information-log")
async def send_change_personal_information_log(
        request: Request,
        x_signature: Annotated[str, Header()],
        log: ChangePersonalInformationLog
):
    await verify_signature(log.dict(), x_signature, request)

    return await process_and_send_log(log)


@settings_action_router.post("/send-change-email-log")
async def send_change_email_log(
        request: Request,
        x_signature: Annotated[str, Header()],
        log: ChangeEmailLog
):
    await verify_signature(log.dict(), x_signature, request)

    return await process_and_send_log(log)


@settings_action_router.post("/send-change-password-log")
async def send_change_password_log(
        request: Request,
        x_signature: Annotated[str, Header()],
        log: ChangePasswordLog
):
    await verify_signature(log.dict(), x_signature, request)

    return await process_and_send_log(log)


@settings_action_router.post("/send-delete-account-log")
async def send_delete_account_log(
        request: Request,
        x_signature: Annotated[str, Header()],
        log: DeleteAccountLog
):
    await verify_signature(log.dict(), x_signature, request)

    return await process_and_send_log(log)
