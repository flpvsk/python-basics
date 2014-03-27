'''
Created on Mar 13, 2014

@author: bessvla
'''

__all__ = ['TestRunner']


class TestRunnerBase():
    def __init__(self):
        self.pending = []
        self.passed = []
        self.failed = []
        self.ran = []

    def add_test(self, fn):
        self.pending.append((fn))

    def passed_tests(self):
        return self.passed

    def pending_tests(self):
        return self.pending

    def ran_tests(self):
        return self.ran

    def failed_tests(self):
        return self.failed

    def clear_state(self):
        self.pending, self.passed, self.failed, self.ran = [], [], [], []

    def report_all_finished(self, r, p, f):
        print "Ran: %s Passed: %s Failed: %s" % (r, p, f)

    def run(self, testclass):
        testclass_instance = testclass()
        testmethods = [i for i in dir(testclass_instance)\
                        if i.startswith('test_')]
        for test in testmethods:
            try:
                self.report_test_started(test)
            except:
                pass
            try:
                testclass_instance.set_up()
            except:
                pass
            try:
                getattr(testclass_instance, test)()
                self.passed.append(test)
                try:
                    self.report_test_passed(test)
                except:
                    pass
            except:
                self.failed.append(test)
                try:
                    self.report_test_failed(test)
                except:
                    pass
            finally:
                self.ran.append(test)
                try:
                    testclass_instance.tear_down()
                except:
                    pass

        r = len(self.ran)
        p = len(self.passed)
        f = len(self.failed)
        self.report_all_finished(r, p, f)
        return (r, p, f)

class TestRunnerVerboseReporting(TestRunnerBase):
    def report_test_started(self, test):
        print test + " started"
    
    def report_test_passed(self, test):
        print test + " passed"

    def report_test_failed(self, test):
        print test + " failed"


class TestRunnerFailReporting(TestRunnerBase):
    def report_test_started(self, test):
        pass
    
    def report_test_passed(self, test):
        print "."

    def report_test_failed(self, test):
        print test + " failed"

class TodoTestCase(object):

    def __init__(self):
        print "initializing"

    def set_up(self):
        print "set_up"

    def test_add_todo_adds_pending_item(self):
        print "test1"

    def test_add_return_value(self):
        raise Exception 

    def tear_down(self):
        print "teardown"

testrunner = TestRunnerVerboseReporting()
testrunner.run(TodoTestCase)

testrunner = TestRunnerFailReporting()
testrunner.run(TodoTestCase)