'''
Created on Mar 24, 2014

@author: Java Student
'''

from practice_2.ivan_assertions import assert_equal
from examples_4 import todo
from ivan.autotest.test_runner import TestRunner

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
    todo.clear()
    assert () == todo.items()


def test_add():
    todo.clear()
    todo.add('Sandwich')
    assert_equal(('Sandwich', todo.PENDING) == todo.items())


def test_add_index():
    todo.clear()
    index = todo.add('Sandwich')
    assert_equal(0, index)


def test_duplicates():
    todo.clear()
    index = todo.add('Sandwich')
    assert_equal(0, index)
    index = todo.add('Sandwich')
    assert_equal(0, index)
    assert_equal(('Sandwich', todo.PENDING) == todo.items())


def test_description():
    todo.clear()
    try:
        todo.add("")
    except Exception as e:
        expected_message = "No description"
        assert_equal(expected_message, e.message)


def test_status_by_index():
    todo.clear()
    text2 = "Beer"
    index1 = todo.add('Meat')
    index2 = todo.add('Beer')
    todo.mark_completed_by_text(text2)
    assert_equal(todo.PENDING, todo.status_by_index(index1))
    assert_equal(todo.COMPLETED, todo.status_by_index(index2))


def test_status_by_text():
    todo.clear()
    text1 = 'Meat'
    text2 = "Beer"
    todo.add('Meat')
    todo.add('Beer')
    todo.mark_completed_by_text(text2)
    assert_equal(todo.PENDING, todo.status_by_text(text1))
    assert_equal(todo.COMPLETED, todo.status_by_text(text2))


def test_mark_completed_by_index():
    todo.clear()
    todo1_text = "Meat"
    todo2_text = "Beer"
    todo.add(todo1_text)
    todo2_index = todo.add(todo2_text)
    todo.mark_completed_by_index(todo2_index)
    expected_result = ((todo1_text, todo.PENDING),
                       (todo2_text, todo.COMPLETED))
    assert_equal(expected_result, todo.items())


def test_mark_completed_by_text():
    todo.clear()
    todo1_text = "Meat"
    todo2_text = "Beer"
    todo.add(todo1_text)
    todo.add(todo2_text)
    todo.mark_completed_by_text(todo1_text)
    expected_result = ((todo1_text, todo.COMPLETED),
                       (todo2_text, todo.PENDING))
    assert_equal(expected_result, todo.items())


def test_index_by_text():
    todo.clear()
    todo1_text = "Meat"
    todo2_text = "Beer"
    todo.add(todo1_text)
    assert_equal(0, todo._index_by_text(todo1_text))
    todo.add(todo2_text)
    assert_equal(1, todo._index_by_text(todo2_text))

testrunner = TestRunner()
testrunner.add_test(test_clear)
testrunner.add_test(test_add)
testrunner.add_test(test_add_index)
testrunner.add_test(test_duplicates)
testrunner.add_test(test_description)
testrunner.add_test(test_status_by_index)
testrunner.add_test(test_status_by_text)
testrunner.add_test(test_mark_completed_by_index)
testrunner.add_test(test_mark_completed_by_text)
testrunner.add_test(test_index_by_text)

print testrunner.run()
