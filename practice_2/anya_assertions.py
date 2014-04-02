'''
Created on Mar 9, 2014

@author: ROO
'''

#assert_equal
def assert_equal(a, b):
    assert a==b

try:
    assert_equal(1, 1)
except AssertionError:
    raise("Test assert_equal(1, 1) failed!")
    
try:
    assert_equal(1, 2)
except AssertionError:
    pass
else:
    print("Test assert_equal(1, 2) failed!")
    
#assert_not_equal(a,b)
def assert_not_equal(a,b):
    assert a!=b

try:
    assert_not_equal(1,1)
except AssertionError:
    print ("Test assert_not_equal(1,1)  passed")
else:
    print ("Test assert_not_equal(1,1) failed.")

try:
    assert_not_equal(-1,1)
except AssertionError:
    print ("Test assert_not_equal(-1,1) failed.")
else:
    print ("Test assert_not_equal(-1,1) passed.")

#assert_true    
def assert_true(x):
    assert x
    
try:
    assert_true('a')
except AssertionError:
    print ("Test assert_true(a) failed.")
else:
    print ("Test assert_true(a) passed.")
    
try:
    assert_true(0)
except AssertionError:
    print ("Test assert_true(0) passed.")
else:
    print ("Test assert_true(0) failed.")
    
try:
    assert_true("")
except AssertionError:
    print ("Test assert_true("") passed.")
else:
    print ("Test assert_true("") failed.")
    
#assert_false
def assert_false(x):
    assert bool(x) == False
    
try:
    assert_false("")
except AssertionError:
    print ("Test assert_false('') failed.")
else:
    print ("Test assert_false('') passed.")
    
try:
    assert_false(1)
except AssertionError:
    print ("Test assert_false('1') passed.")
else:
    print ("Test assert_false('1') failed.")
    
#assert_is

def assert_is(a,b):
    assert a is b

try:
    assert_is(1,1)
except AssertionError:
    print ("Test assert_is(1,1) failed.")
else:
    print ("Test assert_is(1,1) passed.")
    
try:
    assert_is("1","1.0")
except AssertionError:
    print ("Test assert_is(1,1.0) passed.")
else:
    print ("Test assert_is(1,1.0) failed.")

    
#assert_is_not
def assert_is_not(a,b):
    assert a is not b
    
try:
    assert_is_not(1,1)
except AssertionError:
    print ("Test assert_is_not(1,1) passed.")
else:
    print ("Test assert_is_not(1,1) failed.")
    
try:
    assert_is_not("1","1.0")
except AssertionError:
    print ("Test assert_is_not(1,1.0) failed.")
else:
    print ("Test assert_is_not(1,1.0) passed.")

#assert_is_none    
def assert_is_none(x):
    assert x is None
    
try:
    assert_is_none('')
except AssertionError:
    print ("Test assert_is_none("") passed.")
   # print id(None)
   # print id('')
else:
    print ("Test assert_is_none("") failed.")
    
try:
    assert_is_none(0)
except AssertionError:
    print ("Test assert_is_none(0) passed.")
else:
    print ("Test assert_is_none(0) failed.")
    
#assert_is_not_none    
def assert_is_not_none(x):
    assert x is not None
    
try:
    assert_is_not_none('')
except AssertionError:
    print ("Test assert_is_not_none("") failed.")
else:
    print ("Test assert_is_not_none("") passed.")
    
try:
    assert_is_not_none(0)
except AssertionError:
    print ("Test assert_is_not_none(0) failed.")
else:
    print ("Test assert_is_not_none(0) passed.")
    
#asser_in
def assert_in(a,b):
    assert a in b 

try:
    assert_in('casper',[21,'casper',0,''])
except AssertionError:
    print ("Test assert_in failed.")
else:
    print ("Test assert_in passed.")
    
try:
    assert_in('casper',[21,'CASPER',0,''])
except AssertionError:
    print ("Test assert_in passed.")
else:
    print ("Test assert_in failed.")
    
#asser_not_in
def assert_not_in(a,b):
    assert a not in b 

try:
    assert_not_in('casper',[21,'Casper',0,''])
except AssertionError:
    print ("Test assert_not_in failed.")
else:
    print ("Test assert_in passed.")
    
try:
    assert_not_in('casper',[21,'casper',0,''])
except AssertionError:
    print ("Test assert_not_in passed.")
else:
    print ("Test assert_in failed.")



    
    





