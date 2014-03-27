'''
Created on Mar 13, 2014

@author: Java Student
'''
from test_result import TestResult
import traceback


class TestRunner():
    _PENDING = "pending"
    _PASSED = "passed"
    _FAILED = "failed"
    # key: test
    # value: None-pending, 0-passed, 1-failed
    def __init__(self, TestClass=None):
        self._tests = dict()
        self._test_res_list = []
        if TestClass != None:
            self._TestClass = TestClass()

    # Test as a function
    def add_test(self, fn):
        self._tests[fn] = self._PENDING

    # Tests as class methods
    def add_tests_from_class(self):
        tst_list = dir(self._TestClass)
        self._tests = {getattr(self._TestClass, tst):self._PENDING for tst in tst_list if tst.find('test') == 0}

    def pending_tests(self):
        return [func for func in self._tests.keys() if self._tests[func] == self._PENDING]

    def run(self):
        to_run = self.pending_tests()
        for tst in to_run:
            try:
                self._TestClass.set_up()
                tst()
                self._TestClass.tear_down()
            except:
                self._tests[tst] = self._FAILED
                t = TestResult(tst.__name__, self._FAILED, traceback.format_exc())
                self._test_res_list.append(t)
            else:
                self._tests[tst] = self._PASSED
                t = TestResult(tst.__name__, self._PASSED)
                self._test_res_list.append(t)
        return (len(self.ran_tests()), len(self.passed_tests()), len(self.failed_tests()))

# TODO: return list of TestResult objects
    def ran_tests(self):
        return [func for func in self._tests.keys() if self._tests[func] != self._PENDING]

# TODO: return list of TestResult objects
    def passed_tests(self):
        return [func for func in self._tests.keys() if self._tests[func] == self._PASSED]

# TODO: return list of TestResult objects
    def failed_tests(self):
        return [func for func in self._tests.keys() if self._tests[func] == self._FAILED]

# TODO: return list of TestResult objects
    def clear_state(self):
        self._tests.clear()
