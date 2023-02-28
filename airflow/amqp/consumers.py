import asyncio
import json

import env_vars
from constants import StatusEnum
from db import session_maker
from models import Record
from providers.service import ProviderServiceA, ProviderServiceB


class Handler:
    def __init__(self, app):
        self.app = app

    async def handle(self, channel, body, envelope, properties):
        data = json.loads(body.decode())

        provider_service_a = ProviderServiceA()
        provider_service_b = ProviderServiceB()

        results = await asyncio.gather(
            provider_service_a.post_search(),
            provider_service_b.post_search(),
            return_exceptions=True
        )

        async with session_maker() as session:
            await Record.update_by_uuid(
                session,
                request_uuid=data['request_uuid'],
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
