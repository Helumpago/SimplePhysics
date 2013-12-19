
import threading

"""
" Base class for all objects that will interact with the Workspace
"""
class BaseObj(object):
	"""
	" CONSTRUCTOR
	" @param string name: Name for this object
	" @param Workspace parent: Reference to the workspace this object should be parented to
	"""
	def __init__(self, Name = "object", parent = None):
		self.Name = Name
		self.parent = None
		self.setParent(parent)
		self.lock = threading.Semaphore()

	"""
	" Sets the parent workspace for this object
	" @param Workspace target: Reference to the workspace to which this object should be parented
	"""
	def setParent(self, target):
		if self.parent == target:
			return
		elif target != None:
			target.addChild(self)
		self.parent = target

	"""
	" Extends the dot operator so that the Semaphore for this object will be
	" automatically acquired.
	"""
	def __getitem__(self, key):
		self.lock.acquire()
		o = object.__getitem__(self, key)
		self.lock.release()
		return o

	"""
	" Automatically acquires the Semaphore for this object
	"""
	def __setitem__(self, key, value):
		self.lock.acquire()
		object.__setitem__(self, key, value)
		self.lock.release()