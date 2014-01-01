
from ..drawable import Drawable
from .collidable import Collidable

"""
" Creates a circle that can collide with other objects.
"""
class Ball(Collidable, Drawable):
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
	def __init__(self, parent = None, Name = "Collidable", size = (float("inf"), float("inf")), pos = (0, 0), scale = 1, canCollide = True):
		RectRegion.__init__(self, parent = parent, Name = Name, size = size, pos = pos, scale = scale, canCollide = canCollide)