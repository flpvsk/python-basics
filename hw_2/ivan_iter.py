'''
Created on 18 Mar 2014
@author: paraiva
'''


def unique(lst):
    newset = set(lst)
    return list(newset)
print 'uique function test:\n'
print unique([1, 2, 1, 3, 4, 3, 3, 3])


def divide(a, b):
    try:
        result = a / b
        return result
    except:
        return (False, None)
print '\ndivide function test:\n'
print divide(1, 0)
print divide([], 4)
print divide(4, 2)


def wc(s):
    res = {'Symbols': None, 'Words': None, 'Lines': 1}
    countWords = 0
    countSymbols = 0
    countLines = 1
    if s is '':
        res['Words'] = 0
        res['Symbols'] = 0
        res['Lines'] = 0
    for i in s:
        if ' ' not in s:
            res['Words'] = 1
        elif i == ' ':
            countWords += 1
            res['Words'] = countWords + 1
        elif type(i) == str:
            countSymbols += 1
            res['Symbols'] = countSymbols + countWords
        elif i == '\n':
            countLines += 1
            res['Lines'] = countLines
        elif ' ' not in s:
            res['Words'] = 1
    return res
#Some tests
print '\nwc function tests\n'
print wc("One two three")
print wc("One\ntwo\nthree")
print wc('')
