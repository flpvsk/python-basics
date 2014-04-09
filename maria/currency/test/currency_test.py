import shutil
import os
from maria.currency.exchange_rates_loaders import WebLoader
from maria.currency.converter_entities import Currency


DUMP_FILES_DIR = "dumps"
LOAD_CURRENCIES = ['RUB', 'USD', 'EUR']


def set_up(test):
    
    def f():
        shutil.rmtree(DUMP_FILES_DIR)
        test()
        
    return f
    

@set_up
def test_load_rates_from_web():
    web_rate_loader = WebLoader("http://rate-exchange.appspot.com/currency?")
    ruble = Currency("Rubles", "rub", "RUB", web_rate_loader)
    assert ruble.exchange_rates.keys() == LOAD_CURRENCIES
        

@set_up
def test_save_rates_on_disk():
    shutil.rmtree(DUMP_FILES_DIR)
    web_rate_loader = WebLoader("http://rate-exchange.appspot.com/currency?")
    web_rate_loader.load('USD')
    for file_name in os.listdir(DUMP_FILES_DIR):
        print file_name


