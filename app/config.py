"""Captures all the configurable values of system components"""
from pydantic import BaseSettings

class Settings(BaseSettings):
    """Global values which can be accessed by the system"""    
    REDIS_SERVER: str
    REDIS_PORT: str
    REDIS_DB: int = 0

    FEED_SET: str
    PAGE_OFFSET: int = 2

    class Config:
        """Defines the location or pattern to load values"""
        case_sensitive = True
        env_file = ".env"

settings = Settings()
