''' 
Created on Mar 21, 2014 

@author: arakann 
''' 

import sys
import traceback
from TestResult import TestResult


__all__ = ['TestRunner']


def fn(): 
    print 'another notRun test has been just run' 


class TestRunner():
    
    
    _PASSED = 'Passed'
    _FAILED = 'Failed'
    _NOT_RUN = 'NotRun'
    
    
    def __init__(self):
        self.pending_lst=[] 
        self.run_lst=[] 
        self.failed_lst=[] 
        self.passed_lst=[] 


    def add_test(self,fn): 
        self.pending_lst.append(fn)
         
         
    def pending_tests(self): 
        return self.pending_lst 
    

    def class_run(self, test):
        test_case_instance = TestCase()
        testmethods = [i for i in dir(test_case_instance) if i.startswith('test_')]
        for i in testmethods:
            test = getattr(test_case_instance, i)
            try:
                test_case_instance.set_up()
            except:
                pass
            try:
                test()
                test_result = TestResult(test, TestRunner._PASSED)
                test_result_lst = [test_result._TESTNAME, test_result._TESTRESULT, test_result._STACKTRACE]
                self.passed_lst.append(test_result_lst)
            except:
                test_result = TestResult(test, TestRunner._FAILED, traceback.format_exc())
                test_result_lst = [test_result._TESTNAME, test_result._TESTRESULT,]
                self.failed_lst.append(test_result_lst)
            finally:
                self.run_lst.append(i)
                try:
                    test_case_instance.tear_down()
                except:
                    pass
        return (len(self.run_lst), len(self.passed_lst), len(self.failed_lst))


    def run(self, pending_lst): 
        for test in self.pending_lst: 
            try: 
                test
                self.passed_lst.append(test.__name__) 
            except AssertionError: 
                self.failed_lst.append(test.__name__) 
            finally: 
                self.run_lst.append(test.__name__) 
                self.pending_lst.remove(test) 
        return (len(self.run_lst), len(self.passed_lst), len(self.failed_lst)) 
    
    
    def run_tests(self): 
        return self.run_lst
    
    
    def passed_tests(self): 
        return self.passed_lst
    
    
    def failed_tests(self): 
        return self.failed_lst 

    def clear_state(self):
        self.pending_lst, self.passed_lst, self.failed_lst, self.run_lst = [], [], [], []
        
        
class TestRunnerBase():
    def __init__(self):
        self.pending_lst=[] 
        self.run_lst=[] 
        self.failed_lst=[] 
        self.passed_lst=[] 


    def add_test(self,fn): 
        self.pending_lst.append(fn)
         
         
    def pending_tests(self): 
        return self.pending_lst 


    def class_run(self, test):
        test_case_instance = TestCase()
        testmethods = [i for i in dir(test_case_instance) if i.startswith('test_')]
        for i in testmethods:
            self.report_test_started(i)
            try:
                test_case_instance.set_up()
                getattr(test_case_instance, i)()
            except:
                pass
            try:
                getattr(test_case_instance, i)()
                self.passed_lst.append(i)
                self.tests_dict[i]='Passed'
                self.report_test_passed(i)
            except:
                self.failed_lst.append(i)
                #self.report_test_failed(i)
            finally:
                self.run_lst.append(i)
                try:
                    test_case_instance.tear_down()
                except:
                    pass
        return (len(self.run_lst), len(self.passed_lst), len(self.failed_lst))
        #self.report_all_finished(run, passed, failed)

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
        return self.passed_lst
    
    
    def failed_tests(self): 
        return self.failed_lst 

    def clear_state(self):
        self.pending_lst, self.passed_lst, self.failed_lst, self.run_lst = [], [], [], []


class TestCase():


    def __init__(self):
        print "Initializing..."


    def set_up(self):
        print "set_UP"


    def test_2(self):
        print "Test2"


    def test_1(self):
        print "Test1"
    
    

class TestRunnerVerboseReporting(TestRunnerBase):
    
    
    def report_test_started(self, test):
        print 'Starting'
    '''
    def report_test_finished(self):
        pass
    '''
    def report_test_passed(self,test):
        print test
    def report_test_failed(self,test,stack):
        print 'Failed'
    def report_all_finished(self):
        pass
    
class TestRunnerFailReporting(TestRunnerBase):
    
    
    def report_test_started(self,test):
        pass
    def report_test_passed(self,test):
        print '.'
    def report_test_failed(self,test,stack):
        print 'Failed'
    '''
    def report_test_finished(self):
        pass
    '''
    #def report_all_finished(self, run, passed, failed):
        #return (run, passed, failed)
    

testrunner=TestRunner()



print testrunner.pending_tests() 
print testrunner.class_run(TestCase)
print testrunner.passed_tests() 

'''
print testrunner.run(testrunner.pending_tests()) 

print testrunner.failed_tests() 
print testrunner.passed_tests()
'''
