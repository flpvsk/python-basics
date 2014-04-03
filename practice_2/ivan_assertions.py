'''
Created on 20 Mar 2014

@author: CenturyChild
'''


def assert_equal(a, b, message='not equal'):
    try:
        assert a == b, message
    except:
        AssertionError(message)


#print 'assert_equal function tests: \n'
#assert_equal(3, 5)
#assert_equal(4, 4)


def assert_not_equal(a, b, message='equal'):
    try:
        assert a != b, message
    except:
        AssertionError(message)
#print '\rassert_not_equal function tests: \n'
#assert_not_equal(3, 5)
#assert_not_equal(4, 4)


def assert_true(x, message='false'):
    try:
        assert x, message
    except:
        AssertionError(message)
#print '\rassert_true function tests: \n'
#assert_true(1)
#assert_true(0)


def assert_false(x, message='true'):
    try:
        assert not x, message
    except:
        AssertionError(message)

#print '\rassert_false function tests: \n'
#assert_false(1)
#assert_false(0)


def assert_is(a, b, message=' is not'):
    try:
        assert a is b, message
    except:
        AssertionError(message)

#print '\rassert_is function tests: \n'
#assert_is(3, 5)
#assert_is(4, 4)


def assert_is_not(a, b, message='is'):
    try:
        assert a is not b, message
    except:
        AssertionError(message)

#print '\rassert_is_not function tests: \n'
#assert_is_not(3, 5)
#assert_is_not(4, 4)


def assert_is_none(x, message='not None'):
    try:
        assert x is None, message
    except:
        AssertionError(message)

#print '\rassert_is_none function tests: \n'
#assert_is_none(None)
#assert_is_none(1)


def assert_is_not_none(x, message='None'):
    try:
        assert x is not None, message
    except:
        AssertionError(message)
#print '\rassert_is_not_none function tests: \n'
#assert_is_not_none(None)
#assert_is_not_none(1)


def assert_in(a, b, message='not in'):
    try:
        assert a in b, message
    except:
        AssertionError(message)

#print '\rassert_in function tests: \n'
#lst1 = [1, 2, 3, 4, 5]
#lst2 = [3, 6, 8, 0]
#assert_in(3, lst1)
#assert_in(5, lst2)


def assert_not_in(a, b, message='in'):
    try:
        assert a not in b, message
    except:
        AssertionError(message)
#print '\rassert_not_in function tests: \n'
#lst1 = [1, 2, 3, 4, 5]
#lst2 = [3, 6, 8, 0]
#assert_not_in(3, lst1)
#assert_not_in(5, lst2)
