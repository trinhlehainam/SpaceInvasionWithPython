import pygame
import os

import constants
from player import Player
from enemy import Enemy
from bullet import Bullet
from mymath import MyMath

class App:
	def __init__(self):
		pygame.init()

		self.active = True
		self.screen_width = 800
		self.screen_height = 600
		self.clock = pygame.time.Clock()
		self.fps = 60
		self.bg_color = constants.WHITE
		self.bg_image = pygame.image.load('Assets/space.png')

		self.window = pygame.display.set_mode((self.screen_width,self.screen_height))
		pygame.display.set_caption('My Engine')

		
		player = Player(self.window)
		player.load_image('Assets/spaceship_yellow.png')
		player.set_position((self.screen_width - player.rect.width)/2,self.screen_height - player.rect.height)
		player.set_velocity(5,5)
		player.rotate(180)
		self.player = player

		bullet_prototype = Bullet(self.window)
		bullet_prototype.load_image('Assets/pixel_laser_green.png')
		bullet_prototype.set_size(32,32)
		bullet_prototype.set_velocity(0,-10)

		player.set_bullet_prototype(bullet_prototype)

		self.objects = []
		self.create_enemy(10,3,800,200)

		
	def create_enemy(self, col, row, width, height):
		bullet_prototype = Bullet(self.window)
		bullet_prototype.load_image('Assets/pixel_laser_red.png')
		bullet_prototype.set_size(32,32)
		bullet_prototype.set_velocity(0,3)

		offset_x = width / col
		offset_y = height / row
		for y in range(0,row):
			for x in range(0, col):
				enemy = Enemy(self.window)
				enemy.load_image('Assets/spaceship_red.png')
				enemy.set_velocity(2,0)
				enemy.set_position(x * offset_x, y * offset_y)
				enemy.set_move_range(offset_x)
				enemy.set_bullet_prototype(bullet_prototype)
				self.objects.append(enemy)


	def check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.active = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.active = False

	def update(self):
		self.player.update()
		for object in self.objects:
			object.update()

		for bullet in self.player.bullets:
			for object in self.objects:
				if MyMath.check_rect_rect(bullet.rect, object.rect):
					object.active = False
					bullet.active = False

		for object in self.objects:
			for bullet in object.bullets:
				if MyMath.check_rect_rect(self.player.rect, bullet.rect):
					bullet.active = False

		for object in self.objects:
			if object.active == False:
				self.objects.remove(object)


	def render(self):
		self.window.fill(self.bg_color)
		self.window.blit(self.bg_image,pygame.Rect(0,0,self.screen_width,self.screen_height))
		self.player.render()
		for object in self.objects:
			object.render()
		pygame.display.update()

	def run(self):
		while self.active:
			self.clock.tick(self.fps)
			self.check_events()
			self.update()
			self.render()

		pygame.quit()


	
if __name__ == '__main__':
	App().run()

