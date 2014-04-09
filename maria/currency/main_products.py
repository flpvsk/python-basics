from converter_entities import Currency
from converter_entities import Money
from exchange_rates_loaders import loader_instance


RUBLE = Currency("Rubles", "rub", "RUB", loader_instance)
DOLLAR = Currency("Dollar", "$", "USD", loader_instance)
EURO = Currency("Euro", "eur", "EUR", loader_instance)


def rubles(n):
    return Money(n, RUBLE)


def dollars(n):
    return Money(n, DOLLAR)


def euro(n):
    return Money(n, EURO)
