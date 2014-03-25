from TestRunnerBase import TestRunnerBase


class TestRunnerVerboseReporting(TestRunnerBase):

    def report_test_started(self, test):
        print "Test '{}' has been started".format(test.__name__)

    def report_test_finished(self, test_result):
        print test_result
