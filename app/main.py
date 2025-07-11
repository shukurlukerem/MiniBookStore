from fastapi import FastAPI
from app.api.v1.routes import auth_routes, book_routes, orders_routes
from app.core.config import Base, engine
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
import aioredis
from app.core.rate_limiter import init_rate_limiter

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mini BookStore")

app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
app.include_router(book_routes.router, prefix="/books", tags=["Books"])
app.include_router(orders_routes.router, prefix="/orders", tags=["Orders"])


@app.get("/test")
def test():
    return {"message": "OK"}

@app.on_event("startup")
async def startup():
    redis = await aioredis.from_url("redis://localhost:6379")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


@app.on_event("startup")
async def startup():
    await init_rate_limiter()