import math
from VectorMath import *

class AIpoint(object):
    def __init__(self, vector):
        self.position = vector
        self.velocity = Vector(1, 0)
        self.max_speed = 15

    def Steering(self, target):
        desired_velocity = Normalize(Vector(target.x - self.position.x, target.y - self.position.y))
        Vel = desired_velocity
        if Magnitude(Vector(target.x - self.position.x, target.y - self.position.y)) < 20:
            Vel = Normalize(Vector(-self.velocity.x / 50, -self.velocity.y / 50))
        return Vel

    def ApplyForce(self, force):
        self.velocity = Vector(self.velocity.x + force.x, self.velocity.y + force.y)
        if Magnitude(self.velocity) > self.max_speed:
            newVec = Normalize(self.velocity)
            self.velocity = Vector(newVec.x * self.max_speed, newVec.y * self.max_speed)

    def UpdatePos(self):
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y