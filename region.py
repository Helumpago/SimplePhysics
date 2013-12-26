
from base_obj import BaseObj

"""
" Represents a section of the two-dimensional simulation space. Essentially a bounding box
"""
class Region(BaseObj):
	"""
	" CONSTRUCTOR
	" @param BaseObj parent: Object to which the new object should be parented.
	" 		Expected to be either a BaseObj, subclass of BaseObj, or None
	" @param string Name: Name for this object.
	" @param (number sizeX, number sizeY) size: Size of this region. Can make it include the entire
	" 		world by setting it equal to (float("inf"), float("inf"))
	" @param (posX, posY) pos: Center of this region
	" @param number scale: Scale to apply to all objects rendering themselves in this window
	"""
	def __init__(self, parent = None, Name = "Region", size = (float("inf"), float("inf")), pos = (0, 0), scale = 1):
		BaseObj.__init__(self, parent = parent, Name = Name)
		self.size = size
		self.pos = pos
		self.scale = scale

	"""
	" Gets the center of this region
	"""
	def getPos(self):
		return self.pos

	"""
	" Gets the size of this region
	"""
	def getSize(self):
		return self.size

	"""
	" Decides whether a given object is inside this region
	" @param Region o: Reference to the object to check
	" @return: True if the object is inside.  Otherwise, False
	"""
	def isSurrounding(self, o):
		if (o.getPos()[0] >= self.getPos()[0] - self.getSize()[0]/2 and
				o.getPos()[0] <= self.getPos()[0] + self.getSize()[0]/2 and
				o.getPos()[1] >= self.getPos()[1] - self.getSize()[1]/2 and
				o.getPos()[1] <= self.getPos()[1] + self.getSize()[1]/2):
			return True
		else:
			return False