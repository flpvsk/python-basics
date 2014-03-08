'''
Created on 08 March 2014

@author: Yaha
'''


def dividers(x):
    res = []
    try:
        for i in xrange(1, x / 2 + 1):
            if x % i == 0:
                res.append(i)
    except Exception as e:
        print e.message
    return res

print dividers(147)
print dividers("s")


def to_bool(lst):
    pass
