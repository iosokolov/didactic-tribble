import asyncio

import aioamqp

import settings
from amqp.consumers import consumer


async def bind_queue(channel, queue_name, exchange_name, routing_key=None, arguments=None):
    await channel.queue_declare(queue_name, durable=True, arguments=arguments)
    await channel.queue_bind(
        queue_name=queue_name,
        exchange_name=exchange_name,
        routing_key=routing_key if routing_key is not None else queue_name,
    )


async def open_amqp(app):
    transport, protocol = await aioamqp.connect(
        host=settings.AMQP_HOST,
        login=settings.AMQP_USER,
        password=settings.AMQP_PASS,
        virtualhost=settings.AMQP_VHOST,
        port=settings.AMQP_PORT,
    )

    channel = await protocol.channel()
    app.ctx.transport = transport
    app.ctx.protocol = protocol
    app.ctx.channel = channel

    await app.ctx.channel.exchange_declare(
        exchange_name=settings.EXCHANGE,
        type_name='direct',
        durable=True
    )

    await bind_queue(
        channel=app.ctx.channel,
        queue_name=settings.QUEUE,
        exchange_name=settings.EXCHANGE,
        arguments={
            'x-dead-letter-exchange': settings.EXCHANGE,
        }
    )


async def close_amqp(app):
    await app.ctx.protocol.close()
    app.ctx.transport.close()


async def start_consume(app, loop):
    asyncio.ensure_future(consumer(app), loop=loop)


