'''
Created on Mar 18, 2014

@author: bessvla
'''

import itertools

def sum_args(*args):
    if type(args[0]) == str:
        return ''.join(args)
    elif type(args[0]) == tuple or type(args[0]) == list:
        return type(args[0])(itertools.chain(*args))
    else:
        return sum(args)

print sum_args(1, 1)
print sum_args("aaa", "bbb", "ccc")
print sum_args((1, 2), (3, 4))