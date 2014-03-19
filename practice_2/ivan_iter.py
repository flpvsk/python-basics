'''
Created on 20 Mar 2014

@author: CenturyChild
'''
def dividers(x):
    lst = [] 
    for i in xrange(1, x + 1):
        if x % i == 0:
            lst.append(i)
    print lst
print 'test dividers\n'
dividers(10)
dividers(100)