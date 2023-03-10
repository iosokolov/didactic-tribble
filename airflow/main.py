import sys

from sanic import Sanic

import settings
import routes
from amqp.connection import start_consume, open_amqp, close_amqp
from redis_service.connection import start_redis, stop_redis
from cron_jobs import init_scheduler, update_currency_rates

app = Sanic(settings.APP_NAME, strict_slashes=True)

if __name__ == '__main__':
    command = sys.argv[1]

    if command == 'server':
        port = settings.API_PORT
        app.blueprint(routes.api)

        app.listener('before_server_start')(update_currency_rates)

        app.listener('before_server_start')(open_amqp)
        app.listener('before_server_stop')(close_amqp)

        app.listener('before_server_start')(start_redis)
        app.listener('before_server_stop')(stop_redis)

    elif command == 'consumer':
        port = settings.CONSUMER_PORT

        app.listener('after_server_start')(start_consume)

        app.listener('before_server_start')(open_amqp)
        app.listener('before_server_stop')(close_amqp)

        app.listener('before_server_start')(start_redis)
        app.listener('before_server_stop')(stop_redis)

    elif command == 'scheduler':
        app.listener('before_server_start')(init_scheduler)
        port = settings.SCHEDULE_PORT

    else:
        raise Exception

    app.blueprint(routes.srv)

    app.run(
        host=settings.HOST,
        port=port,
        workers=settings.WORKERS,
        debug=settings.DEBUG,
        # auto_reload=settings.AUTO_RELOAD,
        single_process=True,
    )
