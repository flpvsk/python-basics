from maria.autotest import TestRunner
from practice_4.maria.test_runner_tests import test_1

test_runner = TestRunner()
test_runner.add_test(test_1)
test_runner.run()
print test_runner.pending_tests()
print test_runner.passed_tests()
print test_runner.failed_tests()
