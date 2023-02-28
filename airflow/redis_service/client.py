import json

import env_vars


async def redis_get(app, *, key: str, default=None):
    res = await app.ctx.redis.get(key)
    if res is None:
        return default

    return json.loads(res)


async def redis_set(app, *, key, value, expire=env_vars.REDIS_EXPIRE):
    await app.ctx.redis.set(
        key,
        json.dumps(value),
        ex=expire,
    )
