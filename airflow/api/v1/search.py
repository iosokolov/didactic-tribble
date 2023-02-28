import json
from uuid import UUID

import sanic
from sanic import exceptions

from amqp.producers import send_search_task_to_amqp
from constants import StatusEnum, CurrencyEnum
from db import session_maker

from models import Record
from redis_service.client import redis_get
from schemas import SearchOutSchema, ResultOutSchema


# @app.post('/search')
async def post_search(request):
    async with session_maker() as session:
        record = await Record.create(session, data={'status': StatusEnum.PENDING})

        schema = SearchOutSchema()
        res = schema.load({'search_id': record.request_uuid})
        res = schema.dump(res)
        await session.commit()
        await send_search_task_to_amqp(request.app, request_uuid=res['search_id'])
        return sanic.response.JSONResponse(res)


# @app.get('/results/<search_id>/<currency>/')
async def get_search(request, search_id: UUID, currency: CurrencyEnum):
    async with session_maker() as session:
        record = await Record.select_one_or_none(session, request_uuid=search_id)
        if not record:
            raise exceptions.NotFound

        items = await redis_get(request.app, key=str(search_id))

        schema = ResultOutSchema()
        res = schema.dump({
            'search_id': record.request_uuid,
            'status': record.status,
            'items': items,
        })
        await session.commit()
        return sanic.response.JSONResponse(res)
