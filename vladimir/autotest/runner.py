'''
Created on Mar 13, 2014
 
@author: bessvla
'''

__all__ = ["add_test", "passed_tests", "pending_tests", "ran_tests", \
           "failed_tests", "clear_state", "run"]


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

