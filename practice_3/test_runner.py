'''
Created on Mar 13, 2014

@author: Java Student
'''

# key: test
# value: None, 0-passed, 1-failed
tests = dict()


def add_test(fn):
    tests[fn.__name__] = None


def pending_tests():
    return [func for func in tests.keys() if tests[func] == None]


def run():
    return (len(ran_tests()), len(passed_tests()), len(failed_tests()))


def ran_tests():
    return [func for func in tests.keys() if tests[func] != None]


def passed_tests():
    return [func for func in tests.keys() if tests[func] == 0]


def failed_tests():
    return [func for func in tests.keys() if tests[func] == 1]


def clear_state():
    for func in tests.keys():
        tests[func] = None


def q():
    pass


add_test(q)

print pending_tests()

print run()
