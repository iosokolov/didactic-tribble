import datetime
from typing import List

from nbk.client import NbkClient
from nbk.exceptions import NbkDataError
from nbk.schemas import ItemInSchema

import xmltodict


class NbkService:
    def parse(self, text: str) -> List[ItemInSchema]:
        data = xmltodict.parse(text)['rates']
        items = data['item']
        if isinstance(items, dict):
            items = [items]
        elif isinstance(items, list):
            ...
        else:
            raise NbkDataError(f"unknown type {items}")

        schema = ItemInSchema()
        res = []
        for item in items:
            res.append(schema.load({
                **item,
                'date': data['date'],
            }))

        return res

    async def get_rates(self, date_in: datetime.date) -> List[ItemInSchema]:
        client = NbkClient()
        response = await client.get_rates(date_in=date_in)
        response.raise_for_status()
        return self.parse(response.text)
