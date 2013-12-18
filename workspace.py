
import pygame
from pygame.locals import *
import threading
from vector2d import Vector2d

"""
" Manages the simulation
"""
class Workspace(threading.Thread):
	"""
	" CONSTRUCTOR
	" @param Vector2d windowSize:  Defines the size of the window in pixels
	" @param int scale: Defines the window's scale.  In units of pixels per distance unit.
	"""
	def __init__(self, windowSize = Vector2d(256, 256), scale = 1):
		threading.Thread.__init__(self)
		self.windowSize = windowSize
		self.scale = scale
		self.view = None # Reference to the pygame window

	"""
	" Closes the pygame window attached to this object
	"""
	def close(self):
		if self.view != None:
			pygame.quit()
			self.view = None

	"""
	" Main execution loop for the simulation, as well as the entry point
	" for when the Workspace becomes a separate thread
	"""
	def run(self):
		## Open the pygame window ##
		if(self.view != None):
			return
		pygame.init()
		self.view = pygame.display.set_mode((self.windowSize.x, self.windowSize.y), 0, 32)

		## Main execution loop ##
		while True:
			## Check Pygame events ##
			for event in pygame.event.get():
				if event.type == QUIT:
					self.close()
					return