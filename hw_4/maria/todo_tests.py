from examples_4.todo import clear
from examples_4.todo import add
from examples_4.todo import mark_completed_by_text
from examples_4.todo import next_pending

__all__ = ('test_next_pending')


def compare(expected, actual, m="Test Failed: expected - {}, actual - {}"):
    assert expected == actual, m.format(expected, actual)


def test_next_pending():
    clear()
    add("Sandwich")
    add("Learn some python")
    add("Sleep")
    compare("Sandwich", next_pending())
    mark_completed_by_text("Learn some python")
    compare("Sandwich", next_pending())
    mark_completed_by_text("Sandwich")
    compare("Sleep", next_pending())
