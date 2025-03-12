from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost/bookmark_manager"
    REDIS_URL: str = "redis://localhost"
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Bookmark Manager"

settings = Settings()
