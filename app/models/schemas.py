from typing import Optional
from pydantic import BaseModel

class Message(BaseModel):
    text: str

class FeedItem(BaseModel):
    timestamp: int
    text: str
