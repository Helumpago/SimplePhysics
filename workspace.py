
import pygame
from pygame.locals import *
import threading
from vector2d import Vector2d
from base_obj import BaseObj
from drawable import Drawable
from physical import Physical
import events

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
	def __init__(self, Name = "Workspace", windowSize = Vector2d((256, 256)), scale = 1):
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
	" Gets the first child that has a given name
	" @param string name: Name of the child to look for
	" @return: Reference to the first object with the given name.
	" 		Returns None if no object with that name was found.
	"""
	def getChild(self, name):
		## Check if there are any children with the given name ##
		try:
			self.children[name]
		except KeyError:
			return None
		return self.children[name][0] # Get the first object with the given name

	"""
	" Gets all children that have a given name
	" @param string name: Object name to look for
	"""
	def getChildren(self, name):
		try:
			self.children[name]
		except KeyError:
			return None
		return self.children[name] # Get all objects with the given name

	"""
	" Render the current frame
	"""
	def render(self):
		self.view.lock()
		self.view.fill((0, 0, 0))
		for name in self.children:
			for o in self.getChildren(name):
				if(isinstance(o, Drawable)):
					o.draw()
		self.view.unlock()
		pygame.display.update()

	"""
	" Runs the callbacks for all fired events
	"""
	def fireEvents(self):
		BaseObj.fireEvents(self)
		try:
			for cb in self.events[events.QUIT]:
				cb(self)
		except KeyError:
			pass

	"""
	" Move to the next frame in the simulation
	" @param int dt: Number of milliseconds since the last frame
	"""
	def step(self, dt):
		self.fireEvents()

		## Step child object's frames ##
		for name in self.children:
			for o in self.getChildren(name):
				if(isinstance(o, Physical)):
					o.step(dt)

	"""
	" Get all the events for this object that have been fired
	"""
	def collectEvents(self):
		## Check pygame events ##
		for event in pygame.event.get():
			if event.type == QUIT:
				self.events[events.QUIT] = self.callbacks[events.QUIT]

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
		clock = pygame.time.Clock()

		## Main execution loop ##
		while True:
			dt = clock.tick(60) # Get the amount of time since the last frame

			self.collectEvents()
			self.render()
			self.step(dt)