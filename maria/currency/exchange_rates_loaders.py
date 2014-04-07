import urllib2
import urllib
import json
import sqlite3
from dump_decorators import dump_new_data_to_file
from dump_decorators import use_dumped_data


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
    RESOURCE_URLS_POOL = ("http://rate-exchange.appspot.com/currency?",
                         "http://andreysalomatin.me/exchange-rates?")
    LOAD_CURRENCIES = ("RUB", "USD", "EUR")

    @use_dumped_data
    @dump_new_data_to_file
    def load(self, currency_iso):
        exchange_rates = {}
        for target_currency_iso in self.LOAD_CURRENCIES:
            try:
                exchange_rate = self._get_response(urllib.urlencode(
                     {'from': currency_iso, 'to': target_currency_iso}))
                exchange_rates.update(
                     {str(exchange_rate["to"]): exchange_rate["rate"]})
            except:
                #Should write to log with level 'ERROR'
                print "Impossible to load data for {} currency".format(
                                                      target_currency_iso)
        return exchange_rates

    def _get_response(self, arguments):
        for resource_url in self.RESOURCE_URLS_POOL:
            full_url = resource_url + arguments
            try:
                response = urllib2.urlopen(full_url)
            except urllib2.HTTPError as e:
                #Should write to log with level 'WARNING'
                print "Resource {} is not available. Caught error: {}".format(
                                                                full_url, e)
                continue
            else:
                #Should write to log with level 'INFO'
                print "Using data from resource: {}".format(full_url)
                break
        return json.loads(response.read())


class DBLoader(object):
    DB_NAME = "rates.db"
    
    def __init__(self, currency_iso=""):
        self.currency_iso = currency_iso
        
    def load(self, currency_iso):
        exchange_rates = {}
        with sqlite3.connect(self.DB_NAME) as connection:
            connection.row_factory = sqlite3.Row
            for row in connection.execute('SELECT * from rates where "from" = ?',
                           (currency_iso, )):
                exchange_rates.update({row["to"]: row["rate"]})
        return exchange_rates
    
    def __getitem__(self, target_currency_iso):
        with sqlite3.connect(self.DB_NAME) as connection:
            connection.row_factory = sqlite3.Row
            rate_row = connection.execute('SELECT * from rates where "from" = ? and "to" = ?',
                           (self.currency_iso, target_currency_iso)).fetchone()
            return rate_row["rate"]

    
    
    