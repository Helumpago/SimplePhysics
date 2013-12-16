
import threading

"""
" Container for all simulation objects in this world (drawable, physics stuff, etc.)
"""
class Workspace:
	def __init__(self, windowSize = (256, 256), scale = 1, delay = .05):
		self.windowSize = windowSize
		self.scale = scale
		self.delay = delay # Number of seconds to wait between each frame
		self.view = None # Reference to the Pygame window object
		self.objects = []
		self.lock = threading.Semaphore()