class A(object):

    @classmethod
    def class_method(cls, x):
        print('\t\tclass_method({}, {})'.format(cls, x))


a = A()
print('a.class_method(1):')
a.class_method(1)

print('A.class_method(1):')
A.class_method(1)
