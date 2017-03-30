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

def Magnitude(Vec):
    return math.sqrt(Vec.x * Vec.x + Vec.y * Vec.y)

def Normalize(Vec):
    Mag = Magnitude(Vec)
    if Mag > 0:
        return Vector(Vec.x / Mag, Vec.y / Mag)
    else:
        return Vector(0, 0)

def Velocity(Truncate):
    return Truncate(Velocity + Steering, max_speed)

