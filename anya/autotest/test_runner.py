'''
Created on Mar 27, 2014

@author: Java Student
'''




import traceback
from test_reporter import TextFileReporter, FailReporter, VerboseReporter



class TestCase():


    def __init__(self):
        print "Initializing test..."


    def set_up(self):
        print "default set_UP"


    def tear_down(self):
        print "default tear_Down"


    #@with_set_up(my_set_up)
    def test_2(self):
        raise Exception

    #@with_tear_down(my_tear_down)
    def test_1(self):
        print "running Test1"




class TestResult():
    def __init__(self, test, test_result, stacktrace = ''):
        if test.im_class == 'TestCase':
            self.test_name = test.__module__ + '.' + test.im_class.__name__ + '.' + test.__name__
        else:
            self.test_name = test.__module__ + '.'+ test.__name__
        self.test_name = test.__module__ +'.' + test.__name__
        self.test_result = test_result
        self.stack_trace = stacktrace




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
                self.test_result_lst.append(test_result)
                self.reporter.report_test_finished(test, TestRunner._PASSED, test_result)
                tear_down()
            except:
                test_result = TestResult(test, TestRunner._FAILED, traceback.format_exc())
                self.test_result_lst.append(test_result)
                self.reporter.report_test_finished(test, TestRunner._FAILED, test_result)             
            finally:
                self.run_lst.append(i)                    
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




#reporter=VerboseReporter
#runner=TestRunner(reporter)
#runner.class_run(TestCase)

testrunner=TestRunner(TextFileReporter())
testrunner.class_run(TestCase)