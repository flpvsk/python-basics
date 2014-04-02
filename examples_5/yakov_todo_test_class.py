'''
Created on Mar 24, 2014

@author: Java Student
'''
from todo import Todo
from yakov.autotest import assertions as ass


class TodoTestCases():

    def __init__(self):
        self._todo = Todo()
        self._tst_pending = 'pending'
        self._tst_compl = 'completed'

    def set_up(self):
        self._todo.clear()

    def tear_down(self):
        pass

    def _three_items(self):
        self._todo.add('one')
        self._todo.add('two')
        self._todo.add('three')

    def _test_pass(self, fn, *args):
        try:
            fn(*args)
        except:
            print "{0}{1} failed".format(args[-1], args[:-1])
            # I don't like this 'raise' but couldn't choose better approach
            # And it works
            raise
        else:
            #print "{0}{1} passed".format(fn.__name__, args)
            pass

    def test_add(self):
        self._todo.add('bbb')
        self._test_pass(ass.assert_equal, self._todo.items(), (('bbb', self._tst_pending),), self.test_add.__name__)

    def test_clear(self):
        self._test_pass(ass.assert_equal, self._todo.items(), (), self.test_clear.__name__)

    def test_new_add_index(self):
        self._test_pass(ass.assert_equal, self._todo.add('txt'), 0, self.test_new_add_index.__name__)

    def test_existing_add_index(self):
        self._todo.add('zero')
        self._test_pass(ass.assert_equal, self._todo.add('zero'), 0, self.test_existing_add_index.__name__)

    def test_items_not_duplicated(self):
        self._todo.add('oppa')
        self._todo.add('oppa')
        self._test_pass(ass.assert_equal, self._todo.items(), (('oppa', self._tst_pending),), self.test_items_not_duplicated.__name__)

    # How to catch exception by assertions?
    def test_empty_add_error(self):
        self._test_pass(ass.assert_is_none, self._todo.add(''), self.test_empty_add_error.__name__)

    def test_several_tasks(self):
        self._three_items()
        self._test_pass(ass.assert_equal, self._todo.items(), (('one', self._tst_pending), ('two', self._tst_pending), ('three', self._tst_pending)), self.test_several_tasks)

    def test_completed_status_by_index(self):
        self._three_items()
        self._todo.mark_completed_by_index(1)
        self._test_pass(ass.assert_equal, self._todo.status_by_index(1), self._tst_compl, self.test_completed_status_by_index.__name__)

    def test_only_one_completed_by_index(self):
        self._three_items()
        self._todo.mark_completed_by_index(1)
        self._test_pass(ass.assert_equal, self._todo.items(), (('one', self._tst_pending), ('two', self._tst_compl), ('three', self._tst_pending)), self.test_only_one_completed_by_index.__name__)

    def test_completed_status_by_text(self):
        self._three_items()
        self._todo.mark_completed_by_text('one')
        self._test_pass(ass.assert_equal, self._todo.status_by_index(0), self._tst_compl, self.test_completed_status_by_text.__name__)

    def test_only_one_completed_by_text(self):
        self._three_items()
        self._todo.mark_completed_by_text('three')
        self._test_pass(ass.assert_equal, self._todo.items(), (('one', self._tst_pending), ('two', self._tst_pending), ('three', self._tst_compl)), self.test_only_one_completed_by_text.__name__)

    def test_check_status_by_text(self):
        self._three_items()
        self._test_pass(ass.assert_equal, self._todo.status_by_text('one'), self._tst_pending, self.test_check_status_by_text.__name__)
