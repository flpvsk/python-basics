'''
Created on 08 March 2014.

@author: Yaha
'''


def divider(string):
    stars = "*****"
    print("\n {}".format(stars + " " + string + " " + stars))


def test(res, exp):
    print res == exp


def assert_equal(a, b):
    res = False
    string = assert_equal.__name__ + ": " + str(a) + ", " + str(b)
    try:
        assert a == b
    except:
        pass
    else:
        res = True
    finally:
        print string
        return res


#Tests
divider("assert_equal")
test(assert_equal(1, 1), True)
test(assert_equal(1, 2), False)
test(assert_equal("abc", "abc"), True)
test(assert_equal("qwerty ", "qwerty"), False)


def assert_not_equal(a, b):
    res = False
    string = assert_not_equal.__name__ + ": " + str(a) + ", " + str(b)
    try:
        assert a != b
    except:
        pass
    else:
        res = True
    finally:
        print string
        return res

#Tests
divider("assert_not_equal")
test(assert_not_equal(1, 1), False)
test(assert_not_equal(1, 2), True)
test(assert_not_equal("abc", "abc"), False)
test(assert_not_equal("qwerty ", "qwerty"), True)


def assert_true(x):
    res = False
    string = assert_true.__name__ + ": " + str(x)
    try:
        assert x
    except:
        pass
    else:
        res = True
    finally:
        print string
        return res

#Tests
divider("assert_true")
test(assert_true(1), True)
test(assert_true(0), False)
test(assert_true(3 > 0), True)
test(assert_true(10 > 11), False)


def assert_false(x):
    res = False
    string = assert_false.__name__ + ": " + str(x)
    try:
        assert not x
    except:
        pass
    else:
        res = True
    finally:
        print string
        return res

#Tests
divider("assert_false")
test(assert_false(1), False)
test(assert_false(0), True)
test(assert_false(3 > 0), False)
test(assert_false(10 > 11), True)

def assert_is(a, b):
    pass

#Tests


def assert_is_not(a, b):
    pass

#Tests


def assert_is_none(x):
    pass

#Tests


def assert_is_not_none(x):
    pass

#Tests


def assert_in(a, b):
    pass

#Tests


def assert_not_in(a, b):
    pass

#Tests
