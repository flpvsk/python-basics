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
