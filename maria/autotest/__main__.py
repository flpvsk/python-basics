import sys
import importlib
from TestRunner import TestRunner

if __name__ == '__main__':
    package_name = sys.argv[1]
    module = importlib.import_module(package_name)
    test_functions = [f for f in dir(module) if f in module.__all__]
    testRunner = TestRunner()
    for func in test_functions:
        testRunner.clear_state()
        testRunner.add_test(getattr(module, func))
        testRunner.run()
        if len(testRunner.failed_tests()) != 0:
            sys.exit(1)
        else:
            sys.exit(0)
