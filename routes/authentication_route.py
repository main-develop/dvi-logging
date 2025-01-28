from flask import Blueprint
from utils.setup_logger import setup_logger
from utils.process_log_entry import process_log_entry

sign_up_logger = setup_logger("sign_up_logger")
log_in_logger = setup_logger("log_in_logger")
log_out_logger = setup_logger("log_out_logger")

authentication = Blueprint("authentication", __name__)


@authentication.route("/send-sign-up-log", methods=["POST"])
def send_sign_up_log():
    return process_log_entry(sign_up_logger)


@authentication.route("/send-log-in-log", methods=["POST"])
def send_log_in_log():
    return process_log_entry(log_in_logger)


@authentication.route("/send-log-out-log", methods=["POST"])
def send_log_out_log():
    return process_log_entry(log_out_logger)
