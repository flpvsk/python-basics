from examples_2.utils import print_stars
from tests import *
from test_runner import *

def test_runner_test(fn):
    try:
        passed_test_message = fn
    except AssertionError as e:
        print("Failed - Exception caught: %r" % e.message)
    else:
        print("Passed - {0}".format(passed_test_message))
    finally:
        print_stars()

def empty_list_test():
    print("Test Empty pending_tests List")
    print_stars()
    clear_state()
    assert len(pending_tests()) == 0, "Pending test list is not empty"
    return "Pending test list is empty"

def not_empty_pending_list_test():
    print("Test Not Empty pending_tests List")
    print_stars()
    clear_state()
    add_test(equal_passed_test)
    assert len(pending_tests()) == 1, "Expected length: {}, Actual length: {}".format(1, len(pending_tests()))
    assert pending_tests()[0] == equal_passed_test.__name__, "Expected: {}, Actual: {}".format(pending_tests()._name_, pending_tests()[0])
    return "Pending test list contains 1 test"

def run_passed_test():
    print("Test run function without assertion errors")
    print_stars()
    clear_state()
    add_test(equal_passed_test)
    test_run_result = run()
    assert test_run_result == (1, 1, 0), "Expected : 1 test run, 1 test passed, 0 test failed, Actual: {} test run, {} test passed, {} test failed".format(*test_run_result)
    return "Result: 1 test run, 1 test passed, 0 test failed"

def run_failed_test():
    print("Test run function with assertion errors")
    print_stars()
    clear_state()
    add_test(equal_failed_test)
    test_run_result = run()
    assert test_run_result == (1, 0, 1), "Expected : 1 test run, 0 test passed, 1 test failed, Actual: {} test run, {} test passed, {} test failed".format(*test_run_result)
    return "Result: 1 test run, 0 test passed, 1 test failed"

def list_passed_run_test():
    print("Test passed_tests and failed_tests functions without assertion errors")
    print_stars()
    clear_state()
    add_test(equal_passed_test)
    run()
    assert len(passed_tests()) == 1, "Expected length: {}, Actual length: {}".format(1, len(passed_tests()))
    assert passed_tests()[0] == equal_passed_test.__name__, "Expected: {}, Actual: {}".format(passed_tests()._name_, passed_tests()[0])
    assert len(failed_tests()) == 0, "Expected length: {}, Actual length: {}".format(0, len(passed_tests()))
    return "Result: 1 test passed, 0 test failed"

def list_failed_run_test():
    print("Test passed_tests and failed_tests functions with assertion errors")
    print_stars()
    clear_state()
    add_test(equal_failed_test)
    run()
    assert len(passed_tests()) == 0, "Expected length: {}, Actual length: {}".format(0, len(passed_tests()))
    assert len(failed_tests()) == 1, "Expected length: {}, Actual length: {}".format(1, len(failed_tests()))
    assert failed_tests()[0] == equal_failed_test.__name__, "Expected: {}, Actual: {}".format(failed_tests()._name_, failed_tests()[0])
    return "Result: 1 test passed, 0 test failed"
    
test_runner_test(empty_list_test())
test_runner_test(not_empty_pending_list_test())
test_runner_test(run_passed_test())
test_runner_test(run_failed_test())
test_runner_test(list_passed_run_test())
test_runner_test(list_failed_run_test())

    