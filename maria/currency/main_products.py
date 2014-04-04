from converter_entities import Currency
from converter_entities import Money
from exchange_rates_loaders import WebLoader


RUBLE = Currency("Rubles", "rub", "RUB", WebLoader())
DOLLAR = Currency("Dollar", "$", "USD", WebLoader())
EURO = Currency("Euro", "eur", "EUR", WebLoader())


def rubles(n):
    return Money(n, RUBLE)


def dollars(n):
    return Money(n, DOLLAR)


def euro(n):
    return Money(n, EURO)
