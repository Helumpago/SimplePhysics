
"""
" Entry point for testing the physics library
"""

from vector2d import Vector2d
from workspace import Workspace
from base_obj import BaseObj

class thing(BaseObj):
	def __init__(self, name = "object", parent = None):
		BaseObj.__init__(self, name, parent)

w = Workspace(Vector2d(1000, 100))

t1 = thing(parent = w)

w.start()

print("Hi!")