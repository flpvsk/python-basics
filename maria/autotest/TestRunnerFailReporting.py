from TestRunnerBase import TestRunnerBase
from TestResult import TestResult


class TestRunnerFailReporting(TestRunnerBase):

    def report_test_started(self, test):
        pass

    def report_test_finished(self, test_result):
        if test_result.test_result_status == TestResult.PASSED_TEST_RESULT:
            print "."
        else:
            print test_result
