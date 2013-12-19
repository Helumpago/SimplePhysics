
"""
" Defines a vector in two-dimensional space
"""
class Vector2d(object):
	"""
	" CONSTRUCTOR
	" @param (int X, int Y) pos: Position of the vector
	"""
	def __init__(self, pos):
		self.pos = pos

	"""
	" Allow the vector to be indexed with "x" and "y"
	"""
	def __getattribute__(self, name):
		if name == "x":
			return object.__getattribute__(self, "pos")[0]
		elif name == "y":
			return object.__getattribute__(self, "pos")[1]
		else:
			return object.__getattribute__(self, name)

	"""
	" Allow the vector to be set by indexing "x" and "y"
	"""
	def __setattr__(self, key, value):
		if key == "x":
			object.__setattr__(self, "pos", (value, self.y))
		elif key == "y":
			object.__setattr__(self, "pos", (self.x, value))
		else:
			object.__setattr__(self, key, value)