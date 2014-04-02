class Point(object):

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        print('\tin get x')
        return self._x

    @property
    def y(self):
        print('\tin get y')
        return self._y


start = Point(0, 0)
print('start.x is %r' % start.x)
print('start.y is %r' % start.y)

try:
    start.x = 1
except AttributeError:
    # by default, property is read-only
    print('Caught AttributeError')


# Although you can change internal state of object.
# But you shouldn't.
start._x = 1
print('start.x is %r' % start.x)

