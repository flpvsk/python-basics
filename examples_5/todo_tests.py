"""Tests for todo-app"""
from maria.autotest import assert_equal

from todo import Todo

__all__ = ('TodoTestCase',)


class TodoTestCase(object):

    def __init__(self):
        self._todo = Todo()

    def set_up(self):
        self._todo.clear()

    def test_add_todo_adds_pending_item(self):
        self._todo.add("Sandwich")

        items = self._todo.items()
        assert_equal(("Sandwich", Todo.PENDING), items)
    
    def test_add_todo_adds_pending_item2(self):
        self._todo.add("Sand")

        items = self._todo.items()
        assert_equal((("Sand", Todo.PENDING),), items)
    
    def tear_down(self):
        print("tear_down")

    def test_add_return_value(self):
        add_return_index = self._todo.add("Sandwich")
        assert_equal(0, add_return_index)
