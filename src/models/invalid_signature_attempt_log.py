from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Literal
from models.base_log import LogLevel, EventType


class InvalidSignatureAttemptAttributes(BaseModel):
    client_ip: str
    message: str


class InvalidSignatureAttemptLog(BaseModel):
    sent_at: datetime
    log_level: Literal[LogLevel.WARNING]
    event_type: Literal[EventType.INVALID_SIGNATURE_ATTEMPT]

    attributes: InvalidSignatureAttemptAttributes

    model_config = ConfigDict(extra="forbid")
