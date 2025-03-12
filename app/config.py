from pydantic_settings import BaseSettings
from pydantic import Extra
import os

class Settings(BaseSettings):
    TESTING: bool = False
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "bookmark_manager"
    POSTGRES_HOST: str = "db"  # Changed from localhost to container name
    POSTGRES_PORT: str = "5432"
    REDIS_URL: str = "redis://redis:6379"  # Changed from localhost to container name
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Bookmark Manager"

    @property
    def DATABASE_URL(self) -> str:
        if self.TESTING:
            return "sqlite:///./test.db"
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    class Config:
        extra = Extra.allow

settings = Settings()
