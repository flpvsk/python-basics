#from assert_message import *
import assert_message
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
                    test = getattr(assert_message, x)
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
    

my_runner = runner()
my_runner.add_test(assert_message.test1)
print my_runner.tests

my_runner.add_test(assert_message.test2)
print my_runner.tests

my_runner.add_test(assert_message.test3)
print my_runner.tests


my_runner.run()
print my_runner.tests

print my_runner.failed_tests()

print my_runner.passed_tests()

