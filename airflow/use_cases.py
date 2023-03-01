import itertools
from collections import defaultdict
from decimal import Decimal
from fractions import Fraction
from typing import List

from models import Rate


class CurrencyConverter:
    def __init__(self, rates: List[Rate]):
        rate_by_currency = {
            rate.currency: rate
            for rate in rates
        }

        coefs = defaultdict(lambda: defaultdict())
        currency_list = [r.currency for r in rates]
        for from_, to_ in itertools.product(currency_list, currency_list):
            rate_from = rate_by_currency[from_]
            rate_to = rate_by_currency[to_]

            coef_from = Fraction(int(rate_from.quant_kzt * 100), int(rate_from.quant * 100))
            coef_to = Fraction(int(rate_to.quant_kzt * 100), int(rate_to.quant * 100))

            coefs[from_][to_] = coef_from / coef_to

        for rate in rates:
            coefs[rate.currency]['KZT'] = Fraction(
                int(rate.quant_kzt * 100),
                int(rate.quant * 100),
            )
            coefs['KZT'][rate.currency] = Fraction(
                int(rate.quant * 100),
                int(rate.quant_kzt * 100),
            )

        self.coefs = coefs

    def convert(self, *, amount: Decimal, from_: str, to_: str) -> Decimal:
        if from_ == to_:
            return amount

        coef = self.coefs[from_][to_]
        res = Fraction(amount) * coef
        res_decimal = res.numerator / Decimal(res.denominator)
        return res_decimal


def convert_results_to_currency(
        converter: CurrencyConverter,
        search_results: List[dict],
        currency: str,
) -> List[dict]:
    for item in search_results:
        pricing = item['pricing']

        amount = converter.convert(
            amount=Decimal(pricing['total']),
            from_=pricing['currency'],
            to_=currency,
        )

        item['price'] = {
            "amount": amount,
            "currency": currency,
        }

    return search_results
