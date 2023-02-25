import asyncio
import json

from sanic import Sanic
import sanic

from constants import StatusEnum
from db import session_maker
from models import Record
from schemas import SearchOutSchema

app = Sanic("my_first_app")


@app.post('/search')
async def post_search(request):
    async with session_maker() as session:
        record = await Record.create(session, data={'status': StatusEnum.PENDING})
        await session.commit()

        schema = SearchOutSchema()
        res = schema.load({'search_id': record.request_uuid})
        res = schema.dump(res)
        return sanic.response.JSONResponse(res)


if __name__ == '__main__':
    app.run(port=9000)
