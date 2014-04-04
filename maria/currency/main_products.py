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


hundred_rubles = rubles(100)
print hundred_rubles + hundred_rubles
print hundred_rubles.convert_to(DOLLAR)
hundred_dollars = dollars(100)
print hundred_dollars + hundred_rubles
print hundred_dollars - hundred_rubles
print hundred_rubles + hundred_dollars