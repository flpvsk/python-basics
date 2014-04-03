from examples_2.utils import print_stars
from assertions_with_message import assert_equal, assert_is_none

def equal_passed_test():
    print("Test lists equality, result - passed")
    print_stars()
    a = [1, 4]
    b = [1, 4]
    assert_equal(a, b)
    
def equal_failed_test():
    print("Test lists equality, result - failed")
    print_stars()
    a = [1, 4]
    b = [1, 5]
    assert_equal(a, b)

def is_none_passed_test():
    print("Test if variable is none, result - passed")
    print_stars()
    x = None
    assert_is_none(x)
    
def is_none_failed_test():
    print("Test if variable is none, result - failed")
    print_stars()
    x = None
    assert_is_none(x)




