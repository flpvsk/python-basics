'''
Created on Mar 13, 2014

@author: Java Student
'''

# key: test
# value: None-pending, 0-passed, 1-failed
tests = dict()


def add_test(fn):
    tests[fn] = None


def pending_tests():
    return [func for func in tests.keys() if tests[func] == None]


def run():
    to_run = pending_tests()
    for tst in to_run:
        try:
            tst()
        except:
            tests[tst] = 1
        else:
            tests[tst] = 0
    return (len(ran_tests()), len(passed_tests()), len(failed_tests()))


def ran_tests():
    return [func for func in tests.keys() if tests[func] != None]


def passed_tests():
    return [func for func in tests.keys() if tests[func] == 0]


def failed_tests():
    return [func for func in tests.keys() if tests[func] == 1]


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
