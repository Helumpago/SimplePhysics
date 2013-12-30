
from event import Event

"""
" Declares necessary methods to allow an object (and its children) to participate
" 		in the modeling stage
"""
class Physical(object):
	"""
	" CONSTRUCTOR
	"""
	def __init__(self):
		Event(parent = self.events, Name = "onStep") # Contains callbacks to run for each frame

	"""
	" Allows this object and all its children to generate their next step
	" @param number dt: Amount of time since last frame
	"""
	def __step__(self, dt):
		stepcb = self.events.getFirst("onStep")
		stepcb.dt = dt
		stepcb.owner = self
		stepcb.forceRun()

		for o in self.getChildren():
			if isinstance(o, Physical):
				o.__step__(dt)