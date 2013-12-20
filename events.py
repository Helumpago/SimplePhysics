
"""
" Contains definitions for all SimplePhysics events
"""

"""
" Base event class
"""
class EVENT(object):
	string = "EVENT" # Unique string to index dictionaries off of

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
	string = "QUIT" # Unique string to index dictionaries off of

	def __init__(self, callback = None):
		EVENT.__init__(self, callback)

	def callback(self):
		self.cb(self)