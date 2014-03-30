class A(object):

    @staticmethod
    def method(*args):
        print("\t\targs {}".format(args))


a = A()

print('Instance method():')
a.method()

print('Instance method("argument")')
a.method("argument")

print('Class method():')
A.method()
