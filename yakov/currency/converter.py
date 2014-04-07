'''
Created on Apr 3, 2014

@author: Java Studen
'''
import json
import urllib2


URL = 'http://andreysalomatin.me/exchange-rates?from={0}&to={1}'
CURRENCIES = [('Ruble', 'rub', 'RUB'), ('Euro', 'eur', 'EUR'), ('Dollar', '$', 'USD')]


class currency():

    def __init__(self, curr_tuple):
        self._name = curr_tuple[0]
        self._symbol = curr_tuple[1]
        self._iso_code = curr_tuple[2]
        self._rates = {cur[2]: self._get_rates(cur[2]) for cur in CURRENCIES}

    def __str__(self):
        return '{0} ({1})'.format(self._name, self._symbol)

    def _get_rates(self, iso_code):
        resp = urllib2.urlopen(URL.format(self._iso_code, iso_code))
        rate_str = json.loads(resp.read())
        return rate_str['rate']

    def get_rate(self, iso_code):
        return self._rates[iso_code]


class money():

    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def convert_to(self, currency):
        return money(self._amount * self._currency.get_rate(currency._iso_code), currency)

    def __str__(self):
        return '{0} {1}'.format(self._amount, self._currency._symbol)


RUB = currency(CURRENCIES[0])
EUR = currency(CURRENCIES[1])
USD = currency(CURRENCIES[2])


def rubles(amount):
    return money(amount, RUB)