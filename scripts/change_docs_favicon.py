import os
from src.settings import settings
import re
from src.loggers.setup_loggers import setup_console_logger

OPENAPI_DOCS_PATH = os.path.join(
    os.getcwd(), ".venv", "Lib", "site-packages", "fastapi", "openapi", "docs.py"
)

PATTERN = r'"https://fastapi.tiangolo.com/img/favicon.png"'
REPLACEMENT = rf'"{settings.host + settings.favicon_url}"'

logger = setup_console_logger()


def change_docs_favicon() -> None:
    if not os.path.exists(OPENAPI_DOCS_PATH):
        logger.warning(f"⚠️  The {OPENAPI_DOCS_PATH} file was not found.")
        logger.disabled = True
        return None

    with open(OPENAPI_DOCS_PATH, 'r', encoding="utf-8") as file:
        content = file.read()

    if re.search(PATTERN, content):
        new_content = re.sub(PATTERN, REPLACEMENT, content)

        with open(OPENAPI_DOCS_PATH, 'w', encoding="utf-8") as file:
            file.write(new_content)

        logger.info("✅ Successfully changed Swagger UI documentation favicon.")
    else:
        logger.warning("⚠️  Swagger UI documentation favicon has already been changed or cannot be found.")
