from assertions import assert_equal, assert_not_equal, assert_is_none

__all__ = ["test_assert_equal", "test_assert_not_equal", "test_assert_is_none"]
def test_assert_equal():
    assert_equal(1,2)
    
    
def test_assert_not_equal():
    assert_not_equal(1,1)
    
    
def test_assert_is_none():
    assert_is_none(None)