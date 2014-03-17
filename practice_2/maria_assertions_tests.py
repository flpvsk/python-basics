from examples_2.utils import print_stars
from practice_2.maria_assertions import *

def assert_equal_test(a, b):
    try:
        assert_equal(a, b)
    except AssertionError as e:
        print("Failed - Exception caught: %r" % e.message)
    else:
        print("Passed - '{}' is equal to '{}'".format(a, b))
    finally:
        print_stars()
        
def assert_not_equal_test(a, b):
    try:
        assert_not_equal(a, b)
    except AssertionError as e:
        print("Failed - Exception caught: %r" % e.message)
    else:
        print("Passed - '{}' is not equal to '{}'".format(a, b))
    finally:
        print_stars()
        
def assert_true_test(x):
    try:
        assert_true(x)
    except AssertionError as e:
        print("Failed - Exception caught: %r" % e.message)
    else:
        print("Passed - '{}' is true".format(x))
    finally:
        print_stars()  
        
def assert_false_test(x):
    try:
        assert_false(x)
    except AssertionError as e:
        print("Failed - Exception caught: %r" % e.message)
    else:
        print("Passed - '{}' is false".format(x))
    finally:
        print_stars()   
        
def assert_is_test(a, b):
    try:
        assert_is(a, b)
    except AssertionError as e:
        print("Failed - Exception caught: %r" % e.message)
    else:
        print("Passed - '{}' is identical to '{}'".format(id(a), id(b)))
    finally:
        print_stars() 
        
def assert_is_not_test(a, b):
    try:
        assert_is_not(a, b)
    except AssertionError as e:
        print("Failed - Exception caught: %r" % e.message)
    else:
        print("Passed - '{}' is not identical to '{}'".format(id(a), id(b)))
    finally:
        print_stars()     
        
def assert_is_none_test(x):
    try:
        assert_is_none(x)
    except AssertionError as e:
        print("Failed - Exception caught: %r" % e.message)
    else:
        print("Passed - '{}' is none".format(x))
    finally:
        print_stars()  
        
def assert_is_not_none_test(x):
    try:
        assert_is_not_none(x)
    except AssertionError as e:
        print("Failed - Exception caught: %r" % e.message)
    else:
        print("Passed - '{}' is not none".format(x))
    finally:
        print_stars()  
        
def assert_in_test(a, b):
    try:
        assert_in(a, b)
    except AssertionError as e:
        print("Failed - Exception caught: %r" % e.message)
    else:
        print("Passed - '{}' in '{}'".format(a, b))
    finally:
        print_stars()   
        
def assert_not_in_test(a, b):
    try:
        assert_not_in(a, b)
    except AssertionError as e:
        print("Failed - Exception caught: %r" % e.message)
    else:
        print("Passed - '{}' not in '{}'".format(a, b))
    finally:
        print_stars()            

print_stars()
print("Test 'assert_equal' function")
print_stars()
a = [1, 4]
b = [1, 4]
assert_equal_test(a, b)
b = [1, 5]
assert_equal_test(a, b)

print("Test 'assert_not_equal' function")
print_stars()
a = [1, 4]
b = 7
assert_not_equal_test(a, b)
b = [1, 4]
assert_not_equal_test(a, b)

print("Test 'assert_true' function")
print_stars()
x = 5
assert_true_test(x)
x = 0
assert_true_test(x)

print("Test 'assert_false' function")
print_stars()
x = ""
assert_false_test(x)
x = " String "
assert_false_test(x)

print("Test 'assert_is' function")
print_stars()
a = [1, 4]
b = a
assert_is_test(a, b)
b = [1, 4]
assert_is_test(a, b)

print("Test 'assert_is_not' function")
print_stars()
a = [1, 4]
b = [1, 4]
assert_is_not_test(a, b)
b = a
assert_is_not_test(a, b)

print("Test 'assert_is_none' function")
print_stars()
x = None
assert_is_none_test(x)
x = 0
assert_is_none_test(x)

print("Test 'assert_is_not_none' function")
print_stars()
x = ""
assert_is_not_none_test(x)
x = None
assert_is_not_none_test(x)

print("Test 'assert_in' function")
print_stars()
a = 3
b = [1, 2, 3]
assert_in_test(a, b)
a = 7
assert_in_test(a, b)

print("Test 'assert_in' function")
print_stars()
a = "z"
b = "String"
assert_not_in_test(a, b)
a = "t"
assert_not_in_test(a, b)
