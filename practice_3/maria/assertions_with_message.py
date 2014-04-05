def assert_equal(a, b, m = "'{}' is not equal to '{}'"):
    assert a == b, m.format(a, b)
    
def assert_not_equal(a, b, m = "'{}' is equal to '{}'"):
    assert a != b, m.format(a, b)
    
def assert_true(x, m = "'{}' is not true"):
    assert x, m.format(x)
    
def assert_false(x, m = "'{}' is not false"):
    assert not x, m.format(x)
    
def assert_is(a, b, m = "'{}' is not identical to '{}'"):
    assert a is b, m.format(id(a), id(b))
    
def assert_is_not(a, b, m = "'{}' is identical to '{}'"):
    assert a is not b, m.format(id(a), id(b))
    
def assert_is_none(x, m = "'{}' is not none"):
    assert x is None, m.format(x)
    
def assert_is_not_none(x, m = "'{}' is none"):
    assert x is not None, m.format(x)

def assert_in(a, b, m = "'{}' doesn't contain '{}"):
    assert a in b, m.format(b, a)

def assert_not_in(a, b, m = "'{}' contains '{}"):
    assert a not in b, m.format(b, a)