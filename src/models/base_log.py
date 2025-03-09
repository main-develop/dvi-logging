from enum import Enum
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Literal


class LogLevel(str, Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


class EventType(str, Enum):
    SIGN_UP = "sign_up"
    LOG_IN = "log_in"
    LOG_OUT = "log_out"
    PAGE_NAVIGATION = "page_navigation"
    CHANGE_PERSONAL_INFORMATION = "change_personal_information"
    CHANGE_EMAIL = "change_email"
    CHANGE_PASSWORD = "change_password"
    DELETE_ACCOUNT = "delete_account"
    INVALID_SIGNATURE_ATTEMPT = "invalid_signature_attempt"


base_examples = [
    {
        "sent_at": "2025-03-01T19:54:13.830Z",
        "processed_at": "2025-03-01T19:54:13.830Z",
        "latency_ms": 0,
        "log_level": LogLevel.INFO,
        "event_type": EventType.LOG_IN
    }
]


class BaseLog(BaseModel):
    sent_at: datetime = Field(description="Log send time in ISO format.")
    processed_at: datetime | None = Field(
        None,
        description="Log process time in ISO format."
    )
    latency_ms: int | None = Field(None, description="Latency in milliseconds.")
    log_level: LogLevel
    event_type: EventType

    model_config = ConfigDict(
        extra="forbid",
        json_schema_extra={"examples": base_examples}
    )

    def dict(self, **kwargs):
        return super().model_dump(exclude_unset=True, **kwargs)


class BaseAttributes(BaseModel):
    user_id: str
    success: bool

    model_config = ConfigDict(extra="forbid")


class SuccessfulActionAttributes(BaseAttributes):
    success: Literal[True]


class FailedActionAttributes(BaseAttributes):
    success: Literal[False]
    message: str


LogAttributes = SuccessfulActionAttributes | FailedActionAttributes
