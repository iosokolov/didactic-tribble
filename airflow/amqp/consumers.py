import asyncio
import json
import logging
import sys

import env_vars
from constants import StatusEnum
from db import session_maker
from models import Record
from providers.service import ProviderServiceA, ProviderServiceB
from redis_service.client import redis_set

logger = logging.Logger(name=__name__, level='DEBUG')
logger.addHandler(logging.StreamHandler(sys.stdout))


class Handler:
    def __init__(self, app):
        self.app = app

    async def handle(self, channel, body, envelope, properties):
        data = json.loads(body.decode())

        search_id = data['request_uuid']

        provider_service_a = ProviderServiceA()
        provider_service_b = ProviderServiceB()

        results = await asyncio.gather(
            provider_service_a.post_search(),
            provider_service_b.post_search(),
            return_exceptions=True
        )

        results_to_save = []
        for res in results:
            if isinstance(res, Exception):
                logger.error(f'Handler.handle error: {res}')
                continue
            results_to_save.extend(res)

        await redis_set(self.app, key=search_id, value=results_to_save)

        async with session_maker() as session:
            await Record.update_by_uuid(
                session,
                request_uuid=search_id,
                data={'status': StatusEnum.COMPLETED},
            )
            await session.commit()


async def consumer(app):
    async def callback(channel, body, envelope, properties):
        handler = Handler(app)
        await handler.handle(channel, body, envelope, properties)

    await app.ctx.channel.basic_qos(prefetch_count=10)
    await app.ctx.channel.basic_consume(
        callback=callback,
        queue_name=env_vars.QUEUE,
        no_ack=True
    )
