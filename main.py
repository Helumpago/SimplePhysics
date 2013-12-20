
"""
" Entry point for testing the physics library
"""

import time
from vector2d import Vector2d
from workspace import Workspace
from circle import Circle
import events

def onQuit(self):
	self.close()
	exit()

def onQuit2(self):
	print("yeahhhh, it worked!")

w = Workspace(windowSize = Vector2d((1000, 500)), scale = 1.5)

c = Circle(parent = w, radius = 5, pos = Vector2d((100, 50)), color = (50, 250, 150), velocity = Vector2d((40, 4)))

w.registerCallback(events.QUIT, onQuit2)
w.registerCallback(events.QUIT, onQuit)

w.start()

time.sleep(1)
c.pos = Vector2d((50, 200))
time.sleep(1)
c.velocity = Vector2d((50, -50))