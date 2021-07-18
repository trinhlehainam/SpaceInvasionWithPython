import pygame.font
import pygame.mouse
import pygame.key

class Button:
	def __init__(self,window,text):
		self.active = True
		self.window = window
		self.text = text
		self.width, self.height = 200, 50
		self.button_color = (0,255,0)
		self.text_color = (255,255,255)
		self.font = pygame.font.SysFont(None,48)
		self.rect = pygame.Rect(0,0,self.width,self.height)
		self.rect.center = window.get_rect().center

		self._prepare_text(text)

	def _prepare_text(self,text):
		self.text_img = self.font.render(text,True,self.text_color,self.button_color)
		self.text_img_rect = self.text_img.get_rect()
		self.text_img_rect.center = self.rect.center

	def set_button_color(self,color):
		self.button_color = color

	def set_text_color(self,color):
		self.text_color = color

	def set_position(self,x,y):
		self.rect.center = (x,y)
		self.text_img_rect.center = self.rect.center

	def on_mouse_entered(self) -> bool:
		mouse_pos = pygame.mouse.get_pos()
		is_in_range_x = mouse_pos[0] >= self.rect.x and mouse_pos[0] <= (self.rect.x + self.rect.width)
		is_in_range_y = mouse_pos[1] >= self.rect.y and mouse_pos[1] <= (self.rect.y + self.rect.height)
		return is_in_range_x and is_in_range_y

	def on_mouse_pressed(self) -> bool:
		return pygame.mouse.get_pressed()[0] and self.on_mouse_entered()

	def render(self):
		if self.on_mouse_pressed():
			self.text_img = self.font.render(self.text,True,self.text_color,tuple(color/3 for color in self.button_color))
			self.window.fill(tuple(color/3 for color in self.button_color), self.rect)
		elif self.on_mouse_entered():
			self.text_img = self.font.render(self.text,True,self.text_color,tuple(color/1.5 for color in self.button_color))
			self.window.fill(tuple(color/1.5 for color in self.button_color), self.rect)
		else:
			self.text_img = self.font.render(self.text,True,self.text_color,self.button_color)
			self.window.fill(self.button_color, self.rect)

		self.window.blit(self.text_img, self.text_img_rect)


