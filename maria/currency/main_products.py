from converter_entities import Currency
from converter_entities import Money
from exchange_rates_loaders import default_loader


RUBLE = Currency("Rubles", "rub", "RUB", default_loader)
DOLLAR = Currency("Dollar", "$", "USD", default_loader)
EURO = Currency("Euro", "eur", "EUR", default_loader)


def rubles(n):
    return Money(n, RUBLE)


def dollars(n):
    return Money(n, DOLLAR)


def euro(n):
    return Money(n, EURO)
