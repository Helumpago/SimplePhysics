
"""
" Entry point for testing the physics library
"""

import time
from vector2d import Vector2d
from workspace import Workspace
from circle import Circle
import events
from wall import Wall

def onQuit(self):
	self.close()
	exit()

w = Workspace(windowSize = Vector2d((1000, 500)), scale = 1)
w.registerCallback(events.QUIT, onQuit)

## Create scene ##
c = Circle(parent = w, radius = 5, pos = Vector2d((100, 50)), color = (50, 250, 150), velocity = Vector2d((40, 4)))
Wall(parent = w, pos1 = Vector2d((0, 0)), pos2 = Vector2d((w.windowSize.x, 0)))
Wall(parent = w, pos1 = Vector2d((0, w.windowSize.y - 1)), pos2 = Vector2d((w.windowSize.x, w.windowSize.y - 1)))
Wall(parent = w, pos1 = Vector2d((0, 0)), pos2 = Vector2d((0, w.windowSize.y)))
Wall(parent = w, pos1 = Vector2d((w.windowSize.x - 1, 0)), pos2 = Vector2d((w.windowSize.x - 1, w.windowSize.y)))

w.start()

print(w.getChildren())

time.sleep(1)
c.pos = Vector2d((50, 200))
time.sleep(1)
c.velocity = Vector2d((50, -50))