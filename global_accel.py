
import pygame
from pygame.locals import *
from region import Region

"""
" Defines an acceleration that acts on all Moveable objects in the scene.
" Example use: Gravity due to Earth
"""
class GlobalAccel(Region):
	"""
	" CONSTRUCTOR
	" @param string name: Name for this object
	" @param Workspace parent: Reference to the workspace this object should be parented to
	" @param number a: Acceleration
	"""
	def __init__(self, Name = "GlobalForce", parent = None, a = 0):
		Region.__init__(self, Name = Name, parent = parent)
		self.clock = pygame.time.Clock()

	"""
	" Callback for all objects in the workspace
	"""
	def act(hit):
		dt = self.clock.get_time()

		