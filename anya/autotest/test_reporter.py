'''
Created on Apr 2, 2014

@author: Java Student

'''
from datetime import datetime
import os


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
