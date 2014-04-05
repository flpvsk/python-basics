from assertions import *

class runner():
    tests = {}
    
    def add_test(self, fn):
        self.tests[fn.__name__] = ["pending", fn]
        
    def pending_tests(self):
        return [x for x in self.tests if self.tests[x][0] == "pending"]
    
    def run(self):
        for x in self.tests:
            if self.tests[x][0] == "pending":
                try:
                    test = self.tests[x][1]
                    test()
                    self.tests[x] = ["passed", test]
                except:
                    self.tests[x] = ["failed", test]


    def ran_tests(self):
        return [x for x in self.tests if (self.tests[x][0] == "passed" or self.tests[x][0] == "failed")]
    
    def passed_tests(self):
        return [x for x in self.tests if self.tests[x][0] == "passed"]
    
    def failed_tests(self):
        return [x for x in self.tests if self.tests[x][0] == "failed"]
    
    def clear_state(self):
        self.tests = {}
    

if __name__ == "__main__":
    my_runner = runner()
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

