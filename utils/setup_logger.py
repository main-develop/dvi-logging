from dotenv import load_dotenv
import os
import logging
from logging.handlers import RotatingFileHandler

load_dotenv()

logs_paths = {
    "navigation_logger": os.environ.get("NAVIGATION_LOGS_PATH"),
    "sign_up_logger": os.environ.get("SIGN_UP_LOGS_PATH"),
    "log_in_logger": os.environ.get("LOG_IN_LOGS_PATH"),
    "log_out_logger": os.environ.get("LOG_OUT_LOGS_PATH"),
    "change_personal_information_logger": os.environ.get("CHANGE_PERSONAL_INFORMATION_LOGS_PATH"),
    "change_email_logger": os.environ.get("CHANGE_EMAIL_LOGS_PATH"),
    "change_password_logger": os.environ.get("CHANGE_PASSWORD_LOGS_PATH"),
    "delete_account_logger": os.environ.get("DELETE_ACCOUNT_LOGS_PATH"),
}
logging.config.fileConfig("logging.conf")


def setup_logger(name: str, maxBytes: int = 52428800, backupCount: int = 1) -> logging.Logger | None:
    """Create and configure a logger with :class:`RotatingFileHandler` handler for logging specific 
    events with level ``INFO`` or higher.

    The logs file path is fetched from environment variables using the ``name`` parameter.

    Return:
    :param logging.Logger: A logger instance configured with the specified parameters.
    :param None: If the logs path is not set in the environment variables or an invalid ``name`` 
    parameter is passed.
    """
    log_path = logs_paths.get(name)

    if not log_path:
        logging.warning(f"Logs path for {name} is not set. Logging will not work.")
        
        return None

    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    logger = logging.getLogger(name)
    handler = RotatingFileHandler(log_path, maxBytes=maxBytes, backupCount=backupCount)

    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    logger.propagate = False

    return logger
