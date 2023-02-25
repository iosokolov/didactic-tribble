import asyncio
import json

from sanic import Sanic
import sanic


app = Sanic("my_first_app")


@app.post('/search')
async def post_search(request):
    await asyncio.sleep(60)
    with open('response_b.json') as f:
        text = f.read()

    data = json.loads(text)
    return sanic.response.json(data)


if __name__ == '__main__':
    app.run(port=9002)
