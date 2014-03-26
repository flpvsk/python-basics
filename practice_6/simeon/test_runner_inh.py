import traceback

class TestRunnerBase(object):
    def __init__(self):
        self.tests = {}

    def add_test(self, fn):
        self.tests.update({fn: "pending"})

    def pending_tests(self):
        return [test for test, status in self.tests.items() if status == "pending"]
    
    def run(self):
        ran = 0
        passed = 0
        failed = 0
        for test in self.pending_tests():
            try:
                self.report_test_started(test)
                test()
            except:
                self.report_test_failed(test, traceback.format_exc())
                failed = failed + 1
                ran = ran + 1
                self.tests[test] = "failed"
            else:
                self.report_test_passed(test)
                passed = passed + 1
                ran = ran + 1
                self.tests[test] = "passed"
        ran = len([test for test, status in self.tests.items() if status in ('passed','failed')])
        passed = len([test for test, status in self.tests.items() if status == "passed"])
        failed = len([test for test, status in self.tests.items() if status == "failed"])
        self.report_all_finished(ran,passed,failed)
#         return (ran, passed, failed)

            
    def report_all_finished(self, ran, passed, failed):
        print("ran:({}) passed:({}) failed:({})".format(ran, passed, failed))


class TestRunnerVerboseReporting(TestRunnerBase):

    def report_test_started(self, test):
        print "started: %r" % test

    def report_test_passed(self, test):
        print "passed: %r" % test

    def report_test_failed(self, test, stack):
        print("failed: {} traceback: {}".format(test, stack))


class TestRunnerFailReporting(TestRunnerBase):

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

print "\nTestRunnerVerboseReporting"
a = TestRunnerVerboseReporting()

a.add_test(fn)
a.add_test(fn2)
a.add_test(fn3)
a.add_test(test_assert_equal)

a.run()


print "\nTestRunnerFailReporting"
a = TestRunnerFailReporting()

a.add_test(fn)
a.add_test(fn2)
a.add_test(fn3)
a.add_test(test_assert_equal)

a.run()