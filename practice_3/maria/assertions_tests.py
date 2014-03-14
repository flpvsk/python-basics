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

print("Test 'assert_not_equal' function")
print_stars()
passed_test_message = "Passed - '{}' is not equal to '{}'"
a = [1, 4]
b = 7
assertion_test(assert_not_equal, passed_test_message, a, b)
b = [1, 4]
assertion_test(assert_not_equal, passed_test_message, a, b)
error_message = "Not default error message"
assertion_test(assert_not_equal, passed_test_message, a, b, error_message)

print("Test 'assert_true' function")
print_stars()
passed_test_message = "Passed - '{}' is true"
x = 5
assertion_test(assert_true, passed_test_message, x)
x = 0
assertion_test(assert_true, passed_test_message, x)
error_message = "Not default error message"
assertion_test(assert_true, passed_test_message, x, error_message)

print("Test 'assert_false' function")
print_stars()
passed_test_message = "Passed - '{}' is false"
x = ""
assertion_test(assert_false, passed_test_message, x)
x = " String "
assertion_test(assert_false, passed_test_message, x)
error_message = "Not default error message"
assertion_test(assert_false, passed_test_message, x, error_message)

print("Test 'assert_is' function")
print_stars()
passed_test_message = "Passed - '{}' is identical to '{}'"
a = [1, 4]
b = a
assertion_test(assert_is, passed_test_message, a, b)
b = [1, 4]
assertion_test(assert_is, passed_test_message, a, b)
error_message = "Not default error message"
assertion_test(assert_is, passed_test_message, a, b, error_message)

print("Test 'assert_is_not' function")
print_stars()
passed_test_message = "Passed - '{}' is not identical to '{}'"
a = [1, 4]
b = [1, 4]
assertion_test(assert_is_not, passed_test_message, a, b)
b = a
assertion_test(assert_is_not, passed_test_message, a, b)
error_message = "Not default error message"
assertion_test(assert_is_not, passed_test_message, a, b, error_message)

print("Test 'assert_is_none' function")
print_stars()
passed_test_message = "Passed - '{}' is none"
x = None
assertion_test(assert_is_none, passed_test_message, x)
x = 0
assertion_test(assert_is_none, passed_test_message, x)
error_message = "Not default error message"
assertion_test(assert_is_none, passed_test_message, x, error_message)

print("Test 'assert_is_not_none' function")
print_stars()
passed_test_message = "Passed - '{}' is not none"
x = ""
assertion_test(assert_is_not_none, passed_test_message, x)
x = None
assertion_test(assert_is_not_none, passed_test_message, x)
error_message = "Not default error message"
assertion_test(assert_is_not_none, passed_test_message, x, error_message)

print("Test 'assert_in' function")
print_stars()
passed_test_message = "Passed - '{}' is in '{}'"
a = 3
b = [1, 2, 3]
assertion_test(assert_in, passed_test_message, a, b)
a = 7
assertion_test(assert_in, passed_test_message, a, b)
error_message = "Not default error message"
assertion_test(assert_in, passed_test_message, a, b, error_message)

print("Test 'assert_not_in' function")
print_stars()
passed_test_message = "Passed - '{}' is not in '{}'"
a = "z"
b = "String"
assertion_test(assert_not_in, passed_test_message, a, b)
a = "t"
assertion_test(assert_not_in, passed_test_message, a, b)
error_message = "Not default error message"
assertion_test(assert_not_in, passed_test_message, a, b, error_message)



