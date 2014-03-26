'''
Created on Mar 13, 2014

@author: Java Student
'''
__all__ = ('add_test', 'pending_test', 'run', 'run_tests', 'passed_tests', 'failed_tests', 'clear_state')


global pending_test_list
pending_test_list = []
failed_test_list = []
run_test_list = []
passed_test_list = []

def add_test(fn, *args):
    pending_test_list.append((fn, args))
        
def pending_test(pending_test_list):
        return pending_test_list
        
def run(pending_test_list):
    for i in pending_test_list:
        try:
            i[0](*i[1])
        except AssertionError as er:
            print("An error occurred: " + er)
            failed_test_list.append(i)
        finally:
            run_test_list.append(i)
            pending_test_list.remove(i)
    return (len(run_test_list), len(passed_test_list), len(failed_test_list))
    
    
def run_tests():
    for i in run_test_list:
        return i
    
def passed_tests():
    for i in passed_test_list:
        return i
    
def failed_tests():
    for i in failed_test_list:
        return i
    
def clear_state():
    pending_test_list = []
    failed_test_list = []
    run_test_list = []
    passed_test_list = []

def foo():
    print'iugh'

add_test(foo)
print run(add_test(foo))

