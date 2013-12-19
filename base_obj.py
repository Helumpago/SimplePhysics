
"""
" Base class for all objects that will interact with the Workspace
"""
class BaseObj(object):
	"""
	" CONSTRUCTOR
	" @param string name: Name for this object
	"""
	def __init__(self, Name = "object", parent = None):
		self.Name = Name
		self.parent = None
		self.setParent(parent)

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