
from event import Event

"""
" Defines an object that can do stuff during the render cycle
"""
class Drawable(object):
	"""
	" CONSTRUCTOR
	"""
	def __init__(self):
		Event(parent = self.events, Name = "onDraw")

	"""
	" Allows this object and all its children to render themselves
	" @param View view: Reference to the object that will be doing the drawing
	"""
	def __draw__(self, view = None):
		## Run this object's draw callbacks ##
		drawcb = self.events.getFirst("onDraw")
		drawcb.view = view
		drawcb.owner = self
		drawcb.forceRun()

		## Allow children to run their callbacks ##
		for o in self.getChildren():
			if isinstance(o, Drawable):
				o.__draw__(view)