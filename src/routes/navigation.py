from flask import Blueprint
from utils.process_log_entry import process_log_entry

navigation = Blueprint("navigation", __name__)


@navigation.route("/send-navigation-log", methods=["POST"])
def send_navigation_log():
    return process_log_entry()
