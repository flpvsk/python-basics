'''
Created on 18 Mar 2014
 
@author: paraiva
'''
def wc(s):
    
    res = {'Symbols': None, 'Words': None, 'Lines': 1 }
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
print wc("One two three")
print wc("One\ntwo\nthree")
print wc('')

