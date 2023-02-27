from envparse import env

env.read_envfile()

APP_NAME = 'awesome_app'

HOST = env.str('HOST', default='0.0.0.0')
API_PORT = env.int('API_PORT', default=9000)
AMQ_PORT = env.int('AMQ_PORT', default=8091)
SCHEDULE_PORT = env.int('SCHEDULE_PORT', default=8092)

DEBUG = env.bool('DEBUG', default=False)
AUTO_RELOAD = env.bool('AUTO_RELOAD', default=False)

WORKERS = env.int('WORKERS', default=1)

POSTGRES_USER = env.str("POSTGRES_USER", default='airflow_db')
POSTGRES_PASSWORD = env.str("POSTGRES_PASSWORD", default='airflow_db')
POSTGRES_HOST = env.str("POSTGRES_HOST", default='localhost')
POSTGRES_DB = env.str("POSTGRES_DB", default='airflow_db')
POSTGRES_PORT = env.str("POSTGRES_PORT", default='5577')

ECHO = env.bool("ECHO", default=False)

DB_POOL_SIZE: int = 5
DB_MAX_OVERFLOW: int = 15

CRON_CURRENCY_HOUR = env.str("CRON_CURRENCY_HOUR", default='12')
CRON_CURRENCY_MINUTE = env.str("CRON_CURRENCY_MINUTE", default='00')

AMQP_HOST = env.str('AMQP_HOST', default='localhost')
AMQP_USER = env.int('AMQP_USER', default='guest')
AMQP_PASS = env.str('AMQP_PASS', default='guest')
AMQP_VHOST = env.str('AMQP_VHOST', default='/')
AMQP_PORT = env.int('AMQP_PORT', default=5672)

EXCHANGE = env.str('EXCHANGE', default='my.exchange')
QUEUE = env.str('QUEUE', default='my.main')
QUEUE_DLQ = env.str('QUEUE_DLQ', default='my.main.dlq')
QUEUE_ERROR = env.str('QUEUE_ERROR', default='my.main.error')

RECONNECT_RESTART_COUNT = env.int('RECONNECT_RESTART_COUNT', default=10)
RECONNECT_SLEEP_TIME = env.int('RECONNECT_SLEEP_TIME', default=5)
