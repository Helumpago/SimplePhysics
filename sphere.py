
import pygame
from pygame.locals import *
from drawable import Drawable
from moveable import Moveable

"""
" Sphere class
"""
class Sphere(Drawable, Moveable):
	"""
	" CONSTRUCTOR
	" @param r: int: Radius of the sphere
	" @param color: (int Red, int Green, int Blue): Color for this object
	" @param pos: (int x, int y): Sphere's position
	"""
	def __init__(self, r = 1, pos = (0, 0), color = (255, 255, 255), velocity = (0, 0), parent = None):
		Moveable.__init__(self, velocity, parent = parent)
		self.radius = r
		self.pos = pos
		self.color = color

	"""
	" Get this object's position
	"""
	def getPos(self):
		return self.pos

	"""
	" Change this object's position
	"""
	def setPos(self, pos):
		self.pos = pos

	"""
	" Draw this object to the window
	"""
	def draw(self, window):
		pos = (round(self.pos[0]), round(self.pos[1]))
		pygame.draw.circle(window.view, self.color, pos, self.radius * window.scale, 0)