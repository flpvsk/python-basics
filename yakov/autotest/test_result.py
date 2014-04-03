'''
Created on Mar 27, 2014

@author: Java Student
'''


class TestResult():

    PASSED = 'passed'
    FAILED = 'failed'

    def __init__(self, name, result, stack=''):
        self._name = name
        self._result = result
        self._stack = stack

    def name(self):
        return self._name

    def result(self):
        return self._result

    def stacktrace(self):
        if self._result == self.FAILED:
            return self._stack
        return ''

    def __str__(self):
        return '{0} is {1}\n{2}\n'.format(self._name, self._result, self._stack)
