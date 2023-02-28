from decimal import Decimal
from typing import List, Optional


class CurrencyConverter:
    def __init__(self, rates):
        self.rates = rates

    def convert(self, *, amount: Decimal, from_: str, to_: str) -> Decimal:
        ...


def convert_results_to_currency(
        converter: CurrencyConverter,
        search_results: List[dict],
        currency: str,
) -> List[dict]:
    for item in search_results:
        pricing = item['pricing']

        amount = converter.convert(
            amount=pricing['currency'],
            from_=pricing['currency'],
            to_=currency,
        )

        item['pricing'] = {
            "amount": amount,
            "currency": currency,
        }

    return search_results
