
"""
" Defines an object that can do stuff during the render cycle
"""
class Drawable(object):
	"""
	" CONSTRUCTOR
	"""
	def __init__(self):
		pass

	"""
	" What this object should do during the render stage
	"""
	def draw(self, view = None):
		pass

	"""
	" Allows this object and all its children to render themselves
	" @param View view: Reference to the object that will be doing the drawing
	"""
	def __draw__(self, view = None):
		self.draw(view)
		for o in self.getChildren():
			if isinstance(o, Drawable):
				o.__draw__(view)