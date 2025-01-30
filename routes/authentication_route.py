from flask import Blueprint
from utils.process_log_entry import process_log_entry

authentication = Blueprint("authentication", __name__)


@authentication.route("/send-sign-up-log", methods=["POST"])
def send_sign_up_log():
    return process_log_entry()


@authentication.route("/send-log-in-log", methods=["POST"])
def send_log_in_log():
    return process_log_entry()


@authentication.route("/send-log-out-log", methods=["POST"])
def send_log_out_log():
    return process_log_entry()
