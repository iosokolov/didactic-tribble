from uuid import UUID

from sanic import Sanic
import sanic
from sanic import exceptions

from amqp.connection import open_amqp, close_amqp, start_consume
from amqp.producers import send_search_task_to_amqp
from constants import StatusEnum, CurrencyEnum
from cron_jobs import init_scheduler
from db import session_maker
from models import Record
from schemas import SearchOutSchema, ResultOutSchema

app = Sanic("my_first_app")


@app.post('/search')
async def post_search(request):
    async with session_maker() as session:
        record = await Record.create(session, data={'status': StatusEnum.PENDING})

        schema = SearchOutSchema()
        res = schema.load({'search_id': record.request_uuid})
        res = schema.dump(res)
        await session.commit()
        return sanic.response.JSONResponse(res)


@app.get('/results/<search_id>/<currency>/')
async def get_search(request, search_id: UUID, currency: CurrencyEnum):
    async with session_maker() as session:
        record = await Record.select_one_or_none(session, request_uuid=search_id)
        if not record:
            raise exceptions.NotFound

        schema = ResultOutSchema()
        res = schema.dump({
            'search_id': record.request_uuid,
            'status': record.status,
            'items': [{'a': True}]
        })
        await session.commit()
        await send_search_task_to_amqp(app, request_uuid=record.request_uuid)
        return sanic.response.JSONResponse(res)


if __name__ == '__main__':
    app.listener('before_server_start')(init_scheduler)
    app.listener('before_server_start')(open_amqp)

    app.listener('after_server_start')(start_consume)

    app.listener('before_server_stop')(close_amqp)

    app.run(port=9000)
