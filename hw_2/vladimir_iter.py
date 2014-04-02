'''
Created on Mar 13, 2014

@author: bessvla
'''


def unique(lst):
    output = set(lst)
    return list(output)

print unique([1, 2, 1, 3, 4, 3, 3, 3])


def divide(a, b):
    try:
        result = a / b
        return (True, result)
    except:
        return (False, None)

print divide(1, 0)
print divide([], 4)
print divide(4, 2)
