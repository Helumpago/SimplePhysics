
"""
" Contains definitions for all SimplePhysics events
"""

"""
" Base event class
"""
class EVENT(object):
	"""
	" CONSTRUCTOR
	"""
	def __init__(self, callback = None):
		self.cb = callback # Function to call when the event is fired

	"""
	" Run the callback
	"""
	def callback(self):
		self.cb()

"""
" Fired when Pygame asks to exit
"""
class QUIT(EVENT):
	def __init__(self, callback = None):
		EVENT.__init__(self, callback)

	def callback(self):
		self.cb(self)