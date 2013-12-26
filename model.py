
import threading
from base_obj import BaseObj, ParentError
from drawable import Drawable

"""
" Controls the flow of the simulation. In other words,
" 	this object defines the event-model-render loop.
" This object is the root of the scene graph for all
" 	simulations
"""
class Model(BaseObj, Drawable, threading.Thread):
	"""
	" CONSTRUCTOR
	" @param string Name: Name for this object.
	" @param int fps: Maximum number of frames per second allowable.
	"""
	def __init__(self, Name = "Model", fps = 60):
		BaseObj.__init__(self, parent = None, Name = Name)
		Drawable.__init__(self)
		threading.Thread.__init__(self)
		self.fps = fps

	"""
	" Prevent this object from being parented to anything
	"""
	def setParent(self, parent = None):
		if parent == None:
			object.__setattr__(self, "parent", None)
		else:
			raise ParentError("Can't parent a Model to any object")

	"""
	" Actions to perform before every frame is generated
	"""
	def preStep(self):
		pass

	"""
	" Actions to perform before after frame is generated
	"""
	def postStep(self):
		pass

	"""
	" ABSTRACT
	" Limits the number of frames per second to the given number
	" 		and gets the number of miliseconds since the last frame.
	" @param number t: Maximum FPS
	" @return: Number of miliseconds since the last frame
	"""
	def tick(self, t):
		raise NotImplementedError("tick() method left unimplemented")

	"""
	" Main execution loop for the simulation.  Separates itself
	" 	into a separate process
	"""
	def run(self):
		while True:
			self.dt = self.tick(self.fps)

			## Step the simulation ##
			self.preStep()
			self.__step__()
			self.postStep()

			self.__draw__()