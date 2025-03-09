from models.base_log import BaseLog
from datetime import datetime, timezone
from models.authentication_action_log import AuthenticationActionLog
from models.page_navigation_log import PageNavigationLog
from models.settings_action_log import SettingsActionLog
from loggers.setup_loggers import setup_logstash_logger
from fastapi import HTTPException

loggers = [
    {
        "name": "authentication_logger",
        "log_type": AuthenticationActionLog,
        "message": "Received authentication log"
    },
    {
        "name": "page_navigation_logger",
        "log_type": PageNavigationLog,
        "message": "Received page navigation log"
    },
    {
        "name": "settings_action_logger",
        "log_type": SettingsActionLog,
        "message": "Received settings action log"
    }
]


def process_log_entry(log: BaseLog) -> BaseLog:
    processed_at = datetime.now(timezone.utc)
    log.processed_at = processed_at

    latency_ms = int((processed_at - log.sent_at).total_seconds() * 1000)
    log.latency_ms = latency_ms

    return log


def send_log(log: BaseLog):
    try:
        for i, item in enumerate(loggers):
            if isinstance(log, item["log_type"]):
                logger = setup_logstash_logger(
                    item["name"],
                    {"data": log.dict()}
                )
                logger.info(item["message"])
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to send log")

    return {"message": "Log sent successfully"}


async def process_and_send_log(log: BaseLog):
    processed_log = process_log_entry(log)
    return send_log(processed_log)
