
"""
" Defines an object that can be drawn onto the screen during the render cycle
"""
class Drawable(object):
	"""
	" CONSTRUCTOR
	" @param (int R, int G, int B) color: RGB color value for this object
	"""
	def __init__(self, color = (0, 0, 0)):
		self.color = color

	"""
	" Draws this object to the given screen
	"""
	def draw(self):
		raise NotImplementedError("Draw method left unimplemented")