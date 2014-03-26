class A(object):
    a_attr = 'a'


class B(A):
    b_attr = 'b'


b = B()
print('b.a_attr: %r, b.b_attr: %r' % (b.a_attr, b.b_attr))
