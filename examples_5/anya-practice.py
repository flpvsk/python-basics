'''
Created on Mar 20, 2014

@author: Java Student
'''
class MyClass(object):
    lst=[]
    
    def __init__(self, a, b, *args):
        self.lst += args
        self.a = a
        self.b = b
        
    def add(self,x):
        self.lst.append(x)
    
    
my_obj1 = MyClass(1,2,3,4,5)



print my_obj1.lst
print MyClass.lst