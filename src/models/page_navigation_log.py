from pydantic import BaseModel, ConfigDict
from models.base_log import BaseLog, LogLevel, EventType
from typing import Literal

page_navigation_examples = [
    {
        "sent_at": "2025-03-01T19:54:13.830Z",
        "processed_at": "2025-03-01T19:54:13.830Z",
        "latency_ms": 0,
        "log_level": LogLevel.INFO,
        "event_type": EventType.PAGE_NAVIGATION,
        "attributes": {
            "referrer": "string",
            "user_agent": "string",
            "page": "string",
            "time_spent_s": 0
        }
    }
]


class PageNavigationAttributes(BaseModel):
    referrer: str
    user_agent: str
    page: str
    time_spent_s: float

    model_config = ConfigDict(extra="forbid")


class PageNavigationLog(BaseLog):
    event_type: Literal[EventType.PAGE_NAVIGATION]
    attributes: PageNavigationAttributes

    model_config = ConfigDict(
        json_schema_extra={"examples": page_navigation_examples}
    )
