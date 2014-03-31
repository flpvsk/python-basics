import argparse
from test_runner_launcher import TestRunnerLauncher

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('module_name', help='Name of the module with tests')
    parser.add_argument('test_container', help='Type of test container',
                        choices=[TestRunnerLauncher.TEST_FUNCTIONS_CONTAINER,
                                 TestRunnerLauncher.CLASS_TEST_CONTAINER])
    parser.add_argument('-reporter', help='Type of test reporter',
                        choices=[TestRunnerLauncher.FAIL_REPORTER,
                                 TestRunnerLauncher.VERBOSE_REPORTER,
                                 TestRunnerLauncher.TEXT_FILE_REPORTER],
                        default=TestRunnerLauncher.FAIL_REPORTER)
    args = parser.parse_args()
    launcher = TestRunnerLauncher(args.module_name,
                                args.test_container, args.reporter)
    launcher.execute_tests()
