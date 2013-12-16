
from physical import Physical

"""
" Extend this class to allow an object to participate in collisions
"""
class Moveable(Physical):
	"""
	" CONSTRUCTOR
	" @param canCollide: Boolean: True if this object can cause collisions
	" @param anchored: Boolean: False if this object can move.  Note that anchored objects
	"		can still have velocity.  They themselves will not be affected by the velocity,
	"		but collisions with another object will act as though this object was moving.
	" @param velocity: (int X, int Y): Vector indicating the direction the objec is moving.
	"""
	def __init__(self, canCollide = True, anchored = False, velocity = (0, 0)):
		self.canCollide = canCollide
		self.anchored = anchored
		self.velocity = velocity

	"""
	" Get this object's position
	"""
	def getPos(self):
		return (0, 0)

	"""
	" Set the position of this object
	"""
	def setPos(self, pos):
		pass

	"""
	" Checks for collisions and moves this object accordingly
	" @param window: Window: Container object describing the render window, scale, and
	"		objects in this world
	"""
	def frame(self, window):
		if(self.anchored == True):
			return

		pos = self.getPos()
		pos = (pos[0] + self.velocity[0] * window.scale, pos[0] + self.velocity[1] * window.scale)
		self.setPos(pos)