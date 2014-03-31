class A(object):

    def _method(*args):
        print('\t\targs: {}'.format(args))


    method = staticmethod(_method)


a = A()

print('Instance _method():')
a._method()

print('Instance _method("argument"):')
a._method("argument")

print('Instance method():')
a.method()

print('Instance method("argument")')
a.method("argument")

print('Class method():')
A.method()
