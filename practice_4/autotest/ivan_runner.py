'''
Created on Mar 13, 2014

@author: Java Student
'''

from ivan_assertions import  *
from tests import *

__all__ = ('add_test', 'pending_test', 'run',
           'run_tests', 'passed_tests', 'failed_tests', 'clear_state')


global pending_test_list
pending_test_list = []
failed_test_list = []
run_test_list = []
passed_test_list = []


def add_test(fn, *args):
    pending_test_list.append((fn, args))


def pending_test(pending_test_list):
    return pending_test_list


def run(pending_test_list):
    for i in pending_test_list:
        try:
            i[0](*i[1])
        except AssertionError as er:
            print("An error occurred: " + er)
            failed_test_list.append(i)
        finally:
            run_test_list.append(i)
            pending_test_list.remove(i)
    return (len(run_test_list), len(passed_test_list), len(failed_test_list))


def run_tests():
    return run_test_list


def passed_tests():
    return passed_test_list


def failed_tests():
    return failed_test_list


def clear_state():
    pending_test_list = []
    failed_test_list = []
    run_test_list = []
    passed_test_list = []


def foo():
    print'iugh'

add_test(foo)
print run(add_test(foo))

if __name__ == '__main__':
    add_test(test_that_fails)
    add_test(test_function_attribute_name)
    run()
