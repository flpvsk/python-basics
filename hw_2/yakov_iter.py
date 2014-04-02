'''
Created on 09 March 2014

@author: Yaha
'''
import practice_2.yakov_assertions as ya


def unique(lst):
    return {el: None for el in lst}.keys()


def test_unique():
    ya.divider("unique")
    print ya.assert_equal(unique([1, 2, 3, 2, 1]), [1, 2, 3])
    print ya.assert_equal(unique([]), [])
    print ya.assert_equal(unique(["a", 1, (1, 2), "qw", (1, 2)]),
                          ["a", 1, (1, 2), "qw"])
    l = [3, 2, 1]
    print ya.assert_equal(unique(l), [1, 2, 3])

test_unique()


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
    print ya.assert_equal(divide(10, 0), fls)
    print ya.assert_equal(divide(0, 10), [True, 0])
    print ya.assert_equal(divide("abc", "fgh"), fls)
    print ya.assert_equal(divide("100", "50"), fls)
    print ya.assert_equal(divide(-5.0, -2.0), [True, 2.5])
    print ya.assert_equal(divide([2], [1]), fls)

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
            w = len(st.split())
            # Find lines number
            l = len(st.split("\n"))
        except:
            pass
        res = {sym: s, wrd: w, lns: l}
    return res


def test_wc():
    ya.divider("wc")
    zero = {sym: 0, wrd: 0, lns: 0}
    print ya.assert_equal(wc("abcdefghij"), {sym: 10, wrd: 1, lns: 1})
    print ya.assert_equal(wc(""), zero)
    print ya.assert_equal(wc("a\nb\nc"), {sym: 5, wrd: 3, lns: 3})
    print ya.assert_equal(wc(1), zero)
    print ya.assert_equal(wc(["a", "bd"]), zero)

test_wc()
