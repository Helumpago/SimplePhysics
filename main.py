
"""
" Entry point for the simulation.  Starts the simulation thread and watches for input
"""

import time
from world import World
from sphere import Sphere
from wall import Wall

mthread = World(windowSize = (600, 500), scale = 2)
mthread.addObj(Sphere(r = 3, pos = (50, 50), color = (0, 100, 100), velocity = (50, 10)))
mthread.start()

mthread.addObj(Wall(pos1 = (50, 50), pos2 = (100, 100)))
mthread.addObj(Wall(pos1 = (70, 50), pos2 = (200, 100)))