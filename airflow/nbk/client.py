import datetime

import httpx


class NbkClient:
    async def get_rates(self, date_in: datetime.date) -> httpx.Response:
        # https://nationalbank.kz/rss/get_rates.cfm?fdate=23.02.2009
        params = {
            'fdate': date_in.strftime('%d.%m.%Y'),
        }
        r = httpx.get('https://nationalbank.kz/rss/get_rates.cfm', params=params)
        return r
