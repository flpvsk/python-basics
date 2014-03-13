def assert_equal(a, b, m = "'{}' is not equal to '{}'"):
    assert a == b, m.format(a, b)
    
def assert_not_equal(a, b, m = "'{}' is equal to '{}'"):
    assert a != b, m.format(a, b)