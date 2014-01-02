
from ..eventless_object import NamedDictionary
from ..model import Model
from .collidable import Collidable

"""
" Defines a model that, in addition to the regular tasks of a model,
" 		checks for collisions between objects
"""
class CollisionModel(Model):
	"""
	" STATIC
	" Recursively moves through a list of objects, checking for those that are collidable
	" 		Includes all descendants of anything in the list
	" @param [EventlessObject] collidables: List of objects to check.
	" @return: List of all collidable objects (in no particular order)
	"""
	def collapseChildren(collidables):
		l = [] # List of Collidables that descend from self.collidables
		for o in collidables:
			l += CollisionModel.collapseChildren(o.getChildren())

			if isinstance(o, Collidable) != True:
				continue
			l.append(o)

		return l

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
		self.collidables = collidables
		self.mayCollide = NamedDictionary() # Holds info on objects that may be colliding. Key: Reference to object1. Value: List of objects that may be colliding with object1

	"""
	" Runs the two part collision detection algorithm
	"""
	def checkCollisions(self):
		self.broadPhase()
		self.narrowPhase()

	"""
	" Algorithm that decides whether objects could possibly collide (broad phase collision detection)
	"""
	def broadPhase(self):
		raise NotImplementedError("broadPhase() method left unimplemented")

	"""
	" Allows all possible collisions to confirm that they are touching
	"""
	def narrowPhase(self):
		for o in self.mayCollide:
			for target in self.mayCollide[o]:
				o.events.getFirst("onCollision").fire = o.confirmCollision(target)
				# target.getFirst("onCollision").fire = target.confirmCollision(o)
			 
	"""
	" Gets the list of objects that may be colliding with a given particle
	" @param Collidable particle: Reference to the object that should be checked
	"""
	def getPossibleCollisions(self, particle):
		raise NotImplementedError("getPossibleCollisions() method left unimplemented")