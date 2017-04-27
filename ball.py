import random
import math


class ball:
    def __init__(self, xpos, ypos, vol):
        self.xpos = xpos
        self.ypos = ypos
        self.vol = vol
        self.yvol = 10
        self.xvol = 10

    def update(self, rect):

        if self.xpos + 10 >= 725:
            self.xvol = random.randint(5, self.vol) * -1
        if self.ypos + 10 >= 1320:
            self.yvol = random.randint(5, self.vol) * -1
        if self.xpos - 10 <= 0:
            self.xvol = random.randint(5, self.vol)
        if self.ypos - 10 <= -20:
            self.yvol = random.randint(5, self.vol)

        self.xpos += int(self.xvol)
        self.ypos += int(self.yvol)

        return self

