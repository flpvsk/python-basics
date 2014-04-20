# -*- coding: utf-8 -*-
#Money entity
class Money(object):
    
    
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency
        
    @property    
    def amount(self):
        return self._amount
    
    @property
    def currency(self):
        return self._currency
    
    
    def convert_to(self, to_currency):
        return Money(self.amount * self.currency.exchange_rate(to_currency),
                     to_currency)


    def __add__(self, money2):
        return Money((self.amount + money2.convert_to(self.currency).amount), self.currency)
    
    
    def __sub__(self, money2):
        return Money((self.amount - money2.convert_to(self.currency).amount), self.currency)
    
    
    def __str__(self):
        return ("{} {}".format(self.amount, self.currency._symbol))
    
    
#Currency entity
class Currency(object):


    def __init__(self, name, symbol):
        
        self._name = name
        self._symbol = symbol
        self._exchange_rate = {}
        
    @property    
    def name(self):
        return self._name
    
    @property
    def symbol(self):
        return self._symbol 
    
    
    def __str__(self):
        return ("{} ({})".format(self._name, self._symbol))

    
    def exchange_rate(self, target_curr):
        return self._exchange_rate[target_curr]




#Constants
RUBLE=Currency('RUBLE','RUB')
DOLLAR=Currency('DOLLAR','$')
EURO=Currency('EURO','�')



#rates as dict are assigned for each currency
RUBLE._exchange_rate={DOLLAR:0.33,EURO:0.47, RUBLE:1 }
DOLLAR._exchange_rate={EURO:1.2, RUBLE:36, DOLLAR:1}
EURO._exchange_rate={DOLLAR:0.7, RUBLE:49, EURO:1}



#Factory methods, create object Money with defined amount and appropriate currency
def rubles(n):
    return Money(n, RUBLE)
def dollars(n):
    return Money(n, DOLLAR)
def euro(n):
    return Money(n, EURO)

print euro(20)
