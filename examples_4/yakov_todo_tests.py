'''
Created on Mar 20, 2014

@author: Java Student
'''
__all__ = ["test_add", 'test_clear', 'test_new_add_index', 'test_existing_add_index']

import todo
import yakov.autotest.assertions as ass

tst_pending = 'pending'
tet_compl = 'completed'


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
    todo.add('bbb')
    test_pass(ass.assert_equal, todo.items(), (('bbb', tst_pending),), test_add.__name__)


def test_clear():
    todo.clear()
    test_pass(ass.assert_equal, todo.items(), (0), test_clear.__name__)


def test_new_add_index():
    todo.clear()
    test_pass(ass.assert_equal, todo.add('txt'), 0, test_new_add_index.__name__)


def test_existing_add_index():
    todo.clear()
    todo.add('zero')
    test_pass(ass.assert_equal, todo.add('one'), 2, test_existing_add_index.__name__)


def test_empty_add_error():
    pass
