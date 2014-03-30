class TestResult():
    def __init__(self, test, test_result, stacktrace = ''):
        self.test_name = test.__module__ + '.' + test.im_class.__name__ + '.' + test.__name__
        self.test_name = test.__module__ +'.' + test.__name__
        self.test_result = test_result
        self.stack_trace = stacktrace
