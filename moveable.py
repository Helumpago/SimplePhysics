
from physical import Physical
from vector2d import Vector2d
import events

"""
" Defines an object that can participate in collisions
"""
class Moveable(Physical):
	"""
	" CONSTRUCTOR
	" @param Vector2d velocity: Object's velocity
	"""
	def __init__(self, Name = "object", parent = None, canCollide = True, anchored = False, velocity = Vector2d((0, 0))):
		Physical.__init__(self, Name = Name, parent = parent)
		self.velocity = velocity
		self.anchored = anchored
		self.canCollide = canCollide

	"""
	" Get the shape's position
	" @return: Vector2d indicating the shape's position
	"""
	def getPos(self):
		return Vector2d((0, 0))

	"""
	" Set the shape's position
	" @param Vector2d pos: New position
	"""
	def setPos(self, pos):
		pass

	"""
	" Get whether a given point is inside this object
	" @param Vector2d pos: Point to check
	" @return: None if the point is not contained in this shape.  Otherwise,
	" 		returns a Vector2d value that represents the normal unit vector of the collision
	"""
	def hasPoint(self, pos):
		return None

	"""
	" Move this shape according to its velocity
	" @param int dt: Number of milliseconds since the last frame
	"""
	def step(self, dt):
		if(self.anchored == True):
			return

		pos = self.getPos()
		pos = Vector2d((pos.x + self.velocity.x * (dt/1000) * self.parent.scale, pos.y + self.velocity.y * (dt/1000) * self.parent.scale))
		self.setPos(pos)

	"""
	" Check for collisions
	"""
	def collectEvents(self):
		Physical.collectEvents(self)

		## If this object is anchored, ignore all collision events ##
		if self.canCollide == False or self.anchored == True:
			return

		## Check for collisions with this object ##
		allObjs = self.parent.getChildren()
		for o in allObjs:
			## Ignore this object and any non-moveable objects##
			if (isinstance(o, Moveable) != True) or (o == self):
				continue

			## If the current object isn't colliding with this object, skip ##
			if o.hasPoint(self.getPos()) == None:
				continue

			## If the current object is colliding ##
			try:
				cbs = self.events[events.COLLISION] # get all registered callbacks
			except KeyError: # If there are no registered callbacks, all collisions are ignored, so break out of the loop
				break

			## Create a new sequence of parameterized callbacks for this collision ##
			thisCollision = [] # List of specific collision events for this collision
			for cb in cbs:
				ev = events.COLLISION(hit = o, callback = cb)
				thisCollision.append(ev)

			self.events += thisCollision # Append the new set of collision callbacks

	"""
	" Runs the callbacks for all fired events
	"""
	def fireEvents(self):
		Physical.fireEvents(self)

		try:
			for cb in self.events(events.COLLISION):
				cb.call()
		except KeyError:
			pass