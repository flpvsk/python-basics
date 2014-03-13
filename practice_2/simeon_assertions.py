print("\n***assert_equal(a, b)***\n")
def assert_equal(a, b):
    assert a == b, "({}) is not equal ({})".format(a,b)
    print("({}) is equal ({})".format(a,b))
#     if a == b:
#         print("({}) is equal ({})".format(a,b))
#         return True
#     else:
#         print("({}) is not equal ({})".format(a,b))
#         return False
         

def test(a,b):
    try:
        assert_equal(a,b)
    except BaseException as e:
        print("Exception caught: {}".format(e))

test(1,1)
test(1,-1)
test("qwe","qwe")
test("qwe","Qwe")
test([1,2,3],[1,2,3])
test(True,1)
test(0,False)
test(False,1)
test("",0)
test("",None)
test(0,None)

try:
    assert_equal("", )
except BaseException as e:
    print("Exception caught: {}".format(e))

try:
    assert_equal(1,)
except BaseException as e:
    print("Exception caught: {}".format(e))

try:
    assert_equal()
except BaseException as e:
    print("Exception caught: {}".format(e))

try:
    assert_equal(1)
except BaseException as e:
    print("Exception caught: {}".format(e))

try:
    assert_equal(1,1,1)
except BaseException as e:
    print("Exception caught: {}".format(e))


print("\n***assert_not_equal(a, b)***\n")
def assert_not_equal(a, b):
    assert a != b, "({}) is equal ({})".format(a,b)
    print("({}) is not equal ({})".format(a,b))
         

def test2(a,b):
    try:
        assert_not_equal(a,b)
    except BaseException as e:
        print("Exception caught: {}".format(e))

test2(1,1)
test2(1,-1)
test2(True,1)
test2(False,1)
test2(0,None)

try:
    assert_not_equal()
except BaseException as e:
    print("Exception caught: {}".format(e))

try:
    assert_not_equal(1,1,1)
except BaseException as e:
    print("Exception caught: {}".format(e))


print("\n***assert_true(x)***\n")
def assert_true(x):
    assert x, "({}) not True".format(x)
    print("({}) True".format(x))
         

def test3(x):
    try:
        assert_true(x)
    except BaseException as e:
        print("Exception caught: {}".format(e))

test3(1)
test3(0)
test3(2)
test3(False)
test3(True)
test3(1 is 1)
test3("")
test3(None)

try:
    assert_true(2 is not "A")
except BaseException as e:
    print("Exception caught: {}".format(e))

try:
    assert_true(0,0)
except BaseException as e:
    print("Exception caught: {}".format(e))


# assert_false(x)
print("\n***assert_false(x)***\n")
def assert_false(x):
    assert not x , "({}) not False".format(x)
    print("({}) False".format(x))
         

def test4(x):
    try:
        assert_false(x)
    except BaseException as e:
        print("Exception caught: {}".format(e))

test4(1)
test4(0)
test4(2)
test4("")
test4(None)
test4(False)
test4(True)
test4(1 is 1)

try:
    assert_false(2 is "A")
except BaseException as e:
    print("Exception caught: {}".format(e))

try:
    assert_false(0,0)
except BaseException as e:
    print("Exception caught: {}".format(e))

# assert_is(a, b)

print("\n***assert_is(a, b)***\n")
def assert_is(a, b):
    assert a is b , "({}) is not ({})".format(a,b)
    print("({}) is ({})".format(a,b))
         

def test5(a,b):
    try:
        assert_is(a, b)
    except BaseException as e:
        print("Exception caught: {}".format(e))

test5(1,1)
test5(1,-1)
test5([1,2,3],[1,2,3])
test5(True,1)
test5(False,1 is not 1)
test5("",None)

try:
    assert_is()
except BaseException as e:
    print("Exception caught: {}".format(e))

try:
    assert_is(1,1,1)
except BaseException as e:
    print("Exception caught: {}".format(e))

# assert_is_not(a, b)
print("\n***assert_is_not(a, b)***\n")
def assert_is_not(a, b):
    assert a is not b , "({}) is ({})".format(a,b)
    print("({}) is not ({})".format(a,b))
         

def test6(a,b):
    try:
        assert_is_not(a, b)
    except BaseException as e:
        print("Exception caught: {}".format(e))

test6(1,1)
test6(1,-1)
test6(True,1)
test6(False,1 is not 1)
test6("",None)

try:
    assert_is_not()
except BaseException as e:
    print("Exception caught: {}".format(e))

try:
    assert_is_not(a,b,c)
except BaseException as e:
    print("Exception caught: {}".format(e))

# assert_is_none(x)
print("\n***assert_is_none(x)***\n")
def assert_is_none(x):
    assert x is None , "({}) is not None".format(x)
    print("({}) is None".format(x))
         

def test7(x):
    try:
        assert_is_none(x)
    except BaseException as e:
        print("Exception caught: {}".format(e))

test7(1)
test7(0)
test7(True)
test7([])
test7(None)
test7("")

try:
    assert_is_none()
except BaseException as e:
    print("Exception caught: {}".format(e))

try:
    assert_is_none(a,b,c)
except BaseException as e:
    print("Exception caught: {}".format(e))

# assert_is_not_none(x)
print("\n***assert_is_not_none(x)***\n")
def assert_is_not_none(x):
    assert x is not None , "({}) is None".format(x)
    print("({}) is not None".format(x))
         

def test8(x):
    try:
        assert_is_not_none(x)
    except BaseException as e:
        print("Exception caught: {}".format(e))

test8(1)
test8(0)
test8(True)
test8([])
test8(None)
test8("")

try:
    assert_is_not_none()
except BaseException as e:
    print("Exception caught: {}".format(e))

try:
    assert_is_not_none(a,b,c)
except BaseException as e:
    print("Exception caught: {}".format(e))

# assert_in(a, b)
print("\n***assert_in(a, b)***\n")
def assert_in(a, b):
    assert a in b , "({}) not in ({})".format(a,b)
    print("({}) in ({})".format(a,b))
         

def test9(a,b):
    try:
        assert_in(a, b)
    except BaseException as e:
        print("Exception caught: {}".format(e))

test9(1,[1])
test9(1,[-1,1,0,2,3])
test9([1,2],[1,2,3])
test9([1,2],[[1,2,3],[1,2]])
test9(1,[[1,2,3],[1,2]])
test9("tr","control")
test9(None,[])

try:
    assert_in(None,["",0, False])
except BaseException as e:
    print("Exception caught: {}".format(e))

try:
    assert_in(a, b)
except BaseException as e:
    print("Exception caught: {}".format(e))

try:
    assert_in(1,1,1)
except BaseException as e:
    print("Exception caught: {}".format(e))

# assert_not_in(a, b)
print("\n***assert_not_in(a, b)***\n")
def assert_not_in(a, b):
    assert a not in b , "({}) in ({})".format(a,b)
    print("({}) not in ({})".format(a,b))
         

def test10(a,b):
    try:
        assert_not_in(a, b)
    except BaseException as e:
        print("Exception caught: {}".format(e))

test10(1,[1])
test10(1,[-1,1,0,2,3])
test10([1,2],[1,2,3])
test10([1,2],[[1,2,3],[1,2]])
test10(1,[[1,2,3],[1,2]])
test10("tr","control")
test10(None,[])

try:
    assert_not_in(None,["",0, False])
except BaseException as e:
    print("Exception caught: {}".format(e))

try:
    assert_not_in(a, b)
except BaseException as e:
    print("Exception caught: {}".format(e))

try:
    assert_not_in(1,1,1)
except BaseException as e:
    print("Exception caught: {}".format(e))


# in commit don't forget add comment
# __init__.py
# andrey.txt
# hash_my_name.py

# filipovski
# AyratSaubanov
