
"""
" Entry point for the simulation.  Starts the simulation thread and watches for input
"""

import time
from world import World
from sphere import Sphere
from wall import Wall

wSize = (1000, 500)

mthread = World(windowSize = wSize, scale = 2)
s = Sphere(r = 3, pos = (50, 50), color = (0, 100, 100), velocity = (50, 10), parent = mthread.workspace)

Wall(pos1 = (0, 0), pos2 = (wSize[0], 0), parent = mthread.workspace)
Wall(pos1 = (0, wSize[1] - 1), pos2 = (wSize[0], wSize[1] - 1), parent = mthread.workspace)
Wall(pos1 = (0, 0), pos2 = (0, wSize[1]), parent = mthread.workspace)
Wall(pos1 = (wSize[0] - 1, 0), pos2 = (wSize[0] - 1, wSize[1]), parent = mthread.workspace)

mthread.start()

time.sleep(1)
s.velocity = (40, 100)
time.sleep(1)
s.anchored = True