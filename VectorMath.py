import math

#This is my vector
class Vector(object):
    def __init__(self, xn, yn):
        self._x = xn
        self._y = yn

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

def Magnitude(x, y):
    return math.sqrt(x * x + y * y)

def Normalize(x, y):
    Mag = Magnitude(x, y)
    return Vector(x / Mag, y / Mag)

# class UpdateStuff(object):
#     def __init__(self, dostuff)
    