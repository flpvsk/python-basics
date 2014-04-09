'''
Created on Apr 9, 2014

@author: Java Student
'''
from yakov.currency.converter import *


def setup():
    d = date.today()
    file_name = '%r-%r%r%r.json' % (CURRENCIES[0][2], d.year, d.month, d.day)
    if os.path.isfile(file_name):
        os.remove(file_name)
    return file_name


def test_load_from_inet():
    file_name = setup()
    assert not os.path.isfile(file_name)
    cu = currency(CURRENCIES[0])
    assert os.path.isfile(file_name)


def test_save_to_file():
    file_name = setup()
    cu = currency(CURRENCIES[0])
    with open(file_name, 'r') as f:
        content = f.read()
    assert len(content) > 0
    content.index(CURRENCIES[0][2])


def test_file_exists():
    file_name = setup()
    cu = currency(CURRENCIES[0])
    data = {"RUB": 55, "USD": 66, "EUR": 77}
    cu._save_rates(file_name, data)
    cu2 = currency(CURRENCIES[0])
    assert cu2.get_rate('RUB') == 55
    assert cu2.get_rate('USD') == 66
    assert cu2.get_rate('EUR') == 77
