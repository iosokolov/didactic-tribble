import itertools
from collections import defaultdict
from decimal import Decimal
from fractions import Fraction
from typing import List

from models import Rate


class CurrencyConverter:
    def __init__(self, rates: List[Rate]):
        self.rates = rates
        coefs = defaultdict(lambda: defaultdict())
        currency_list = [r.currency for r in rates]
        for from_, to_ in itertools.product(currency_list, currency_list):
            coefs[from_][to_] = None

        for rate in rates:
            coefs[rate.currency]['KZT'] = Fraction(
                int(rate.quant_kzt * 100),
                int(rate.quant * 100),
            )

        self.coefs = coefs

    def convert(self, *, amount: Decimal, from_: str, to_: str) -> Decimal:
        if from_ == to_:
            return amount

        coef = self.coefs[from_][to_]
        res = Fraction(amount) * coef
        return res.numerator / Decimal(res.denominator)


def convert_results_to_currency(
        converter: CurrencyConverter,
        search_results: List[dict],
        currency: str,
) -> List[dict]:
    for item in search_results:
        pricing = item['pricing']

        amount = converter.convert(
            amount=pricing['total'],
            from_=pricing['currency'],
            to_=currency,
        )

        item['price'] = {
            "amount": amount,
            "currency": currency,
        }

    return search_results
