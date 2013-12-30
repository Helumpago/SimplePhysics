
"""
" This file contains definitions for how regions should be drawn using Pygame
"""

import pygame
from pygame.locals import *
from drawable import Drawable
from region import RectRegion, CircleRegion
from pygame_view import PygameView

"""
" Allows the CircleRegion class to draw itself
"""
class PygameCircle(CircleRegion, Drawable):
	"""
	" CONSTRUCTOR
	" @param BaseObj parent: Object to which the new object should be parented.
	" 		Expected to be either a BaseObj, subclass of BaseObj, or None
	" @param string Name: Name for this object.
	" @param number radius: Radius of the circle. Can make it include the entire
	" 		world by setting it equal to (float("inf"), float("inf"))
	" @param (posX, posY) pos: Center of this region
	" @param number scale: Scale to apply to all objects rendering themselves in this window
	" @param (int R, int G, int B) color: RGB color for this shape
	"""
	def __init__(self, parent = None, Name = "Circle", radius = 1, pos = (0, 0), scale = 1, color = (0, 0, 0)):
		CircleRegion.__init__(self, parent = parent, Name = Name, radius = radius, pos = pos, scale = scale)
		Drawable.__init__(self)
		self.color = color

	"""
	" What this object should do during the render stage
	"""
	def draw(self, view = None):
		## If this shape doesn't have a View object as an ancestor, don't do anything ##
		if view == None:
			return

		if isinstance(view, PygameView) != True:
			raise TypeError("PygameCircle objects can only draw to PygameView objects")

		pos = self.pos.getAValue()
		scale = self.scale.getAValue()
		pos = (round(pos[0] * scale), round(pos[1] * scale))
		pygame.draw.circle(view.window, self.color, pos, round(self.radius.getValue() * scale), 0)

"""
" Draws a line across a RectRegion
"""
class PygameLine(RectRegion, Drawable):
	"""
	" CONSTRUCTOR
	" @param BaseObj parent: Object to which the new object should be parented.
	" 		Expected to be either a BaseObj, subclass of BaseObj, or None
	" @param string Name: Name for this object.
	" @param (number sizeX, number sizeY) size: Size of this region. Can make it include the entire
	" 		world by setting it equal to (float("inf"), float("inf"))
	" @param (posX, posY) pos: Center of this region
	" @param number scale: Scale to apply to all objects rendering themselves in this window
	"""
	def __init__(self, parent = None, Name = "Line", size = (0, 0), pos = (0, 0), scale = 1, color = (0, 0, 0)):
		RectRegion.__init__(self, parent = parent, Name = Name, size = size, pos = pos, scale = scale)
		Drawable.__init__(self)
		self.color = color

	def draw(self, view = None):
		## If this shape doesn't have a View object as an ancestor, don't do anything ##
		if view == None:
			return

		if isinstance(view, PygameView) != True:
			raise TypeError("PygameCircle objects can only draw to PygameView objects")

		pos = self.pos.getAValue()
		scale = self.scale.getAValue()
		pos = (round(pos[0] * scale), round(pos[1] * scale))
		size = self.size.getValue()
		pygame.draw.line(view.window, self.color, pos, (round(pos[0] + size[0] * scale), round(pos[1] + size[1] * scale)), 1)