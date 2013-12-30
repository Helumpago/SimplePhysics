
"""
" Test script for Phy
"""

import time
import random
from pygame_model import PygameModel
from base_obj import BaseObj
from drawable import Drawable
from pygame_view import PygameView
from region import Region
from value import Number, Vector2d
from pygame_shapes import PygameCircle, PygameLine
from physical import Physical

class Ball(PygameCircle, Physical):
	def __init__(self, parent = None, Name = "Circle", radius = 1, pos = (0, 0), scale = 1, color = (0, 0, 0), velocity = (0, 0)):
		PygameCircle.__init__(self, parent = parent, Name = Name, radius = radius, pos = pos, scale = scale, color = color)
		Physical.__init__(self)
		self.color = color
		self.velocity = velocity
		self.timer = 0

def setPos(event):
	self = event.owner
	if self.timer > 1000:
		self.timer = 0
		PygameCircle(parent = self.parent, Name = "Trace", radius = 2, pos = self.pos.getValue(), color = (255, 255, 255))
	else:
		self.timer += event.dt

	posRef = event.owner.pos
	posRef.setValue((posRef.getValue()[0] + event.owner.velocity[0] * event.dt/1000, posRef.getValue()[1] + event.owner.velocity[1] * event.dt/1000))

def gravity(event):
	vel = event.owner.velocity
	event.owner.velocity = (vel[0], vel[1] + 9.81 * event.dt/1000)

def zoom(event):
	scale = event.owner.scale.getValue()
	event.owner.scale.setValue(scale + event.dt/10000)

def changeColor(event):
	if event.owner.timer > 1000:
		event.owner.color = (random.randrange(255), random.randrange(255), random.randrange(255))

w = PygameModel(fps = 60)
v = PygameView(parent = w, scale = 1, size = (1000, 500))
c = Ball(parent = v, Name = "Main", pos = (0, 0), radius = 10, color = (0, 255, 0), velocity = (-25, -65))
Ball(parent = c, color = (0, 0, 255), radius = 5, Name = "Center")
PygameLine(parent = v, color = (255, 255, 255), pos = (0, 0), size = (7.071, 7.071))

c.events.getFirst("onStep").regcb(setPos)
c.events.getFirst("onStep").regcb(gravity)
c.events.getFirst("onDraw").regcb(changeColor)
# v.onStep.regcb(zoom)

w.events.getFirst("onQuit").regcb(v.close)
w.start()