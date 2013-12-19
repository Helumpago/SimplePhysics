
"""
" Entry point for testing the physics library
"""

import time
from vector2d import Vector2d
from workspace import Workspace
from circle import Circle

w = Workspace(windowSize = Vector2d((1000, 500)), scale = 1)

c = Circle(parent = w, radius = 5, pos = Vector2d((100, 50)), color = (50, 250, 150), velocity = Vector2d((40, 4)))

w.start()

time.sleep(1)
c.pos = Vector2d((50, 200))
time.sleep(1)
c.velocity = Vector2d((50, 50))