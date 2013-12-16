
import threading

"""
" Container for all simulation objects in this world (drawable, physics stuff, etc.)
"""
class Workspace(object):
	def __init__(self, windowSize = (256, 256), scale = 1):
		self.windowSize = windowSize
		self.scale = scale
		self.view = None # Reference to the Pygame window object
		self.objects = []
		self.lock = threading.Semaphore()

	"""
	" Adds a new object to this workspace
	"""
	def addObj(self, o):
		self.objects.append(o)