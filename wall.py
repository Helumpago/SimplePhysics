
import pygame
from pygame.locals import *
from moveable import Moveable
from drawable import Drawable

"""
" Defines an object that participates in collisions but is itself unaffected.
"""
class  Wall(Drawable, Moveable):
	"""
	" CONSTRUCTOR
	" @param (int x, int y) pos1: Position of the first corner of the wall
	" @param (int x, int y) pos2: Position of the second corner of the wall
	" @param color: (int Red, int Green, int Blue): Color for this object
	"""
	def __init__(self, pos1 = (0, 0), pos2 = (0, 0), color = (255, 255, 255)):
		Moveable.__init__(self, anchored = True, velocity = (0, 0))
		self.pos1 = pos1
		self.pos2 = pos2
		self.color = color

	"""
	" Get this object's position
	"""
	def getPos():
		return pos

	"""
	" Draw this object to the window
	"""
	def draw(self, window):
		pygame.draw.line(window.view, self.color, self.pos1, self.pos2, 1)