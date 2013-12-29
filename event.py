
from base_obj import BaseObj

"""
" An object that holds a method and can be placed in the scene graph.
" Used to hold the actions for events.
"""
class Callback(BaseObj):
	"""
	" CONSTRUCTOR
	" @param callable cb: Callback to run when this object is called
	" @param BaseObj parent: Object to which the new object should be parented.
	" 		Expected to be either a BaseObj, subclass of BaseObj, or None
	" @param string Name: Name for this object.
	"""
	def __init__(self, cb, parent = None, Name = "Callback"):
		BaseObj.__init__(self, parent = parent, Name = Name)
		self.cb = cb 

	def __call__(self):
		self.cb()

"""
" Container for multiple callbacks.  Provides methods that will decide
" 		whether the descending callbacks should be run.
"""
class Event(BaseObj):
	"""
	" CONSTRUCTOR
	" @param BaseObj parent: Object to which the new object should be parented.
	" 		Expected to be either a BaseObj, subclass of BaseObj, or None
	" @param string Name: Name for this object.
	"""
	def __init__(self, parent = None, Name = "Event"):
		BaseObj.__init__(self, parent = parent, Name = Name)
		self.fire = False #Flag indicating whether this object can fire its callbacks

	"""
	" Methods that decides whether the attached callbacks should be run.
	" Note, does not actually fire the callbacks. Only sets 
	" 		self.fire to True so that they can be run.  To actually
	" 		run the callbacks, call run()
	"""
	def collectEvents(self):
		pass

	"""
	" If this event is allowed to run, fire all child callbacks
	"""
	def run(self):
		if self.fire != True:
			return

		## Loop through and run all callbacks that directly descend from this object ##
		for cb in self.getChildren():
			if hasattr(cb, '__call__'): # Ensure that this object is callable
				cb()

		self.fire = False

	"""
	" Registers a new callback with this event.
	" Simply creates a new un-named Callback object with the provided method
	" 		and parents it to this object.
	" @param callable method: Method to call when this event fires.
	" @return: Reference to the new Callback that was created
	"""
	def regcb(self, method):
		return Callback(cb = method, parent = self)