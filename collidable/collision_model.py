
from ..model import Model
from .broad_phase import BroadPhase

"""
" Defines a model that, in addition to the regular tasks of a model,
" 		checks for collisions between objects
"""
class CollisionModel(Model, BroadPhase):
	"""
	" CONSTRUCTOR
	" @param string Name: Name for this object.
	" @param int fps: Maximum number of frames per second allowable.
	" @param collidables []: List of objects that should be checked during broad phase.
	" 		Note that the objects in this list do not have to be Collidable objects 
	" 		themselves, as all objects descending from the objects in this list will be checked.
	"""
	def __init__(self, Name = "CollisionModel", fps = 60, collidables = []):
		Model.__init__(self, Name = Name, fps = fps)
		BroadPhase.__init__(collidables = collidables)

	"""
	" Algorithm that decides whether objects could possibly collide (broad phase collision detection)
	"""
	def test(self):
		raise NotImplementedError("test() method left unimplemented")

	"""
	" Gets the list of objects that may be colliding with a given particle
	" @param Collidable particle: Reference to the object that should be checked
	"""
	def getPossibleCollisions(self, particle):
		raise NotImplementedError("getPossibleCollisions() method left unimplemented")