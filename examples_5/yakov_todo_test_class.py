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

    def test_add(self):
        self._todo.add('bbb')
        ass.assert_equal(self._todo.items(), (('bbb', self._tst_pending),), self.test_add.__name__)

    def test_clear(self):
        ass.assert_equal(self._todo.items(), (), self.test_clear.__name__)

    def test_new_add_index(self):
        ass.assert_equal(self._todo.add('txt'), 0, self.test_new_add_index.__name__)

    def test_existing_add_index(self):
        self._todo.add('zero')
        ass.assert_equal(self._todo.add('zero'), 0, self.test_existing_add_index.__name__)

    def test_items_not_duplicated(self):
        self._todo.add('oppa')
        self._todo.add('oppa')
        ass.assert_equal(self._todo.items(), (('oppa', self._tst_pending),), self.test_items_not_duplicated.__name__)

    # How to catch exception by assertions?
    def test_empty_add_error(self):
        try:
            self._todo.add('')
        except:
            pass
        else:
            raise AssertionError(self.test_empty_add_error.__name__)

    def test_several_tasks(self):
        self._three_items()
        res = self._todo.items()
        ass.assert_equal(3, len(res), self.test_several_tasks + ' - length')
        ass.assert_in(('one', self._tst_pending), res, self.test_several_tasks + ' - item one')
        ass.assert_in(('two', self._tst_pending), res, self.test_several_tasks + ' - item two')
        ass.assert_in(('three', self._tst_pending), res, self.test_several_tasks + ' - item three')

    def test_completed_status_by_index(self):
        self._three_items()
        self._todo.mark_completed_by_index(1)
        ass.assert_equal(self._todo.status_by_index(1), self._tst_compl, self.test_completed_status_by_index.__name__)

    def test_only_one_completed_by_index(self):
        self._three_items()
        self._todo.mark_completed_by_index(1)
        ass.assert_equal(self._todo.items(), (('one', self._tst_pending), ('two', self._tst_compl), ('three', self._tst_pending)), self.test_only_one_completed_by_index.__name__)

    def test_completed_status_by_text(self):
        self._three_items()
        self._todo.mark_completed_by_text('one')
        ass.assert_equal(self._todo.status_by_index(0), self._tst_compl, self.test_completed_status_by_text.__name__)

    def test_only_one_completed_by_text(self):
        self._three_items()
        self._todo.mark_completed_by_text('three')
        ass.assert_equal(self._todo.items(), (('one', self._tst_pending), ('two', self._tst_pending), ('three', self._tst_compl)), self.test_only_one_completed_by_text.__name__)

    def test_check_status_by_text(self):
        self._three_items()
        ass.assert_equal(self._todo.status_by_text('one'), self._tst_pending, self.test_check_status_by_text.__name__)
