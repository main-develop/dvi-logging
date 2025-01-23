from flask import Blueprint, request, jsonify
from dotenv import load_dotenv
from datetime import datetime
import os
import logging.config
import json
import yaml

load_dotenv()

LOGS_DIR = os.environ.get("LOGS_DIR")
NAVIGATION_LOGS_FILE = os.path.join(LOGS_DIR, os.environ.get("NAVIGATION_LOGS_FILE"))

# The directory for logs will be created automatically, no need to create it manually
os.makedirs(LOGS_DIR, exist_ok=True)

with open("log_config.yaml", 'r') as file:
    log_config = yaml.safe_load(file)

# Dynamic log file path specification
log_config["handlers"]["file"]["filename"] = NAVIGATION_LOGS_FILE

logging.config.dictConfig(log_config)
navigation_logger = logging.getLogger("navigation_logger")

navigation = Blueprint("navigation", __name__)

@navigation.route("/send-navigation-log", methods=["POST"])
def send_navigation_log():
    received_at = datetime.utcnow().isoformat() + 'Z'
    data = request.get_json(silent=True)

    if data:
        data["received_at"] = received_at

        sent_at_datetime = datetime.fromisoformat(data["sent_at"])
        received_at_datetime = datetime.fromisoformat(received_at)

        latency_ms = (received_at_datetime - sent_at_datetime).total_seconds() * 1000
        data["latency_ms"] = int(latency_ms)
        
        navigation_logger.info(json.dumps(data))

        return jsonify({"message": "Successfully saved log"}), 200
    
    return jsonify({"message": "Failed to save log. No data received"}), 400
