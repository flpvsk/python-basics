class TestResult():
    def __init__(self, test, test_result, stacktrace = ''):
        self._TESTNAME = test.__module__ + '.' + test.im_class.__name__ + '.' + test.__name__
        self._TESTRESULT = test_result
        self._STACKTRACE = stacktrace