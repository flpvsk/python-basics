# -*- coding: UTF-8 -*-
'''
Created on Mar 31, 2014

@author: Java Student
'''

__all__ = ['Money', 'Currency', 'RUBLE', 'EURO', 'DOLLAR', 'rubles', 'dollars', 'euros']
currencies = []

class Currency (object):
    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name
        self.rate={self:1}
        currencies.append(self)
    
    def __str__(self):
        return self.symbol 

class Money (object):
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    
    def convert_to(self, another_currency):
        another_currency_amount = float(self.amount) / self.currency.rate[another_currency]
        result = Money(another_currency_amount, another_currency)
        return result
    def __add__(self, another_money):
        another_money_amount = float(another_money.amount) / another_money.currency.rate[self.currency]
        result = Money(self.amount + another_money_amount, self.currency)
        return result
    def __sub__(self, another_money):
        another_money_amount = float(another_money.amount) / another_money.currency.rate[self.currency]
        result = Money(self.amount - another_money_amount, self.currency)
        return result
    def __str__(self):
        return str(self.amount)  +  str(self.currency)
        

RUBLE = Currency("rub", "Ruble")
EURO = Currency("€", "Euro")
DOLLAR = Currency("$", "Dollar")

RUBLE.rate[EURO] = 3
RUBLE.rate[DOLLAR] = 2
DOLLAR.rate[RUBLE] = 0.5
DOLLAR.rate[EURO] = 0.2
EURO.rate[RUBLE] = 0.5
EURO.rate[DOLLAR] = 0.2


def rubles(amount):
    return Money(amount, RUBLE)

def euros (amount):
    return Money(amount, EURO)

def dollars (amount):
    return Money(amount, DOLLAR)


three_rubles = rubles(3)

print three_rubles.amount, three_rubles.currency

three_rubles_in_dollars = three_rubles.convert_to(DOLLAR)
print three_rubles_in_dollars.amount

result_in_rubles = euros(100) + dollars(2)
print result_in_rubles
result_in_rubles = dollars(100) - euros(2)
print result_in_rubles







