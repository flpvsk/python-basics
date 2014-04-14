'''
Created on 18 Mar 2014

@author: paraiva
'''


def add_to_dict(req_param, **kwargs):
    for i, j in kwargs.items():
        req_param[i] = j
print 'Test1\n'

try:
    add_to_dict()
except TypeError, ex:
    print ex
finally:
    pass

print '\nTest2\n'
d = {'x': 1}
add_to_dict(d, y = 2, z = 2)
print d

print '\nTest3\n'
add_to_dict(d, t = 123, ghj = 2354, s = 0, qa = 6, test= -10)
print d
