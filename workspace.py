
import pygame
from pygame.locals import *
import threading
from vector2d import Vector2d
from base_obj import BaseObj

"""
" Manages the simulation
"""
class Workspace(BaseObj, threading.Thread):
	"""
	" CONSTRUCTOR
	" @param string name: Name for this workspace
	" @param Vector2d windowSize:  Defines the size of the window in pixels
	" @param int scale: Defines the window's scale.  In units of pixels per distance unit.
	"""
	def __init__(self, Name = "Workspace", windowSize = Vector2d(256, 256), scale = 1):
		BaseObj.__init__(self, Name)
		threading.Thread.__init__(self)
		self.windowSize = windowSize
		self.scale = scale
		self.view = None # Reference to the pygame window
		self.children = {} # Dictionary containing all objects parented to this workspace

	"""
	" Closes the pygame window attached to this object
	"""
	def close(self):
		if self.view != None:
			pygame.quit()
			self.view = None

	"""
	" Adds an object to the set of objects that belong to this workspace
	" @param BaseObj child: Reference to the new child
	"""
	def addChild(self, child):
		## Ensure that the child is of the correct type ##
		if(isinstance(child, BaseObj) != True):
			raise TypeError("Attempt to parent a non-BaseObj type")

		## Check if a list of subobjects with this name already exist ##
		try:
			self.children[child.Name]
		except KeyError:
			self.children[child.Name] = [] # Define a new list of subobjects matching the given name

		self.children[child.Name].append(child) # Add the new child

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