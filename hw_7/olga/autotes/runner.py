import traceback
from assertions import *
from todo_tests import *
from todo import *
import functools
from datetime import datetime
import sys
import os


class TestRunnerReporter(object):
    tests = {}
    PENDING = "pending"
    FAILED = "failed"
    PASSED = "passed"
    reporter = None
    
    def set_up(self): pass
    def tear_down(self): pass
    
    def __init__(self, some_reporter):
        self.reporter = some_reporter
        test_case = TodoTestCase()
        self.tests = {m: [self.PENDING, getattr(test_case, m)] for m in dir(test_case) if m.startswith("test_")}
        if hasattr(test_case, "set_up"):
            self.set_up = getattr(test_case, "set_up")
        if hasattr(test_case, "tear_down"):
            self.tear_down = getattr(test_case, "tear_down")
    
    def add_test(self, fn):
        self.tests[fn.__name__] = ["pending", fn]
        
    def pending_tests(self):
        return [x for x in self.tests if self.tests[x][0] == "pending"]
    
    
    def run(self):
        for x in self.tests:
            if self.tests[x][0] == "pending":
                self.reporter.report_test_started(x)
                try:
                    test = self.tests[x][1]
                    test()
                    self.tests[x] = ["passed", test]
                    self.reporter.report_test_finished(x)
                except Exception:
                    self.tests[x] = ["failed", test]
                    self.reporter.report_test_finished(x, traceback.format_exc())
        self.reporter.report_all_finished(self.passed_tests(), self.failed_tests(), self.ran_tests())


    def ran_tests(self):
        return [x for x in self.tests if (self.tests[x][0] == "passed" or self.tests[x][0] == "failed")]
    
    def passed_tests(self):
        return [x for x in self.tests if self.tests[x][0] == "passed"]
    
    def failed_tests(self):
        return [x for x in self.tests if self.tests[x][0] == "failed"]
    
    def clear_state(self):
        self.tests = {}
    


class VerboseReporter(object):
    def report_test_started(self, test):
        print("Started test '{0}'".format(test))
    
    def report_test_finished(self, test, e=None):
        if e:
            print("Test '{0}' failed: {1}".format(test, e))
        else:
            print("Test '{0}' passed".format(test))
    
    def report_all_finished(self, passed, failed, ran):
        print({"PASSED": passed,
                "FAILED": failed,
                "RAN": ran})        
    


class FailReporter(object):
    def report_test_started(self, x=None):
        pass
    
    def report_test_finished(self, test, e=None):
        if e:
            print("test '{0}' failed: {1}".format(test, e))
        else:
            print(".")
    def report_all_finished(self, passed, failed, ran):
        print({"PASSED": passed,
                "FAILED": failed,
                "RAN": ran})


class logReporter(object):
    LOG_DIR = "C:\\test-results\[{isodatetime}]-tests-results.txt"
        
    def __init__(self):
        self.LOG_DIR = self.LOG_DIR.format(isodatetime=datetime.now().isoformat().replace(':', '.'))
        if not os.path.exists(os.path.dirname(self.LOG_DIR)):
            os.makedirs(os.path.dirname(self.LOG_DIR))

    def report_test_started(self, test):
        with open(self.LOG_DIR, 'a') as file:
            #lines = file.read()
            file.writelines("Started test '{0}'".format(test))
            #if lines:
                #file.writelines(lines)
    
    def report_test_finished(self, test, e=None):
        with open(self.LOG_DIR, 'a') as file:
            if e:
                file.writelines("Test '{0}' failed: {1}".format(test, e))
            else:
                file.writelines("Test '{0}' passed".format(test))
    
    def report_all_finished(self, passed, failed, ran):
        with open(self.LOG_DIR, 'a') as file:
            file.writelines(str({"PASSED": passed,
                    "FAILED": failed,
                    "RAN": ran}))

if __name__ == "__main__":
    my_runner = TestRunnerReporter(logReporter())
    my_runner.add_test(test_assert_equal)
    my_runner.add_test(test_assert_is_none)
    my_runner.add_test(test_assert_not_equal)
    my_runner.run()
    
    
    
    '''
    my_runner1 = TestRunnerReporter(FailReporter())
    my_runner1.add_test(test_assert_equal)
    my_runner1.add_test(test_assert_is_none)
    my_runner1.add_test(test_assert_not_equal)    
    my_runner1.run()'''
    