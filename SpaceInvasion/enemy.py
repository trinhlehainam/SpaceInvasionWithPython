import pygame
from random import uniform

from ship import Ship

class Enemy(Ship):
	def __init__(self, window):
		super().__init__(window)
		self.dir = 1;
		self.distance = 100
		self.origin = self.rect.x
		self.bullet_cooldown = uniform(0,4)

	def set_move_range(self,distance):
		self.origin = self.rect.x
		self.distance = distance

	def check_distance(self):
		ret = False
		if self.rect.x <= self.origin:
			self.rect.x = self.origin
			ret = True
		if self.rect.x >= (self.origin + self.distance - self.rect.width):
			self.rect.x = (self.origin + self.distance - self.rect.width)
			ret = True
		return ret

	def update(self, deltaTime_s):
		self.rect.x += (self.vel[0] * deltaTime_s)
		
		if self.check_distance():
			self.dir  = (((self.dir + 1) % 2) - 0.5) * 2
			self.vel[0] *= self.dir

		if self.bullet_cooldown <= 0:
			self.shoot_bullet()
			self.bullet_cooldown = uniform(0,4)

		self.bullet_update(deltaTime_s)

		self.bullet_cooldown -= deltaTime_s



		

		

