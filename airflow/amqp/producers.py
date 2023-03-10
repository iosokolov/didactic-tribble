import json
from uuid import UUID

import settings


async def publish(app, payload: dict):
    await app.ctx.channel.publish(
        payload=json.dumps(payload),
        exchange_name=settings.EXCHANGE,
        routing_key=settings.QUEUE,
    )


async def send_search_task_to_amqp(app, *, request_uuid: UUID):
    await publish(
        app,
        {'request_uuid': request_uuid},
    )
