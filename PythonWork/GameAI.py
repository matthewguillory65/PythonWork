import math
import pygame
import random
from VectorMath import *

class AIpoint(object):
    def __init__(self, vector):
        self.position = vector
        self.velocity = Vector(1, 0)
        self.max_speed = 15

    def __inits__(self, screenbounds):
        self.engine = pygame
        self.engine.inits()
        self._screen = self.engine.display.set_mode(screenbounds)

    def Steering(self, target):
        desired_velocity = Normalize(Vector(target.x - self.position.x, target.y - self.position.y))
        Vel = desired_velocity
        if Magnitude(Vector(target.x + self.position.x, target.y + self.position.y)) < 1:
            Vel = Normalize(Vector(-self.velocity.x / 1, -self.velocity.y / 1))
        return Vel

    def ApplyForce(self, force, deltatime):
        #Seeking
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.velocity.x += force.x * deltatime
            self.velocity.y += force.y * deltatime
        #Fleeing
        elif pygame.key.get_pressed()[pygame.K_n]:
            self.velocity.x -= force.x * deltatime * 2
            self.velocity.y -= force.y * deltatime * 2
        #Wandering
        Norm = Normalize(self.velocity)
        Direc = random.randrange(310)
        Newforce = Normalize(Vector(math.cos(Direc), math.sin(Direc)))
        self.lastforce = Newforce
        self.velocity.x -= Newforce.x
        self.velocity.y -= Newforce.y
        if Magnitude(self.velocity) > self.max_speed:
            newVec = Normalize(self.velocity)
            self.velocity = Vector(newVec.x * self.max_speed, newVec.y * self.max_speed)

    def UpdatePos(self):
        self.position.x += self.velocity.x
        print "Position x:", self.position.x
        self.position.y += self.velocity.y
        print "Position y:", self.position.y