
import pygame
from pygame.locals import *
import sys
import time
import threading
from drawable import Drawable
from physical import Physical
from workspace import Workspace
from sphere import Sphere

"""
" Manages the simulation
"""	
class World(threading.Thread):
	"""
	" CONSTRUCTOR
	" @param windowSize: Tuple of the form (xSize, ySize).  Defines the size of the window in pixels
	" @param scale: Defines the window's scale.  In units of pixels per distance unit.
	"""
	def __init__(self, windowSize = (256, 256), scale = 1):
		threading.Thread.__init__(self)
		self.workspace = Workspace(windowSize, scale)

	"""
	" Begins execution of the program.
	" If an instance is already running, that instance will be removed and a new one created (iow, the program will restart)
	"""
	def open(self):
		if(self.workspace.view != None):
			pygame.quit()

		pygame.init()
		self.workspace.view = pygame.display.set_mode((self.workspace.windowSize[0], self.workspace.windowSize[1]), 0, 32)

	"""
	" Closes the pygame window attached to this object
	"""
	def close(self):
		if self.workspace.view != None:
			pygame.quit()
			self.workspace.view = None

	"""
	" Adds a new object to this world's workspace
	"""
	def addObj(self, o):
		self.workspace.lock.acquire() # Unlock the workspace
		self.workspace.objects.append(o)
		self.workspace.lock.release()

	"""
	" Render all drawable objects
	"""
	def render(self):
		self.workspace.view.lock()
		self.workspace.view.fill((0, 0, 0))
		for o in self.workspace.objects:
			if isinstance(o, Drawable):
				o.draw(self.workspace)
		self.workspace.view.unlock()
		pygame.display.update()

	"""
	" Generate the next physics frame
	" @param int dt: Number of milliseconds since the last frame
	"""
	def step(self, dt):
		for o in self.workspace.objects:
				if isinstance(o, Physical):
					o.frame(self.workspace, dt)

	"""
	" Main execution loop for the simulation
	"""
	def run(self):
		self.open()

		while True:
			clock = pygame.time.Clock()
			dt = clock.tick(60) # Get the amount of time since the last frame ("Delta time")
			#self.workspace.lock.acquire()

			## Watch for events ##
			for event in pygame.event.get():
				if event.type == QUIT:
					self.close()
					return

			self.render()
			self.step(dt)

			#self.workspace.lock.release()