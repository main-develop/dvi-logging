from src.settings import settings
from modify_fastapi_cli import modify_fastapi_cli
from change_docs_favicon import change_docs_favicon
import subprocess
import sys

if __name__ == "__main__":
    if settings.env == "development":
        try:
            modify_fastapi_cli()
            change_docs_favicon()

            subprocess.run([sys.executable, "-m", "fastapi", "dev", "./src/app.py"])
        except KeyboardInterrupt:
            pass
