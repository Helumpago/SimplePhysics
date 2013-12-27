
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

def printChildren(obj, depth = 1):
	for _ in range(1, depth):
		print('\t', end = "")

	print("%s" % obj.Name)
	for o in obj.getChildren():
		printChildren(o, depth + 1)

w = PygameModel(fps = 60)

n = w
for i in range(0, 3):
	n = Vector2d(parent = n, value = (1,1))

printChildren(w)
# print("%d" % n.getAValue())
print("%s, %s" % (n.getValue(), n.getAValue()))

#w.start()