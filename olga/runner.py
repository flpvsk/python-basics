#from assertions import test_assert_equal, test_assert_not_equal, test_assert_is_none
import assertions
class runner():
    tests = {}
    
    def add_test(self, fn):
        self.tests[fn.__name__] = "pending"
        
    def pending_tests(self):
        return [x for x in self.tests if self.tests[x] == "pending"]
    
    def run(self):
        for x in self.tests:
            if self.tests[x] == "pending":
                try:
                    test = getattr(assertions, x)
                    test()
                    self.tests[x] = "passed"
                except:
                    self.tests[x] = "failed"
            
    
    def ran_tests(self):
        return [x for x in self.tests if (self.tests[x] == "passed" or self.tests[x] == "failed")]
    
    def passed_tests(self):
        return [x for x in self.tests if self.tests[x] == "passed"]
    
    def failed_tests(self):
        return [x for x in self.tests if self.tests[x] == "failed"]
    
    def clear_state(self):
        self.tests = {}
    

if __name__ == "__main__":
    my_runner = runner()
    my_runner.add_test(assertions.test_assert_equal)
    print my_runner.tests
    
    my_runner.add_test(assertions.test_assert_is_none)
    print my_runner.tests
    
    my_runner.add_test(assertions.test_assert_not_equal)
    print my_runner.tests
    
    my_runner.run()
    print my_runner.tests
    print my_runner.failed_tests()
    print my_runner.passed_tests()

