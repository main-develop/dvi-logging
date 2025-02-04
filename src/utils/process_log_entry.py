from flask import request, jsonify
from datetime import datetime
import logging
import json
from models.log import PageNavigationLog, AuthenticationActionLog, SettingsActionLog
from pydantic import ValidationError
from utils.setup_logger import setup_logger


def process_log_entry() -> tuple[dict, int]:
    """Process and validate a log entry received in JSON format.

    Return a ``tuple`` with:
    :param dict: A :class:`~flask.Response` object with the ``application/json`` mimetype.
    :param int: An HTTP status code.
    """
    if not request.is_json:
        return jsonify({"message": "Invalid content type, expected application/json."}), 400

    data = request.get_json(silent=False, force=True)

    if not data:
        return jsonify({"message": "Failed to process log. No data received."}), 400
    
    try:
        processed_at_iso = datetime.utcnow().isoformat() + 'Z'
        data["processed_at"] = processed_at_iso

        sent_at_dt: datetime = datetime.fromisoformat(data["sent_at"])
        processed_at_dt: datetime = datetime.fromisoformat(processed_at_iso)

        latency_ms: int = int((processed_at_dt - sent_at_dt).total_seconds() * 1000)
        data["latency_ms"] = latency_ms

        event_type = data["event_type"]

        if event_type == "page_navigation":
            log = PageNavigationLog.model_validate(data)

            navigation_logger = setup_logger("navigation_logger", {"data": data})
            navigation_logger.info("Received page navigation log")
        elif event_type in {"sign_up", "log_in", "log_out"}:
            log = AuthenticationActionLog.model_validate(data)

            authentication_logger = setup_logger("authentication_logger", {"data": data})
            authentication_logger.info("Received authentication action log")
        elif event_type in {"change_personal_information", "change_email", "change_password", "delete_account"}:
            log = SettingsActionLog.model_validate(data)

            settings_logger = setup_logger("settings_logger", {"data": data})
            settings_logger.info("Received settings action log")

        return jsonify({"message": "Successfully saved log."}), 200
    except ValidationError as error:
        details: dict = dict(list(error.errors()[0].items())[:-1])
        
        logging.error(f"Log entry validation failed: {details}")

        return jsonify({"message": "Log entry validation failed.", "error": details}), 400
    
    except Exception as error:
        logging.error(f"Unexpected error occurred while processing a log entry: {error}")

        return jsonify({"message": "Unexpected error occurred while processing a log entry.", "error": error}), 500
