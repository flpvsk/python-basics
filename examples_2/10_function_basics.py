from examples_2.utils import print_stars


def f():
    pass

print("f() = %r" % f())
print_stars()


def f_docstring():
    """Empty function. Does nothing, returns None."""
    pass

help(f_docstring)
print_stars()


def mean(v1, v2):
    """Calculates mean value.
    >>> mean(1, 1)
    1.0
    >>> mean(2,4)
    3.0
    """
    return (v1 + v2) / 2.0

print("mean(1, 1) = %r" % mean(1, 1))
print("mean(2, 4) = %r" % mean(2, 4))
help(mean)
print_stars()


# Blocks have scopes
if True:
    def f_true():
        pass
else:
    def f_false():
        pass

print('f_true:  %r' % f_true)
print('f_false: %r' % f_false)
