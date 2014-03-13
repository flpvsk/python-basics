'''
Created on Mar 13, 2014

@author: Java Student
'''



def assert_equal(a,b,message="Default"):
   if a==b:
       return True
   else:
       raise AssertionError(message)
   
assert_equal(1,2,"Eddfg")
   


       