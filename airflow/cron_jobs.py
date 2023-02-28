import logging
import sys
from datetime import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from db import session_maker
from env_vars import CRON_CURRENCY_HOUR, CRON_CURRENCY_MINUTE
from models import Rate
from nbk.service import NbkService

logger = logging.Logger(name=__name__, level='DEBUG')
logger.addHandler(logging.StreamHandler(sys.stdout))


async def update_currency_rates(app):
    logger.info('update_currency_rates start')
    nbk_service = NbkService()
    rates = await nbk_service.get_rates(date_in=datetime.now().date())

    async with session_maker() as session:
        rate_list = nbk_service.prepare_rate_list(rates=rates)
        await Rate.bulk_upsert(session, rate_list)
        await session.commit()

    logger.info('update_currency_rates finish')


def init_scheduler(app, loop):
    scheduler = AsyncIOScheduler({
        'event_loop': loop,
    })

    scheduler.add_job(
        update_currency_rates,
        'cron',
        hour=CRON_CURRENCY_HOUR,
        minute=CRON_CURRENCY_MINUTE,
        kwargs={'app': app}
    )

    for job in scheduler.get_jobs():
        logger.info(f"name: {job.name}, trigger: {job.trigger}")

    scheduler.start()
