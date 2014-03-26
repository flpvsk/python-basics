'''
Created on Mar 13, 2014

@author: bessvla
'''

from practice_3.vladimir.asserts import *

pending = []
passed = []
failed = []
ran = []


def add_test(fn):
    pending.append(fn)


def passed_tests():
    return passed


def pending_tests():
    return pending


def ran_tests():
    return ran


def failed_tests():
    return failed


def clear_state():
    global pending, passed, failed, ran
    pending, passed, failed, ran = [], [], [], []


def run():
    for i in pending_tests:
        try:
            i
            passed.append(pending.pop(i))
        except:
            failed.append(pending.pop(i))
        finally:
            ran.append(i)
    ran = len(ran)
    passed = len(passed)
    failed = len(failed)
    return (ran, passed, failed)


add_test(assert_true)
add_test(assert_true)
add_test(assert_equal)
add_test(assert_equal)
add_test(assert_false)
add_test(assert_false)
print pending_tests()
