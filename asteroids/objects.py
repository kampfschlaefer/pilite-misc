# -*- coding: utf8 -*-

import math as m


class BaseObject(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def timetick(self, amount):
        pass


class BaseVelocityObject(BaseObject):
    def __init__(self, x, y, radiant, velocity):
        super(BaseVelocityObject, self).__init__(x, y)
        self.radiant = radiant
        self.velocity = velocity

    def timetick(self, amount):
        movement = self.velocity * amount
        #print("movement: %g" % movement)
        self.x = self.x + m.cos(self.radiant) * movement
        self.y = self.y + m.sin(self.radiant) * movement

    def changevelocity(self, diff):
        self.velocity += diff

    def changeradiant(self, diff):
        self.radiant += diff
