from typing import Any
from datetime import datetime, timezone
from orjson import dumps, OPT_PASSTHROUGH_DATETIME
from settings import settings
import hmac
import hashlib
from fastapi import Request, HTTPException
from models.invalid_signature_attempt_log import InvalidSignatureAttemptLog
from models.base_log import LogLevel, EventType
from loggers.setup_loggers import setup_logstash_logger


def datetime_serializer(obj: Any):
    """
    JSON serializer to ISO format for :class:`datetime` objects.
    """
    if isinstance(obj, datetime):
        return obj.isoformat(timespec="milliseconds")[:-6] + 'Z'
    raise TypeError(f"{type(obj)} is not JSON serializable")


async def verify_signature(payload: dict, signature: str, request: Request):
    encoded_payload = dumps(
        payload,
        datetime_serializer,
        OPT_PASSTHROUGH_DATETIME
    )
    expected_signature = hmac.new(
        settings.secret_key.encode(),
        encoded_payload,
        hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(expected_signature, signature):
        client_ip = request.client.host
        message = f"Invalid signature attempt from {client_ip}"

        log = InvalidSignatureAttemptLog(
            sent_at=datetime.now(timezone.utc),
            log_level=LogLevel.WARNING,
            event_type=EventType.INVALID_SIGNATURE_ATTEMPT,
            attributes={"client_ip": client_ip, "message": message}
        )

        logger = setup_logstash_logger(
            "invalid_signature_logger",
            {"data": log.dict()}
        )
        logger.warning("Received invalid signature attempt log")

        raise HTTPException(status_code=403, detail="Invalid signature")
