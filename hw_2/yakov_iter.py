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


def divide(a, b):
    res = [False, None]
    try:
        r = a / b
    except:
        return res
    else:
        return [True, r]


def test_divide():
    ya.divider("divide")
    fls = [False, None]
    ya.test(divide(10, 0), fls)
    ya.test(divide(0, 10), [True, 0])
    ya.test(divide("abc", "fgh"), fls)
    ya.test(divide("100", "50"), fls)
    ya.test(divide(-5.0, -2.0), [True, 2.5])
    ya.test(divide([2], [1]), fls)

#test_divide()

sym = "symbols"
wrd = "words"
lns = "lines"


def wc(st):
    s = 0
    w = 0
    l = 0
    res = {sym: s, wrd: w, lns: l}
    if isinstance(st, str):
        try:
            # Find symbols number
            s = len(st)
            # Find words number
            # Find lines number
        except:
            pass
        res = {sym: s, wrd: w, lns: l}
    return res


def test_wc():
    ya.divider("wc")
    exp1 = {sym: 10, wrd: 1, lns: 1}
    exp2 = {sym: 0, wrd: 0, lns: 0}
    exp3 = {sym: 5, wrd: 3, lns: 3}
    print ya.assert_equal(wc("abcdefghij"), exp1)
    print ya.assert_equal(wc(""), exp2)
    print ya.assert_equal(wc("a\nb\nc"), exp3)
    print ya.assert_equal(wc(1), exp2)
    print ya.assert_equal(wc(["a", "bd"]), exp2)

test_wc()
