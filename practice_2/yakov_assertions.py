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
test(assert_equal([2, 3], [2, 3]), True)
test(assert_equal([2, 3], [2]), False)
test(assert_equal((2, 3), (2, 3)), True)
test(assert_equal((2, 3), (2)), False)


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
test(assert_not_equal([2, 3], [2, 3]), False)
test(assert_not_equal([2, 3], [2]), True)
test(assert_not_equal((2, 3), (2, 3)), False)
test(assert_not_equal((2, 3), (2)), True)


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
    res = False
    string = assert_is.__name__ + ": " + str(a) + ", " + str(b)
    try:
        assert a is b
    except:
        pass
    else:
        res = True
    finally:
        print string
        return res

#Tests
divider("assert_is")
test(assert_is(1, 1), True)
test(assert_is(1, 2), False)
test(assert_is("abc", "abc"), True)
test(assert_is("qwerty ", "qwerty"), False)
test(assert_is([2, 3], [2, 3]), False)
test(assert_is([2, 3], [2]), False)
test(assert_is((2, 3), (2, 3)), False)
test(assert_is((2, 3), (2)), False)
a = ["a", "b"]
b = ["b", "a"]
test(assert_is(a, a), True)
test(assert_is(a, b), False)
c = (1.1, 2.2)
d = (3.3, 4.4)
test(assert_is(c, c), True)
test(assert_is(c, d), False)


def assert_is_not(a, b):
    res = False
    string = assert_is.__name__ + ": " + str(a) + ", " + str(b)
    try:
        assert a is not b
    except:
        pass
    else:
        res = True
    finally:
        print string
        return res

#Tests
divider("assert_is_not")
test(assert_is_not(1, 1), False)
test(assert_is_not(1, 2), True)
test(assert_is_not("abc", "abc"), False)
test(assert_is_not("qwerty ", "qwerty"), True)
test(assert_is_not([2, 3], [2, 3]), True)
test(assert_is_not([2, 3], [2]), True)
test(assert_is_not((2, 3), (2, 3)), True)
test(assert_is_not((2, 3), (2)), True)
a = ["a", "b"]
b = ["b", "a"]
test(assert_is_not(a, a), False)
test(assert_is_not(a, b), True)
c = (1.1, 2.2)
d = (3.3, 4.4)
test(assert_is_not(c, c), False)
test(assert_is_not(c, d), True)


def assert_is_none(x):
    res = False
    string = assert_false.__name__ + ": " + str(x)
    try:
        assert x is None
    except:
        pass
    else:
        res = True
    finally:
        print string
        return res

#Tests
divider("assert_is_none")
test(assert_is_none(0), False)
test(assert_is_none([]), False)
test(assert_is_none(()), False)
test(assert_is_none(""), False)
test(assert_is_none(None), True)
test(assert_is_none(False), False)


def assert_is_not_none(x):
    res = False
    string = assert_false.__name__ + ": " + str(x)
    try:
        assert x is not None
    except:
        pass
    else:
        res = True
    finally:
        print string
        return res

#Tests
divider("assert_is__not_none")
test(assert_is_not_none(0), True)
test(assert_is_not_none([]), True)
test(assert_is_not_none(()), True)
test(assert_is_not_none(""), True)
test(assert_is_not_none(None), False)
test(assert_is_not_none(False), True)


def assert_in(a, b):
    res = False
    string = assert_is.__name__ + ": " + str(a) + ", " + str(b)
    try:
        assert a in b
    except:
        pass
    else:
        res = True
    finally:
        print string
        return res

#Tests
divider("assert_in")
test(assert_in(1, [2, 1]), True)
test(assert_in([], [2, 1]), False)
test(assert_in("r", "forever"), True)
test(assert_in("fork", "forever"), False)
test(assert_in(["one", "two"], ["one", ["one", "two"], "two"]), True)
test(assert_in(["one", "two"], ["one", "two"]), False)
test(assert_in(("one", "two"), ("one", ("one", "two"), "two")), True)
test(assert_in(("one", "two"), ("one", "two")), False)


def assert_not_in(a, b):
    res = False
    string = assert_is.__name__ + ": " + str(a) + ", " + str(b)
    try:
        assert a not in b
    except:
        pass
    else:
        res = True
    finally:
        print string
        return res

#Tests
divider("assert_not_in")
test(assert_not_in(1, [2, 1]), False)
test(assert_not_in([], [2, 1]), True)
test(assert_not_in("r", "forever"), False)
test(assert_not_in("fork", "forever"), True)
test(assert_not_in(["one", "two"], ["one", ["one", "two"], "two"]), False)
test(assert_not_in(["one", "two"], ["one", "two"]), True)
test(assert_not_in(("one", "two"), ("one", ("one", "two"), "two")), False)
test(assert_not_in(("one", "two"), ("one", "two")), True)
