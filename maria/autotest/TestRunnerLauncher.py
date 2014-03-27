import importlib
import sys
from TestRunnerVerboseReporting import TestRunnerVerboseReporting
from TestRunnerFailReporting import TestRunnerFailReporting
from FailReporter import FailReporter
from VerboseReporter import VerboseReporter
from TestRunnerReporter import TestRunnerReporter
from utils import noop


class TestRunnerLauncher(object):
    TEST_METHOD_PREFIX = "test_"
    SET_UP_METHOD_NAME = "set_up"
    TEAR_DOWN_METHOD_NAME = "tear_down"
    TEST_FUNCTIONS_CONTAINER_TYPE_NAME = "module_functions"
    CLASS_TEST_CONTAINER_TYPE_NAME = "class"
    VERBOSE_REPORTING_TYPE_NAME = "verbose"
    FAIL_REPORTING_TYPE_NAME = "fail"
    VERBOSE_REPORTER_TYPE_NAME = "verbose_reporter"
    FAIL_REPORTER_TYPE_NAME = "fail_reporter"

    test_runners_dict = {VERBOSE_REPORTING_TYPE_NAME:
                        TestRunnerVerboseReporting,
                        FAIL_REPORTING_TYPE_NAME:
                        TestRunnerFailReporting,
                        VERBOSE_REPORTER_TYPE_NAME:
                        VerboseReporter,
                        FAIL_REPORTER_TYPE_NAME:
                        FailReporter}

    def __init__(self, test_module_name, test_container_type,
                 test_reporting_name=FAIL_REPORTING_TYPE_NAME):
        '''Specifies test runner launcher

        :param test_module_name: name of module with tests
        :param test_container_type: test container type (class or functions)
        :param test_reporting_name: optional, reporting type (4 are available)
        '''
        self.test_module = importlib.import_module(test_module_name)
        self.test_container_type = test_container_type
        if test_reporting_name == self.VERBOSE_REPORTER_TYPE_NAME or \
               test_reporting_name == self.FAIL_REPORTER_TYPE_NAME:
            self.test_runner = TestRunnerReporter(
                            self.test_runners_dict[test_reporting_name]())
        else:
            self.test_runner = self.test_runners_dict[test_reporting_name]()
        self.test_extractors_dict = \
                {self.TEST_FUNCTIONS_CONTAINER_TYPE_NAME:
                 self.__extract_tests_from_module_functions,
                 self.CLASS_TEST_CONTAINER_TYPE_NAME:
                 self.__extract_tests_from_classes}

    def execute_tests(self):
        test_lists_info = self.test_extractors_dict[self.test_container_type]()
        self.test_runner.clear_state()
        for test_list_info in test_lists_info:
            self.test_runner.set_tests_set_up(test_list_info.set_up_method)
            self.test_runner.set_tests_tear_down(test_list_info.
                                                 tear_down_method)
            [self.test_runner.add_test(test) for test in
                                             test_list_info.test_list]
            self.test_runner.run()
        if len(self.test_runner.failed_tests()) != 0:
            sys.exit(1)
        else:
            sys.exit(0)

    def __extract_tests_from_module_functions(self):
        tests = [getattr(self.test_module, f) for f
                in dir(self.test_module) if f in self.test_module.__all__]
        return TestListInfoContainer(tests, noop, noop)

    def __extract_tests_from_classes(self):
        test_classes = [getattr(self.test_module, f)() for f
                         in dir(self.test_module)
                         if f in self.test_module.__all__]
        return [self.__get_test_lists_info(test_class) for
                test_class in test_classes]

    def __get_test_lists_info(self, test_class):
        set_up_method = noop
        tear_down_method = noop
        tests = []
        for method_name in dir(test_class):
            if method_name.startswith(self.TEST_METHOD_PREFIX):
                tests.append(getattr(test_class, method_name))
            if method_name == self.SET_UP_METHOD_NAME:
                set_up_method = getattr(test_class, method_name)
            if method_name == self.TEAR_DOWN_METHOD_NAME:
                tear_down_method = getattr(test_class, method_name)
        return TestListInfoContainer(tests, set_up_method, tear_down_method)


class TestListInfoContainer(object):

    def __init__(self, test_list, set_up_method, tear_down_method):
        self.test_list = test_list
        self.set_up_method = set_up_method
        self.tear_down_method = tear_down_method
