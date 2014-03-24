'''
Created on Mar 13, 2014

@author: bessvla
'''


def unique(lst):
    result = {x: None for x in lst}
    return result.keys()

print unique([])
print unique([1])
print unique([1, 2])
print unique([1, 1])

