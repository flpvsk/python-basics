class Currency(object):

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.exchange_rate = {}

    def __str__(self):
        return self.name + self.symbol

class Money(object):
    def __init__(self, amount, currency):