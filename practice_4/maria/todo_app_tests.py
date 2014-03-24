from examples_4.todo import clear
from examples_4.todo import items
from examples_4.todo import add
from examples_4.todo import PENDING
from examples_4.todo import COMPLETED
from examples_4.todo import status_by_index
from examples_4.todo import status_by_text
from examples_4.todo import mark_completed_by_text
from examples_4.todo import mark_completed_by_index
from examples_4.todo import _index_by_text

__all__ = ('test_clear', 'test_items', 'test_add_return_value',
           'test_same_task', 'test_task_with_no_descr',
           'test_status_by_index', 'test_status_by_text',
           'test_mark_completed_by_index', 'test_mark_completed_by_text',
           'test_index_by_text')


def compare(expected, actual, m="Test Failed: expected - {}, actual - {}"):
    assert expected == actual, m.format(expected, actual)


def test_clear():
    clear()
    compare((), items(), "Test Failed: items object is not empty")


def test_items():
    clear()
    add("Sandwich")
    expected_result = ("Sandwich", PENDING)
    actual_result = items()
    compare(1, len(actual_result))
    compare(expected_result, actual_result[0])


def test_add_return_value():
    clear()
    add_return_index = add("Sandwich")
    compare(0, add_return_index)


def test_same_task():
    clear()
    task_name = "Sandwich"
    add_return_index = add(task_name)
    compare(0, add_return_index)
    add_return_index = add(task_name)
    compare(0, add_return_index)
    actual_result = items()
    expected_result = (task_name, PENDING)
    compare(1, len(actual_result))
    compare(expected_result, actual_result[0])


def test_task_with_no_descr():
    clear()
    try:
        add("")
    except ValueError as e:
        expected_message = "Empty item can't be added"
        compare(expected_message, e.message)
    else:
        assert False, "Test failed: ValueError exception should be thrown"


def test_status_by_index():
    clear()
    todo1_text = "Cheese Sandwich"
    todo2_text = "Meat Sandwich"
    todo1_index = add(todo1_text)
    todo2_index = add(todo2_text)
    mark_completed_by_text(todo2_text)
    compare(PENDING, status_by_index(todo1_index))
    compare(COMPLETED, status_by_index(todo2_index))


def test_status_by_text():
    clear()
    todo1_text = "Cheese Sandwich"
    todo2_text = "Meat Sandwich"
    add(todo1_text)
    add(todo2_text)
    mark_completed_by_text(todo2_text)
    compare(PENDING, status_by_text(todo1_text))
    compare(COMPLETED, status_by_text(todo2_text))


def test_mark_completed_by_index():
    clear()
    todo1_text = "Cheese Sandwich"
    todo2_text = "Meat Sandwich"
    add(todo1_text)
    todo2_index = add(todo2_text)
    mark_completed_by_index(todo2_index)
    expected_result = ((todo1_text, PENDING), (todo2_text, COMPLETED))
    compare(expected_result, items())


def test_mark_completed_by_text():
    clear()
    todo1_text = "Cheese Sandwich"
    todo2_text = "Meat Sandwich"
    add(todo1_text)
    add(todo2_text)
    mark_completed_by_text(todo1_text)
    expected_result = ((todo1_text, COMPLETED), (todo2_text, PENDING))
    compare(expected_result, items())


def test_index_by_text():
    clear()
    todo1_text = "Cheese Sandwich"
    todo2_text = "Meat Sandwich"
    add(todo1_text)
    compare(0, _index_by_text(todo1_text))
    add(todo2_text)
    compare(1, _index_by_text(todo2_text))
