from typing import Optional
from time import time
from fastapi import FastAPI, Response, status, Header

from .models.schemas import Message, FeedItem
from .db.redis import pool, redis_instance
from .config import settings

app = FastAPI()

@app.on_event("startup")
async def startup():
    app.state.redis = redis_instance

@app.get("/")
def read_root():
    return {"message": "hit /message to get data feeds"}


@app.get("/message/all")
def read_item():
    rnge = (0, - 1)
    return app.state.redis.zrange(settings.FEED_SET, *rnge, withscores=True)


@app.get("/message")
def read_item(page_no: Optional[int] = Header(0)):
    rnge = getNextPage(page_no)
    return app.state.redis.zrange(settings.FEED_SET, *rnge, withscores=True)


@app.post("/message", response_model=FeedItem, status_code=status.HTTP_201_CREATED)
def update_item(inItem: Message, response: Response):
    item = getMapping(inItem)
    print(item)
    success = app.state.redis.zadd(settings.FEED_SET, {item.text: item.timestamp})
    if 0 == success:
        response.status_code = status.HTTP_304_NOT_MODIFIED
    return item


def getNextPage(current: int):
    offset = settings.PAGE_OFFSET
    page = 0
    if type(current) is int and current >= 0:
        page = current
    return ((page * offset), (page * offset) + (offset - 1))


def getMapping(item: Message) -> FeedItem:
    return FeedItem(text=item.text, timestamp=int(time()))
