# -*- coding: utf8 -*-

import math as m

from pytest import mark

from .viewport import ViewPort


class TestViewPort(object):
    def setup(self):
        self.view = ViewPort(xinterval=(0, 10), yinterval=(-4, 4), direction=0, basex=0, basey=0)

    def test_init(self):
        assert self.view.xinterval == (0, 10)
        assert self.view.yinterval == (-4, 4)

    @mark.parametrize('coord, inside, direction, base', (
        # Unrotated
        ((0, 0), True, 0, (0, 0)),
        ((1, 0), True, 0, (0, 0)),
        ((10, 0), True, 0, (0, 0)),
        ((11, 0), False, 0, (0, 0)),
        ((0, 0), True, 0, (0, 0)),
        ((0, 4), True, 0, (0, 0)),
        ((0, 5), False, 0, (0, 0)),
        ((0, -4), True, 0, (0, 0)),
        ((0, -5), False, 0, (0, 0)),
        # Rotated backwards
        ((0, 0), True, m.pi, (0, 0)),
        ((1, 0), False, m.pi, (0, 0)),
    ))
    def test_in_viewport(self, coord, inside, direction, base):
        self.view.direction = direction
        self.view.base = base
        assert self.view.in_viewport(coord[0], coord[1]) == inside
