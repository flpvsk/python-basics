__all__ = ("test_assert_equal", "test_assert_not_equal",
           "test_assert_is_none", "assert_equal",
            "assert_not_equal", "assert_is_none")

def assert_equal(a, b, message="assert_equal default message"):
    assert a == b, "{0} {1} != {2}".format(message, a, b)


#assert_equal(1, 2, "pass")
assert_equal(5, 5)

def assert_not_equal(a, b, message="assert_not_equal dm"):
    assert a != b, "{0} {1} == {2}".format(message, a, b)

assert_not_equal(1,"1")
#assert_not_equal(5, 5)


def assert_true(x, message="assert_true dm"):
    assert x, "{0} {1} is False".format(message,x)

#assert_true(False)
#assert_true(None)
assert_true(1==1)
#assert_true(1!=1, "ddd ")


def assert_false(x, message="assert_false dm"):
    assert not x, "{0} {1} is True".format(message, str(x))

assert_false(False)
assert_false(None)
#assert_false(1==1, "some not deafault txt")
assert_false(1!=1)

def assert_is(a, b, message="assert_is dm"):
    assert a is b, "{0} {1} is not {2}".format(message, str(a), str(b))

#assert_is(1, 2, "fkfjfjfj")
assert_is(1, 1)


def assert_is_not(a, b, message="assert_is_not dm"):
    assert a is not b, "{0} {1} is {2}".format(message, str(a), str(b))

assert_is_not(1, 2)
#assert_is_not(1, 1, "fff")


def assert_is_none(x, message="assert_is_none dm"):
    assert x is None, "{1} {0} is not None".format(str(x), message)

#assert_is_none(1, "some txt")
#assert_is_none(1)
assert_is_none(None)

def assert_is_not_none(x, message="assert_is_not_none dm"):
    assert x is not None, "{1} {0} is None".format(str(x), message)

assert_is_not_none(1, "dd")
#assert_is_not_none(None, "ff")


def assert_in(a, b, message="assert_in dm"):
    assert a in b, "{2} {0} is not in {1}".format(str(a), str(b), message)

assert_in(1, range(5))
assert_in("a", "actually")
#assert_in("b", "actually", "gjgjgj")


def assert_not_in(a=None, b=[]):
    try:
        assert a not in b, "{0} is in {1}".format(str(a), str(b))
    except AssertionError as er:
        print("An error occurred: " + er.message)


assert_not_in("b", "actually")
assert_not_in("aa")
assert_not_in()


def test_assert_equal():
    assert_equal(1,2)
def test_assert_not_equal():
    assert_not_equal(1,1)
def test_assert_is_none():
    assert_is_none(None)