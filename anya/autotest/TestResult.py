class TestResult():
    def __init__(self, test):
        self._TESTNAME = test.__module__ + '.' + test.im_class.__name__ + '.' + test.__name__
        self._TESTRESULT = ''
        self.STACKTRACE = ''