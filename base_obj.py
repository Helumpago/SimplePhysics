
"""
" Base class for all objects that can be parented to a Workspace
"""
class Base(object):
	"""
	" CONSTRUCTOR
	" @param Workspace p: Workspace that this object should be parented to. If set to None,
	" 		the object will be in "null space", and it will be assumed that no thread
	" 		synchronization is needed.
	"""
	def __init__(self, p = None):
		self.parent(p)

	"""
	" Sets the parent for this object
	" @param Workspace p: The workspace that this object should be parented to
	"""
	def parent(self, p):
		if p != None:
			p.addObj(self)
			
		self.p = p

	"""
	" Extends the dot operator so that the Semaphore for this object will be
	" automatically acquired.
	"""
	def __getitem__(self, key):
		self.p.lock.acquire()
		o = object.__getitem__(self, key)
		self.p.lock.release()
		return o

	"""
	" Automatically acquires the Semaphore for this object
	"""
	def __setitem__(self, key, value):
		self.p.lock.acquire()
		object.__setitem__(self, key, value)
		self.p.lock.release()