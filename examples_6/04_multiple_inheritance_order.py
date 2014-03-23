class A(object):
    attr = 'a'


class B(object):
    attr = 'b'


class AB(A, B):
    pass


class BA(B, A):
    pass


ab = AB()
ba = BA()
print('ab.attr: %r, AB.__mro__: %r' % (ab.attr, AB.__mro__))
print('ba.attr: %r, BA.__mro__: %r' % (ba.attr, BA.__mro__))
