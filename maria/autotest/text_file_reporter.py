import os
from datetime import datetime


class TextFileReporter(object):
    BASE_DIR = os.path.join("C:\\", "test-results")

    def __init__(self):
        self.file_name = None

    def report_test_started(self, test):
        if not self.file_name:
            self.__create_text_file()
        with open(self.file_name, 'a') as f:
            f.write("Test '{}' has been started\n".format(test.__name__))

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
