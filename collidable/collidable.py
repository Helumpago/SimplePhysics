
from ..drawable import Drawable
from ..region import RectRegion
from ..event import Event

"""
" Defines a region that can participate in collisions.
"""
class Collidable(RectRegion):
	"""
	" CONSTRUCTOR
	" @param BaseObj parent: Object to which the new object should be parented.
	" 		Expected to be either a BaseObj, subclass of BaseObj, or None
	" @param string Name: Name for this object.
	" @param (number sizeX, number sizeY) size: Size of this region. Can make it include the entire
	" 		world by setting it equal to (float("inf"), float("inf"))
	" @param (posX, posY) pos: Center of this region
	" @param number scale: Scale to apply to all objects rendering themselves in this window
	" @param bool canCollide: Whether or not this object can participate in collisions
	"""
	def __init__(self, parent = None, Name = "Collidable", size = (0, 0), pos = (0, 0), scale = 1, canCollide = True):
		RectRegion.__init__(self, parent = parent, Name = Name, size = size, pos = pos, scale = scale)
		self.canCollide = canCollide
		Event(parent = self.events, Name = "onCollision")

	"""
	" Checks whether two objects that may be colliding are actually touching.
	" 		In other words, this method defines the Narrow Phase part of the
	"		collision detection algorithm.
	"""
	def confirmCollision(self, particle):
		raise NotImplementedError("confirmCollision() method left unimplemented")

"""
" Defines a shape that can collide with other objects
"""
class CollidableShape(Collidable, Drawable):
	"""
	" CONSTRUCTOR
	" @param BaseObj parent: Object to which the new object should be parented.
	" 		Expected to be either a BaseObj, subclass of BaseObj, or None
	" @param string Name: Name for this object.
	" @param (number sizeX, number sizeY) size: Size of this region. Can make it include the entire
	" 		world by setting it equal to (float("inf"), float("inf"))
	" @param (posX, posY) pos: Center of this region
	" @param number scale: Scale to apply to all objects rendering themselves in this window
	" @param bool canCollide: Whether or not this object can participate in collisions
	"""
	def __init__(self, parent = None, Name = "CollidableShape", size = (0, 0), pos = (0, 0), scale = 1, canCollide = True):
		Collidable.__init__(self, parent = parent, Name = Name, size = size, pos = pos, scale = scale, canCollide = canCollide)
		Drawable.__init__(self)