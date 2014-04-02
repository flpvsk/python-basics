'''
Created on 08 March 2014.

@author: Yaha
'''

__all__ = ['assert_equal', 'assert_not_equal', 'assert_true', 'assert_false',
           'assert_is', 'assert_is_not', 'assert_is_none',
           'assert_is_not_none', 'assert_in', 'assert_not_in']


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


def args_to_str(*args):
    return " " + str(args)

fl = "Assertion failed."


def assert_equal(a, b, message=fl):
    assert a == b, message + args_to_str(a, b)


#Tests
def test_assert_equal():
    divider("assert_equal")
    test_pass(assert_equal, 1, 2)
    test_fail(assert_equal, 1, 2)
    test_pass(assert_equal, "abc", "abc")
    test_fail(assert_equal, "qwerty ", "qwerty")
    test_pass(assert_equal, [2, 3], [2, 3])
    test_fail(assert_equal, [2, 3], [2])
    test_pass(assert_equal, (2, 3), (2, 3))
    test_fail(assert_equal, (2, 3), (2))

#test_assert_equal()


def assert_not_equal(a, b, message=fl):
    assert a != b, message


#Tests
def test_assert_not_equal():
    divider("assert_not_equal")
    test_fail(assert_not_equal, 1, 1)
    test_pass(assert_not_equal, 1, 2)
    test_fail(assert_not_equal, "abc", "abc")
    test_pass(assert_not_equal, "qwerty ", "qwerty")
    test_fail(assert_not_equal, [2, 3], [2, 3])
    test_pass(assert_not_equal, [2, 3], [2])
    test_fail(assert_not_equal, (2, 3), (2, 3))
    test_pass(assert_not_equal, (2, 3), (2))

#test_assert_not_equal()


def assert_true(x, message=fl):
    assert x, message


#Tests
def test_assert_true():
    divider("assert_true")
    test_pass(assert_true, 1)
    test_fail(assert_true, 0)
    test_pass(assert_true, 3 > 0)
    test_fail(assert_true, 10 > 11)

#test_assert_true()


def assert_false(x, message=fl):
    assert not x, message


#Tests
def test_assert_false():
    divider("assert_false")
    test_fail(assert_false, 1)
    test_pass(assert_false, 0)
    test_fail(assert_false, 3 > 0)
    test_pass(assert_false, 10 > 11)

#test_assert_false()


def assert_is(a, b, message=fl):
    assert a is b, message


#Tests
def test_assert_is():
    divider("assert_is")
    test_pass(assert_is, 1, 1)
    test_fail(assert_is, 1, 2)
    test_pass(assert_is, "abc", "abc")
    test_fail(assert_is, "qwerty ", "qwerty")
    test_fail(assert_is, [2, 3], [2, 3])
    test_fail(assert_is, [2, 3], [2])
    test_fail(assert_is, (2, 3), (2, 3))
    test_fail(assert_is, (2, 3), (2))
    a = ["a", "b"]
    b = ["b", "a"]
    test_pass(assert_is, a, a)
    test_fail(assert_is, a, b)
    c = (1.1, 2.2)
    d = (3.3, 4.4)
    test_pass(assert_is, c, c)
    test_fail(assert_is, c, d)

#test_assert_is()


def assert_is_not(a, b, message=fl):
    assert a is not b, message


#Tests
def test_assert_is_not():
    divider("assert_is_not")
    test_fail(assert_is_not, 1, 1)
    test_pass(assert_is_not, 1, 2)
    test_fail(assert_is_not, "abc", "abc")
    test_pass(assert_is_not, "qwerty ", "qwerty")
    test_pass(assert_is_not, [2, 3], [2, 3])
    test_pass(assert_is_not, [2, 3], [2])
    test_pass(assert_is_not, (2, 3), (2, 3))
    test_pass(assert_is_not, (2, 3), (2))
    a = ["a", "b"]
    b = ["b", "a"]
    test_fail(assert_is_not, a, a)
    test_pass(assert_is_not, a, b)
    c = (1.1, 2.2)
    d = (3.3, 4.4)
    test_fail(assert_is_not, c, c)
    test_pass(assert_is_not, c, d)

#test_assert_is_not()


def assert_is_none(x, message=fl):
    assert x is None, message


#Tests
def test_assert_is_none():
    divider("assert_is_none")
    test_fail(assert_is_none, 0)
    test_fail(assert_is_none, [])
    test_fail(assert_is_none, ())
    test_fail(assert_is_none, "")
    test_pass(assert_is_none, None)
    test_fail(assert_is_none, False)

#test_assert_is_none()


def assert_is_not_none(x, message=fl):
    assert x is not None, message


#Tests
def test_assert_is_not_none():
    divider("assert_is__not_none")
    test_pass(assert_is_not_none, 0)
    test_pass(assert_is_not_none, [])
    test_pass(assert_is_not_none, ())
    test_pass(assert_is_not_none, "")
    test_fail(assert_is_not_none, None)
    test_pass(assert_is_not_none, False)

#test_assert_is_not_none()


def assert_in(a, b, message=fl):
    assert a in b, message


#Tests
def test_assert_in():
    divider("assert_in")
    test_pass(assert_in, 1, [2, 1])
    test_fail(assert_in, [], [2, 1])
    test_pass(assert_in, "r", "forever")
    test_fail(assert_in, "fork", "forever")
    test_pass(assert_in, ["one", "two"], ["one", ["one", "two"], "two"])
    test_fail(assert_in, ["one", "two"], ["one", "two"])
    test_pass(assert_in, ("one", "two"), ("one", ("one", "two"), "two"))
    test_fail(assert_in, ("one", "two"), ("one", "two"))

#test_assert_in()


def assert_not_in(a, b, message=fl):
    assert a not in b, message


#Tests
def test_assert_not_in():
    divider("assert_not_in")
    test_fail(assert_not_in, 1, [2, 1])
    test_pass(assert_not_in, [], [2, 1])
    test_fail(assert_not_in, "r", "forever")
    test_pass(assert_not_in, "fork", "forever")
    test_fail(assert_not_in, ["one", "two"], ["one", ["one", "two"], "two"])
    test_pass(assert_not_in, ["one", "two"], ["one", "two"])
    test_fail(assert_not_in, ("one", "two"), ("one", ("one", "two"), "two"))
    test_pass(assert_not_in, ("one", "two"), ("one", "two"))

#test_assert_not_in()
