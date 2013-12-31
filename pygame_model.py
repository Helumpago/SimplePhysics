
import pygame
from pygame.locals import *
from .model import Model

"""
" Creates a Model that uses Pygame as its graphics library
"""
class PygameModel(Model):
	"""
	" CONSTRUCTOR
	" @param string Name: Name for this object.
	" @param int fps: Maximum number of frames per second allowable.
	"""
	def __init__(self, Name = "PygameModel", fps = 60):
		Model.__init__(self, Name = Name, fps = fps)
		self.clock = pygame.time.Clock()

	"""
	" Limits the number of frames per second to the given number
	" 		and gets the number of miliseconds since the last frame.
	" @param number t: Maximum FPS
	" @return: Number of milliseconds since the last frame
	"""
	def tick(self, t):
		return self.clock.tick(t)

	"""
	" Decide which events should be run
	"""
	def collectEvents(self):
		## Check pygame events ##
		for pyevent in pygame.event.get():
			if pyevent.type == QUIT:
				self.events.getFirst("onQuit").fire = True