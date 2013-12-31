
from .base_obj import BaseObj
from .value import Number, Ratio, Vector2d

"""
" Base class for all regions
"""
class Region(BaseObj):
	"""
	" CONSTRUCTOR
	" @param BaseObj parent: Object to which the new object should be parented.
	" 		Expected to be either a BaseObj, subclass of BaseObj, or None
	" @param string Name: Name for this object.
	"""
	def __init__(self, parent = None, Name = "Region"):
		BaseObj.__init__(self, parent = parent, Name = Name)

	"""
	" Decides whether a given object is inside this region
	" @param Region o: Reference to the object to check
	" @return: True if the object is inside.  Otherwise, False
	" @remarks: The base region class will always return True,
	" 		as it is assumed that the region is infinite
	"""
	def isSurrounding(self, o):
		return True

"""
" Represents a rectangular section of the two-dimensional simulation space. Essentially a bounding box
"""
class RectRegion(Region):
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
	def __init__(self, parent = None, Name = "RectRegion", size = (float("inf"), float("inf")), pos = (0, 0), scale = 1):
		Region.__init__(self, parent = parent, Name = Name)
		self.size = Vector2d(parent = self, Name = "size", value = size)
		self.pos = Vector2d(parent = self, Name = "pos", value = pos)
		self.scale = Ratio(parent = self, Name = "scale", value = scale)

	"""
	" Decides whether a given object is inside this region
	" @param Region o: Reference to the object to check
	" @return: True if the object is inside.  Otherwise, False
	"""
	def isSurrounding(self, o):
		spos = self.pos.getAValue()
		opos = o.pos.getAValue()
		if (opos[0] >= spos[0] - self.size.getValue()[0]/2 and
				opos[0] <= spos[0] + self.size.getValue()[0]/2 and
				opos[1] >= spos[1] - self.size.getValue()[1]/2 and
				opos[1] <= spos[1] + self.size.getValue()[1]/2):
			return True
		else:
			return False

"""
" Represents a circular section of the two-dimensional simulation space.
"""
class CircleRegion(Region):
	"""
	" CONSTRUCTOR
	" @param BaseObj parent: Object to which the new object should be parented.
	" 		Expected to be either a BaseObj, subclass of BaseObj, or None
	" @param string Name: Name for this object.
	" @param number radius: Radius of the circle. Can make it include the entire
	" 		world by setting it equal to (float("inf"), float("inf"))
	" @param (posX, posY) pos: Center of this region
	" @param number scale: Scale to apply to all objects rendering themselves in this window
	"""
	def __init__(self, parent = None, Name = "CircleRegion", radius = float("inf"), pos = (0, 0), scale = 1):
		Region.__init__(self, parent = parent, Name = Name)
		self.radius = Number(parent = self, Name = "radius", value = radius)
		self.pos = Vector2d(parent = self, Name = "pos", value = pos)
		self.scale = Ratio(parent = self, Name = "scale", value = scale)

	"""
	" Decides whether a given object is inside this region
	" @param Region o: Reference to the object to check
	" @return: True if the object is inside.  Otherwise, False
	"""
	def isSurrounding(self, o):
		## Find the distance between the two points ##
		spos = self.pos.getAValue()
		opos = o.pos.getAValue()
		dx = spos[0] - opos[0]
		dy = spos[1] - opos[1]
		dist = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))

		## Ensure that the distance between the points is withing the radius ##
		if dist < self.radius.getValue():
			return True
		else:
			return False