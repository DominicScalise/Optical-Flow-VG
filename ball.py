import random
import math


class ball:
    def __init__(self, xpos, ypos, vol):
        self.xpos = xpos
        self.ypos = ypos
        self.vol = vol
        self.yvol = vol
        self.xvol = vol

    def update(self, rectL, rectR):
        scoreL = 0
        scoreR = 0

        if self.xpos + 10 >= 480:
            self.xvol = random.randint(5, self.vol) * -1
        if self.ypos + 10 >= 640:
             #self.yvol = random.randint(5, self.vol) * -1
            scoreL += 1
        if self.xpos - 10 <= 0:
            self.xvol = random.randint(5, self.vol)
        if self.ypos - 10 <= 0:
             #self.yvol = random.randint(5, self.vol)
            scoreR += 1

        if (rectR.center[1] - (rectR.h/2) <= self.xpos <= rectR.center[1] + (rectR.h/2)):
            if self.ypos + 10 >= (rectR.center[0] - (rectL.w/2)):
                self.yvol = random.randint(5, self.vol) * -1

        if ((rectL.center[1] - (rectL.h/2)) <= self.xpos <= (rectL.center[1] + (rectL.h/2))):
            if self.ypos - 10 <= (rectL.center[0] + (rectL.w/2)):
                self.yvol = random.randint(5, self.vol)

        self.xpos += int(self.xvol)
        self.ypos += int(self.yvol)

        return self, scoreL, scoreR

    def start(self):
        self.xvol = int(self.vol)
        self.yvol = int(self.vol)
        return self

