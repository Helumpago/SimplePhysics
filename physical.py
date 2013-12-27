
"""
" Defines an object that can perform operations during the Model stage
"""
class Physical(object):
	"""
	" CONSTRUCTOR
	"""
	def __init__(self):
		pass

	"""
	" Actions for this object to perform during the modeling stage
	" @param number dt: Amount of time since last frame
	"""
	def step(self, dt):
		pass

	"""
	" Allows this object and all its children to generate their next step
	" @param number dt: Amount of time since last frame
	"""
	def __step__(self, dt):
		self.step(dt)
		for o in self.getChildren():
			if isinstance(o, Physical):
				o.__step__(dt)