'''
Created on 26 Mar 2014

@author: paraiva
'''

from practice_5.ivan.test_runner import TestRunner
from practice_5.ivan.test_list import test

test_runner = TestRunner()
test_runner.add_test(test)
test_runner.run()
print test_runner.pending_tests()
print test_runner.passed_tests()
print test_runner.failed_tests()
