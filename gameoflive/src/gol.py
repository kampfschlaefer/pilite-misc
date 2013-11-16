# -*- coding: utf8 -*-
#

import logging
import random

class GameOfLive(object):
    def __init__(self, sizex, sizey):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.resizeboard(sizex, sizey)

    def createboard(self, sizex, sizey):
        return [ [ 0 for y in range(sizey) ] for x in range(sizex) ]

    def resizeboard(self, sizex, sizey):
        self.sizex = sizex
        self.sizey = sizey
        self.board = self.createboard(sizex, sizey)

    def printboard(self):
        output = []
        for row in self.board:
            line = ' '.join([ '{}'.format([' ', '0'][i]) for i in row ])
            output.append(line)
        self.logger.info('current state of the board is:\n{}'.format('\n'.join(output)))

    def getaliveneighbors(self, x, y):
        neighbors = 0
        for i,j in ((x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)):
            try:
                neighbors += self.board[i][j]
            except IndexError:
                #self.logger.warn('Reached outside the board with {}, {}'.format(i, j))
                pass
        return neighbors

    def calculatenextboard(self):
        nextboard = self.createboard(self.sizex, self.sizey)

        for x in range(self.sizex):
            for y in range(self.sizey):
                neighbors = self.getaliveneighbors(x, y)
                if self.board[x][y] and neighbors in [2, 3]:
                    nextboard[x][y] = 1
                if not self.board[x][y] and neighbors == 3:
                    nextboard[x][y] = 1

        self.board = nextboard

if __name__=='__main__':
    logging.basicConfig(level='DEBUG')

    random.seed()

    x, y = (10, 16)
    gol = GameOfLive(x, y)

    for i in range(random.randint(x*y/10, x*y/4)):
        gol.board[random.randrange(x)][random.randrange(y)] = 1

    gol.printboard()

    for i in range(10):
        gol.calculatenextboard()
        gol.printboard()
