class Currency(object):

    def __init__(self, name, symbol, iso_code, exchange_rates_loader):
        self._name = name
        self._symbol = symbol
        self._iso_code = iso_code
        self._exchange_rates = exchange_rates_loader.load(iso_code)

    @property
    def name(self):
        return self._name

    @property
    def symbol(self):
        return self._symbol

    @property
    def iso_code(self):
        return self._iso_code

    @property
    def exchange_rates(self):
        return self._exchange_rates

    def __str__(self):
        return "{} ({})".format(self.name, self.symbol)


class Money(object):

    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    @property
    def amount(self):
        return self._amount

    @property
    def currency(self):
        return self._currency

    def convert_to(self, target_currency):
        return Money(self.amount *
                     self.currency.exchange_rates[target_currency.iso_code],
                     target_currency)

    def __add__(self, other):
        total_amount = self.amount + other.convert_to(self.currency).amount
        return Money(total_amount, self.currency)

    def __sub__(self, other):
        total_amount = self.amount - other.convert_to(self.currency).amount
        return Money(total_amount, self.currency)

    def __str__(self):
        return str(self.amount) + self.currency.symbol
