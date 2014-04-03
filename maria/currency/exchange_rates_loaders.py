import urllib2
import urllib
import json
from converter_entities import Currency
from converter_entities import Money


class StaticLoader(object):
    EXCHANGE_RATES = {'RUB':
                      {'RUB': 1, 'USD': 0.0277, 'EUR': 0.208},
                      'USD':
                      {'USD': 1, 'RUB': 36, 'EUR': 0.750},
                      'EUR':
                      {'EUR': 1, 'RUB': 48, 'USD': 1.333}
                      }

    def load(self, currency_iso):
        return self.EXCHANGE_RATES[currency_iso]


class WebLoader(object):
    RESOURCE_URL = "http://rate-exchange.appspot.com/currency?"
    LOAD_CURRENCIES = ["RUB", "USD", "EUR"]

    def load(self, currency_iso):
        #exchange_rate_url = self.RESOURCE_URL + urllib.urlencode(
        #    {'from': self.source_currency_iso, 'to': self.target_currency_iso})
        #response = urllib2.urlopen(exchange_rate_url)
        exchange_rates = {}
        for target_currency_iso in self.LOAD_CURRENCIES:
            json_string = '{"to": "' + target_currency_iso + '", "rate": 0.02051789999, "from": "' + currency_iso+'"}'
            exchange_rate = json.loads(json_string)
            exchange_rates.update({exchange_rate["to"]: exchange_rate["rate"]})
        return exchange_rates

RUBLE = Currency("Rubles", "rub", "RUB", StaticLoader())
DOLLAR = Currency("Dollar", "$", "USD", StaticLoader())
EURO = Currency("Euro", "eur", "EUR", StaticLoader())


def rubles(self, n):
    return Money(n, self.RUBLE)


def dollars(self, n):
    return Money(n, self.DOLLAR)


def euro(self, n):
    return Money(n, self.EURO)


print Currency("Rubles", "rub", "RUB", WebLoader())
