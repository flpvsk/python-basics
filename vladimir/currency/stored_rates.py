'''
Created on Apr 7, 2014

@author: Java Student
'''

import sqlite3


class StoredRates(object):

    rates_db = 'rates.db'

    def __init__(self, from_currency):
        self.from_currency = from_currency
        self.to_currency = ""

    def __getitem__(self, to_currency):
        with sqlite3.connect(self.rates_db) as connection:
            connection.row_factory = sqlite3.Row
            for row in connection.execute(\
                'SELECT rate from rates where "from"=? and "to"=?',\
                (self.from_currency, to_currency)):
                result = row[0]
            return result

    def __setitem__(self, to_currency, value):
        with sqlite3.connect(self.rates_db, isolation_level='DEFERRED') as connection:
            connection.row_factory = sqlite3.Row
            current_rate = connection.execute('SELECT rate from rates where "from"=? and "to"=?', (self.from_currency, to_currency))
            if current_rate.fetchall():
                connection.execute('''
                UPDATE rates
                SET rate=?
                WHERE "to"=?''', (value, to_currency))
            else:
                connection.execute('''
                INSERT INTO rates
                VALUES (?, ?, ?)''', (self.from_currency, to_currency, value))
            connection.commit()

#rub_rates = StoredRates('RUB')
#print rub_rates['USD']
#rub_rates['JPY'] = 1
#print rub_rates['JPY']
#rub_rates['USD'] = 0.0028
#print rub_rates['USD']
#rub_rates['USD'] = 0.028
#eur_rates = StoredRates('EUR')
#print eur_rates['RUB']
