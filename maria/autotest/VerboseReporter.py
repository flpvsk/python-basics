class VerboseReporter(object):

    def report_test_started(self, test):
        print "Test '{}' has been started".format(test.__name__)

    def report_test_finished(self, test_result):
        print test_result

    def report_all_finished(self, run_tests_list, passed_tests_list,
                            failed_tests_list):
        print "Count of run tests: {}".format(len(run_tests_list))
        print "Count of passed tests: {}".format(
                                            len(passed_tests_list))
        print "Count of failed tests: {}".format(
                                            len(failed_tests_list))
