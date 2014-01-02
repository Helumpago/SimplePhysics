
from .collision_model import CollisionModel
from .collidable import Collidable

"""
" Checks for possible collisions by comparing every object against every other object
"""
class NaiveCollisionModel(CollisionModel):
	"""
	" Checks for intersection between two bounding boxes
	" @param RectRegion box1, box2: Objects to check
	" @return bool: True if the boxes intersect, false otherwise
	"""
	def intersects(box1, box2):
		for signX in range(-1, 1, 2):
			for signY in range(-1, 1, 2):
				corner = (box2.pos.getAValue()[0] + signX * box2.size.getValue()[0]/2, box2.pos.getAValue()[1] + signY * box2.size.getValue()[1]/2)

				if box1.isSurrounding(corner):
					return True

		return False

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
	def broadPhase(self):
		self.mayCollide.flush() # Flush old collision data
		actors = CollisionModel.collapseChildren(self.collidables)

		## Check all pairs of objects for collisions ##
		for o1 in actors:
			for o2 in actors:
				if o1 == o2:
					continue

				if NaiveCollisionModel.intersects(o1, o2):
					self.mayCollide[o1] = o2

	"""
	" Gets the list of objects that may be colliding with a given particle
	" @param Collidable particle: Reference to the object that should be checked
	"""
	def getPossibleCollisions(self, particle):
		return self.data[particle]