class A(object):
    a_attr = 'a'


class B(object):
    b_attr = 'b'


class C(A, B):
    c_attr = 'c'


c = C()
print('c.a_attr: %r, c.b_attr: %r, c.c_attr: %r' % (
       c.a_attr, c.b_attr, c.c_attr))
A.a_attr = 'new a'
print('c.a_attr: %r, c.b_attr: %r, c.c_attr: %r' % (
       c.a_attr, c.b_attr, c.c_attr))
