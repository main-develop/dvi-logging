from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    secret_key: str
    host: str
    docs_url: str
    favicon_url: str
    env: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
