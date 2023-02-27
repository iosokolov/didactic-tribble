import sys

from sanic import Sanic

import env_vars
import routes
from amqp.connection import start_consume, open_amqp, close_amqp
from cron_jobs import init_scheduler

app = Sanic(env_vars.APP_NAME, strict_slashes=True)

if __name__ == '__main__':
    command = sys.argv[1]

    if command == 'server':
        port = env_vars.API_PORT
        app.blueprint(routes.api)
    elif command == 'consume':
        port = env_vars.AMQP_PORT
        app.listener('before_server_start')(open_amqp)
        app.listener('after_server_start')(start_consume)
        app.listener('before_server_stop')(close_amqp)
    elif command == 'schedule':
        app.listener('before_server_start')(init_scheduler)
        port = env_vars.SCHEDULE_PORT
    else:
        raise Exception

    app.run(
        host=env_vars.HOST,
        port=port,
        workers=env_vars.WORKERS,
        debug=env_vars.DEBUG,
        auto_reload=env_vars.AUTO_RELOAD,
        single_process=True,
    )
