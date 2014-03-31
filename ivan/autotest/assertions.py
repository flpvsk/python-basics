'''
Created on Mar 27, 2014

@author: Java Student
'''
__all__ = ('assert_equal', 'assert_not_equal', 'assert_true', 'assert_false',
           'assert_false', 'assert_is', 'assert_is_not', 'assert_is_none',
           'assert_is_not_none', 'assert_in', 'assert_not_in')


def assert_equal(a, b, message='not equal'):
    if a == b:
        print 'True because: \ra = %i\rb = %i' % (a, b)
    else:
        print 'False because: \ra = %i\rb = %i' % (a, b)
        raise Exception


def assert_not_equal(a, b, message='equal'):
    if a != b:
        print 'True because: \ra = %i\rb = %i' % (a, b)
    else:
        raise Exception
        print 'False because: \ra = %i\rb = %i' % (a, b)


def assert_true(x, message='false'):
    if x == True:
        print 'True because: \rx = %i' % (x)
    else:
        raise Exception
        print 'False because: \rx = %i' % (x)


def assert_false(x, message='true'):
    if x == False:
        print 'True because: \rx = %i' % (x)
    else:
        raise Exception
        print 'False because: \rx = %i' % (x)


def assert_is(a, b, message=' is not'):
    if a is b:
        print 'True because: \ra = %i\rb = %i' % (a, b)
    else:
        raise Exception
        print 'False because: \ra = %i\rb = %i' % (a, b)


def assert_is_not(a, b, message='is'):
    if a is not b:
        print 'True because: \ra = %i\rb = %i' % (a, b)
    else:
        raise Exception
        print 'False because: \ra = %i\rb = %i' % (a, b)


def assert_is_none(x, message='not None'):
    if x is None:
        print 'True because: \rx = %s\r' % (x)
    else:
        raise Exception
        print 'False because: \rx = %i' % (x)


def assert_is_not_none(x, message='None'):
    if x is not None:
        print 'True because: \rx = %i\r' % (x)
    else:
        raise Exception
        print 'False because: \rx = %s' % (x)


def assert_in(a, b, message='not in'):
    if a in b:
        print 'True because: \ra = %i\rb = %s' % (a, b)
    else:
        raise Exception
        print 'False because: \ra = %i\rb = %s' % (a, b)


def assert_not_in(a, b, message='in'):
    if a not in b:
        print 'True because: \ra = %i\rb = %s' % (a, b)
    else:
        raise Exception
        print 'False because: \ra = %i\rb = %s' % (a, b)
