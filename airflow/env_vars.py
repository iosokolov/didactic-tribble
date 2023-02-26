from envparse import env

env.read_envfile()

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
