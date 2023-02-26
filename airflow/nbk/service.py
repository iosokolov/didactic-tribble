import datetime

from nbk.client import NbkClient
from nbk.exceptions import NbkDataError
from nbk.schemas import RateInSchema

import xmltodict


class NbkService:
    def parse(self, text: str) -> RateInSchema:
        data = xmltodict.parse(text)['rates']
        items = data['item']
        if isinstance(items, list):
            data['items'] = items
        elif isinstance(items, dict):
            data['items'] = [items]
        else:
            raise NbkDataError(f"unknown type {items}")

        schema = RateInSchema()
        return schema.load(data)

    async def get_rates(self, date_in: datetime.date) -> RateInSchema:
        client = NbkClient()
        response = await client.get_rates(date_in=date_in)
        response.raise_for_status()
        return self.parse(response.text)
