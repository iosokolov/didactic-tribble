import logging
import sys
from datetime import datetime
import os
import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from env_vars import CRON_CURRENCY_HOUR, CRON_CURRENCY_MINUTE
from nbk.service import NbkService

logger = logging.Logger(name=__name__, level='DEBUG')
logger.addHandler(logging.StreamHandler(sys.stdout))


async def update_currency_rates():
    logger.info('update_currency_rates start')
    nbk_service = NbkService()
    data = await nbk_service.get_rates(date_in=datetime.now().date())


    logger.info('update_currency_rates finish')


if __name__ == '__main__':
    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        update_currency_rates,
        'cron',
        hour=CRON_CURRENCY_HOUR,
        minute=CRON_CURRENCY_MINUTE,
    )
    for job in scheduler.get_jobs():
        logger.info(f"name: {job.name}, trigger: {job.trigger}")

    scheduler.start()
    asyncio.get_event_loop().run_forever()
