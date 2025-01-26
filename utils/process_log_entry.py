from flask import request, jsonify
from datetime import datetime
import logging
import json
from models.log_models import PageNavigationLog, AuthenticationActionLog
from pydantic import ValidationError


def process_log_entry(logger: logging.Logger) -> tuple[dict, int]:
    """Process and validate a log entry received in JSON format.

    Return a ``tuple`` with:
    :param dict: A :class:`~flask.Response` object with the ``application/json`` mimetype.
    :param int: An HTTP status code.
    """
    if not request.is_json:
        return jsonify({"message": "Invalid content type, expected application/json."}), 400

    data = request.get_json(silent=False)

    if not data:
        return jsonify({"message": "Failed to process log. No data received."}), 400
    
    try:
        received_at_iso = datetime.utcnow().isoformat() + 'Z'
        data["received_at"] = received_at_iso

        sent_at_dt: datetime = datetime.fromisoformat(data["sent_at"])
        received_at_dt: datetime = datetime.fromisoformat(received_at_iso)

        latency_ms: int = int((received_at_dt - sent_at_dt).total_seconds() * 1000)
        data["latency_ms"] = latency_ms

        event_type = data["event_type"]

        if event_type == "page_navigation":
            log = PageNavigationLog.model_validate(data)
        elif event_type in {"sign_up", "log_in", "log_out"}:
            log = AuthenticationActionLog.model_validate(data)

        logger.info(json.dumps(data, ensure_ascii=False))

        return jsonify({"message": "Successfully saved log."}), 200
    except ValidationError as error:
        details: dict = dict(list(error.errors()[0].items())[:-1])
        
        logging.error(f"Log entry validation failed: {details}.")

        return jsonify({"message": "Log entry validation failed.", "details": details}), 400
    
    except Exception as error:
        logging.error(f"Unexpected error occurred: {error}.")

        return jsonify({"message": "Unexpected error occurred.", "details": error}), 500
