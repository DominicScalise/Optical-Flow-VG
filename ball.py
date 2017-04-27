import random
import math


class ball:
    def __init__(self, xpos, ypos, vol):
        self.xpos = xpos
        self.ypos = ypos
        self.vol = vol
        self.yvol = 10
        self.xvol = 10

    def update(self, rectL, rectR):

        if self.xpos + 10 >= 800:
            self.xvol = random.randint(5, self.vol) * -1
        # if self.ypos + 10 >= 1300:
        #     self.yvol = random.randint(5, self.vol) * -1
        if self.xpos - 10 <= 0:
            self.xvol = random.randint(5, self.vol)
        # if self.ypos - 10 <= 0:
        #     self.yvol = random.randint(5, self.vol)

        if (rectR.center[0] - rectR.h/2 <= self.xpos <= rectR.center[0] + rectR.h/2):
            if self.ypos + 10 >= rectR.center - rectL.w/2:
                self.yvol = random.randint(5, self.vol) * -1

        if (rectL.center[0] - rectL.h/2 <= self.xpos <= rectL.center[0] + rectL.h/2):
            if self.ypos - 10 <= rectL.center + rectL.w/2:
                self.yvol = random.randint(5, self.vol)

        self.xpos += int(self.xvol)
        self.ypos += int(self.yvol)

        return self

