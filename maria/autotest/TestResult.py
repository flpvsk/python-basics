class TestResult(object):

    def __init__(self, test, test_result, stacktrace=None):
        self.full_test_name = test.__module__
        if self.__is_class_function(test):
            self.full_test_name += "." + test.im_class.__name__
        self.test_result = test_result
        self.stacktrace = stacktrace

    def __is_class_function(self, function):
        if 'im_class' in dir(function):
            return True
        return False

    def __str__(self):
        test_result_string = "Test '{}' {}.".format(
                            self.full_test_name, self.test_result)
        if self.stacktrace is not None:
            test_result_string += " Stacktrace:\n {}".format(self.stacktrace)
        return test_result_string
