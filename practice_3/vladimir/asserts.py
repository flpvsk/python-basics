'''
Created on Mar 13, 2014

@author: bessvla
'''


def assert_equal(a, b, message="Not Equal"):
    if a == b:
        return True
    else:
        raise AssertionError(message)


def assert_not_equal(a, b, message="Equal"):
    if a != b:
        return True
    else:
        raise AssertionError(message)(message)


def assert_true(x,  message="Not True"):
    if x:
        return True
    else:
        raise AssertionError(message)


def assert_false(x,  message="Not False"):
    if not x:
        return True
    else:
        raise AssertionError(message)


def assert_is(a, b,  message="Is not"):
    if a is b:
        return True
    else:
        raise AssertionError(message)


def assert_is_not(a, b,  message="Not Is Not"):
    if a is not b:
        return True
    else:
        raise AssertionError(message)


def assert_is_none(x,  message="Not None"):
    if x is None:
        return True
    else:
        raise AssertionError(message)


def assert_is_not_none(x,  message="Is none"):
    if x is not None:
        return True
    else:
        raise AssertionError(message)


def assert_in(a, b, message="Not in"):
    if a in b:
        return True
    else:
        raise AssertionError(message)


def assert_not_in(a, b, message="In"):
    if a not in b:
        return True
    else:
        raise AssertionError(message)
