from pydantic import BaseModel, ConfigDict
from models.base_log import *
from typing import Literal

change_personal_information_examples = [
    {
        "sent_at": "2025-03-01T19:54:13.830Z",
        "processed_at": "2025-03-01T19:54:13.830Z",
        "latency_ms": 0,
        "log_level": LogLevel.INFO,
        "event_type": EventType.CHANGE_PERSONAL_INFORMATION,
        "attributes": {
            "user_id": "string",
            "success": True,
            "message": "string",
            "new_info": {
                "first_name": "string",
                "last_name": "string",
                "gender": "Rather not say"
            },
            "previous_info": {
                "first_name": "string",
                "last_name": "string",
                "gender": "Rather not say"
            }
        }
    }
]
change_email_examples = [
    {
        "sent_at": "2025-03-01T19:54:13.830Z",
        "processed_at": "2025-03-01T19:54:13.830Z",
        "latency_ms": 0,
        "log_level": LogLevel.INFO,
        "event_type": EventType.CHANGE_EMAIL,
        "attributes": {
            "user_id": "string",
            "success": True,
            "message": "string",
            "new_email": "example@example.com",
            "previous_email": "example@example.com"
        }
    }
]
change_password_examples = [
    {
        "sent_at": "2025-03-01T19:54:13.830Z",
        "processed_at": "2025-03-01T19:54:13.830Z",
        "latency_ms": 0,
        "log_level": LogLevel.INFO,
        "event_type": EventType.CHANGE_PASSWORD,
        "attributes": {
            "user_id": "string",
            "success": True,
            "message": "string"
        }
    }
]
delete_account_examples = [
    {
        "sent_at": "2025-03-01T19:54:13.830Z",
        "processed_at": "2025-03-01T19:54:13.830Z",
        "latency_ms": 0,
        "log_level": LogLevel.INFO,
        "event_type": EventType.DELETE_ACCOUNT,
        "attributes": {
            "user_id": "string",
            "success": True,
            "message": "string"
        }
    }
]


# Change personal information log
class PersonalInformation(BaseModel):
    firstName: str | None = None
    lastName: str | None = None
    gender: Literal["Male", "Female", "Rather not say"] | None = None


class SuccessfulChangePersonalInformation(SuccessfulActionAttributes):
    new_info: PersonalInformation
    previous_info: PersonalInformation


class FailedChangePersonalInformation(FailedActionAttributes):
    pass


ChangePersonalInformationAttributes = (
        SuccessfulChangePersonalInformation |
        FailedChangePersonalInformation
)


class ChangePersonalInformationLog(BaseLog):
    event_type: Literal[EventType.CHANGE_PERSONAL_INFORMATION]
    attributes: ChangePersonalInformationAttributes

    model_config = ConfigDict(
        json_schema_extra={"examples": change_personal_information_examples}
    )


# Change email log
class SuccessfulChangeEmail(SuccessfulActionAttributes):
    new_email: str
    previous_email: str


class FailedChangeEmail(FailedActionAttributes):
    pass


class ChangeEmailLog(BaseLog):
    event_type: Literal[EventType.CHANGE_EMAIL]
    attributes: SuccessfulChangeEmail | FailedChangeEmail

    model_config = ConfigDict(
        json_schema_extra={"examples": change_email_examples}
    )


# Other logs
class ChangePasswordLog(BaseLog):
    event_type: Literal[EventType.CHANGE_PASSWORD]
    attributes: LogAttributes

    model_config = ConfigDict(
        json_schema_extra={"examples": change_password_examples}
    )


class DeleteAccountLog(BaseLog):
    event_type: Literal[EventType.DELETE_ACCOUNT]
    attributes: LogAttributes

    model_config = ConfigDict(
        json_schema_extra={"examples": delete_account_examples}
    )


SettingsActionLog = (
        ChangePersonalInformationLog |
        ChangeEmailLog |
        ChangePasswordLog |
        DeleteAccountLog
)
