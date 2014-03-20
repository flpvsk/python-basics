'''
Created on Mar 20, 2014

@author: Java Student
'''
__all__ = ["test_add", 'test_clear']

import todo
#import yakov.autotest.runner as run
import yakov.autotest.assertions as ass

tst_pending = 'pending'
tet_compl = 'completed'
msg = ' doesn\'t work'


def test_add():
    todo.add('bbb')
    print ass.assert_equal(todo.items(), ('bbb', tst_pending), 'Add' + msg)


def test_clear():
    todo.clear()
    print ass.assert_equal(todo.items(), (), 'Clear' + msg)
    