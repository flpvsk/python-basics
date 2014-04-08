def test_that_passes():
    assert 1 == 1


def test_that_failes():
    assert 1 == 2, 'Fail Message'


def test_with_error():
    raise ValueError('Error message')
