import traceback
from utils import noop


class TestRunner(object):

    def __init__(self, reporter):
        self.reporter = reporter
        self.pending_tests_list = []
        self.test_results_list = []

    def add_test(self, fn):
        self.pending_tests_list.append(fn)

    @property
    def pending_tests(self):
        return [t.__name__ for t in self.pending_tests_list]
    
    @property
    def run_tests(self):
        return self.test_results_list
    
    @property
    def passed_tests(self):
        return [test_result for test_result in self.test_results_list if
            test_result.test_result_status == test_result.PASSED_TEST_RESULT]
    
    @property
    def failed_tests(self):
        return [test_result for test_result in self.test_results_list if
            test_result.test_result_status == test_result.FAILED_TEST_RESULT]
    
    def run(self):
        while self.pending_tests_list:
            test = self.pending_tests_list[0]
            test_result = None
            try:
                self.reporter.report_test_started(test)
                test()
            except BaseException:
                test_result = TestResult(test, TestResult.FAILED_TEST_RESULT,
                                         traceback.format_exc())
            else:
                test_result = TestResult(test, TestResult.PASSED_TEST_RESULT)
            finally:
                self.test_results_list.append(test_result)
                self.pending_tests_list.remove(test)
                self.reporter.report_test_finished(test_result)
        self.reporter.report_all_finished(self.run_tests,
                                self.passed_tests, self.failed_tests)
        return (len(self.run_tests), len(self.passed_tests),
                len(self.failed_tests))
    
    def clear_state(self):
        del self.pending_tests_list[:]
        del self.test_results_list[:]
        self.tests_set_up = noop
        self.tests_tear_down = noop


class TestResult(object):
    FAILED_TEST_RESULT = "Failed"
    PASSED_TEST_RESULT = "Pass"

    def __init__(self, test, test_result_status, stacktrace=None):
        self.full_test_name = test.__module__
        try:
            self.full_test_name += "." + test.im_class.__name__
        except AttributeError:
            pass
        self.full_test_name += "." + test.__name__
        self.test_result_status = test_result_status
        self.stacktrace = stacktrace

    def __is_class_function(self, function):
        if 'im_class' in dir(function):
            return True
        return False

    def __str__(self):
        test_result_string = "Test '{}' {}.".format(
                            self.full_test_name, self.test_result_status)
        if self.stacktrace:
            test_result_string += " Stacktrace:\n {}".format(self.stacktrace)
        return test_result_string
