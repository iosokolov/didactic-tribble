import logging
import sys
from datetime import datetime
import os
import asyncio
from typing import List

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from db import session_maker
from env_vars import CRON_CURRENCY_HOUR, CRON_CURRENCY_MINUTE
from models import Currency, Rate
from nbk.service import NbkService

logger = logging.Logger(name=__name__, level='DEBUG')
logger.addHandler(logging.StreamHandler(sys.stdout))


async def update_currency_rates():
    logger.info('update_currency_rates start')
    nbk_service = NbkService()
    rates = await nbk_service.get_rates(date_in=datetime.now().date())

    async with session_maker() as session:
        currency_list = nbk_service.prepare_currency_list(rates)
        await Currency.bulk_upsert(session, currency_list)
        await session.commit()

        currency_mapping = await Currency.select_mapping(session)
        rate_list = nbk_service.prepare_rate_list(rates=rates, currency_mapping=currency_mapping)
        await Rate.bulk_upsert(session, rate_list)
        await session.commit()

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
