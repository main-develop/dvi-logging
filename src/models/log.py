from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Literal, Optional, Union, TypeVar, Generic, Annotated

T = TypeVar("T", bound=BaseModel)

LogLevel = Literal["INFO", "WARNING", "ERROR"]
EventType = Literal[
    "page_navigation", "sign_up", "log_in", 
    "log_out", "change_personal_information", 
    "change_email", "change_password", "delete_account"
]


class BaseLog(BaseModel):
    sent_at: datetime = Field(..., description="Send time in ISO format.")
    processed_at: datetime = Field(..., description="Process time in ISO format.")
    latency_ms: int = Field(..., description="Latency in milliseconds.")
    log_level: LogLevel
    event_type: EventType

    model_config = ConfigDict(extra="forbid")


class LogWithAttributes(BaseLog, Generic[T]):
    attributes: T


class BaseAttributes(BaseModel):
    user_id: str
    success: bool
    message: Optional[str] = None


class PageNavigationAttributes(BaseModel):
    referrer: str
    user_agent: str
    page: str
    time_spent_s: float

# SettingsActionLog attributes
class PersonalInformation(BaseModel):
    first_name: str
    last_name: str
    gender: Literal["Male", "Female", "Rather not say"]


class ChangePersonalInformationAttributes(BaseAttributes):
    new_info: PersonalInformation
    previous_info: PersonalInformation


class ChangeEmailAttributes(BaseAttributes):
    new_email: str
    previous_email: str


SettingsActionAttributes = Union[
    ChangePersonalInformationAttributes, ChangeEmailAttributes, 
    BaseAttributes
]

# Log models
class PageNavigationLog(LogWithAttributes[PageNavigationAttributes]):
    pass


class AuthenticationActionLog(LogWithAttributes[BaseAttributes]):
    """``Note``: actions such as ``sign_up``, ``log_in`` and ``log_out`` have the same log attributes
    defined the :class:`BaseAttributes` class.

    If one of these actions requires adding new attributes, a separate class ``[ActionName]Attributes`` 
    must be created and common type must be inferred, which will take into account the attributes 
    of the new ``[ActionName]Attributes`` class.
    """
    pass


class SettingsActionLog(LogWithAttributes[SettingsActionAttributes]):
    """``Note``: actions such as ``change_password`` and ``delete_account`` have the same log attributes
    defined in the :class:`BaseAttributes` class.

    If one of these actions requires adding new attributes, a separate class ``[ActionName]Attributes`` 
    must be created and common type must be inferred, which will take into account the attributes 
    of the new ``[ActionName]Attributes`` class.
    """
    pass
