from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Literal, Union, TypeVar, Generic

T = TypeVar("T", bound=BaseModel)

LogLevel = Literal["INFO", "WARNING", "ERROR"]
EventType = Literal["page_navigation", "sign_up", "log_in", "log_out"]


class BaseLog(BaseModel):
    sent_at: datetime = Field(..., description="Send time in ISO format.")
    received_at: datetime = Field(..., description="Receive time in ISO format.")
    latency_ms: int = Field(..., description="Latency in milliseconds.")
    log_level: LogLevel
    event_type: EventType

    model_config = ConfigDict(extra="forbid")


class LogWithAttributes(BaseLog, Generic[T]):
    attributes: T


class PageNavigationAttributes(BaseModel):
    referrer: str
    user_agent: str
    page: str
    time_spent_s: float


class AuthenticationActionAttributes(BaseModel):
    success: bool
    email: str
    message: str | None = None


class PageNavigationLog(LogWithAttributes[PageNavigationAttributes]):
    pass


class AuthenticationActionLog(LogWithAttributes[AuthenticationActionAttributes]):
    pass
