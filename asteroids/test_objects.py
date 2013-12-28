# -*- coding: utf8 -*-

import math as m
from pytest import mark

from objects import (
    BaseObject,
    BaseVelocityObject,
)


class TestBaseObject(object):
    def setup(self):
        self.obj = BaseObject(0, 0)

    def test_init(self):
        assert self.obj.x == 0
        assert self.obj.y == 0

    def test_timetick(self):
        self.obj.timetick(1)
        assert self.obj.x == 0
        assert self.obj.y == 0

class TestBaseVelocityObject(object):
    def setup(self):
        self.obj = BaseVelocityObject(0, 0, 0, 1)

    def test_velocityinit(self):
        assert (self.obj.x, self.obj.y) == (0, 0)
        assert self.obj.radiant == 0
        assert self.obj.velocity == 1

    def test_movement1(self):
        self.obj.timetick(1)
        assert self.obj.x == 1
        assert self.obj.y == 0
        self.obj.timetick(0.5)
        assert self.obj.x == 1.5
        assert self.obj.y == 0

    @mark.parametrize('radiant, x, y', [
        (0, 1, 0),
        (m.pi/2, 0, 1),
        (m.pi, -1, 0),
        (m.pi*1.5, 0, -1),
    ])
    def test_movement2(self, radiant, x, y):
        self.obj.radiant = radiant
        self.obj.timetick(1)
        assert self.obj.x - x < 1e-5
        assert self.obj.y - y < 1e-5

    def test_movement3(self):
        self.obj.radiant = 0
        self.obj.velocity = 2
        self.obj.timetick(0.5)
        assert self.obj.x == 1
        assert self.obj.y == 0
        self.obj.timetick(0.5)
        assert self.obj.x == 2
        assert self.obj.y == 0
        self.obj.timetick(1)
        assert self.obj.x == 4
        assert self.obj.y == 0

    def test_changevelocity(self):
        self.obj.timetick(1)
        assert self.obj.x == 1
        self.obj.changevelocity(1)
        self.obj.timetick(1)
        assert self.obj.x == 3
        self.obj.changevelocity(-1)
        self.obj.timetick(1)
        assert self.obj.x == 4
        self.obj.changevelocity(-1)
        self.obj.timetick(1)
        assert self.obj.x == 4

    def test_changeradiant(self):
        for x, y in ((1, 0), (1, 1), (0, 1), (0, 0)):
            self.obj.timetick(1)
            assert self.obj.x - x < 1e-5
            assert self.obj.y - y < 1e-5
            self.obj.changeradiant(m.pi/2)
