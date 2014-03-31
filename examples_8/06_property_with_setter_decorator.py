class Point(object):

    @property
    def x(self):
        print('In `x` getter')
        return self._x

    @x.setter
    def x(self, value):
        print('In `x` setter')
        self._x = value


    @property
    def y(self):
        print('In `y` getter')
        return self._y

    @y.setter
    def y(self, value):
        print('In `y` setter')
        self._y = value


start = Point()

start.x = 0
start.y = 0

print(start.x)
print(start.y)
