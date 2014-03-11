def assert_equal(a, b):
    if a != b:
        raise AssertionError("'{}' is not equal to '{}'".format(a, b))
    
def assert_not_equal(a, b):
    if a == b:
        raise AssertionError("'{}' is equal to '{}'".format(a, b))
    
def assert_true(x):
    if not x:
        raise AssertionError("'{}' is not true".format(x))
    
def assert_false(x):
    if x:
        raise AssertionError("'{}' is not false".format(x))
    
def assert_is(a, b):
    if a is not b:
        raise AssertionError("'{}' is not identical to '{}'".format(id(a), id(b)))
    
def assert_is_not(a, b):
    if a is b:
        raise AssertionError("'{}' is identical to '{}'".format(id(a),id(b)))
    
def assert_is_none(x):
    if x is not None:
        raise AssertionError("'{}' is not none".format(x))
    
def assert_is_not_none(x):
    if x is None:
        raise AssertionError("'{}' is none".format(x))

def assert_in(a, b):
    if a not in b:
        raise AssertionError("'{}' doesn't contain '{}'".format(b, a))

def assert_not_in(a, b):
    if a in b:
        raise AssertionError("'{}' contains '{}'".format(b, a))

