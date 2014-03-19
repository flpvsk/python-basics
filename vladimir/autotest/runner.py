'''
Created on Mar 13, 2014
 
@author: bessvla
'''

__all__ = ["add_test", "passed_tests", "pending_tests", "ran_tests", \
           "failed_tests", "clear_state", "run"]

from vladimir.autotest import assert_true, assert_not_equal

pending = []
passed = []
failed = []
ran = []


def add_test(fn, *args):
    global pending
    pending.append((fn, args))


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
    global pending, passed, failed, ran
    for i in pending_tests():
        try:
            i[0](*i[1])
            passed.append(i)
        except:
            failed.append(i)
        finally:
            ran.append(i)
    ran = len(ran)
    passed = len(passed)
    failed = len(failed)
    return (ran, passed, failed)


add_test(assert_true, True)
add_test(assert_true, False)
add_test(assert_not_equal, 3, 3)
add_test(assert_not_equal, 3, 3)
print pending_tests()
