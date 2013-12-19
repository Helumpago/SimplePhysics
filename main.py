
"""
" Entry point for testing the physics library
"""

from vector2d import Vector2d
from workspace import Workspace
from base_obj import BaseObj

class thing(BaseObj):
	def __init__(self, Name = "object", parent = None):
		BaseObj.__init__(self, Name, parent)

w = Workspace(windowSize = Vector2d((1000, 500)))

t1 = thing()
thing(parent = w)
thing(parent = w, Name = "Thing")
t1.setParent(target = w)

w.start()

for o in w.getChildren("object"):
	print(o.Name)

print()
print(w.getChild("Thing").Name)