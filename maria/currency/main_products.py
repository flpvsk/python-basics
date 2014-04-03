from converter_entities import Currency
from converter_entities import Money

__all__ = ('RUBLE', 'DOLLAR', 'EURO', 'rubles', 'dollars', 'euro')


RUBLE = Currency("Rubles", "rub",
                 {'Rubles': 1, 'Dollar': 0.0277, 'Euro': 0.208})
DOLLAR = Currency("Dollar", "$", {'Dollar': 1, 'Rubles': 36, 'Euro': 0.750})
EURO = Currency("Euro", "eur", {'Euro': 1, 'Rubles': 48, 'Dollar': 1.333})


def rubles(n):
    return Money(n, RUBLE)


def dollars(n):
    return Money(n, DOLLAR)


def euro(n):
    return Money(n, EURO)
