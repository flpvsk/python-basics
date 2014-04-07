'''
Created on Mar 27, 2014

@author: Java Student
'''


class TestResult():

    PASSED = 'passed'
    FAILED = 'failed'

    def __init__(self, test, result, stack=''):
        self._test = test
        self._fullname = test.__module__ + '::' + test.im_class.__name__
        self._result = result
        self._stack = stack

    def test_name(self):
        return self._fullname + '::' + self._test.__name__

    def result(self):
        return self._result

    def stacktrace(self):
        if self._result == self.FAILED:
            return self._stack
        return ''

    def __str__(self):
        return '{0} is {1}\n{2}\n'.format(self.test_name(), self._result, self._stack)
