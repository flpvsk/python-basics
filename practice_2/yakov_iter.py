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
    res = [bool(item) for item in lst]
    return res

print to_bool([])
print to_bool([1, 0, [], ()])
