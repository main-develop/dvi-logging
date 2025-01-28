from flask import Blueprint
from utils.setup_logger import setup_logger
from utils.process_log_entry import process_log_entry

navigation_logger = setup_logger("navigation_logger")

navigation = Blueprint("navigation", __name__)


@navigation.route("/send-navigation-log", methods=["POST"])
def send_navigation_log():
    return process_log_entry(navigation_logger)
