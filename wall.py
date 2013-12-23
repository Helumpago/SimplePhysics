
import pygame
from pygame.locals import *
from drawable import Drawable
from moveable import Moveable
from vector2d import Vector2d

"""
" Defines a stationary participant in collisions
"""
class Wall(Moveable, Drawable):
	"""
	" CONSTRUCTOR
	" @param string name: Name for this object
	" @param Workspace parent: Reference to the workspace this object should be parented to
	" @param (int R, int G, int B) color: Color for this shape
	" @param Vector2d pos1, pos2: Starting and ending position for the line
	"""
	def __init__(self, Name = "wall", parent = None, color = (255, 255, 255), pos1 = Vector2d((0, 0)), pos2 = Vector2d((0, 0))):
		Moveable.__init__(self, Name = Name, parent = parent, canCollide = True, anchored = True, velocity = Vector2d((0, 0)))
		Drawable.__init__(self)

		self.color = color
		self.pos1 = pos1
		self.pos2 = pos2

	"""
	" Draw a single line at the given positions
	"""
	def draw(self):
		if self.parent == None:
			return

		pos1 = Vector2d((round(self.pos1.x * self.parent.scale), round(self.pos1.y * self.parent.scale)))
		pos2 = Vector2d((round(self.pos2.x * self.parent.scale), round(self.pos2.y * self.parent.scale)))
		pygame.draw.line(self.parent.view, self.color, pos1.pos, pos2.pos, 1)