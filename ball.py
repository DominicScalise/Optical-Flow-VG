
# import pygame, sys, pygame.locals
# pygame.init()

# screen = pygame.display.set_mode((800,800), 0, 30)
# WHITE = (255,255,255)
# screen.fill(WHITE)
# ball = pygame.draw.circle(frame, (60,100,100) , (400, 400) , (40, 0)
# y = 400
# x = 400
# velocity = 1

# while true:
# 	for event in pygame.event.get():
# 	pressed = pygame.key.get_pressed()
# 	if pressed[K_RIGHT]: x + 5
# 	if pressed[K_LEFt]: X - 5
# 	pygame.display.update()

import random

class ball:

 
	def __init__ (self, xpos, ypos, vol):
		self.xpos = xpos
		self.ypos = ypos
		self.vol = vol
		self.yvol = 10
		self.xvol = 10

	def update(self, rect):
		
		y = random.randint(10, 15)
		x = random.randint(10, 15)

		if self.xpos + 10 >= 600:
			self.xvol = x * - 1 
		if self.ypos + 10 >= 600:
			self.yvol = y * - 1 
		if self.xpos - 10 <= 0:				
			self.xvol = x 
		if self.ypos - 10 <= 0:
			self.yvol = y 

		self.xpos += self.xvol
		self.ypos += self.yvol			
		return self
