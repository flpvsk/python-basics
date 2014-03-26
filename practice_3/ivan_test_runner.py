'''
Created on Mar 13, 2014

@author: Java Student
'''
global pending_test_list
global failed_test_list
global run_test_list
global passed_test_list

pending_test_list = []
failed_test_list = []
run_test_list = []
passed_test_list = []


def add_test(fn):
    pending_test_list.append(fn)


def pending_test():
    return pending_test_list


def run():
    for i in pending_test_list:
        try:
            i()
        except AssertionError as er:
            print("An error occurred: " + er)
            failed_test_list.append(i)
        finally:
            run_test_list.append(i)
            pending_test_list.remove(i)
    return (len(run_test_list),
            len(passed_test_list),
            len(failed_test_list))


def run_tests():
    return run_test_list


def passed_tests():
    return passed_test_list


def failed_tests():
    return failed_test_list


def clear_state():
    del pending_test_list[:]
    del run_test_list[:]
    del failed_test_list[:]
    del passed_test_list[:]
