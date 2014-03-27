''' Launches TestRunner

Extracts all tests from specified source and launch testRunner for them
'''

import importlib
import sys
from TestRunner import TestRunner


class TestRunnerLauncher(object):
    TEST_METHOD_PREFIX = "test_"
    SET_UP_METHOD_NAME = "set_up"
    TEAR_DOWN_METHOD_NAME = "tear_down"
    TEST_FUNCTIONS_CONTAINER_TYPE_NAME = "module_functions"
    CLASS_TEST_CONTAINER_TYPE_NAME = "class"

    def __init__(self, test_module_name, test_container_type):
        '''Specifies test runner launcher

        :param test_module_name: name of module with tests
        :param test_container_type: test container type (class or functions)
        '''
        self.test_module = importlib.import_module(test_module_name)
        self.test_container_type = test_container_type
        self.test_extractors_dict = \
                {self.TEST_FUNCTIONS_CONTAINER_TYPE_NAME:
                 self.__extract_tests_from_module_functions,
                 self.CLASS_TEST_CONTAINER_TYPE_NAME:
                 self.__extract_tests_from_classes}

    def execute_tests(self):
        '''Runs test runner for specified tests'''
        all_tests = self.test_extractors_dict[self.test_container_type]()
        for tests in all_tests:
            testRunner = TestRunner()
            testRunner.clear_state()
            testRunner.set_tests_set_up(tests[1])
            testRunner.set_tests_tear_down(tests[2])
            [testRunner.add_test(test) for test in tests[0]]
            testRunner.run()
            for test_run_result in testRunner.run_tests():
                print test_run_result
            if len(testRunner.failed_tests()) != 0:
                sys.exit(1)
            else:
                sys.exit(0)

    def __extract_tests_from_module_functions(self):
        '''Returns tuple with tests.

        Tuple consists of 3 pointers:
        to list of test functions, to setup function and to teardown function.
        As there is no setup and teardown functions for module test functions,
        None is returned
        '''
        return [([getattr(self.test_module, f) for f in dir(self.test_module)
                 if f in self.test_module.__all__], None, None)]

    def __extract_tests_from_classes(self):
        '''Returns list of tuples with tests from classes.

        Each tuple consists of 3 pointers:
        to list of class test functions, to setup function and to
        teardown function.
        '''
        test_classes = [getattr(self.test_module, f)() for f
                         in dir(self.test_module)
                         if f in self.test_module.__all__]
        return [self.__get_tests(test_class) for test_class in test_classes]

    def __get_tests(self, test_class):
        '''Returns tuple with tests from class.

        Tuple consists of 3 pointers:
        to list of class test functions, to setup function and to
        teardown function.
        '''
        set_up_method = None
        tear_down_method = None
        tests = []
        for method_name in dir(test_class):
            if method_name == self.SET_UP_METHOD_NAME:
                set_up_method = getattr(test_class, method_name)
            if method_name == self.TEAR_DOWN_METHOD_NAME:
                tear_down_method = getattr(test_class, method_name)
            if method_name.startswith(self.TEST_METHOD_PREFIX):
                tests.append(getattr(test_class, method_name))
        return (tests, set_up_method, tear_down_method)
