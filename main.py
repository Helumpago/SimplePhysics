
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

v = PygameView(parent = w, scale = 4)
c = PygameCircle(parent = v, Name = "Main", pos = (50, 50), radius = 50, scale = 1, color = (50, 255, 40))
PygameCircle(parent = c, pos = (0, 0), radius = 25, scale = 1, color = (50, 50, 250))

w.start()

while True:
	v.scale.setValue(v.scale.getValue() / 1.01)
	time.sleep(0.01)