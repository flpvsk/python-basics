import traceback

class TestRunnerReporter(object):
    def __init__(self, reporter):
        self.tests = {}

    def add_test(self, fn):
        self.tests.update({fn: "pending"})

    def pending_tests(self):
        return [test for test, status in self.tests.items() if status == "pending"]
    
    def run(self):
        for test in self.pending_tests():
            try:
                reporter.report_test_started(test)
                test()
            except:
                reporter.report_test_failed(test, traceback.format_exc())
                self.tests[test] = "failed"
            else:
                reporter.report_test_passed(test)
                self.tests[test] = "passed"
        ran = len([test for test, status in self.tests.items() if status in ('passed','failed')])
        passed = len([test for test, status in self.tests.items() if status == "passed"])
        failed = len([test for test, status in self.tests.items() if status == "failed"])
        self.report_all_finished(ran,passed,failed)
          
    def report_all_finished(self, ran, passed, failed):
        print("ran:({}) passed:({}) failed:({})".format(ran, passed, failed))


class VerboseReporter(object):
    def report_test_started(self, test):
        print "started: %r" % test

    def report_test_passed(self, test):
        print "passed: %r" % test

    def report_test_failed(self, test, stack):
        print("failed: {} traceback: {}".format(test, stack))    


class FailReporter(object):
    def report_test_started(self, test):
        pass
 
    def report_test_passed(self, test):
        print "."
 
    def report_test_failed(self, test, stack):
        print("test failed: traceback: {}".format(stack))  

# Functions

def fn():
    return


def fn2():
    return 2


def fn3():
    return 3


def test_assert_equal():
    assert_equal(1, 2)


def assert_equal(a, b, msg="{} is not equal {}"):
    assert a == b, msg.format(a, b)
    print("({}) is equal ({})".format(a, b))


reporter = VerboseReporter()
runner = TestRunnerReporter(reporter)

runner.add_test(fn)
runner.add_test(fn2)
runner.add_test(fn3)
runner.add_test(test_assert_equal)

runner.run()

reporter = FailReporter()
runner = TestRunnerReporter(reporter)

runner.add_test(fn)
runner.add_test(fn2)
runner.add_test(fn3)
runner.add_test(test_assert_equal)

runner.run()