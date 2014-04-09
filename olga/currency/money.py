#! /usr/bin/env python
#encoding:UTF-8
import urllib2
import json
import os
from datetime import datetime
import sqlite3

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
        return Money(new_currency, self.amount * self.currency.exchange_rate[new_currency.code])
        #return Money(Currency(new_currency), self.amount * response['rate'])
    
    def __add__(self, cur2):
        return Money(self.currency, self.amount + cur2.convert_to(self.currency).amount)
    
    def __sub__(self, cur2):
        return Money(self.currency, self.amount - cur2.convert_to(self.currency).amount)
    
class Currency(object):
    
    RUB = "rub"
    USD = "$"
    EUR = "в‚¬"
    CODES =["RUB", "USD", "EUR"]
    RATES_URL = "http://andreysalomatin.me/exchange-rates?"
    LOG_DIR = "C:\\test-results\[{base}]-[{year}][{month}][{day}].txt"
    
    #rates = {RUB: {USD: 1/35, EUR: 1/50,RUB: 1},
    ##         USD: {USD: 1, EUR: 0.8,RUB: 35},
    #         EUR: {USD: 1.4, EUR: 1,RUB: 50}}
    
    exchange_rate = {}
    
    def __init__(self, symbol=USD):
        self._symbol = symbol
        self.RATES_URL += "from=" + self.code + "&to="

        self.LOG_DIR = self.LOG_DIR.format(base=self.name,
                                           year=datetime.now().year,
                                           month=datetime.now().month,
                                           day=datetime.now().day)
        
        if not os.path.exists(os.path.dirname(self.LOG_DIR)):
            os.makedirs(os.path.dirname(self.LOG_DIR))
        
        if not os.path.exists(self.LOG_DIR):
            self.exchange_rate = {x: json.load(urllib2.urlopen(self.RATES_URL + x))["rate"]
                               for x in self.CODES}
            with open(self.LOG_DIR, 'a') as fil:
                fil.writelines(json.dumps(self.exchange_rate))
        else:
            with open(self.LOG_DIR, 'r') as fil:
                self.exchange_rate = json.load(fil)
    
    @property
    def symbol(self):
        return self._symbol
    
    @property
    def name(self):
        if self.symbol == self.RUB:
            return "Rubles"
        elif self.symbol == self.USD:
            return "Dollars"
        elif self.symbol == self.EUR:
            return "Euros"
    
    @property
    def code(self):
        if self.symbol == self.RUB:
            return "RUB"
        elif self.symbol == self.USD:
            return "USD"
        elif self.symbol == self.EUR:
            return "EUR"
    
    def __str__(self):
        return "{0} {1}".format(self.name, self.symbol)


RUB = Currency("rub")
USD = Currency("$")
EUR = Currency("в‚¬")

def rubles(amount):
        return Money(RUB, amount)
    
def dollars( amount):
    return Money(USD, amount)


def euros( amount):
    return Money(EUR, amount)


class StoredRates(dict):
    
    def __init__(self, key):
        self._code = key
        with sqlite3.connect("rates.db") as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT "to", "rate" FROM "rates" WHERE "from" = :code', {"code": key})
            rates = cursor.fetchall()
            self.update({row[0]: row[1] for row in rates})
            #print self
    
    def __getitem__(self, key):
        if self.has_key(key):
            return super( StoredRates, self).__getitem__(key)
        return None
    
    def __setitem__(self, key, value):
        if self.has_key(key):
            if self[key] == value:
                return self[key]
            else:
                with sqlite3.connect("rates.db") as connection:
                    cursor = connection.cursor()
                    cursor.execute('UPDATE "rates" SET "rate" = :value WHERE "from" = :from  and "to" = :to',
                                   {"from": self._code, "to": key, "value": value})
                super( StoredRates, self).__setitem__(key, value)
        else:
            with sqlite3.connect("rates.db") as connection:
                cursor = connection.cursor()
                cursor.execute('INSERT INTO "rates" ("from", "to", "rate") values (:from, :to, :value)',
                               {"from": self._code, "to": key, "value": value})
                super(StoredRates, self).__setitem__(key, value)
        
    

if __name__ == "__main__":

    r = dollars(50)
    print(str(r))
    print (str(r.convert_to(RUB)))
       
    s1 = rubles(1000)
    s2 = euros(5)

    print(s2)
    print(s2 + s1)
    print(s1 - s2)
    
    c = StoredRates("RUB")
    print(c["USD"])
    print(c["JP"])
    c["JP"] = 0.6
    
    
    
    