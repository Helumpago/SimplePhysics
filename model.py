
import threading
from base_obj import BaseObj, ParentError
from drawable import Drawable
from event import Event

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
		self.events = BaseObj(parent = self, Name = "Events") # Container for all events that this object can trigger
		Event(parent = self.events, Name = "QUIT") # Fired when the Model thread is ready to shut down

	"""
	" Prevent this object from being parented to anything
	"""
	def setParent(self, parent = None):
		if parent == None:
			object.__setattr__(self, "parent", None)
		else:
			raise ParentError("Can't parent a Model to any object")

	"""
	" ABSTRACT
	" Limits the number of frames per second to the given number
	" 		and gets the number of miliseconds since the last frame.
	" @param number t: Maximum FPS
	" @return: Number of miliseconds since the last frame
	"""
	def tick(self, t):
		raise NotImplementedError("Model's tick() method left unimplemented")

	"""
	" Calculate this object's next frame.
	"""
	def step(self, dt):
		for ev in self.events.getChildren():
			ev.run()

	"""
	" Main execution loop for the simulation.  Separates itself
	" 	into a separate process
	"""
	def run(self):
		while True:
			self.dt = self.tick(self.fps)

			## Step the simulation ##
			self.__draw__()
			self.__collectEvents__()
			self.__step__(self.dt)