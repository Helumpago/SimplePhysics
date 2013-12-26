
"""
" Test script for Phy
"""

from base_obj import BaseObj
import drawable
import events

def printChildren(obj, depth = 1):
	for _ in range(1, depth):
		print('\t', end = "")

	print("%s" % obj.Name)
	for o in obj.getChildren():
		printChildren(o, depth + 1)

w = BaseObj(Name = "Workspace")
BaseObj(Name = "Object", parent = w)
BaseObj(Name = "Object", parent = w)
BaseObj(Name = "Object", parent = w)
t = BaseObj(Name = "Thing", parent = w.getFirst("Object"))

printChildren(w)

print("-------")
w.getChildren("Object")[1].parent = t
printChildren(w)