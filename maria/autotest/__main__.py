import sys
from TestRunnerLauncher import TestRunnerLauncher

if __name__ == '__main__':
    if(len(sys.argv) != 3):
        error_message = "2 arguments are required: test module name and \
type of tests. If you want to launch tests from module functions - enter '{}',\
if from classes - enter '{}'. E.g.- 'my.test.module {}'"\
        .format(TestRunnerLauncher.TEST_FUNCTIONS_CONTAINER_TYPE_NAME,
               TestRunnerLauncher.CLASS_TEST_CONTAINER_TYPE_NAME,
               TestRunnerLauncher.CLASS_TEST_CONTAINER_TYPE_NAME)
        raise ValueError(error_message)
    module_name = sys.argv[1]
    test_container_type = sys.argv[2]
    test_runner_launcher = TestRunnerLauncher(module_name, test_container_type)
    test_runner_launcher.execute_tests()
