from flask import Blueprint
from utils.process_log_entry import process_log_entry

settings = Blueprint("settings", __name__)


@settings.route("/send-change-personal-information-log", methods=["POST"])
def send_change_personal_information_log():
    return process_log_entry()


@settings.route("/send-change-email-log", methods=["POST"])
def send_change_email_log():
    return process_log_entry()


@settings.route("/send-change-password-log", methods=["POST"])
def send_change_password_log():
    return process_log_entry()


@settings.route("/send-delete-account-log", methods=["POST"])
def send_delete_account_log():
    return process_log_entry()
