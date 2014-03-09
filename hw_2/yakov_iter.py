'''
Created on 09 March 2014

@author: Yaha
'''
import practice_2.yakov_assertions as ya


def unique(lst):
    res = []
    i = 0
    for item in lst:
        if lst.index(item) == i:
            res.append(item)
        i = i + 1
    return res


def test_unique():
    ya.divider("unique")
    ya.test(unique([1, 2, 3, 2, 1]), [1, 2, 3])

test_unique()
