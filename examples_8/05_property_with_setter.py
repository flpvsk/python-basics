class Point(object):

    def _get_x(self):
        print('In get x')
        return self._x

    def _set_x(self, value):
        print('In set x to %r' % value)
        self._x = value

    def _get_y(self):
        print('In get y')
        return self._y

    def _set_y(self, value):
        print('In set y to %r' % value)
        self._y = value


    x = property(_get_x, _set_x)
    y = property(_get_y, _set_y)


start = Point()

start.x = 0
start.y = 0

print('start.x is %r' % start.x)
print('start.y is %r' % start.y)


