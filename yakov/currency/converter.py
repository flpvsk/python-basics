'''
Created on Apr 3, 2014

@author: Java Studen
'''
import json
import urllib2
from datetime import date
import os


URL = 'http://andreysalomatin.me/exchange-rates?from={0}&to={1}'
CURRENCIES = [('Ruble', 'rub', 'RUB'), ('Euro', 'eur', 'EUR'), ('Dollar', '$', 'USD')]


class currency():

    def __init__(self, curr_tuple):
        self._name = curr_tuple[0]
        self._symbol = curr_tuple[1]
        self._iso_code = curr_tuple[2]
        self._get_rates()

    def __str__(self):
        return '{0} ({1})'.format(self._name, self._symbol)

    def _get_rates(self):
        d = date.today()
        file_name = '%r-%r%r%r.json' % (self._iso_code, d.year, d.month, d.day)
        rates = {}
        if os.path.isfile(file_name):
            rate_dict = self._read_rates(file_name)
            self._rates = rate_dict
        else:
            for curr in CURRENCIES:
                resp = urllib2.urlopen(URL.format(self._iso_code, curr[2]))
                rate_dict = json.loads(resp.read())
                rates[curr[2]] = rate_dict['rate']
            self._save_rates(file_name, rates)
            self._rates = rates

    def get_rate(self, iso_code):
        return self._rates[iso_code]

    def _save_rates(self, filename, data):
        with open(filename, 'w+') as f:
            json.dump(data, f)

    def _read_rates(self, filename):
        with open(filename, 'r') as f:
            return json.load(f)


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