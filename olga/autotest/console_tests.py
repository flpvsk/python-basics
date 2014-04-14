from assertions import *
import sys

__all__ = ["console_test_assert_equal", "console_test_assert_not_equal", "console_test_assert_is_none"]

def console_test_assert_equal():
    assert_equal(1,1)
    
    
def console_test_assert_not_equal():
    assert_not_equal(1,1)
    
    
def console_test_assert_is_none():
    assert_is_none(None)
   

if __name__ == "__main__":
    console_test_assert_equal()
    console_test_assert_not_equal()
    console_test_assert_is_none()
    