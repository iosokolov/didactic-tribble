import datetime

import httpx


class NbkClient:
    async def get_rates(self, date: datetime.date):
        # https://nationalbank.kz/rss/get_rates.cfm?fdate=23.02.2009
        params = {
            'fdate': date.strftime('DD.MM.YYYY'),
        }
        r = httpx.get('https://nationalbank.kz/rss/get_rates.cfm', params=params)
