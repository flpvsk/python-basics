# 
# def assert_equal(a, b, msg="{} is not equal {}"):
# #     assert a == b, "({}) is not equal ({})".format(a,b)
#     assert a == b, msg.format(a, b)
#     print("({}) is equal ({})".format(a, b))
# 
# 
# assert_equal(1, 2)
# assert_equal(1, 2, "Assertion failed")
# 
# def assert_not_equal(a, b, msg = "({}) is equal ({})"):
#     assert a != b, msg.format(a, b)
#     print("({}) is not equal ({})".format(a, b))
# 
# assert_not_equal(1, 2)
# assert_not_equal(1, 1)
# assert_not_equal(1, 1, "Assertion Failed")
# assert_not_equal(1, 2, "Assertion Failed")


def assert_true(x, msg="({}) not True"):
    assert x, msg.format(x)
    print("({}) True".format(x))

assert_true(True)
assert_true(False, "Assertion Failed")

