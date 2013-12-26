
"""
" Test script for Phy
"""

from pygame_model import PygameModel
from base_obj import BaseObj
from drawable import Drawable
import events

def printChildren(obj, depth = 1):
	for _ in range(1, depth):
		print('\t', end = "")

	print("%s" % obj.Name)
	for o in obj.getChildren():
		printChildren(o, depth + 1)

w = PygameModel(fps = 1)
w.start()