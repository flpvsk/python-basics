pending_tests_list = []
run_tests_list = []
failed_tests_list = []
passed_tests_list = []

def add_test(fn):
    pending_tests_list.append(fn)
    
def pending_tests():
    return [t.__name__ for t in pending_tests_list];

def run():
    for test in pending_tests_list:
        try:
            test()
        except AssertionError:
            failed_tests_list.append(test)
        else:
            passed_tests_list.append(test)
        finally:
            run_tests_list.append(test)
            pending_tests_list.remove(test)
    return (len(run_tests_list), len(passed_tests_list), len(failed_tests_list))
    
def run_tests():
    return [t.__name__ for t in run_tests_list];

def passed_tests():
    return [t.__name__ for t in passed_tests_list];

def failed_tests():
    return [t.__name__ for t in failed_tests_list];

def clear_state():
    del pending_tests_list[:]
    del run_tests_list[:]
    del failed_tests_list[:]
    del passed_tests_list[:]
    
            
    
        
    