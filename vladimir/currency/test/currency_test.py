'''
Created on Apr 9, 2014

@author: Java Student
'''

import vladimir.currency.currency as currency

class response_mocked(object):
    def __init__(self):
        pass
    def read(self):
        return '{"from":"RUB","to":"USD","rate":1}'
    
def urllib2_open_mocked(URL):
    return response_mocked()

currency.urllib2.urlopen = urllib2_open_mocked



RUBLE = currency.Currency("rub", "Ruble", "RUB")

def test_currency_rates():
    assert RUBLE.rate["USD"] == 1