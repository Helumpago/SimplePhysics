
"""
" Contains definitions for all SimplePhysics events
"""

"""
" Base event class
"""
class EVENT(object):
	"""
	" CONSTRUCTOR
	" @param callable callback: Method to call when this event is fired
	"""
	def __init__(self, callback = None):
		self.callback = callback

	"""
	" Run the given callback
	"""
	def call(self):
		self.callback()

"""
" Fired when Pygame asks to exit
"""
class QUIT(EVENT):
	"""
	" CONSTRUCTOR
	" @param callable callback: Method to call when this event is fired
	"""
	def __init__(self, workspace, callback = None):
		EVENT.__init__(self, callback)
		self.workspace = workspace

	def call(self):
		self.callback(self.workspace)

"""
" Fired when a collision occurs between two Moveable objects
"""
class COLLISION(EVENT):
	"""
	" CONSTRUCTOR
	" @param Moveable hit: Object that this object collided with
	" @param callable callback: Method to call when this event is fired
	"""
	def __init__(self, hit, callback = None):
		EVENT.__init__(self, callback)
		self.hit = hit

	def call(self):
		self.callback(self.hit)