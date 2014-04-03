'''
Created on Mar 27, 2014

@author: Java Student
'''
__all__ = ('assert_equal', 'assert_not_equal', 'assert_true', 'assert_false',
           'assert_false', 'assert_is', 'assert_is_not', 'assert_is_none',
           'assert_is_not_none', 'assert_in', 'assert_not_in')


def assert_equal(a, b, message='not equal'):
    try:
        assert a == b, message
    except:
        AssertionError(message)


def assert_not_equal(a, b, message='equal'):
    try:
        assert a != b, message
    except:
        AssertionError(message)


def assert_true(x, message='false'):
    try:
        assert x, message
    except:
        AssertionError(message)


def assert_false(x, message='true'):
    try:
        assert not x, message
    except:
        AssertionError(message)


def assert_is(a, b, message=' is not'):
    try:
        assert a is b, message
    except:
        AssertionError(message)


def assert_is_not(a, b, message='is'):
    try:
        assert a is not b, message
    except:
        AssertionError(message)


def assert_is_none(x, message='not None'):
    try:
        assert x is None, message
    except:
        AssertionError(message)


def assert_is_not_none(x, message='None'):
    try:
        assert x is not None, message
    except:
        AssertionError(message)


def assert_in(a, b, message='not in'):
    try:
        assert a in b, message
    except:
        AssertionError(message)


def assert_not_in(a, b, message='in'):
    try:
        assert a not in b, message
    except:
        AssertionError(message)
