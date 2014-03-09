'''
Created on 08 March 2014

@author: Yaha
'''
from yakov_assertions import divider


def dividers(x):
    res = []
    try:
        x = abs(x)
        for i in xrange(1, x / 2 + 1):
            if x % i == 0:
                res.append(i)
    except Exception as e:
        print e.message
    return res


def test_dividers():
    print "dividers"
    print dividers(147)
    print dividers("s")
    print dividers(-15)


def to_bool(lst):
    res = []
    try:
        res = [bool(item) for item in lst]
    except Exception as e:
        print e.message
    return res


def test_to_bool(self):
    print "to_bool"
    print to_bool([])
    print to_bool([1, 0, [], ()])
    print to_bool(2)
    print to_bool((2, 4, 0))
