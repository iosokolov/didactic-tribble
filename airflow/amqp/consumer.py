import json

import env_vars


class Handler:
    def __init__(self, app):
        self.app = app

    async def handle(self, channel, body, envelope, properties):
        data = json.loads(body.decode())


async def consumer(app):
    async def callback(channel, body, envelope, properties):
        handler = Handler(app)
        await handler.handle(channel, body, envelope, properties)

    await app.channel.basic_qos(prefetch_count=10)
    await app.channel.basic_consume(
        callback=callback,
        queue_name=env_vars.QUEUE,
    )
