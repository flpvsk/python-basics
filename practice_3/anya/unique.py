'''
Created on Mar 13, 2014

@author: Java Student
'''

def unique(lst):
    output = {i : None for i in lst}
    return output.keys()

print unique([1,2,3,1])
