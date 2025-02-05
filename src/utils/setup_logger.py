import logging
import os
from typing import Mapping, Any
from logstash import LogstashHandler

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
logging.config.fileConfig(os.path.join(BASE_DIR, "logging.conf"))


def setup_logger(name: str, data: Mapping[str, Any]) -> logging.Logger:
    """Create and configure a logger with :class:`LogstashHandler` handler for logging specific 
    events with level ``INFO`` or higher. Logs are automatically sent to Elasticsearch.

    Return:
    :param logging.Logger: A logger instance configured with the specified parameters.
    """
    logger = logging.getLogger(name)
    logstash_handler = LogstashHandler("logstash", 5002, version=1)

    logger.setLevel(logging.INFO)
    logger.addHandler(logstash_handler)
    logger.propagate = False

    logger = logging.LoggerAdapter(logger, data)

    return logger
