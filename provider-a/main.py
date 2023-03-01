import asyncio
import json

from sanic import Sanic
import sanic


app = Sanic("my_first_app")


@app.post('/search')
async def post_search(request):
    await asyncio.sleep(30)
    with open('response_a.json') as f:
        text = f.read()

    data = json.loads(text)
    return sanic.response.json(data)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=9001,
    )
