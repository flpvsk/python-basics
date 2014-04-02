class Currency(object):

    def __init__(self, name, symbol, exchange_rates=[]):
        self._name = name
        self._symbol = symbol
        self._exchange_rates = exchange_rates

    @property
    def name(self):
        return self._name

    @property
    def symbol(self):
        return self._symbol

    @property
    def exchange_rates(self):
        return self._exchange_rates

    def __str__(self):
        return "{} ({})".format(self.name, self.symbol)


class Money(object):

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def convert_to(self, target_currency):
        return self.amount * \
                 self.currency.exchange_rates[target_currency.name]

    def __str__(self):
        return self.amount + self.currency.symbol


dict = {'Euro': 23}
cur = Currency("dollar", "$", dict)

print cur
print cur.exchange_rates