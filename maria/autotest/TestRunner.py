import traceback
from TestResult import TestResult


class TestRunner(object):

    def __init__(self):
        self.pending_tests_list = []
        self.run_tests_list = []
        self.failed_tests_list = []
        self.passed_tests_list = []
        self.tests_set_up = None
        self.tests_tear_down = None

    def add_test(self, fn):
        self.pending_tests_list.append(fn)

    def pending_tests(self):
        return [t.__name__ for t in self.pending_tests_list]

    def run(self):
        while len(self.pending_tests_list) != 0:
            test = self.pending_tests_list[0]
            test_result = None
            try:
                if self.tests_set_up is not None:
                    self.__run_test_set_up()
                    self.tests_set_up = None
                test()
                if self.tests_tear_down is not None:
                    self.__run_test_tear_down()
                    self.tests_tear_down = None
            except BaseException:
                test_result = TestResult(test, "Failed",
                                         traceback.format_exc())
                self.failed_tests_list.append(test_result)
            else:
                test_result = TestResult(test, "Passed")
                self.passed_tests_list.append(test_result)
            finally:
                self.run_tests_list.append(test_result)
                self.pending_tests_list.remove(test)
        return (len(self.run_tests_list), len(self.passed_tests_list),
                len(self.failed_tests_list))

    def run_tests(self):
        return self.run_tests_list

    def passed_tests(self):
        return self.passed_tests_list

    def failed_tests(self):
        return self.failed_tests_list

    def set_tests_set_up(self, tests_set_up):
        self.tests_set_up = tests_set_up

    def set_tests_tear_down(self, tests_tear_down):
        self.tests_tear_down = tests_tear_down

    def clear_state(self):
        del self.pending_tests_list[:]
        del self.run_tests_list[:]
        del self.failed_tests_list[:]
        del self.passed_tests_list[:]
        self.tests_set_up = None
        self.tests_tear_down = None

    def __run_test_set_up(self):
        try:
            self.tests_set_up()
        except BaseException as e:
            print "Failed to set up tests"
            raise e
        else:
            print "Test environment prepared - '{}' executed".format(
                                            self.tests_set_up.__name__)

    def __run_test_tear_down(self):
        try:
            self.tests_tear_down()
        except BaseException as e:
            print "Failed to tear down tests"
            raise e
        else:
            print "Test environment cleaned - '{}' executed".format(
                                            self.tests_tear_down.__name__)
