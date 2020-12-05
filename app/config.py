from pydantic import BaseSettings

class Settings(BaseSettings):
    REDIS_SERVER: str
    REDIS_PORT: str
    REDIS_DB: int = 0

    FEED_SET: str
    PAGE_OFFSET: int = 2

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()    