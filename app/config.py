from pydantic_settings import BaseSettings
from pydantic import Extra
import os

class Settings(BaseSettings):
    TESTING: bool = False
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "bookmark_manager"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: str = "5432"
    REDIS_URL: str = "redis://localhost"
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Bookmark Manager"

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    class Config:
        extra = Extra.allow

settings = Settings()
