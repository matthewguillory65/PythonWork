import math
from VectorMath import *

class AIpoint(object):
    def __init__(self, vector):
        self.position = vector
        self.velocity = Vector(1, 0)
        self.max_speed = 25

    def Steering(self, target):
        desired_velocity = Normalize(Vector(target.x - self.position.x, target.y - self.position.y))
        #Vel = Vector((desired_velocity.x - self.velocity.x) * self.max_speed, (desired_velocity.y - self.velocity.y) * self.max_speed)
        Vel = desired_velocity
        if Magnitude(Vector(target.x - self.position.x, target.y - self.position.y)) < 15:
            Vel = Normalize(Vector(-self.velocity.x / 1, -self.velocity.y / 1))
        return Vel

    def ApplyForce(self, force):
        self.velocity = Vector(self.velocity.x + force.x, self.velocity.y + force.y)
        if Magnitude(self.velocity) > self.max_speed:
            newVec = Normalize(self.velocity)
            self.velocity = Vector(newVec.x * self.max_speed, newVec.y * self.max_speed)

    def UpdatePos(self):
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y