''' 
Created on Mar 21, 2014 

@author: arakann 
''' 

import sys 


__all__=["add_test", "pending_tests", "run", "run_tests", "passed_tests", \
         "failed_tests", "fn"]
tests_dict = {'test1': 'Passed', 'test3': 'Failed'} 
pending_lst=[] 
run_lst=[] 
failed_lst=[] 
passed_lst=[] 

def add_test(fn): 
    tests_dict[fn.__name__]='NotRun' 
     
     
def fn(): 
    print 'another notRun test has been just run' 


def pending_tests(): 
    pending_lst=[key for key in tests_dict.keys() if tests_dict.get(key) == 'NotRun'] 
    return pending_lst 

def run(pending_lst): 
    for test in pending_lst: 
        try: 
            getattr(sys.modules[__name__], test)() 
            passed_lst.append(test) 
            tests_dict[test]='Passed' 
        except AssertionError: 
            failed_lst.append(test) 
            tests_dict[test]='Failed' 
        finally: 
            run_lst.append(test) 
            pending_lst.remove(test) 
    return (len(run_lst), len(passed_lst), len(failed_lst)) 


def run_tests(): 
    return [key for key in tests_dict.keys() if tests_dict.get(key) == 'Passed' or tests_dict.get(key) == 'Failed'] 


def passed_tests(): 
    return [key for key in tests_dict.keys() if tests_dict.get(key) == 'Passed'] 


def failed_tests(): 
    return [key for key in tests_dict.keys() if tests_dict.get(key) == 'Failed'] 

def clear_state():
    pending, passed, failed, ran = [], [], [], []
    
    
test1=fn 
test2=fn 

print add_test(test1) 
print pending_tests() 
print run(pending_tests()) 
print run_tests() 
print failed_tests() 
print passed_tests()