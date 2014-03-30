class Point(object):

    @property
    def x(self):
        print('In getter `x`')
        return self._x

    @x.setter
    def x(self, value):
        print('In setter `x`')
        self._x = value

    @x.deleter
    def x(self):
        print('In deleter `x`')
        del self._x

    @property
    def y(self):
        print('In getter `y`')
        return self._y

    @y.setter
    def y(self, value):
        print('In setter `y`')
        self._y = value


start = Point()
start.x = 1
start.y = 1

del start.x

try:
    start.x
except AttributeError:
    print('Caught AttributeError')
