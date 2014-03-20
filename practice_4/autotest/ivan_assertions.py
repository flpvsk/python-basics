'''
Created on Mar 17, 2014

@author: Java Student
'''

__all__ = ('assert_true', 'assert_not_equal', 'assert_equal')


def assert_equal(a, b):
    if a == b:
        print 'True because: \ra = %s\rb = %s' % (a, b)
    else:
        print 'False because: \ra = %s\rb = %s' % (a, b)


def assert_not_equal(a, b):
    if a != b:
        print 'True because: \ra = %i\rb = %i' % (a, b)
    else:
        print 'False because: \ra = %i\rb = %i' % (a, b)


def assert_true(x):
    if x == True:
        print 'True because: \rx = %i' % (x)
    else:
        print 'False because: \rx = %i' % (x)


def assert_false(x):
    if x == False:
        print 'True because: \rx = %i' % (x)
    else:
        print 'False because: \rx = %i' % (x)


def assert_is(a, b):
    if a is b:
        print 'True because: \ra = %i\rb = %i' % (a, b)
    else:
        print 'False because: \ra = %i\rb = %i' % (a, b)


def assert_is_not(a, b):
    if a is not b:
        print 'True because: \ra = %i\rb = %i' % (a, b)
    else:
        print 'False because: \ra = %i\rb = %i' % (a, b)


def assert_is_none(x):
    if x is None:
        print 'True because: \rx = %s\r' % (x)
    else:
        print 'False because: \rx = %i' % (x)


def assert_is_not_none(x):
    if x is not None:
        print 'True because: \rx = %i\r' % (x)
    else:
        print 'False because: \rx = %s' % (x)


def assert_in(a, b):
    if a in b:
        print 'True because: \ra = %i\rb = %s' % (a, b)
    else:
        print 'False because: \ra = %i\rb = %s' % (a, b)


def assert_not_in(a, b):
    if a not in b:
        print 'True because: \ra = %i\rb = %s' % (a, b)
    else:
        print 'False because: \ra = %i\rb = %s' % (a, b)
