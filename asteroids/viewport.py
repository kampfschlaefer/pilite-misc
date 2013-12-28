# -*- coding: utf8 -*-


class ViewPort(object):
    def __init__(self, xinterval, yinterval, direction, basex, basey):
        self.xinterval = xinterval
        self.yinterval = yinterval
        self.direction = direction
        self.base = (basex, basey)

    def in_viewport(self, x, y):
        return (
            self.xinterval[0] <= x 
            and
            x <= self.xinterval[1]
            and
            self.yinterval[0] <= y 
            and
            y <= self.yinterval[1]
        )
