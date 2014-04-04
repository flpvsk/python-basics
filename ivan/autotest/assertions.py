'''
Created on Mar 27, 2014

@author: Java Student
'''
__all__ = ('assert_equal', 'assert_not_equal', 'assert_true', 'assert_false',
           'assert_false', 'assert_is', 'assert_is_not', 'assert_is_none',
           'assert_is_not_none', 'assert_in', 'assert_not_in')


def assert_equal(a, b, message='not equal'):
        assert a == b, message


def assert_not_equal(a, b, message='equal'):
        assert a != b, message


def assert_true(x, message='false'):
        assert x, message


def assert_false(x, message='true'):
        assert not x, message


def assert_is(a, b, message=' is not'):
        assert a is b, message


def assert_is_not(a, b, message='is'):
        assert a is not b, message


def assert_is_none(x, message='not None'):
        assert x is None, message


def assert_is_not_none(x, message='None'):
        assert x is not None, message


def assert_in(a, b, message='not in'):
        assert a in b, message


def assert_not_in(a, b, message='in'):
        assert a not in b, message
