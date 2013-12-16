
from base_obj import Base

"""
" Extend this class to allow an object to be affected by physics
"""
class Physical(Base):
	"""
	" CONSTRUCTOR
	" @param Workspace p: Workspace that this object should be parented to.
	"""
	def __init__(self, p):
		Base.__init__(self, p);

	"""
	" Implement this function to define the physics that this object participates in
	" @param Window window: Container for all objects being simulated, including details on the pygame window
	" @param int dt: Number of milliseconds since the last frame
	"""
	def frame(self, window, dt):
		pass