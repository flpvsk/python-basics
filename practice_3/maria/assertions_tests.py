from examples_2.utils import print_stars
from assertions_with_message import *

def assertion_test(f, passed_test_message, *args):
    try:
        f(*args)
    except AssertionError as e:
        print("Failed - Exception caught: %r" % e.message)
    else:
        print(passed_test_message.format(*args))
    finally:
        print_stars()

print_stars()
print("Test 'assert_equal' function")
print_stars()
passed_test_message = "Passed - '{}' is equal to '{}'"
a = [1, 4]
b = [1, 4]
assertion_test(assert_equal, passed_test_message, a, b)
b = [1, 5]
assertion_test(assert_equal, passed_test_message, a, b)
error_message = "Not default error message"
assertion_test(assert_equal, passed_test_message, a, b, error_message)


