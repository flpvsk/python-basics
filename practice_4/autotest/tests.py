'''
Created on Mar 20, 2014

@author: Java Student
'''
__all__ = ('test_that_fails', 'test_function_attribute_name')


from ivan_assertions import *


def test_that_fails():
    assert_equal(1, 2)


def test_function_attribute_name():
    def hyper_function():
        pass
    fn = hyper_function
    assert_equal(fn.__name__, "hyper_function")
