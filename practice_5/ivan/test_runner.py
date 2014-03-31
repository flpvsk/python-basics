'''
Created on 26 Mar 2014

@author: paraiva
'''
__all__ = ['TestRunner']


class TestRunner(object):
    def __init__(self):
        self.pending_test_list = []
        self.failed_test_list = []
        self.run_test_list = []
        self.passed_test_list = []

    def add_test(self, fn):
        self.pending_test_list.append(fn)

    def passed_tests(self):
        return self.passed_test_list

    def pending_tests(self):
        return self.pending_test_list

    def ran_tests(self):
        return self.run_test_list

    def failed_tests(self):
        return self.failed_test_list

    def run(self):
        for i in self.pending_test_list:
            try:
                i()
            except AssertionError as er:
                print("An error occurred: " + er)
                self.failed_test_list.append(i)
            finally:
                self.run_test_list.append(i)
                self.pending_test_list.remove(i)
        return (len(self.run_test_list),
                len(self.passed_test_list),
                len(self.failed_test_list))

    def clear_state(self):
        del self.pending_test_list[:]
        del self.run_test_list[:]
        del self.failed_test_list[:]
        del self.passed_test_list[:]
