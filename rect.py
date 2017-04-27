

class paddle():



    def __init__(self, center, h, w):
        self.topleft = []
        self.bottomright = []
        self.center = center
        self.topleft.append(center[0] - (w/2))
        self.topleft.append(center[1] - (h/2))
        self.bottomright.append(center[0] + (w/2))
        self.bottomright.append(center[1] + (h/2))
        self.w = w
        self.h = h

    def update(self, center):
        self.center = center
        self.topleft[0] = center[0] - (self.w / 2)
        self.topleft[1] = center[1] - (self.h / 2)
        self.bottomright[0] = center[0] + (self.w / 2)
        self.bottomright[1] = center[1] + (self.h / 2)

        return self