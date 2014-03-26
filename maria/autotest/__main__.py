import sys
from TestRunnerLauncher import TestRunnerLauncher

if __name__ == '__main__':
    if(len(sys.argv) < 3):
        error_message = "3 arguments should be specified: test module name and\
type of tests - required and test reporting type - optional. If you want to \
launch tests from module functions - enter '{}', if from classes - enter '{}'.\
 If you want to use Verbose reporting - enter '{}', if failed test reporting- \
'{}', verbose reporter- '{}', fail reporter - '{}'. E.g.- 'my.test.module \
{} {}'"\
        .format(TestRunnerLauncher.TEST_FUNCTIONS_CONTAINER_TYPE_NAME,
               TestRunnerLauncher.CLASS_TEST_CONTAINER_TYPE_NAME,
               TestRunnerLauncher.VERBOSE_REPORTING_TYPE_NAME,
               TestRunnerLauncher.FAIL_REPORTING_TYPE_NAME,
               TestRunnerLauncher.VERBOSE_REPORTER_TYPE_NAME,
               TestRunnerLauncher.FAIL_REPORTER_TYPE_NAME,
               TestRunnerLauncher.CLASS_TEST_CONTAINER_TYPE_NAME,
               TestRunnerLauncher.VERBOSE_REPORTING_TYPE_NAME)
        raise ValueError(error_message)
    module_name = sys.argv[1]
    test_container_type = sys.argv[2]
    if len(sys.argv) >= 4:
        test_runner_launcher = TestRunnerLauncher(module_name,
                                test_container_type, sys.argv[3])
    else:
        test_runner_launcher = TestRunnerLauncher(module_name,
                                             test_container_type)
    test_runner_launcher.execute_tests()
