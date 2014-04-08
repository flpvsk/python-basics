'''
Created on 30th of March 2014.

@author: ROO
task:#67
'''

import sys
import traceback
from TestResult import TestResult
from runner import TestCase as TestCase




class TestRunnerBase():
    
    
    _PASSED = 'Passed'
    _FAILED = 'Failed'
    _NOT_RUN = 'NotRun'
    
    
    def __init__(self):
        self.pending_lst=[] 
        self.run_lst=[] 
        self.test_result_lst=[]


    def add_test(self,fn): 
        self.pending_lst.append(fn)
         
         
    def pending_tests(self): 
        return self.pending_lst 

    def class_run(self, test):
            test_case_instance = TestCase()
            testmethods = [i for i in dir(test_case_instance) if i.startswith('test_')]
            noop = lambda : None
            set_up = getattr(test_case_instance, 'set_up', noop)
            tear_down = getattr(test_case_instance,'tear_down',noop)
            for i in testmethods:
                test = getattr(test_case_instance, i)
                try:
                    set_up()
                    self.report_test_started(test, test.__name__)
                    test()
                    test_result = TestResult(test, TestRunnerBase._PASSED,)
                    #test_result_lst = [test_result.test_name, test_result.test_result, test_result.stack_trace]
                    #self.test_result_lst.append([test_result.test_name, test_result.test_result, test_result.stack_trace])
                    self.test_result_lst.append(test_result)
                    self.report_test_finished(test, TestRunnerBase._PASSED, test_result)
                    tear_down()
                except:
                    pass
                    test_result = TestResult(test, TestRunnerBase._FAILED, traceback.format_exc())
                    #test_result_lst = test_result_lst.append(test_result)
                    #test_result_lst = [test_result.test_name, test_result.test_result, test_result.stack_trace]
                    self.test_result_lst.append(test_result)
                    
                    self.report_test_finished(test, TestRunnerBase._FAILED, test_result)
                finally:
                    print self.test_result_lst
                    self.run_lst.append(i)
                    #passed_tests=self.passed_tests()
                    #failed_tests=self.failed_tests()
            run_tests=len(self.run_tests())
            passed_tests=len(self.passed_tests())
            failed_tests=len(self.failed_tests())
            self.report_all_finished(test, run_tests, passed_tests, failed_tests)    


    
    def run(self, pending_lst): 
        for test in self.pending_lst: 
            try: 
                getattr(sys.modules[__name__], test)() 
                self.passed_lst.append(test) 
                self.tests_dict[test]='Passed' 
            except AssertionError: 
                self.failed_lst.append(test) 
                self.tests_dict[test]='Failed' 
            finally: 
                self.run_lst.append(test) 
                self.pending_lst.remove(test) 
        return (len(self.run_lst), len(self.passed_lst), len(self.failed_lst)) 

    def run_tests(self): 
        return self.run_lst
    
    
    def passed_tests(self): 
        return [test_result.test_name
            for test_result in self.test_result_lst
            if test_result.test_result == TestRunnerBase._PASSED]
    
    
    def failed_tests(self): 
        return [test_result.test_name
            for test_result in self.test_result_lst
            if test_result.test_result == TestRunnerBase._FAILED]

    def clear_state(self):
        self.pending_lst, self.passed_lst, self.failed_lst, self.run_lst = [], [], [], []
        
        
class TestRunnerVerboseReporting(TestRunnerBase):
    
    
    def report_test_started(self, test, *test_name):
        print("{} is running now".format(test_name))
    def report_test_finished(self, test, status, test_result ):
        print (test_result.test_name, status, test_result.stack_trace)
    def report_all_finished(self, test, run_tests, passed_tests, failed_tests):
        print ("Run tests: {}, Passed Tests: {}, Failed Tests: {}".format(run_tests, passed_tests, failed_tests))




class TestRunnerFailReporting(TestRunnerBase):
    
    
    def report_test_started(self,test, *test_name):
        print 'Nothing is printed before test running'
    def report_test_finished(self, test, status, test_result):
        if status == 'Passed':
            print '.'
        else:
            print (status, test_result.stack_trace)
            
    def report_all_finished(self, test, ):
        failed_tests=self.failed_tests()
        print len(failed_tests)



'''CodevChecks'''
   

#testrunner=TestRunnerFailReporting()
testrunner=TestRunnerVerboseReporting()
#print testrunner.pending_tests() 
testrunner.class_run(TestCase)
#print testrunner.passed_tests()