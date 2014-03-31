'''
Created on Mar 31, 2014

@author: Java Student
'''

currencies = []

class Currency (object):
    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name
        self.rate={}
        currencies.append(self)

class Money (object):
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    
    def convert_to(self):
        pass
    
    


ruble = Currency("rub", "Ruble")
euro = Currency("ˆ", "Euro")
dollar = Currency("$", "Dollar")

ruble.rate["Euro"] = "3"
ruble.rate["Dollar"] = "2"


def rubles(amount):
    return Money(amount, ruble)

def euros (amount):
    return Money(amount, euro)

def dollars (amount):
    return Money(amount, dollar)







