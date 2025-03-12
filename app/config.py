from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    TESTING: bool = False
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", 
        "postgresql://postgres:postgres@localhost/bookmark_manager"
    )
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost")
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Bookmark Manager"

    class Config:
        env_file = ".env"

settings = Settings()
