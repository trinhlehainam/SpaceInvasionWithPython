import pygame

class MyMath:
	@staticmethod
	def check_overlap(min_a,max_a,min_b,max_b) -> bool:
		return min_a <= max_b and max_a >= min_b

	@staticmethod
	def check_rect_rect(rect_a,rect_b) -> bool:
		check_horizontal = MyMath.check_overlap(
			rect_a.x, rect_a.x + rect_a.width,
			rect_b.x, rect_b.x + rect_b.width)
		check_vertical = MyMath.check_overlap(
			rect_a.y, rect_a.y + rect_a.height,
			rect_b.y, rect_b.y + rect_b.height)
		return check_horizontal and check_vertical 
