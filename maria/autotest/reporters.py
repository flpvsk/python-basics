import os
from datetime import datetime


class FailReporter(object):

    def report_test_started(self, test):
        pass

    def report_test_finished(self, test_result):
        if test_result.test_result_status == TestResult.PASSED_TEST_RESULT:
            print "."
        else:
            print test_result

    def report_all_finished(self, run_tests_list, passed_tests_list,
                            failed_tests_list):
        print "Count of run tests: {}".format(len(run_tests_list))
        print "Count of passed tests: {}".format(
                                            len(passed_tests_list))
        print "Count of failed tests: {}".format(
                                            len(failed_tests_list))


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


class TextFileReporter(object):
    BASE_DIR = os.path.join("C:\\CVS", "test-results")

    def __init__(self):
        self.file_name = None

    def report_test_started(self, test):
        if not self.file_name:
            self.__create_text_file()
        with open(self.file_name, 'a') as f:
            f.write("Test '{}' has been started\n".format(get_full_name(test)))

    def report_test_finished(self, test_result):
        with open(self.file_name, 'a') as f:
            f.write(test_result.__str__() + "\n")

    def report_all_finished(self, run_tests_list, passed_tests_list,
                            failed_tests_list):
        with open(self.file_name, 'a') as f:
            f.write("Count of run tests: {}\n".format(len(run_tests_list)))
            f.write("Count of passed tests: {}\n".format(
                                            len(passed_tests_list)))
            f.write("Count of failed tests: {}\n".format(
                                            len(failed_tests_list)))

    def __create_text_file(self):
        if not os.path.exists(self.BASE_DIR):
            os.makedirs(self.BASE_DIR)
        isodatetime = datetime.now().isoformat().replace(':', '.')
        self.file_name = os.path.join(self.BASE_DIR,
                                      isodatetime + "-tests-results.txt")


class TestResult(object):
    FAILED_TEST_RESULT = "Failed"
    PASSED_TEST_RESULT = "Pass"

    def __init__(self, test, test_result_status, stacktrace=None):
        self.full_test_name = get_full_name(test)
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


def get_full_name(method):
    full_name = method.__module__
    try:
        full_name += "." + method.im_class.__name__
    except AttributeError:
        pass
    full_name += "." + method.__name__

    return full_name
