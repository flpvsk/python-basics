'''
Created on 12.03.2014

@author: vladimirbessmertnyj
'''


def assert_equal(a, b):
    if a == b:
        return True
    else:
        raise Exception


def assert_not_equal(a, b):
    if a != b:
        return True
    else:
        raise Exception


def assert_true(x):
    if x:
        return True
    else:
        raise Exception


def assert_false(x):
    if not x:
        return True
    else:
        raise Exception


def assert_is(a, b):
    if a is b:
        return True
    else:
        raise Exception


def assert_is_not(a, b):
    if a is not b:
        return True
    else:
        raise Exception


def assert_is_none(x):
    if x is None:
        return True
    else:
        raise Exception


def assert_is_not_none(x):
    if x is not None:
        return True
    else:
        raise Exception


def assert_in(a, b):
    if a in b:
        return True
    else:
        raise Exception


def assert_not_in(a, b):
    if a not in b:
        return True
    else:
        raise Exception
#tests
print assert_equal(1, 1)
print assert_equal(1, 2)
print assert_not_equal(1, 1)
print assert_not_equal(1, 2)
print assert_true(True)
print assert_true(False)
print assert_false(False)
print assert_false(True)
a = "abc"
print assert_is(a, a)
print assert_is(a, "abc")
print assert_is_not(a, a)
print assert_is_not(a, "abc")
print assert_is_none(a)
print assert_is_none(None)
print assert_is_not_none(a)
print assert_is_not_none(None)
b = ["abc", 1, 42]
print assert_in(a, b)
print assert_in(a, b[1:])
print assert_not_in(a, b)
print assert_not_in(a, b[1:])
