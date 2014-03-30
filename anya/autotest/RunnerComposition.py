'''
Created on Mar 27, 2014

@author: Java Student
tasks:#79, 82
'''

from anya.autotest.TestResult import TestResult
from anya.autotest.runner import TestCase
import traceback
from datetime import datetime
import os

class TestRunner():
    
    
    _PASSED = 'Passed'
    _FAILED = 'Failed'
    _NOT_RUN = 'NotRun'
    
    
    def __init__(self, reporter):
        self.pending_lst=[] 
        self.run_lst=[] 
        self.failed_lst=[] 
        self.passed_lst=[] 
        self.reporter = reporter


    def add_test(self,fn): 
        self.pending_lst.append(fn)
         
         
    def pending_tests(self): 
        return self.pending_lst 
    

    def class_run(self, test):
        test_case_instance = TestCase()
        testmethods = [i for i in dir(test_case_instance) if i.startswith('test_')]
        for i in testmethods:
            try:
                self.reporter.report_test_started(i)
            except:
                pass
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
                try:
                    self.reporter.report_test_passed(i)
                except:
                    pass
            except:
                test_result = TestResult(test, TestRunner._FAILED, traceback.format_exc())
                test_result_lst = [test_result._TESTNAME, test_result._TESTRESULT,]
                self.failed_lst.append(test_result_lst)
                try:
                    self.reporter.report_test_failed(i)
                except:
                    pass
            finally:
                self.run_lst.append(i)
                try:
                    test_case_instance.tear_down()
                except:
                    pass
        self.reporter.report_all_finished(len(self.run_lst), len(self.passed_lst), len(self.failed_lst))
        #return (len(self.run_lst), len(self.passed_lst), len(self.failed_lst))


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
        
        
        
class TextFileReporter():
    def __init__(self):
        
        isodatetime = str(datetime.now()).replace(":", "_")
        report_name = isodatetime + '-tests-results.txt'
        report_dir = 'C:\\test-results'
        absolute_report = os.path.join(report_dir, report_name)
        self.report = open(absolute_report, 'w') 
    
    def report_test_started(self, test):
        self.report.write('Starting')
    '''
    def report_test_finished(self):
        pass
    '''
    def report_test_passed(self,test):
        self.report.write(test)
    def report_test_failed(self,test,stack):
        self.report.write('Failed')
    def report_all_finished(self, *args):
        self.report.close()

testrunner=TestRunner(TextFileReporter())
testrunner.class_run(TestCase)
