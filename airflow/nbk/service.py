import datetime
from typing import List

from nbk.client import NbkClient
from nbk.exceptions import NbkDataError
from nbk.schemas import ItemInSchema

import xmltodict


class NbkService:
    def prepare_currency_list(self, rates: List[dict]):
        currency_dict = {
            rate['title']: rate['fullname']
            for rate in rates
        }

        currency_list = [
            {
                'code': title,
                'name': fullname,
            }
            for title, fullname in currency_dict.items()
        ]
        return currency_list

    def parse(self, text: str) -> List[dict]:
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

    async def get_rates(self, date_in: datetime.date) -> List[dict]:
        client = NbkClient()
        response = await client.get_rates(date_in=date_in)
        response.raise_for_status()
        return self.parse(response.text)

    def prepare_rate_list(self, rates, currency_mapping):
        return [
            {
                'date': rate['date'],
                'currency_id': currency_mapping[rate['title']],
                'quant': rate['quant'],
                'quant_kzt': rate['description'],
            }
            for rate in rates
        ]
