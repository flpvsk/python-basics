# -*- coding: UTF-8 -*-
'''
Created on Mar 31, 2014

@author: Java Student
'''

__all__ = ['Money', 'Currency', 'RUBLE', 'EURO', 'DOLLAR', \
           'rubles', 'dollars', 'euros']

import urllib2
import json
import datetime
from vladimir.currency.stored_rates import StoredRates


API_URL = "http://andreysalomatin.me/exchange-rates?from={0}&to={1}"
currencies = ["RUB", "USD", "EUR"]


class Currency (object):
    def __init__(self, symbol, name, iso_code):
        self.symbol = symbol
        self.name = name
        self.iso_code = iso_code
        self.rate = {}
        for i in currencies:
            url = API_URL.format(self.iso_code, i)
            response = urllib2.urlopen(url)
            issues_json = json.loads(response.read())

            self.rate[issues_json["to"]] = issues_json["rate"]
           # print self.symbol, str(issues_json)



    def __str__ (self):
        return self.symbol


class CurrencyStored (Currency):
    def __init__(self, symbol, name, iso_code):
        self.symbol = symbol
        self.name = name
        self.iso_code = iso_code
        self.rate = StoredRates(iso_code)

class Money (object):
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def convert_to(self, another_currency):
        another_currency_amount = float(self.amount) * \
            self.currency.rate[another_currency.iso_code]
        result = Money(another_currency_amount, another_currency)
        return result

    def __add__(self, another_money):
        another_money_amount = float(another_money.amount) * \
            another_money.currency.rate[self.currency.iso_code]
        result = Money(self.amount + another_money_amount, self.currency)
        return result

    def __sub__(self, another_money):
        another_money_amount = float(another_money.amount) * \
            another_money.currency.rate[self.currency.iso_code]
        result = Money(self.amount - another_money_amount, self.currency)
        return result

    def __str__(self):
        return str(self.amount) + str(self.currency)

# TESTING

#RUBLE = Currency("rub", "Ruble", "RUB")
#EURO = Currency("€", "Euro", "EUR")
#DOLLAR = Currency("$", "Dollar", "USD")

#RUBLE = CurrencyStored("rub", "Ruble", "RUB")
#EURO = CurrencyStored("€", "Euro", "EUR")
#DOLLAR = CurrencyStored("$", "Dollar", "USD")

#def rubles(amount):
#    return Money(amount, RUBLE)


#def euros(amount):
#    return Money(amount, EURO)


#def dollars(amount):
#    return Money(amount, DOLLAR)


#three_rubles = rubles(3)

#three_rubles_in_dollars = three_rubles.convert_to(DOLLAR)
#print three_rubles_in_dollars.amount

#result_in_rubles = euros(100) + dollars(2)
#print result_in_rubles
#result_in_rubles = dollars(100) - euros(2)
#print result_in_rubles

#now = datetime.date.today()
#print now.year
#print now.month
#print now.day