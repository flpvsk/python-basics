class A(object):
    attr = 'a'


class B(object):
    attr = 'b'


b = B()
print('A.attr: %r, B.attr: %r, b.attr: %r' % (A.attr, B.attr, b.attr))
b.attr = 'instance value shadow'
print('A.attr: %r, B.attr: %r, b.attr: %r' % (A.attr, B.attr, b.attr))
