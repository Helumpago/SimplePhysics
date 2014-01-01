
from .collision_model import CollisionModel
from .collidable import Collidable

"""
" Checks for possible collisions by comparing every object against every other object
"""
class NaiveCollisionModel(CollisionModel):
	"""
	" CONSTRUCTOR
	" @param string Name: Name for this object.
	" @param int fps: Maximum number of frames per second allowable.
	" @param [EventlessObject] collidables: List of objects that should be checked during broad phase.
	" 		Note that the objects in this list do not have to be Collidable objects 
	" 		themselves, as all objects descending from the objects in this list will be checked.
	"""
	def __init__(self, Name = "CollisionModel", fps = 60, collidables = []):
		CollisionModel.__init__(self, Name = Name, fps = fps, collidables = collidables)

	"""
	" Algorithm that decides whether objects could possibly collide (broad phase collision detection)
	"""
	def test(self):
		pass

	"""
	" Gets the list of objects that may be colliding with a given particle
	" @param Collidable particle: Reference to the object that should be checked
	"""
	def getPossibleCollisions(self, particle):
		pass