'''
Created on Mar 20, 2014

@author: Java Student
'''
__all__ = ["test_add", 'test_clear', 'test_new_add_index', 'test_existing_add_index',
           'test_empty_add_error', 'test_items_not_duplicated', 'test_several_tasks',
           'test_completed_status_by_index', 'test_only_one_completed_by_index',
           'test_completed_status_by_text', 'test_only_one_completed_by_text',
           'test_check_status_by_text']

import todo
import yakov.autotest.assertions as ass

_tst_pending = 'pending'
_tst_compl = 'completed'


def _three_items():
    todo.clear()
    todo.add('one')
    todo.add('two')
    todo.add('three')


def test_pass(fn, *args):
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


def test_add():
    todo.clear()
    todo.add('bbb')
    test_pass(ass.assert_equal, todo.items(), (('bbb', _tst_pending),), test_add.__name__)


def test_clear():
    todo.clear()
    test_pass(ass.assert_equal, todo.items(), (), test_clear.__name__)


def test_new_add_index():
    todo.clear()
    test_pass(ass.assert_equal, todo.add('txt'), 0, test_new_add_index.__name__)


def test_existing_add_index():
    todo.clear()
    todo.add('zero')
    test_pass(ass.assert_equal, todo.add('zero'), 0, test_existing_add_index.__name__)


def test_items_not_duplicated():
    todo.clear()
    todo.add('oppa')
    todo.add('oppa')
    test_pass(ass.assert_equal, todo.items(), (('oppa', _tst_pending),), test_items_not_duplicated.__name__)


# How to catch exception by assertions?
def test_empty_add_error():
    todo.clear()
    test_pass(ass.assert_is_none, todo.add(''), test_empty_add_error.__name__)


def test_several_tasks():
    _three_items()
    test_pass(ass.assert_equal, todo.items(), (('one', _tst_pending), ('two', _tst_pending), ('three', _tst_pending)), test_several_tasks)


def test_completed_status_by_index():
    _three_items()
    todo.mark_completed_by_index(1)
    test_pass(ass.assert_equal, todo.status_by_index(1), _tst_compl, test_completed_status_by_index.__name__)


def test_only_one_completed_by_index():
    _three_items()
    todo.mark_completed_by_index(1)
    test_pass(ass.assert_equal, todo.items(), (('one', _tst_pending), ('two', _tst_compl), ('three', _tst_pending)), test_only_one_completed_by_index.__name__)


def test_completed_status_by_text():
    _three_items()
    todo.mark_completed_by_text('one')
    test_pass(ass.assert_equal, todo.status_by_index(0), _tst_compl, test_completed_status_by_text.__name__)


def test_only_one_completed_by_text():
    _three_items()
    todo.mark_completed_by_text('three')
    test_pass(ass.assert_equal, todo.items(), (('one', _tst_pending), ('two', _tst_pending), ('three', _tst_compl)), test_only_one_completed_by_text.__name__)


def test_check_status_by_text():
    _three_items()
    test_pass(ass.assert_equal, todo.status_by_text('one'), _tst_pending, test_check_status_by_text.__name__)
