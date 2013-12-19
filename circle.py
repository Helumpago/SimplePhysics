
import pygame
from pygame.locals import *
from vector2d import Vector2d
from base_obj import BaseObj
from drawable import Drawable

"""
" Defines a shape that acts like a ball
"""
class Circle(BaseObj, Drawable):
	"""
	" CONSTRUCTOR
	" @param string name: Name for this object
	" @param Workspace parent: Reference to the workspace this object should be parented to
	" @param (int R, int G, int B) color: Color for this shape
	" @param Vector2d pos: Position of the circle
	" @param int radius: Circle's radius
	"""
	def __init__(self, Name = "circle", parent = None, color = (255, 255, 255), pos = Vector2d((0, 0)), radius = 1):
		BaseObj.__init__(self, Name, parent)
		self.pos = pos
		self.radius = radius
		self.color = color

	"""
	" Draw this object to the window
	"""
	def draw(self):
		if self.parent == None:
			return

		pos = (round(self.pos.x * self.parent.scale), round(self.pos.y * self.parent.scale))
		pygame.draw.circle(self.parent.view, self.color, pos, round(self.radius * self.parent.scale), 0)