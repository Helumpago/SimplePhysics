
from .eventless_object import EventlessObject
from .event import Event

"""
" Base class for all objects that can be placed in the scene graph
" 		and can act on events
"""
class BaseObj(EventlessObject):
	"""
	" CONSTRUCTOR
	" @param BaseObj parent: Object to which the new object should be parented.
	" 		Expected to be either a BaseObj, subclass of BaseObj, or None
	" @param string Name: Name for this object.
	"""
	def __init__(self, parent = None, Name = "Object"):
		EventlessObject.__init__(self, parent = parent, Name = Name)
		self.events = EventlessObject(Name = "Events") # Container for all events this object can act on
		Event(parent = self.events, Name = "onStep") # Contains callbacks to run for each frame

	"""
	" Runs all attached events
	"""
	def fireEvents(self):
		for event in self.events.getChildren():
			event.run()

	"""
	" Allows this object and all its children to generate their next step
	" @param number dt: Amount of time since last frame
	"""
	def __step__(self, dt):
		stepcb = self.events.getFirst("onStep")
		stepcb.dt = dt
		stepcb.owner = self
		stepcb.forceRun()

		self.fireEvents()
		for o in self.getChildren():
			if isinstance(o, BaseObj):
				o.__step__(dt)