from examples_4.todo import clear
from examples_4.todo import add
from examples_4.todo import mark_completed_by_text
from examples_4.todo import next_pending
from maria.autotest.assertions import assert_equal

__all__ = ['test_next_pending']


def test_next_pending():
    clear()
    add("Sandwich")
    add("Learn some python")
    add("Sleep")
    assert_equal("Sandwich", next_pending())
    mark_completed_by_text("Learn some python")
    assert_equal("Sandwich", next_pending())
    mark_completed_by_text("Sandwich")
    assert_equal("Sleep", next_pending())
