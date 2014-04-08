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
        self.test_result_lst=[] 
        self.reporter = reporter


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
                self.reporter.report_test_started(test, test.__name__)
                test()
                test_result = TestResult(test, TestRunner._PASSED,)
                #test_result_lst = [test_result.test_name, test_result.test_result, test_result.stack_trace]
                #self.test_result_lst.append([test_result.test_name, test_result.test_result, test_result.stack_trace])
                self.test_result_lst.append(test_result)
                self.reporter.report_test_finished(test, TestRunner._PASSED, test_result)
#                self.reporter.report_test_passed(i)
            except:
                test_result = TestResult(test, TestRunner._FAILED, traceback.format_exc())
                self.test_result_lst.append(test_result)
                self.reporter.report_test_finished(test, TestRunner._FAILED, test_result)
#                self.reporter.report_test_failed(i)                
            finally:
                self.run_lst.append(i)
                try:
                    tear_down()
                except:
                    test_result = TestResult(test, TestRunner._FAILED, traceback.format_exc())
                    self.test_result_lst.append(test_result)
                    self.reporter.report_test_finished(test, TestRunner._FAILED, test_result)
                    
                    
        run_tests=len(self.run_tests())
        passed_tests=len(self.passed_tests())
        failed_tests=len(self.failed_tests())
        self.reporter.report_all_finished(test, run_tests, passed_tests, failed_tests)




    def run_tests(self): 
        return self.run_lst


    def passed_tests(self): 
        return [test_result.test_name
            for test_result in self.test_result_lst
            if test_result.test_result == TestRunner._PASSED]
    
    
    def failed_tests(self): 
        return [test_result.test_name
            for test_result in self.test_result_lst
            if test_result.test_result == TestRunner._FAILED]


    def clear_state(self):
        self.pending_lst, self.passed_lst, self.failed_lst, self.run_lst = [], [], [], []
        
        
        
class TextFileReporter():
    def __init__(self):
        
        isodatetime = str(datetime.now()).replace(":", "_")
        report_name = isodatetime + '-tests-results.txt'
        report_dir = 'C:\\test-results'
        absolute_report = os.path.join(report_dir, report_name)
        self.report = open(absolute_report, 'w') 
    
    def report_test_started(self,test, *test_name):
        self.report.write("{} is running now".format(test_name))
        
        
    def report_test_finished(self, test, status, test_result):
        self.report.write("{},{},{}".format(test_result.test_name, status, test_result.stack_trace))
        
        
    def report_all_finished(self, test, run_tests, passed_tests, failed_tests):
        self.report.write("Run tests: {}, Passed Tests: {}, Failed Tests: {}".format(run_tests, passed_tests, failed_tests))
        self.report.close()



class VerboseReporter():
    
    
    def report_test_started(self, test, *test_name):
        print ("{} is running now".format(test_name))
        #print("{} is running now".format(test_name))
    def report_test_finished(self, test, status, test_result):
        print (test_result.test_name, status, test_result.stack_trace)
    def report_all_finished(self, test, run_tests, passed_tests, failed_tests):
        print ("Run tests: {}, Passed Tests: {}, Failed Tests: {}".format(run_tests, passed_tests, failed_tests))




class FailReporter():
    
    
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


#reporter=VerboseReporter
#runner=TestRunner(reporter)
#runner.class_run(TestCase)

testrunner=TestRunner(TextFileReporter())
testrunner.class_run(TestCase)
