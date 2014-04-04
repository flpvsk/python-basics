import urllib2
import urllib
import json
from decorators import dump_result_to_file


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

    @dump_result_to_file
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
