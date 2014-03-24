'''
Created on Mar 24, 2014

@author: Java Student
'''
from examples_4.todo import *
from practice_2.ivan_assertions import *


def test_clear():
    clear()
    assert () == items()


def test_add():
    clear()
    add('Sandwich')
    assert_equal(('Sandwich', PENDING) == items())


def test_add_index():
    clear()
    index = add('Sandwich')
    assert_equal(0, index)
