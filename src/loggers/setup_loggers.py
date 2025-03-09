import logging
import os
from logging import config, LoggerAdapter, Logger
from typing import Mapping, Any
from logstash import LogstashHandler

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
config.fileConfig(os.path.join(BASE_DIR, "logging.conf"))


def setup_logstash_logger(
        name: str, data: Mapping[str, Any]
) -> LoggerAdapter[Logger | LoggerAdapter[Any] | Any]:
    """
    Create and configure a logger with :class:`LogstashHandler` handler for logging specific 
    events with level ``INFO`` or higher. Logs are automatically sent to Elasticsearch.

    Return:
    :param logging.Logger: A logger instance configured with the specified parameters.
    """
    try:
        logger = logging.getLogger(name)
        logstash_handler = LogstashHandler("logstash", 5002, version=1)

        logger.setLevel(logging.INFO)
        logger.addHandler(logstash_handler)
        logger.propagate = False

        logger = logging.LoggerAdapter(logger, data)

        return logger
    except Exception:
        pass


def setup_console_logger() -> logging.Logger:
    """
    Create and configure a logger with :class:`StreamHandler` handler for logging specific 
    events with level ``INFO`` or higher.

    Return:
    :param logging.Logger: A logger instance configured with the ``logging.conf`` file.
    """
    try:
        logger = logging.getLogger("console")
        return logger
    except Exception:
        pass
