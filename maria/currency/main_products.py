from converter_entities import Currency
from converter_entities import Money
from exchange_rates_loaders import DBLoader


RUBLE = Currency("Rubles", "rub", "RUB", DBLoader())
DOLLAR = Currency("Dollar", "$", "USD", DBLoader())
EURO = Currency("Euro", "eur", "EUR", DBLoader())


def rubles(n):
    return Money(n, RUBLE)


def dollars(n):
    return Money(n, DOLLAR)


def euro(n):
    return Money(n, EURO)


hundred_rubles = rubles(100)
print hundred_rubles + hundred_rubles
#200rub
print hundred_rubles.convert_to(DOLLAR)
#2.8$
hundred_dollars = dollars(100)
print hundred_dollars + hundred_rubles
#102.8$
print hundred_dollars - hundred_rubles
#97.2$
print hundred_rubles + hundred_dollars


rub_rates = DBLoader('RUB')
print rub_rates['USD'] 
eur_rates = DBLoader('EUR')
print eur_rates['RUB']
