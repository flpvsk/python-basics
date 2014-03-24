import traceback

class TestRunnerReporter(object):
    def __init__(self, reporter):
        self.tests = {}
        self.pen_tests = []
        self.ran_t = []
        self.pass_t = []
        self.fail_t = []

    def add_test(self, fn):
        self.tests.update({fn: "pending"})

    def pending_tests(self):
        self.pen_tests = []
        for k, v in self.tests.items():
            if v == "pending":
                self.pen_tests.append(k)
        return self.pen_tests

    def run(self):
        ran = 0
        passed = 0
        failed = 0
        self.pending_tests()
        for test in self.pen_tests:
            try:
                reporter.report_test_started(test)
                test()
            except:
                reporter.report_test_failed(test, traceback.format_exc())
                failed = failed + 1
                ran = ran + 1
                self.tests[test] = "failed"
            else:
                reporter.report_test_passed(test)
                passed = passed + 1
                ran = ran + 1
                self.tests[test] = "passed"
        self.report_all_finished(ran,passed,failed)
        return (ran, passed, failed)

    def ran_tests(self):
        for k, v in self.tests.items():
            if v in ("failed", "passed"):
                self.ran_t.append(k)
        return self.ran_t

    def passed_tests(self):
        for k, v in self.tests.items():
            if v == "passed":
                self.pass_t.append(k)
        return self.pass_t

    def failed_tests(self):
        for k, v in self.tests.items():
            if v == "failed":
                self.fail_t.append(k)
        return self.fail_t

    def clear_state(self):
        del self.pen_tests[:]
        del self.ran_t[:]
        del self.pass_t[:]
        del self.fail_t[:]
        for k, v in self.tests.items():
            self.tests[k] = ""
            
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