"""Manages Redis connection parameters and database abstraction"""
import redis
from ..config import settings

pool = redis.ConnectionPool(
        host=settings.REDIS_SERVER,
        port=settings.REDIS_PORT,
        db=settings.REDIS_DB)

redis_instance = redis.Redis(connection_pool=pool)
