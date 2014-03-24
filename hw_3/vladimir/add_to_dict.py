'''
Created on Mar 14, 2014

@author: bessvla
'''


def add_to_dict(dic, **kwargs):
    dic.update(**kwargs)

# add_to_dict()
d = {"x": 1}

add_to_dict(d, y=2, z=3)

print d

add_to_dict(d, y=2, z=3, x="asdasd", zx=42, zxz=[1, 2, 3])


print d