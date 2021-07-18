import pygame

from obj import Object

class Bullet(Object):
	def __init__(self,window):
		super().__init__(window)

	def copy_attributes(self, other):
		self.window = other.window
		self.width = other.width
		self.height = other.height
		self.image = other.image
		self.surface = other.surface
		self.vel = other.vel
		self.rect = pygame.Rect(other.rect.x, other.rect.y,other. rect.width, other.rect.height)
		self.limit = other.limit

	def update(self, deltaTime_s):
		self.rect.x += (self.vel[0] * deltaTime_s)
		self.rect.y += (self.vel[1] * deltaTime_s)
		if self.check_limit_position() == True:
			self.active = False
	