'''
Created on 13.03.2014

@author: vladimirbessmertnyj
'''


def dividers(x):
    return [i for i in range(1, x) if x % i == 0]

print dividers(10)
print dividers(100)

def to_bool(lst):
    return [bool(i) for i in lst]

print to_bool([0, 1, '', 'a'])