import pygame

from ship import Ship

class Input:
	def __init__(self,up=pygame.K_UP,down=pygame.K_DOWN,left=pygame.K_LEFT,right=pygame.K_RIGHT,shoot=pygame.K_SPACE):
		self.up = up
		self.down = down
		self.left = left
		self.right = right
		self.shoot = shoot

class Player(Ship):
	def __init__(self,window):
		super().__init__(window)
		self.input = Input()
		self.keys = pygame.key.get_pressed()
		self.old_keys = pygame.key.get_pressed()

	def set_move_keys(self,left, top, right ,bottom, shoot):
		self.input = MoveKey(left, top, right ,bottom, shoot)

	def update(self, deltaTime_s):
		# Movement
		self.keys = pygame.key.get_pressed()

		if self.keys[self.input.up]:
			self.rect.y -= (self.vel[1] * deltaTime_s)
		elif self.keys[self.input.down]:
			self.rect.y += (self.vel[1] * deltaTime_s)
		elif self.keys[self.input.left]:
			self.rect.x -= (self.vel[0] * deltaTime_s)
		elif self.keys[self.input.right]:
			self.rect.x += (self.vel[0] * deltaTime_s)
		#

		if self.keys[self.input.shoot] and self.old_keys[self.input.shoot] == False:
			self.shoot_bullet()

		self.bullet_update(deltaTime_s)
		self.check_limit_position()

		self.old_keys = pygame.key.get_pressed()

	def render(self):
		assert self.surface != None
		self.window.blit(self.surface, self.rect)

		for bullet in self.bullets:
			bullet.render()