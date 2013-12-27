
"""
" Test script for Phy
"""

import time
from pygame_model import PygameModel
from base_obj import BaseObj
from drawable import Drawable
from pygame_view import PygameView
from region import Region
from value import Number, Vector2d
from pygame_shapes import PygameCircle

def printChildren(obj, depth = 1):
	for _ in range(1, depth):
		print('\t', end = "")

	print("%s" % obj.Name)
	for o in obj.getChildren():
		printChildren(o, depth + 1)

w = PygameModel(fps = 60)

v = PygameView(parent = w)
c = PygameCircle(parent = v, pos = (100, 100), radius = 5, color = (255, 255, 255))

printChildren(w)
print(c.pos.getAValue())

w.start()