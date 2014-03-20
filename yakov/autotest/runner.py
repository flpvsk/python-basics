'''
Created on Mar 13, 2014

@author: Java Student
'''

__all__ = ['add_test', 'pending_tests', 'run', 'ran_tests', 'passed_tests',
           'failed_tests', 'clear_state']

PENDING = "pending"
PASSED = "passed"
FAILED = "failed"

# key: test
# value: None-pending, 0-passed, 1-failed
tests = dict()


def add_test(fn):
    tests[fn] = PENDING


def pending_tests():
    return [func for func in tests.keys() if tests[func] == PENDING]


def run():
    to_run = pending_tests()
    for tst in to_run:
        try:
            tst()
        except:
            tests[tst] = FAILED
        else:
            tests[tst] = PASSED
    return (len(ran_tests()), len(passed_tests()), len(failed_tests()))


def ran_tests():
    return [func for func in tests.keys() if tests[func] != PENDING]


def passed_tests():
    return [func for func in tests.keys() if tests[func] == PASSED]


def failed_tests():
    return [func for func in tests.keys() if tests[func] == FAILED]


def clear_state():
    tests.clear()


#Testing
def q():
    return 0


def p():
    raise "asd"


def framework_testing():
    add_test(q)
    add_test(p)
    print "Pending: {0}".format(pending_tests())
    print "Ran, passed, failed: {0}".format(run())
    print "Passed: {0}".format(passed_tests())
    print "Failed: {0}".format(failed_tests())

#framework_testing()
