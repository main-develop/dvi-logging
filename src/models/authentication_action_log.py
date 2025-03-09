from pydantic import ConfigDict
from models.base_log import BaseLog, LogAttributes, LogLevel, EventType
from typing import Literal

sign_up_examples = [
    {
        "sent_at": "2025-03-01T19:54:13.830Z",
        "processed_at": "2025-03-01T19:54:13.830Z",
        "latency_ms": 0,
        "log_level": LogLevel.INFO,
        "event_type": EventType.SIGN_UP,
        "attributes": {
            "user_id": "string",
            "success": False,
            "message": "string"
        }
    }
]
log_in_examples = [
    {
        "sent_at": "2025-03-01T19:54:13.830Z",
        "processed_at": "2025-03-01T19:54:13.830Z",
        "latency_ms": 0,
        "log_level": LogLevel.INFO,
        "event_type": EventType.LOG_IN,
        "attributes": {
            "user_id": "string",
            "success": False,
            "message": "string"
        }
    }
]
log_out_examples = [
    {
        "sent_at": "2025-03-01T19:54:13.830Z",
        "processed_at": "2025-03-01T19:54:13.830Z",
        "latency_ms": 0,
        "log_level": LogLevel.INFO,
        "event_type": EventType.LOG_OUT,
        "attributes": {
            "user_id": "string",
            "success": False,
            "message": "string"
        }
    }
]


class SignUpLog(BaseLog):
    event_type: Literal[EventType.SIGN_UP]
    attributes: LogAttributes

    model_config = ConfigDict(
        json_schema_extra={"examples": sign_up_examples}
    )


class LogInLog(BaseLog):
    event_type: Literal[EventType.LOG_IN]
    attributes: LogAttributes

    model_config = ConfigDict(
        json_schema_extra={"examples": log_in_examples}
    )


class LogOutLog(BaseLog):
    event_type: Literal[EventType.LOG_OUT]
    attributes: LogAttributes

    model_config = ConfigDict(
        json_schema_extra={"examples": log_out_examples}
    )


AuthenticationActionLog = SignUpLog | LogInLog | LogOutLog
