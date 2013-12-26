
import pygame
from pygame.locals import *
from base_obj import BaseObj
from drawable import Drawable

"""
" Creates a window in which to render objects
"""
class PygameView(BaseObj, Drawable):
	"""
	" CONSTRUCTOR
	" @param BaseObj parent: Object to which the new object should be parented.
	" 		Expected to be either a BaseObj, subclass of BaseObj, or None
	" @param string Name: Name for this object.
	" @param (sizeX, sizeY) windowSize: Size (in pixels) of the window
	" @param (posX, posY) pos: World coordinates of the camera
	" @param number scale: Scale to apply to all objects rendering themselves in this window
	"""
	def __init__(self, parent = None, Name = "View", windowSize = (256, 256), pos = (0, 0), scale = 1):
		BaseObj.__init__(self, parent = parent, Name = Name)
		Drawable.__init__(self)
		self.windowSize = windowSize
		self.pos = pos
		self.scale = scale
		self.window = None # Reference to the Pygame window

	"""
	" If a pygame window has not already been created, open one
	"""
	def initWindow(self):
		## Initialize Pygame window ##
		if(self.window != None):
			return
		pygame.init()
		self.window = pygame.display.set_mode((self.windowSize[0], self.windowSize[1]), 0, 32)

	def draw(self):
		self.initWindow()