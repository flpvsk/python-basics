'''
Created on Mar 24, 2014

@author: Java Student
'''

from practice_2.ivan_assertions import assert_equal
from examples_4.todo import clear
from examples_4.todo import items
from examples_4.todo import add
from examples_4.todo import PENDING
from examples_4.todo import COMPLETED
from examples_4.todo import status_by_index
from examples_4.todo import mark_completed_by_text
from examples_4.todo import mark_completed_by_index
from examples_4.todo import _index_by_text

__all__ = ('test_clear',
           'test_add',
           'test_add_index',
           'test_duplicates',
           'test_description',
           'test_status_by_index',
           'test_status_by_text',
           'test_mark_completed_by_index',
           'test_mark_completed_by_text',
           'test_index_by_text')


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


def test_duplicates():
    clear()
    index = add('Sandwich')
    assert_equal(0, index)
    index = add('Sandwich')
    assert_equal(0, index)
    assert_equal(('Sandwich', PENDING) == items())


def test_description():
    clear()
    try:
        add("")
    except Exception as e:
        expected_message = "No description"
        assert_equal(expected_message, e.message)


def test_status_by_index():
    clear()
    text2 = "Beer"
    index1 = add('Meat')
    index2 = add('Beer')
    mark_completed_by_text(text2)
    assert_equal(PENDING, status_by_index(index1))
    assert_equal(COMPLETED, status_by_index(index2))


def test_status_by_text():
    clear()
    text1 = 'Meat'
    text2 = "Beer"
    add('Meat')
    add('Beer')
    mark_completed_by_text(text2)
    assert_equal(PENDING, status_by_index(text1))
    assert_equal(COMPLETED, status_by_index(text2))


def test_mark_completed_by_index():
    clear()
    todo1_text = "Meat"
    todo2_text = "Beer"
    add(todo1_text)
    todo2_index = add(todo2_text)
    mark_completed_by_index(todo2_index)
    expected_result = ((todo1_text, PENDING), (todo2_text, COMPLETED))
    assert_equal(expected_result, items())


def test_mark_completed_by_text():
    clear()
    todo1_text = "Meat"
    todo2_text = "Beer"
    add(todo1_text)
    add(todo2_text)
    mark_completed_by_text(todo1_text)
    expected_result = ((todo1_text, COMPLETED), (todo2_text, PENDING))
    assert_equal(expected_result, items())


def test_index_by_text():
    clear()
    todo1_text = "Meat"
    todo2_text = "Beer"
    add(todo1_text)
    assert_equal(0, _index_by_text(todo1_text))
    add(todo2_text)
    assert_equal(1, _index_by_text(todo2_text))
