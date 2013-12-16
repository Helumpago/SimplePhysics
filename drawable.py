
from base_obj import Base

"""
" Extend this object to allow an object to be drawable
"""
class Drawable(Base):
	"""
	" CONSTRUCTOR
	" @param Workspace p: Workspace that this object should be parented to.
	"""
	def __init__(self, p):
		Base.__init__(self, p);
	
	"""
	" Draw this object to the window
	"""
	def draw(self, window):
		pass