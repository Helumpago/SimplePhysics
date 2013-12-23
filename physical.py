
from base_obj import BaseObj

"""
" Base class for all objects that will change their behavior from frame to frame
"""
class Physical(BaseObj):
	"""
	" CONSTRUCTOR
	" @param string name: Name for this object
	" @param Workspace parent: Reference to the workspace this object should be parented to
	"""
	def __init__(self, Name = "object", parent = None):
		BaseObj.__init__(self, Name, parent)

	"""
	" Move to the next frame in the simulation
	" @param int dt: Number of milliseconds since the last frame
	"""
	def step(self, dt):
		self.fireEvents()