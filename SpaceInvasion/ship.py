import pygame

from obj import Object
from bullet import Bullet

class Ship(Object):
	def __init__(self,window):
		super().__init__(window)
		self.bullets = []
		self.bullet_prototype = None
		self.max_bullets = 3

	def set_bullet_prototype(self, bullet_prototype):
		self.bullet_prototype = bullet_prototype

	def shoot_bullet(self):
		if(len(self.bullets) < self.max_bullets):
			self.bullet_prototype.set_position(self.rect.x + (self.rect.width-self.bullet_prototype.rect.width)/2, self.rect.y)
			new_bullet = Bullet(self.window)
			new_bullet.copy_attributes(self.bullet_prototype)
			self.bullets.append(new_bullet)

	def bullet_update(self, deltaTime_s):
		for bullet in self.bullets:
			bullet.update(deltaTime_s)

		for bullet in self.bullets:
			if bullet.active == False:
				self.bullets.remove(bullet)

	def render(self):
		assert self.surface != None
		self.window.blit(self.surface, self.rect)

		for bullet in self.bullets:
			bullet.render()

