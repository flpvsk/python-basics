import sys
from TestRunnerLauncher import TestRunnerLauncher

if __name__ == '__main__':
    module_name = sys.argv[1]
    test_container_type = sys.argv[2]
    test_runner_launcher = TestRunnerLauncher(module_name, test_container_type)
    test_runner_launcher.execute_tests()
