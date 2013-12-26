
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
	def draw(self):
		pass

	"""
	" Allows this object and all its children to render themselves
	"""
	def __draw__(self):
		self.draw()
		for o in self.getChildren():
			if isinstance(o, Drawable):
				o.__draw__()