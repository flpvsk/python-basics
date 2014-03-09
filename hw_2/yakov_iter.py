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
    ya.test(unique([]), [])
    ya.test(unique(["a", 1, [], (1, 2), [], "qw", (1, 2)]), ["a", 1, [],
                                                              (1, 2), "qw"])
    ya.test(unique([3, 2, 1]), [3, 2, 1])

#test_unique()
