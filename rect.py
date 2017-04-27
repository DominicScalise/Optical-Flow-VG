

class paddle():

    topleft = [0, 0]
    bottomright = [0, 0]

    def __init__(self, center, h, w):
        self.center = center
        self.topleft[0] = center[0] - h/2
        self.topleft[1] = center[1] - w/2
        self.bottomright[0] = center[0] + h/2
        self.bottomright[1] = center[1] + w/2
        self.w = w
        self.h = h

    def update(self, center):
        self.center = center
        self.topleft[0] = center[0] - self.h / 2
        self.topleft[1] = center[1] - self.w / 2
        self.bottomright[0] = center[0] + self.h / 2
        self.bottomright[1] = center[1] + self.w / 2

        return self