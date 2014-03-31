'''
Created on Mar 27, 2014

@author: Java Student
'''


class TestResult():

    def __init__(self, name, result, stack=''):
        self.res = ['passed', 'failed']
        self._name = name
        self._result = result
        self._stack = stack

    def name(self):
        return self._name

    def result(self):
        return self._result

    def stacktrace(self):
        if self._result == self.res[1]:
            return self._stack
        return ''

    def __str__(self):
        print self._name
