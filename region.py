
from physical import Physical
from vector2d import Vector2d
import events
from moveable import Moveable

"""
" Defines an action that should be taken on any object inside a specific region of space.
" The size for this region is "infinite"; In other words, an object will always be assumed
" to be inside it.
"""
class Region(Physical):
	"""
	" CONSTRUCTOR
	" @param string name: Name for this object
	" @param Workspace parent: Reference to the workspace this object should be parented to
	"""
	def __init__(self, Name = "Region", parent = None):
		Physical.__init__(self, Name = Name, parent = parent)

	"""
	" Gets only the objects of the parent workspace that are considered inside this object.
	" Because this region is "infinite," all Moveable objects will be considered inside.
	"""
	def getObjs(self):
		objs = []
		for o in self.parent.getChildren():
			if isinstance(o, Moveable):
				objs.append(o)

		return objs

	"""
	" Get and fire events for all objects inside this region
	"""
	def collectEvents(self, dt):
		Physical.collectEvents(self, dt)

		for o in self.getObjs():
			for cb in self.callbacks[events.INREGION]:
				try:
					self.events[events.INREGION].append(events.INREGION(hit = o, callback = cb, dt = dt)) 
				except KeyError:
					self.events[events.INREGION] = [events.INREGION(hit = o, callback = cb, dt = dt)]

	"""
	" Runs the callbacks for all fired events
	" @param number dt: Number of milliseconds since last frame
	"""
	def fireEvents(self):
		Physical.fireEvents(self)
		try:
			for cb in self.events[events.INREGION]:
				cb.call()
		except KeyError:
			pass

	"""
	" Perform the registered callbacks on all objects inside this region
	" @param int dt: Number of milliseconds since the last frame
	"""
	def step(self, dt):
		self.fireEvents()