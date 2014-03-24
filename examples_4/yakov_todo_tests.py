'''
Created on Mar 20, 2014

@author: Java Student
'''
__all__ = ["test_add", 'test_clear', 'test_new_add_index', 'test_existing_add_index']

import todo
import yakov.autotest.assertions as ass

tst_pending = 'pending'
tet_compl = 'completed'
msg = ' doesn\'t work'


def test_add():
    todo.add('bbb')
    ass.assert_equal(todo.items(), (('bbb', tst_pending),), test_add.__name__ + msg)


def test_clear():
    todo.clear()
    try:
        ass.assert_equal(todo.items(), (), test_clear.__name__ + msg)
    except Exception as e:
        print e.message


def test_new_add_index():
    todo.clear()
    ass.assert_equal(todo.add('txt'), 0, test_new_add_index.__name__ + msg)


def test_existing_add_index():
    todo.clear()
    todo.add('zero')
    ass.assert_equal(todo.add('one'), 1, test_existing_add_index.__name__ + msg)


def test_empty_add_error():
    pass
