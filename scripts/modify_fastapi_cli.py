import os
from src.settings import settings
import re
from src.loggers.setup_loggers import setup_console_logger

FASTAPI_CLI_PATH = os.path.join(
    os.getcwd(), ".venv", "Lib", "site-packages", "fastapi_cli", "cli.py"
)

PATTERN = r'(url_docs\s*=\s*f"{url})/docs"'
REPLACEMENT = rf'\1{settings.docs_url}"'

logger = setup_console_logger()


def modify_fastapi_cli() -> None:
    if not os.path.exists(FASTAPI_CLI_PATH):
        logger.warning(f"⚠️  The {FASTAPI_CLI_PATH} file was not found.")
        logger.disabled = True
        return None

    with open(FASTAPI_CLI_PATH, 'r', encoding="utf-8") as file:
        content = file.read()

    if re.search(PATTERN, content):
        new_content = re.sub(PATTERN, REPLACEMENT, content)

        with open(FASTAPI_CLI_PATH, 'w', encoding="utf-8") as file:
            file.write(new_content)

        logger.info("✅ Successfully changed Swagger UI documentation URL.")
    else:
        logger.warning("⚠️  Swagger UI documentation URL has already been changed or cannot be found.")
