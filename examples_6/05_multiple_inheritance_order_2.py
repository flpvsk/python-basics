O = object
class F(O):
    attr = 'F'
class E(O):
    attr = 'E'
class D(O):
    attr = 'D'

class C(D, F): pass
class B(D, E): pass
class A(B, C): pass

a = A()
print('a.attr: %r, A.__mro__ : %r' % (a.attr, A.__mro__))
