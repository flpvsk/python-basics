'''
Created on 19 Mar 2014

@author: paraiva
'''
def sum_args(param, *args):
        return sum(args,param)


print 'Test1\n'
try:
    sum_args()
except TypeError, ex:
    print ex
finally: pass

print '\nTest2\n'
print sum_args(1)

print '\nTest3\n'
print sum_args(5,6)

print '\nTest4\n'
print sum_args((1, 2), (3, 4), (4, 5, 6))