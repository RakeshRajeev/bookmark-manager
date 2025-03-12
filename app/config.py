from pydantic_settings import BaseSettings
from pydantic import Extra
import os

class Settings(BaseSettings):
    TESTING: bool = False
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "postgres")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "bookmark_manager")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", "5432")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379")
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
