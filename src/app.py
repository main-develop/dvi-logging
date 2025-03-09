from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.authentication import authentication_router
from routers.page_navigation import page_navigation_router
from routers.settings_action import settings_action_router
from settings import settings
from fastapi.responses import FileResponse

tags_metadata = [
    {
        "name": "Authentication logs",
        "description": "Authentication logs endpoints."
    },
    {
        "name": "Page navigation logs",
        "description": "Page navigation logs endpoints."
    },
    {
        "name": "Settings action logs",
        "description": "Settings action logs endpoints."
    }
]

app = FastAPI(
    title="DVI logging",
    docs_url=None if settings.env == "production" else settings.docs_url,
    redoc_url=None,
    openapi_tags=tags_metadata,
    swagger_ui_parameters={"defaultModelsExpandDepth": -1}
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:80"],
    allow_headers=["X-Signature", "Content-Type"],
    allow_methods=["POST"]
)

app.include_router(authentication_router)
app.include_router(page_navigation_router)
app.include_router(settings_action_router)

if settings.env == "development":
    @app.get("/{favicon:path}", include_in_schema=False)
    async def get_favicon(favicon: str):
        if favicon in {settings.favicon_url.strip("/"), "favicon.ico"}:
            return FileResponse("./static/favicon.ico")
