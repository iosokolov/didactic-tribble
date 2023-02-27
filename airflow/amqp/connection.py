import asyncio

import aioamqp

import env_vars
from amqp.consumer import consumer


async def open_amqp(app):
    transport, protocol = await aioamqp.connect(
        host=env_vars.AMQP_HOST,
        login=env_vars.AMQP_USER,
        password=env_vars.AMQP_PASS,
        virtualhost=env_vars.AMQP_VHOST,
        port=env_vars.AMQP_PORT,
    )

    channel = await protocol.channel()
    app.ctx.transport = transport
    app.ctx.protocol = protocol
    app.ctx.channel = channel


async def close_amqp(app):
    await app.ctx.protocol.close()
    app.ctx.transport.close()


async def bind_queue(channel, queue_name, exchange_name, routing_key=None, arguments=None):
    await channel.queue_declare(queue_name, durable=True, arguments=arguments)
    await channel.queue_bind(
        queue_name=queue_name,
        exchange_name=exchange_name,
        routing_key=routing_key if routing_key is not None else queue_name,
    )


async def start_consume(app, loop):
    await app.ctx.channel.exchange_declare(
        exchange_name=env_vars.EXCHANGE,
        type_name='direct',
        durable=True
    )

    await bind_queue(
        channel=app.ctx.channel,
        queue_name=env_vars.QUEUE,
        exchange_name=env_vars.EXCHANGE,
        arguments={
            'x-dead-letter-exchange': env_vars.EXCHANGE,
        }
    )

    asyncio.ensure_future(consumer(app), loop=loop)
