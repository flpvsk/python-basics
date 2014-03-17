'''
Created on 08 March 2014.

@author: Yaha
'''


def divider(string):
    stars = "*****"
    print "\n {0} {1} {0}".format(stars, string)
    #print("\n {}".format(stars + " " + string + " " + stars))


def test_pass(fn, *args):
    try:
        fn(*args)
    except:
        print "{0}{1} failed".format(fn.__name__, args)
    else:
        print "{0}{1} passed".format(fn.__name__, args)


def test_fail(fn, *args):
    try:
        fn(*args)
    except:
        print "{0}{1} passed".format(fn.__name__, args)
    else:
        print "{0}{1} failed".format(fn.__name__, args)


def test(res, exp):
    print res == exp


def args_to_str(*args):
    return " " + str(args)

fl = "Assertion failed."


def assert_equal(a, b, message=fl):
    assert a == b, message + args_to_str(a, b)


#Tests
def test_assert_equal():
    divider("assert_equal")
    test_pass(assert_equal, 1, 1)
    test_fail(assert_equal, 1, 2)
    test_pass(assert_equal, "abc", "abc")
    test_fail(assert_equal, "qwerty ", "qwerty")
    test_pass(assert_equal, [2, 3], [2, 3])
    test_fail(assert_equal, [2, 3], [2])
    test_pass(assert_equal, (2, 3), (2, 3))
    test_fail(assert_equal, (2, 3), (2))

test_assert_equal()


def assert_not_equal(a, b, message=fl):
    assert a != b, message


#Tests
def test_assert_not_equal():
    divider("assert_not_equal")
    test(assert_not_equal(1, 1), False)
    test(assert_not_equal(1, 2), True)
    test(assert_not_equal("abc", "abc"), False)
    test(assert_not_equal("qwerty ", "qwerty"), True)
    test(assert_not_equal([2, 3], [2, 3]), False)
    test(assert_not_equal([2, 3], [2]), True)
    test(assert_not_equal((2, 3), (2, 3)), False)
    test(assert_not_equal((2, 3), (2)), True)


def assert_true(x, message=fl):
    assert x, message


#Tests
def test_assert_true():
    divider("assert_true")
    test(assert_true(1), True)
    test(assert_true(0), False)
    test(assert_true(3 > 0), True)
    test(assert_true(10 > 11), False)


def assert_false(x, message=fl):
    assert not x, message


#Tests
def test_assert_false():
    divider("assert_false")
    test(assert_false(1), False)
    test(assert_false(0), True)
    test(assert_false(3 > 0), False)
    test(assert_false(10 > 11), True)


def assert_is(a, b, message=fl):
    assert a is b, message


#Tests
def test_assert_is():
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


def assert_is_not(a, b, message=fl):
    assert a is not b, message


#Tests
def test_assert_is_not():
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


def assert_is_none(x, message=fl):
    assert x is None, message


#Tests
def test_assert_is_none():
    divider("assert_is_none")
    test(assert_is_none(0), False)
    test(assert_is_none([]), False)
    test(assert_is_none(()), False)
    test(assert_is_none(""), False)
    test(assert_is_none(None), True)
    test(assert_is_none(False), False)


def assert_is_not_none(x, message=fl):
    assert x is not None, message


#Tests
def test_assert_is_not_none():
    divider("assert_is__not_none")
    test(assert_is_not_none(0), True)
    test(assert_is_not_none([]), True)
    test(assert_is_not_none(()), True)
    test(assert_is_not_none(""), True)
    test(assert_is_not_none(None), False)
    test(assert_is_not_none(False), True)


def assert_in(a, b, message=fl):
    assert a in b, message


#Tests
def test_assert_in():
    divider("assert_in")
    test(assert_in(1, [2, 1]), True)
    test(assert_in([], [2, 1]), False)
    test(assert_in("r", "forever"), True)
    test(assert_in("fork", "forever"), False)
    test(assert_in(["one", "two"], ["one", ["one", "two"], "two"]), True)
    test(assert_in(["one", "two"], ["one", "two"]), False)
    test(assert_in(("one", "two"), ("one", ("one", "two"), "two")), True)
    test(assert_in(("one", "two"), ("one", "two")), False)


def assert_not_in(a, b, message=fl):
    assert a not in b, message


#Tests
def test_assert_not_in():
    divider("assert_not_in")
    test(assert_not_in(1, [2, 1]), False)
    test(assert_not_in([], [2, 1]), True)
    test(assert_not_in("r", "forever"), False)
    test(assert_not_in("fork", "forever"), True)
    test(assert_not_in(["one", "two"], ["one", ["one", "two"], "two"]), False)
    test(assert_not_in(["one", "two"], ["one", "two"]), True)
    test(assert_not_in(("one", "two"), ("one", ("one", "two"), "two")), False)
    test(assert_not_in(("one", "two"), ("one", "two")), True)
