def assert_equal(a=None, b=None):
    try:
        assert a == b, "{0} != {1}".format(str(a), str(b))
    except AssertionError as er:
        print("An error occurred: " + er.message)

print ("assert_equal")
assert_equal(1, "1")
assert_equal(1)
assert_equal()
assert_equal(5, 5) 
    
def assert_not_equal(a=None, b=None):
    try:
        assert a != b, "{0} == {1}".format(str(a), str(b))
    except AssertionError as er:
        print("An error occurred: " + er.message)

print("assert_not_equal")
assert_not_equal(1,"1")
assert_not_equal(1)
assert_not_equal()
assert_not_equal(5,5)


def assert_true(x):
    try:
        assert x, "{0} is False".format(str(x))
    except AssertionError as er:
        print("An error occurred: " + er.message)

print("assert_true")
assert_true(False)
assert_true(None)
assert_true(1==1)
assert_true(1!=1)


def assert_false(x):
    try:
        assert not x, "{0} is True".format(str(x))
    except AssertionError as er:
        print("An error occurred: " + er.message)

print("assert_false")
assert_false(False)
assert_false(None)
assert_false(1==1)
assert_false(1!=1)

def assert_is(a=None, b=None):
    try:
        assert a is b, "{0} is not {1}".format(str(a), str(b))
    except AssertionError as er:
        print("An error occurred: " + er.message)

print("assert_is")
assert_is(1, 2)
assert_is(None, False)
c, d = 1, 1
assert_is(c, d)
c = d = 3
assert_is(c, d)
assert_is()

def assert_is_not(a=None, b=None):
    try:
        assert a is not b, "{0} is {1}".format(str(a), str(b))
    except AssertionError as er:
        print("An error occurred: " + er.message)

print("assert_is_not")
assert_is_not(1, 2)
assert_is_not(None, False)
c, d = 1, 1
assert_is_not(c, d)
c = d = 3
assert_is_not(c, d)
assert_is_not()


def assert_is_none(x=None):
    try:
        assert x is None, "{0} is not None".format(str(x))
    except AssertionError as er:
        print("An error occurred: " + er.message)

print("assert_is_none")
assert_is_none(1)
assert_is_none(None)
assert_is_none(False)
assert_is_none()


def assert_is_not_none(x=None):
    try:
        assert x is not None, "{0} is None".format(str(x))
    except AssertionError as er:
        print("An error occurred: " + er.message)

print("assert_is_not_none")
assert_is_not_none(1)
assert_is_not_none(None)
assert_is_not_none(False)
assert_is_not_none()


def assert_in(a=None, b=[]):
    try:
        assert a in b, "{0} is not in {1}".format(str(a), str(b))
    except AssertionError as er:
        print("An error occurred: " + er.message)

print("assert_in")
assert_in(1, range(5))
assert_in("a", "actually")
assert_in("b", "actually")
assert_in("aa")
assert_in()

def assert_not_in(a=None, b=[]):
    try:
        assert a not in b, "{0} is in {1}".format(str(a), str(b))
    except AssertionError as er:
        print("An error occurred: " + er.message)

print("assert_not_in")
assert_not_in(1, range(5))
assert_not_in("a", "actually")
assert_not_in("b", "actually")
assert_not_in("aa")
assert_not_in()