'''
Created on Mar 13, 2014

@author: Java Student
'''
def unique(l):
    dct={}
    for x in l:
        dct[x] = None
    return list(dct)
print(unique([1,2,3,3]))
print(unique([1,2]))
print(unique([2,2,3,3]))