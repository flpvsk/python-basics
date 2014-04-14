from maria.currency.exchange_rates_loaders import StaticLoader
from maria.currency.converter_entities import Currency
from maria.currency.converter_entities import Money


def test_convert_to_another_currency():
    loader = StaticLoader()
    ruble = Currency("Rubles", "rub", "RUB", loader)
    dollar = Currency("Dollar", "$", "USD", loader)
    dollars = Money(100, ruble).convert_to(dollar)
    assert dollars.amount == 2.77
    assert str(dollars.currency) == "Dollar ($)"


def test_convert_to_same_currency():
    loader = StaticLoader()
    ruble = Currency("Rubles", "rub", "RUB", loader)
    rubles = Money(100, ruble).convert_to(ruble)
    assert rubles.amount == 100
    assert str(rubles.currency) == "Rubles (rub)"


def test_add_another_currency():
    loader = StaticLoader()
    dollars = Money(100, Currency("Dollar", "$", "USD", loader))
    rubles = Money(100, Currency("Rubles", "rub", "RUB", loader))
    total = rubles + dollars
    assert total.amount == 3700
    assert str(total.currency) == "Rubles (rub)"


def test_add_same_currency():
    loader = StaticLoader()
    rubles_100 = Money(100, Currency("Rubles", "rub", "RUB", loader))
    rubles_20 = Money(20, Currency("Rubles", "rub", "RUB", loader))
    total = rubles_20 + rubles_100
    assert total.amount == 120
    assert str(total.currency) == "Rubles (rub)"


def test_sub_another_currency():
    loader = StaticLoader()
    dollars = Money(100, Currency("Dollar", "$", "USD", loader))
    rubles = Money(100, Currency("Rubles", "rub", "RUB", loader))
    total = dollars - rubles
    assert total.amount == 97.23
    assert str(total.currency) == "Dollar ($)"


def test_sub_same_currency():
    loader = StaticLoader()
    rubles_100 = Money(100, Currency("Rubles", "rub", "RUB", loader))
    rubles_20 = Money(20, Currency("Rubles", "rub", "RUB", loader))
    total = rubles_20 - rubles_100
    assert total.amount == -80
    assert str(total.currency) == "Rubles (rub)"
