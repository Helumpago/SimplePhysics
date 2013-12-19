
import pygame
from pygame.locals import *
from vector2d import Vector2d
from moveable import Moveable
from drawable import Drawable

"""
" Defines a shape that acts like a ball
"""
class Circle(Moveable, Drawable):
	"""
	" CONSTRUCTOR
	" @param string name: Name for this object
	" @param Workspace parent: Reference to the workspace this object should be parented to
	" @param (int R, int G, int B) color: Color for this shape
	" @param Vector2d pos: Position of the circle
	" @param int radius: Circle's radius
	"""
	def __init__(self, Name = "circle", parent = None, color = (255, 255, 255), pos = Vector2d((0, 0)), radius = 1, velocity = Vector2d((0, 0))):
		Moveable.__init__(self, Name, parent, velocity = velocity)
		self.pos = pos
		self.radius = radius
		self.color = color

	"""
	" Get the shape's position
	" @return: Vector2d indicating the shape's position
	"""
	def getPos(self):
		return self.pos

	"""
	" Set the shape's position
	" @param Vector2d pos: New position
	"""
	def setPos(self, pos):
		self.pos = pos

	"""
	" Draw this object to the window
	"""
	def draw(self):

		if self.parent == None:
			return

		pos = Vector2d((round(self.pos.x * self.parent.scale), round(self.pos.y * self.parent.scale)))
		pygame.draw.circle(self.parent.view, self.color, pos.pos, round(self.radius * self.parent.scale), 0)