from contextlib import asynccontextmanager

import aioredis
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from .api.routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis))
    yield


app = FastAPI(title="Clean API Example", version="1.0", lifespan=lifespan)

app.include_router(router)
