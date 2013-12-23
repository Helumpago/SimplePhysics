
"""
" Entry point for testing the physics library
"""

import time
from vector2d import Vector2d
from workspace import Workspace
from circle import Circle
import events
from wall import Wall
from region import Region

def onQuit(self):
	self.close()
	exit()

def inside(hit):
	if(hit.Name != "circle"):
		return

	if hit.color[0] < 250 and hit.color[1] < 250 and hit.color[2] < 250:
		hit.color = (hit.color[0] + 1, hit.color[1] + 1, hit.color[2] + 1)
	else:
		hit.color = (0, 0, 0)

w = Workspace(windowSize = Vector2d((1000, 500)), scale = 1)
w.registerCallback(events.QUIT, onQuit)

## Create scene ##
Region(parent = w).registerCallback(events.INREGION, inside)

c = Circle(parent = w, radius = 5, pos = Vector2d((100, 50)), color = (0, 0, 0), velocity = Vector2d((40, 4)))
Wall(parent = w, pos1 = Vector2d((0, 0)), pos2 = Vector2d((w.windowSize.x, 0)))
Wall(parent = w, pos1 = Vector2d((0, w.windowSize.y - 1)), pos2 = Vector2d((w.windowSize.x, w.windowSize.y - 1)))
Wall(parent = w, pos1 = Vector2d((0, 0)), pos2 = Vector2d((0, w.windowSize.y)))
Wall(parent = w, pos1 = Vector2d((w.windowSize.x - 1, 0)), pos2 = Vector2d((w.windowSize.x - 1, w.windowSize.y)))

## Begin the sim ##
w.start()