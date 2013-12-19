
"""
" Entry point for testing the physics library
"""

from vector2d import Vector2d
from workspace import Workspace
from circle import Circle

w = Workspace(windowSize = Vector2d((1000, 500)), scale = 1)

Circle(parent = w, radius = 5, pos = Vector2d((100, 50)), color = (50, 250, 150))

w.start()
