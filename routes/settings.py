from flask import Blueprint
from utils.setup_logger import setup_logger
from utils.process_log_entry import process_log_entry

change_personal_information_logger = setup_logger("change_personal_information_logger")
change_email_logger = setup_logger("change_email_logger")
change_password_logger = setup_logger("change_password_logger")
delete_account_logger = setup_logger("delete_account_logger")

settings = Blueprint("settings", __name__)


@settings.route("/send-change-personal-information-log", methods=["POST"])
def send_change_personal_information_log():
    return process_log_entry(change_personal_information_logger)


@settings.route("/send-change-email-log", methods=["POST"])
def send_change_email_log():
    return process_log_entry(change_email_logger)


@settings.route("/send-change-password-log", methods=["POST"])
def send_change_password_log():
    return process_log_entry(change_password_logger)


@settings.route("/send-delete-account-log", methods=["POST"])
def send_delete_account_log():
    return process_log_entry(delete_account_logger)
