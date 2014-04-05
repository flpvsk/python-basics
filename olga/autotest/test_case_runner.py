from examples_5.todo_tests import *

class runner():
    tests = {}
    PENDING = "pending"
    FAILED = "failed"
    PASSED = "passed"
    set_up = None
    tear_down = None
    
    def __init__(self):
        test_case = TodoTestCase()
        self.tests = {m: [self.PENDING, getattr(test_case, m)] for m in dir(test_case) if m.startswith("test_")}
        for m in dir(test_case):
            if  m == "set_up":
                self.set_up = getattr(test_case, m)
            elif m == "tear_down":
                self.tear_down = getattr(test_case, m)
                
    def add_test(self, fn):
        self.tests  [fn.__name__] = self.PENDING, fn
        
    def pending_tests(self):
        return [x for x in self.tests if self.tests[x][0] == self.PENDING]
    
    def run(self):
        for x in self.tests:
            if self.tests[x][0] == self.PENDING:
                test = self.tests[x][1]
                try:
                    self.set_up()
                    test()
                    self.tear_down()
                    self.tests[x] = self.PASSED, test
                except:
                    self.tests[x] = self.FAILED, test


    def ran_tests(self):
        return [x for x in self.tests if (self.tests[x][0] == self.PASSED or self.tests[x][0] == self.FAILED)]
    
    def passed_tests(self):
        return [x for x in self.tests if self.tests[x][0] == self.PASSED]
    
    def failed_tests(self):
        return [x for x in self.tests if self.tests[x][0] == self.FAILED]
    
    def clear_state(self):
        self.tests = {}
    

if __name__ == "__main__":
    my_runner = runner()
    my_runner.run()
    print("ran tests {0}".format(my_runner.ran_tests()))
    print("failed tests {0}".format(my_runner.failed_tests()))
    print("passed tests {0}".format(my_runner.passed_tests()))
    print("pending tests {0}".format(my_runner.pending_tests()))
    
    
'''
    my_runner.add_test(test_assert_equal)
    print my_runner.tests
    
    my_runner.add_test(test_assert_is_none)
    print my_runner.tests
    
    my_runner.add_test(test_assert_not_equal)
    print my_runner.tests
    
    my_runner.run()
    print my_runner.tests
    print my_runner.failed_tests()
    print my_runner.passed_tests()
'''