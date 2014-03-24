class A(object):
    attr = 'a'

    def print_attr(self):
        print(self.attr)


class B(A):
    attr = 'b'

b = B()
b.print_attr()
