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

def to_bool(lst):
    lst2 = []
    for i in lst:
        lst2.append(bool(i))
    print lst2
print '\ntest to_bool\n'
to_bool([0, 1, '', 'a'])
to_bool(['i', -1, '%'])