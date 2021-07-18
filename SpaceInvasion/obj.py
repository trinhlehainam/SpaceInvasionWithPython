import pygame

class RangeLimit:
	def __init__(self, left, top, right ,bottom):
		self.left = left
		self.top = top
		self.right = right
		self.bottom = bottom

class Object:
	def __init__(self,window):
		self.active = True
		self.window = window
		self.width = 32
		self.height = 32
		self.image = None
		self.surface = None
		self.vel = [0,0]
		self.rect = pygame.Rect(0,0,self.width,self.height)

		window_size = pygame.display.get_window_size()
		self.limit = RangeLimit(0,0,window_size[0],window_size[1])

	def load_image(self, path):
		self.image = pygame.image.load(path)
		self.surface = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

	def set_rect(self,x,y,width,height):
		self.rect = pygame.Rect(x,y,width,height)
		self.surface = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

	def set_position(self,x,y):
		self.rect.x = x
		self.rect.y = y

	def set_size(self, width, height):
		self.rect.width = width
		self.rect.height = height
		self.surface = pygame.transform.scale(self.surface, (width,height))

	def set_velocity(self,x,y):
		self.vel[0] = x
		self.vel[1] = y

	def set_position_limit(self,left,top,right,bottom):
		self.limit = RangeLimit(left,top,right,bottom)

	def set_left_right_limit(self,left,right):
		self.limit.left = left
		self.limit.right = right

	def rotate(self, angle):
		self.surface = pygame.transform.rotate(self.surface, angle)

	def check_left_right_limit(self):
		ret = False
		if self.rect.x <= self.limit.left:
			self.rect.x = self.limit.left
			ret = True
		if self.rect.x >= (self.limit.right - self.rect.width):
			self.rect.x = self.limit.right - self.rect.width
			ret = True
		return ret

	def check_top_bottom_limit(self):
		ret = False
		if self.rect.y <= self.limit.top:
			self.rect.y = self.limit.top
			ret = True
		if self.rect.y >= (self.limit.bottom - self.rect.height):
			self.rect.y = self.limit.bottom - self.rect.height
			ret = True
		return ret

	def check_limit_position(self):
		"""Resolve position in limit range"""
		ret = False
		if self.rect.x <= self.limit.left:
			self.rect.x = self.limit.left
			ret = True
		if self.rect.x >= (self.limit.right - self.rect.width):
			self.rect.x = self.limit.right - self.rect.width
			ret = True
		if self.rect.y <= self.limit.top:
			self.rect.y = self.limit.top
			ret = True
		if self.rect.y >= (self.limit.bottom - self.rect.height):
			self.rect.y = self.limit.bottom - self.rect.height
			ret = True

		return ret
		""""""

	def render(self):
		assert self.surface != None
		if self.active:
			self.window.blit(self.surface, self.rect)