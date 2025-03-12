import os

class Settings:
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://bookmarkadmin:complexpass123@localhost:5432/bookmarks")
    API_VERSION = "1.0.0"
    CACHE_TTL = 3600  # 1 hour
    RATE_LIMIT_TIMES = 10
    RATE_LIMIT_SECONDS = 60

settings = Settings()
