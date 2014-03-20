class TestRunner(object):
    
    def __init__(self):
        self.pending_tests_list = []
        self.run_tests_list = []
        self.failed_tests_list = []
        self.passed_tests_list = []

    def add_test(self, fn):
        self.pending_tests_list.append(fn)

    def pending_tests(self):
        return [t.__name__ for t in self.pending_tests_list]

    def run(self):
        for test in self.pending_tests_list:
            try:
                test()
            except BaseException as e:
                print("Test {} failed - Exception caught: {}".format(test.__name__,
                                                                      e.message))
                self.failed_tests_list.append(test)
            else:
                self.passed_tests_list.append(test)
            finally:
                self.run_tests_list.append(test)
                self.pending_tests_list.remove(test)
        return (len(self.run_tests_list), len(self.passed_tests_list),
                len(self.failed_tests_list))

    def run_tests(self):
        return [t.__name__ for t in self.run_tests_list]

    def passed_tests(self):
        return [t.__name__ for t in self.passed_tests_list]

    def failed_tests(self):
        return [t.__name__ for t in self.failed_tests_list]

    def clear_state(self):
        del self.pending_tests_list[:]
        del self.selfrun_tests_list[:]
        del self.failed_tests_list[:]
        del self.passed_tests_list[:]
