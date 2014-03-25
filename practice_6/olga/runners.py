import traceback
from assertions import *
class TestRunnerBase(object):
    tests = {}
    PENDING = "pending"
    FAILED = "failed"
    PASSED = "passed"
    
    def add_test(self, fn):
        self.tests[fn.__name__] = ["pending", fn]
        
    def pending_tests(self):
        return [x for x in self.tests if self.tests[x][0] == "pending"]
    
    def run(self):
        for x in self.tests:
            if self.tests[x][0] == "pending":
                self.report_test_started(x)
                try:
                    test = self.tests[x][1]
                    test()
                    self.tests[x] = ["passed", test]
                    self.report_test_finished(x)
                except Exception as e:
                    self.tests[x] = ["failed", test]
                    self.report_test_finished(x, traceback.format_exc())
        print(self.report_all_finished())


    def ran_tests(self):
        return [x for x in self.tests if (self.tests[x][0] == "passed" or self.tests[x][0] == "failed")]
    
    def passed_tests(self):
        return [x for x in self.tests if self.tests[x][0] == "passed"]
    
    def failed_tests(self):
        return [x for x in self.tests if self.tests[x][0] == "failed"]
    
    def clear_state(self):
        self.tests = {}
    
    def report_all_finished(self):
        return {self.PASSED: self.passed_tests(),
                self.FAILED: self.failed_tests(),
                "RAN": self.ran_tests()}



class TestRunnerVerboseReporting(TestRunnerBase):
    def report_test_started(self, test):
        print("Started test '{0}'".format(test))
    
    def report_test_finished(self, test, e=None):
        if e:
            print("Test '{0}' failed: {1}".format(test, e))
        else:
            print("Test '{0}' passed".format(test))
    


class TestRunnerFailReporting(TestRunnerBase):
    def report_test_started(self, x=None):
        pass
    
    def report_test_finished(self, test, e=None):
        if e:
            print("test '{0}' failed: {1}".format(test, e))
        else:
            print(".")
    

if __name__ == "__main__":
    my_runner = TestRunnerFailReporting()
    my_runner.add_test(test_assert_equal)
    my_runner.add_test(test_assert_is_none)
    my_runner.add_test(test_assert_not_equal)    
    my_runner.run()
    
    my_runner2 = TestRunnerVerboseReporting()
    my_runner2.add_test(test_assert_equal)
    my_runner2.add_test(test_assert_is_none)
    my_runner2.add_test(test_assert_not_equal)    
    my_runner2.run()