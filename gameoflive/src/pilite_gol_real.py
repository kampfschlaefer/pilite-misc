# -*- coding: utf8 -*-

from gol import GameOfLive

import serial
import time
import random
import logging

if __name__ == '__main__':
    logging.basicConfig(level='DEBUG')

    x, y = (14, 9)
    gol = GameOfLive(x, y)

    #for i in range(random.randint(x*y/10, x*y/4)):
        #gol.board[random.randrange(x)][random.randrange(y)] = 1

    gol.board[0][0:3] = [0, 1, 0]
    gol.board[1][0:3] = [0, 0, 1]
    gol.board[2][0:3] = [1, 1, 1]
    #gol.board[3][0:5] = [0, 0, 1, 1]


    s = serial.Serial('/dev/ttyAMA0', baudrate=9600)
    s.setTimeout(1)

    s.write('$$$ALL,OFF\r')

    #starttime = time.time()

    #while time.time() < starttime + 60:
    while True:
        cmd = '$$$F'
        for row in gol.board:
            cmd += ''.join([ str(i) for i in row])

        s.write(cmd + '\r')

        gol.calculatenextboard()

        time.sleep(0.1)
