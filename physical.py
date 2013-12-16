
"""
" Extend this class to allow an object to be affected by physics
"""
class Physical(object):
	"""
	" Implement this function to define the physics that this object participates in
	" @param Window window: Container for all objects being simulated, including details on the pygame window
	" @param int dt: Number of milliseconds since the last frame
	"""
	def frame(self, window, dt):
		pass