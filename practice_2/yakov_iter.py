'''
Created on 08 March 2014

@author: Yaha
'''


def dividers(x):
    res = []
    for i in xrange(1, x / 2 + 1):
        if x % i == 0:
            res.append(i)
    return res

print dividers(147)
