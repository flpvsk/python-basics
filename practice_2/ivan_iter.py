'''
Created on 20 Mar 2014

@author: CenturyChild
'''
def dividers(x):
    lst = [] 
    for i in xrange(1, x + 1):
        if x % i == 0:
            lst.append(i)
    return lst
print 'test dividers\n'
print dividers(10)
print dividers(100)

def to_bool(lst):
    lst2 = []
    for i in lst:
        lst2.append(bool(i))
    return lst2
print '\ntest to_bool\n'
print to_bool([0, 1, '', 'a'])
print to_bool(['i', -1, '%'])