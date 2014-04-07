import urllib2
import urllib
import json
import logging
from dump_decorators import with_data_dumping


__all__ = ('StaticLoader', 'WebLoader', 'FallbackLoader', 'loader_instance')

logging.basicConfig(filename='converter.log', level=logging.INFO)


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

    def __init__(self, resource_url):
        self.resource_url = resource_url

    @with_data_dumping
    def load(self, currency_iso):
        exchange_rates = {}
        for target_currency_iso in self.LOAD_CURRENCIES:
            arguments = urllib.urlencode({
                                'from': currency_iso,
                                'to': target_currency_iso})
            full_url = self.resource_url + arguments
            response = urllib2.urlopen(full_url)
            rate_json = json.loads(response.read())
            exchange_rates[target_currency_iso] = rate_json["rate"]
        return exchange_rates


class FallbackLoader(object):
    LOG = logging.getLogger('FallbackLoader')

    def __init__(self, *args):
        self.loaders = args

    def load(self, currency_iso):
        'Try all loaders in order, return first successful result.'
        for loader in self.loaders:
            try:
                return loader.load(currency_iso)
            except:
                self.LOG.warning('Loader `%s` failed', loader.__name__)
        raise ValueError('Currency iso code {} was not found'.format(
                                                            currency_iso))

rate_exchage_loader = WebLoader("http://rate-exchange.appspot.com/currency?")
mirror_loader = WebLoader("http://andreysalomatin.me/exchange-rates?")
loader_instance = FallbackLoader(rate_exchage_loader, mirror_loader)
