
"""
" Entry point for testing the physics library
"""

from vector2d import Vector2d
from workspace import Workspace

w = Workspace(Vector2d(1000, 100))
w.start()

print("Hi!")