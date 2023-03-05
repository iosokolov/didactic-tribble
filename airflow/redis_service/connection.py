import aioredis

import settings


async def start_redis(app, loop):
    app.ctx.redis = aioredis.from_url(
        url=f'redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/',
        encoding="utf-8",
        decode_responses=True,
    )


async def stop_redis(app, loop):
    await app.ctx.redis.close()
