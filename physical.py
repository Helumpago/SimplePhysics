
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
		self.onStep = Event(Name = "onStep") # Contains callbacks to run for each frame

	"""
	" Allows this object and all its children to generate their next step
	" @param number dt: Amount of time since last frame
	"""
	def __step__(self, dt):
		self.onStep.dt = dt
		self.onStep.owner = self
		self.onStep.forceRun()

		for o in self.getChildren():
			if isinstance(o, Physical):
				o.__step__(dt)