#! /usr/bin/env python
#encoding:UTF-8

class Money(object):
    
    def __init__(self, currency, amount):
        self._amount = amount
        self._currency = currency
        
    @property
    def currency(self):
        return self._currency
    
    @property
    def amount(self):
        return self._amount
    
    def __str__(self):
        return str(self.amount) + str(self.currency.symbol)
    
    def convert_to(self, new_currency):
        return self.amount * self.currency.exchange_rate[new_currency]
    
    def __add__(self, cur2):
        #if self.currency.symbol != cur2.currency.symbol:
        return Money(self.currency, self.amount + cur2.convert_to(self.currency.symbol))
    
class Currency(Money):
    
    RUBLE = "rub"
    DOLLAR = "$"
    EURO = "€"
    
    rates = {RUBLE: {DOLLAR: 1/35, EURO: 1/50,RUBLE: 1},
             DOLLAR: {DOLLAR: 1, EURO: 0.8,RUBLE: 35},
             EURO: {DOLLAR: 1.4, EURO: 1,RUBLE: 50}}
    exchange_rate = []
    
    def __init__(self):
        pass
    
    def rubles(self, amount):
        self.exchange_rate = self.rates[self.RUBLE]
        self._symbol = self.RUBLE
        return Money(self, amount)
    
    
    def dollars(self, amount):
        self.exchange_rate = self.rates[self.DOLLAR]
        self._symbol = self.DOLLAR
        return Money(self, amount)
    

    def euros(self, amount):
        self.exchange_rate = self.rates[self.EURO]
        self._symbol = self.EURO
        return Money(self, amount)
    
    @property
    def symbol(self):
        return self._symbol




if __name__ == "__main__":
    cur =  Currency()
    r = cur.dollars(50)
    print str(r)
    print (r.convert_to(cur.RUBLE))
    s1 = cur.rubles(1000)
    print str(s1)
    s2 = cur.euros(5)
    print str(s2)
    print str(s1 + s2)
    