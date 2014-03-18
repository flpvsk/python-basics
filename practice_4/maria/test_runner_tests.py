from maria.autotest import assert_equal

__all__ = ('test_1')


def test_1():
    try:
        assert_equal(1, 2)
    except AssertionError as e:
        print("Failed - Exception caught: %r" % e.message)
    else:
        print("Passed - {0}".format("values are equal"))
