import pygame
import os

import constants
from player import Player
from enemy import Enemy
from bullet import Bullet
from mymath import MyMath
from button import Button

class App:
	def __init__(self):
		pygame.init()

		self.active = True
		self.screen_width = 800
		self.screen_height = 600
		self.clock = pygame.time.Clock()
		self.deltaTime_s = 0
		self.fps = 60
		self.bg_color = constants.WHITE
		self.bg_image = pygame.image.load('Assets/space.png')

		self.window = pygame.display.set_mode((self.screen_width,self.screen_height))
		pygame.display.set_caption('Space Invasion')

		self.play_button = Button(self.window,'Play')
		
		player = Player(self.window)
		player.load_image('Assets/spaceship_yellow.png')
		player.set_position((self.screen_width - player.rect.width)/2,self.screen_height - player.rect.height)
		player.set_velocity(200,200)
		player.rotate(180)
		self.player = player

		bullet_prototype = Bullet(self.window)
		bullet_prototype.load_image('Assets/pixel_laser_green.png')
		bullet_prototype.set_size(32,32)
		bullet_prototype.set_velocity(0,-400)

		player.set_bullet_prototype(bullet_prototype)

		self.objects = []
		self.create_enemy(10,3,800,200)

		
	def create_enemy(self, col, row, width, height):
		bullet_prototype = Bullet(self.window)
		bullet_prototype.load_image('Assets/pixel_laser_red.png')
		bullet_prototype.set_size(32,32)
		bullet_prototype.set_velocity(0,200)

		offset_x = width / col
		offset_y = height / row
		for y in range(0,row):
			for x in range(0, col):
				enemy = Enemy(self.window)
				enemy.load_image('Assets/spaceship_red.png')
				enemy.set_velocity(100,0)
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
		if self.play_button.active:
			if self.play_button.on_mouse_pressed():
				self.deltaTime_s = self.clock.get_time()/1000
				self.play_button.active = False
		else:
			self.deltaTime_s = self.clock.get_time()/1000
		

	def update(self, deltaTime_s):
		self.player.update(deltaTime_s)
		for object in self.objects:
			object.update(deltaTime_s)

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

		if self.objects == []:
			self.__init__()


	def render(self):
		self.window.fill(self.bg_color)
		self.window.blit(self.bg_image,pygame.Rect(0,0,self.screen_width,self.screen_height))
		self.player.render()
		for object in self.objects:
			object.render()
		if self.play_button.active:
			self.play_button.render()
		pygame.display.update()

	def run(self):
		while self.active:
			self.clock.tick(self.fps)
			self.check_events()
			self.update(self.deltaTime_s)
			self.render()

		pygame.quit()


	
if __name__ == '__main__':
	App().run()

