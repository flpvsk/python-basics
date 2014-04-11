import shutil
import os
import json
from datetime import date
import maria.currency.config as config
from maria.currency.exchange_rates_loaders import WebLoader
from maria.currency.converter_entities import Currency


def with_set_up_and_tear_down(test):

    def f():
        if os.path.exists(config.BASE_DIR):
            shutil.rmtree(config.BASE_DIR)
        test()
        if os.path.exists(config.BASE_DIR):
            shutil.rmtree(config.BASE_DIR)

    return f


@with_set_up_and_tear_down
def test_load_rates_from_web():
    web_rate_loader = WebLoader()
    ruble = Currency("Rubles", "rub", "RUB", web_rate_loader)
    assert ruble.exchange_rates.keys() == config.LOAD_CURRENCIES


@with_set_up_and_tear_down
def test_save_rates_on_disk():
    web_rate_loader = WebLoader()
    web_rate_loader.load('USD')
    assert len(os.listdir(config.BASE_DIR)) == 1

    today_date = date.today().strftime(config.DATE_FORMAT)
    expected_file_name = config.FILE_NAME_FORMAT.format('USD', today_date)
    assert os.listdir(config.BASE_DIR)[0] == expected_file_name

    dump_file_path = os.path.join(config.BASE_DIR, expected_file_name)
    with open(dump_file_path) as dump_file:
        rates = json.load(dump_file)
        assert len(config.LOAD_CURRENCIES) == len(rates.keys())
        for iso_code in config.LOAD_CURRENCIES:
            assert iso_code in rates.keys()


@with_set_up_and_tear_down
def test_load_rates_from_file():
    web_rate_loader = WebLoader()
    ruble_1 = Currency("Rubles", "rub", "RUB", web_rate_loader)
    ruble_2 = Currency("Rubles", "rub", "RUB", web_rate_loader)
    assert len(os.listdir(config.BASE_DIR)) == 1
    assert ruble_1.exchange_rates == ruble_2.exchange_rates
