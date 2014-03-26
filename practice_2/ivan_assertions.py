'''
Created on 20 Mar 2014

@author: CenturyChild
'''


def assert_equal(a, b):
    if a == b:
        print 'True because: \ra = %i\rb = %i' % (a, b)
    else:
        print 'False because: \ra = %i\rb = %i' % (a, b)
        raise Exception


print 'assert_equal function tests: \n'
assert_equal(3, 5)
assert_equal(4, 4)


def assert_not_equal(a, b):
    if a != b:
        print 'True because: \ra = %i\rb = %i' % (a, b)
    else:
        raise Exception
        print 'False because: \ra = %i\rb = %i' % (a, b)

print '\rassert_not_equal function tests: \n'
assert_not_equal(3, 5)
assert_not_equal(4, 4)


def assert_true(x):
    if x == True:
        print 'True because: \rx = %i' % (x)
    else:
        raise Exception
        print 'False because: \rx = %i' % (x)

print '\rassert_true function tests: \n'
assert_true(1)
assert_true(0)


def assert_false(x):
    if x == False:
        print 'True because: \rx = %i' % (x)
    else:
        raise Exception
        print 'False because: \rx = %i' % (x)

print '\rassert_false function tests: \n'
assert_false(1)
assert_false(0)


def assert_is(a, b):
    if a is b:
        print 'True because: \ra = %i\rb = %i' % (a, b)
    else:
        raise Exception
        print 'False because: \ra = %i\rb = %i' % (a, b)

print '\rassert_is function tests: \n'
assert_is(3, 5)
assert_is(4, 4)


def assert_is_not(a, b):
    if a is not b:
        print 'True because: \ra = %i\rb = %i' % (a, b)
    else:
        raise Exception
        print 'False because: \ra = %i\rb = %i' % (a, b)

print '\rassert_is_not function tests: \n'
assert_is_not(3, 5)
assert_is_not(4, 4)


def assert_is_none(x):
    if x is None:
        print 'True because: \rx = %s\r' % (x)
    else:
        raise Exception
        print 'False because: \rx = %i' % (x)

print '\rassert_is_none function tests: \n'
assert_is_none(None)
assert_is_none(1)


def assert_is_not_none(x):
    if x is not None:
        print 'True because: \rx = %i\r' % (x)
    else:
        raise Exception
        print 'False because: \rx = %s' % (x)

print '\rassert_is_not_none function tests: \n'
assert_is_not_none(None)
assert_is_not_none(1)


def assert_in(a, b):
    if a in b:
        print 'True because: \ra = %i\rb = %s' % (a, b)
    else:
        raise Exception
        print 'False because: \ra = %i\rb = %s' % (a, b)

print '\rassert_in function tests: \n'
lst1 = [1, 2, 3, 4, 5]
lst2 = [3, 6, 8, 0]
assert_in(3, lst1)
assert_in(5, lst2)


def assert_not_in(a, b):
    if a not in b:
        print 'True because: \ra = %i\rb = %s' % (a, b)
    else:
        raise Exception
        print 'False because: \ra = %i\rb = %s' % (a, b)

print '\rassert_not_in function tests: \n'
lst1 = [1, 2, 3, 4, 5]
lst2 = [3, 6, 8, 0]
assert_not_in(3, lst1)
assert_not_in(5, lst2)
