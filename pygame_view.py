
import pygame
from pygame.locals import *
from .view import View
from .drawable import Drawable

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
		## Adjust camera position so that it is focused at the center of the view ##
		self.pos.setValue(((self.pos.getValue()[0] + self.size.getValue()[0]/2) / self.scale.getValue(), (self.pos.getValue()[1] + self.size.getValue()[1]/2) / self.scale.getValue()))
		self.window = None # Reference to the Pygame window
		self.events.getFirst("onDraw").regcb(self.draw).Name = "InitWindow"

	"""
	" If a pygame window has not already been created, open one
	"""
	def initWindow(self):
		## Initialize Pygame window ##
		if(self.window != None):
			return
		pygame.init()
		self.window = pygame.display.set_mode((self.size.getValue()[0], self.size.getValue()[1]), 0, 32)

	"""
	" Check if the pygame window needs to be opened
	"""
	def draw(self, event):
		self.initWindow()

	"""
	" Adds this object as the window to which things should be drawn, then allows
	" 		all children to draw themselves
	" @param View view: Reference to the object that will be doing the drawing
	"""
	def __draw__(self, view = None):
		self.draw(self)
		self.window.lock()
		self.window.fill((0, 0, 0))

		self.events.getFirst("onDraw").forceRun()

		for o in self.getChildren():
			if isinstance(o, Drawable):
				o.__draw__(self)

		self.window.unlock()
		pygame.display.update()

	"""
	" Closes the pygame window created by this view
	"""
	def close(self, event):
		if self.window != None:
			pygame.quit()
			self.view = None