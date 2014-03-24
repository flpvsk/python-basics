'''
Created on Mar 13, 2014

@author: bessvla
'''

__all__ = ['TestRunner']


class TestRunner():
    def __init__(self):
        self.pending = []
        self.passed = []
        self.failed = []
        self.ran = []

    def add_test(self, fn):
        self.pending.append((fn))

    def passed_tests(self):
        return self.passed

    def pending_tests(self):
        return self.pending

    def ran_tests(self):
        return self.ran

    def failed_tests(self):
        return self.failed

    def clear_state(self):
        self.pending, self.passed, self.failed, self.ran = [], [], [], []

    def add_testclass(self, testclass):
        '''        testmethods = [i for i in dir(testclass) if i.startswith('test_')]
        set_up = [i for i in dir(testclass) if i == "set_up"]
        tear_down = [i for i in dir(testclass) if i == "tear_down"]
        for i in testmethods:
            if set_up:
                self.add_test(set_up[0])
            self.add_test(i)
            if tear_down:
                self.add_test(tear_down[0])'''
        self.pending.append((testclass))

    def class_run(self, testclass):
        testclass_instance = testclass()
        testmethods = [i for i in dir(testclass_instance) if i.startswith('test_')]
        for i in testmethods:
            try:
                testclass_instance.set_up()
            except:
                pass
            try:
                getattr(testclass_instance, i)()
                self.passed.append(i)
            except:
                self.failed.append(i)
            finally:
                self.ran.append(i)
                try:
                    testclass_instance.tear_down()
                except:
                    pass
        r = len(self.ran)
        p = len(self.passed)
        f = len(self.failed)
        return (r, p, f)
        
    def run(self):
        for i in self.pending_tests():
            try:
                i()
                self.passed.append(i)
            except:
                self.failed.append(i)
            finally:
                self.ran.append(i)
        r = len(self.ran)
        p = len(self.passed)
        f = len(self.failed)
        del self.pending[:]
        return (r, p, f)


class TodoTestCase(object):

    def __init__(self):
        print "initializing"

    def set_up(self):
        print "set_UP"

    def test_add_todo_adds_pending_item(self):
        print "tEST1"

    def test_add_return_value(self):
        print "Test2"

testrunner = TestRunner()
#testrunner.add_testclass(TodoTestCase)
print testrunner.pending_tests()
print testrunner.class_run(TodoTestCase)