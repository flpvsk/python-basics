'''
Created on Mar 13, 2014

@author: Java Student
'''

from ivan_assertions import  *
from tests import *

__all__ = ('add_test', 'pending_test', 'run',
           'run_tests', 'passed_tests', 'failed_tests', 'clear_state')

pending_test_list = []
failed_test_list = []
run_test_list = []
passed_test_list = []


def add_test(fn):
    pending_test_list.append(fn)


def pending_test():
    for i in pending_test_list:
        return i


def run():
    for i in pending_test_list:
        try:
            i()
        except AssertionError as er:
            print("An error occurred: " + er)
            failed_test_list.append(i)
        finally:
            run_test_list.append(i)
            #pending_test_list.remove(i)
    return (len(run_test_list),
            len(passed_test_list),
            len(failed_test_list))


def run_tests():
    for i in run_test_list:
        return i


def passed_tests():
    for i in passed_test_list:
        return i


def failed_tests():
    for i in failed_test_list:
        return i


def clear_state():
    global pending_test_list
    global failed_test_list
    global run_test_list
    global passed_test_list

    del pending_test_list
    del failed_test_list
    del run_test_list
    del passed_test_list

if __name__ == '__main__':
    add_test(test_that_fails)
    add_test(test_function_attribute_name)
    run()
