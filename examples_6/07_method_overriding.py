class A(object):
    attr = 'a'

    def print_attr(self):
        print(self.attr)


class B(A):
    def print_attr(self):
        print('Don\'t know what to print, sorry')


b = B()
b.print_attr()
