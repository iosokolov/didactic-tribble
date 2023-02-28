import aioredis

import env_vars


async def start_redis(app, loop):
    app.ctx.redis = aioredis.from_url(
        url=f'redis://{env_vars.REDIS_HOST}:{env_vars.REDIS_PORT}/',
        encoding="utf-8",
        decode_responses=True,
    )


async def stop_redis(app, loop):
    await app.ctx.redis.close()
