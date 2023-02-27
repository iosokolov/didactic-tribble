import sanic.response


async def ping(request):
    return sanic.response.HTTPResponse()
