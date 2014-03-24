class A(object):
    attr = 'a'

    def print_attr(self):
        print('Print from A: %r' % self.attr)


class B(A):
    def print_attr(self):
        print('Print from B before A')
        super(B, self).print_attr()
        print('Print from B after A')


b = B()
b.print_attr()
