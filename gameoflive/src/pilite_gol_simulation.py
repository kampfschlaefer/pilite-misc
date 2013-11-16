# -*- coding: utf8 -*-

from gol import GameOfLive
from PiLiteEmulator import PiLITE

import threading
import time
import Tkinter as tk

class GolThread(threading.Thread):
    def __init__(self, pilite):
        super(GolThread, self).__init__(name='GameOfLive')

        self._run = True

        self.gol = GameOfLive(14, 9)

        self.gol.board[3][3:6] = [1, 1, 1]

        self.pilite = pilite

    def stop(self):
        self._run = False
        self.join()

    def run(self):
        time.sleep(10)
        #self.serialbuffer += '$$$SPEED100\r'
        self.pilite.keyEntry(d=1, S='A', i=None, P=None, s=None, v=None, V=None, W=None)
        time.sleep(2)
        #self.pilite.keyEntry(d=1, S='$$$SPEED10\r', i=None, P=None, s=None, v=None, V=None, W=None)
        #time.sleep(5)
        #self.pilite.keyEntry(d=1, S='Arnold', i=None, P=None, s=None, v=None, V=None, W=None)
        #time.sleep(5)
        #self.pilite.keyEntry(d=1, S='$$$ALL,ON\r', i=None, P=None, s=None, v=None, V=None, W=None)
        self.pilite.keyEntry(d=1, S='$$$F000000000000000000000000000000111000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\r', i=None, P=None, s=None, v=None, V=None, W=None)
        time.sleep(5)

        while self._run:
            print "Step!"
            cmd = '$$$F'
            for row in self.gol.board:
                cmd += ''.join([ str(i) for i in row ])
            print "Will send '{}' with length {}".format(cmd, len(cmd))
            self.pilite.keyEntry(d=1, S=(cmd+'\r'), i=None, P=None, s=None, v=None, V=None, W=None)
            #self.serialbuffer += cmd+'\r'

            self.gol.calculatenextboard()

            self._run=False
            time.sleep(5)

if __name__ == '__main__':
    root = tk.Tk()
    app = PiLITE(root,title='Pi-LITE v0.2')
    gol = GolThread(app)
    gol.start()
    root.mainloop()
    gol.stop()
