import importlib
from TestRunner import TestRunner

class TestRunnerLauncher(object):
    
    TEST_METHOD_PREFIX = "test_"
    SET_UP_METHOD_NAME = "set_up"
    TEAR_DOWN_METHOD_NAME = "tear_down"
    
    test_extractors_dict = {"module_functions" : __extract_tests_from_module_functions, 
                            "class": __extract_tests_from_class}    
    
    def __init__(self, test_module_name, test_container_type):
        self.test_module = importlib.import_module(test_module_name)
        self.test_container_type = test_container_type
        
    def execute_tests(self):
        test_containers = [f for f in dir(test_module) if f in test_module.__all__]
        testRunner = TestRunner()
        for func in test_functions:
            testRunner.clear_state()
            testRunner.add_test(getattr(module, func))
            testRunner.run()
            if len(testRunner.failed_tests()) != 0:
                sys.exit(1)
            else:
                sys.exit(0)
            print test_classes
            
    def __extract_tests_from_module_functions(self):
        return [getattr(self.test_module, f) for f in dir(self.test_module) if f in self.test_module.__all__]
        
    def __extract_tests_from_class(self):
        return [getattr(self.test_module, f)() for f in dir(self.test_module) if self.__method_is_test(f)]
    
    def __method_is_test(self, method_name):
        if method_name in self.test_module.__all__  and \
            (method_name.startswith(self.TEST_METHOD_PREFIX) or method_name == self.SET_UP_METHOD_NAME or method_name == self.TEAR_DOWN_METHOD_NAME):
            return True
        return False
    
            

  
test_runner_launcher = TestRunnerLauncher("examples_5.todo_tests")  
test_runner_launcher.execute_tests()