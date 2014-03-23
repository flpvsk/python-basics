"""Maintain a todo-list.

Each task is a tuple of the form (`text`, `status`), where `text` is task
description, `status` is either 'pending' or 'completed'.
E.g. ('Create todo app', 'pending')

    >>> from examples_4 import todo

    >>> todo.add('Sandwich')
    0
    >>> todo.items()
    (('Sandwich', 'pending'),)

    >>> todo.add('Sandwich')
    0

    >>> todo.add('Tests for todo lib')
    1
    >>> todo.items()
    (('Sandwich', 'pending'), ('Tests for todo lib', 'pending'))

    >>> todo.status_by_index(0)
    'pending'
    >>> todo.status_by_text('Sandwich')
    'pending'

    >>> todo.mark_completed_by_index(1)
    >>> todo.status_by_index(1)
    'completed'
    >>> todo.status_by_text('Tests for todo lib')
    'completed'
    >>> todo.items()
    (('Sandwich', 'pending'), ('Tests for todo lib', 'completed'))

    >>> todo.mark_completed_by_text('Sandwich')
    >>> todo.status_by_text('Sandwich')
    'completed'
    >>> todo.items()
    (('Sandwich', 'completed'), ('Tests for todo lib', 'completed'))

    >>> todo.clear()
    >>> todo.items()
    ()
"""

# Possible todo statuses
PENDING = "pending"
COMPLETED = "completed"

# List of todo items
_todos = []


def _index_by_text(text):
    """Get index of todo item by its text."""
    return [el[0] for el in _todos].index(text)


def add(text):
    """Add item to list.

    If item with given `text` already exists, returns its index.

    If item does not exist, adds it with 'pending' status and returns new
    index.

    Raises ValueError in case `text` is empty.
    """

    if not text:
        raise ValueError("Empty item can't be added")

    try:
        index = _index_by_text(text)
        return index
    except ValueError:
        # Item with `text` is not in list
        pass

    new_index = len(_todos)
    _todos.append((text, PENDING))
    return new_index


def items():
    """Get list of all todo items added."""
    return tuple(_todos)


def status_by_index(index):
    """Get status of todo task by its index."""
    return _todos[index][1]


def status_by_text(text):
    """Get status of todo task by its text."""
    index = _index_by_text(text)
    return status_by_index(index)


def mark_completed_by_index(index):
    """Mark item as 'completed' by its index."""
    todo_text = _todos[index][0]
    _todos[index] = (todo_text, COMPLETED)


def mark_completed_by_text(text):
    """Mark item as 'completed' by its text."""
    index = _index_by_text(text)
    mark_completed_by_index(index)


def next_pending():
    return [el[0] for el in _todos if el[1] == PENDING][0]


def clear():
    """Clear todo list"."""
    del _todos[:]
