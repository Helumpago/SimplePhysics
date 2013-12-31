
from .region import RectRegion
from .drawable import Drawable

"""
" Interface that defines an object that is responsible for managing the window
"""
class View(RectRegion, Drawable):
	"""
	" CONSTRUCTOR
	" @param BaseObj parent: Object to which the new object should be parented.
	" 		Expected to be either a BaseObj, subclass of BaseObj, or None
	" @param string Name: Name for this object.
	" @param (sizeX, sizeY) windowSize: Size (in pixels) of the window
	" @param (posX, posY) pos: World coordinates of the camera
	" @param number scale: Scale to apply to all objects rendering themselves in this window
	"""
	def __init__(self, parent = None, Name = "View", size = (256, 256), pos = (0, 0), scale = 1):
		RectRegion.__init__(self, parent = parent, Name = Name, size = size, pos = pos, scale = scale)
		Drawable.__init__(self)

	"""
	" Closes this view
	"""
	def close(self, event):
		raise NotImplementedError("View's close() method left unimplemented")