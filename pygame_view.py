
import pygame
from pygame.locals import *
from view import View

"""
" Creates a window using Pygame in which to render objects
"""
class PygameView(View):
	"""
	" CONSTRUCTOR
	" @param BaseObj parent: Object to which the new object should be parented.
	" 		Expected to be either a BaseObj, subclass of BaseObj, or None
	" @param string Name: Name for this object.
	" @param (sizeX, sizeY) windowSize: Size (in pixels) of the window
	" @param (posX, posY) pos: World coordinates of the camera
	" @param number scale: Scale to apply to all objects rendering themselves in this window
	"""
	def __init__(self, parent = None, Name = "PygameView", size = (256, 256), pos = (0, 0), scale = 1):
		View.__init__(self, parent = parent, Name = Name, size = size, pos = pos, scale = scale)
		self.window = None # Reference to the Pygame window

	"""
	" If a pygame window has not already been created, open one
	"""
	def initWindow(self):
		## Initialize Pygame window ##
		if(self.window != None):
			return
		pygame.init()
		self.window = pygame.display.set_mode((self.getSize()[0], self.getSize()[1]), 0, 32)

	"""
	" Check if the pygame window needs to be opened
	"""
	def draw(self):
		self.initWindow()