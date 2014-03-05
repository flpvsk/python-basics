from utils import print_stars


# Basic try - except - [else] - finally
# `else` - optional
# should have `except` or `finally` or both
print("assert False")
try:
    assert False, "Error message here"
    print("Execution continued")
except AssertionError as e:
    print("Exception caught %r" % e.message)
else:
    print("No exception thrown")
finally:
    print("Finally block")
print_stars()


print("assert True")
try:
    assert True
    print("Execution continued")
except AssertionError as e:
    print("Exception caught")
else:
    print("No exception thrown")
finally:
    print("Finally block")
print_stars()


def raise_assertion_error(msg):
    raise AssertionError(msg)

raise_assertion_error("Custom Message")

# ValueError ~ IllegalStateException, IllegalArgumentException in Java
# TypeError - object of incorrect type was used
# AssertionError ~ AssertionError in Java
