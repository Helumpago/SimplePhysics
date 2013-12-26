
import pygame
from pygame.locals import *
from model import Model

"""
" Creates a Model that uses Pygame as its graphics library
"""
class PygameModel(Model):
	"""
	" CONSTRUCTOR
	" @param string Name: Name for this object.
	" @param int fps: Maximum number of frames per second allowable.
	"""
	def __init__(self, Name = "Model", fps = 60):
		Model.__init__(self, Name = Name, fps = fps)
		self.clock = pygame.time.Clock()

	"""
	" Limits the number of frames per second to the given number
	" 		and gets the number of miliseconds since the last frame.
	" @param number t: Maximum FPS
	" @return: Number of miliseconds since the last frame
	"""
	def tick(self, t):
		return self.clock.tick(t)

	def step(self):
		print("Hi!")