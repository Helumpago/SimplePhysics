
from base_obj import BaseObj

"""
" Base class for all value types that can be placed in the scene graph
"""
class Value(BaseObj):
	"""
	" CONSTRUCTOR
	" @param BaseObj parent: Object to which the new object should be parented.
	" 		Expected to be either a BaseObj, subclass of BaseObj, or None
	" @param string Name: Name for this object.
	"""
	def __init__(self, parent = None, Name = "Value"):
		BaseObj.__init__(self, parent = parent, Name = Name)
		self.__value__ = None # Container for the actual value owned by this object

	"""
	" Get the exact value owned by this object.
	" Does not request any state information from ancestors
	"""
	def getValue(self):
		return self.__value__

	"""
	" Set the value owned by this object
	"""
	def setValue(self, v):
		self.__value__ = v

	"""
	" Get the absolute value for this object
	" Queries necessary state info from ancestors
	"""
	def getAValue(self):
		v = self.initValue()
		## Walk up the parent tree, watching for parents that have a value with the same name ##
		cur = self.parent
		while cur != None:
			if cur.getFirst(self.Name) != None:
				v = self.combine(v, cur.getFirst(self.Name).getValue())
			cur = cur.parent

		return v

	"""
	" Defines how to combine two values. For example, should the value object
	" 		add or multiply ancestor values into this value?
	" Used when this value walks up its parent tree to combine similar values
	"""
	def combine(self, v1, v2):
		raise NotImplementedError("combine() method left unimplemented")

	"""
	" Decides whether the value that belongs to this object should be included when
	" 		calculating the absolute value
	" @return: Value that represents the first value that should be used when walking
	" 		up the parent tree.
	"""
	def initValue(self):
		raise NotImplementedError("initValue() method left unimplemented")

"""
" Number value that can be placed in the scene graph
"""
class Number(Value):
	"""
	" CONSTRUCTOR
	" @param BaseObj parent: Object to which the new object should be parented.
	" 		Expected to be either a BaseObj, subclass of BaseObj, or None
	" @param string Name: Name for this object.
	" @param number value: Starting value for this object
	"""
	def __init__(self, parent = None, Name = "Number", value = 0):
		Value.__init__(self, parent = parent, Name = Name)
		self.__value__ = value # Container for the actual value owned by this object

	"""
	" Adds similar values together
	" Used when this value walks up its parent tree to combine similar values
	"""
	def combine(self, v1, v2):
		return v1 + v2

	"""
	" Decides whether the value that belongs to this object should be included when
	" 		calculating the absolute value
	" @return: Value that represents the first value that should be used when walking
	" 		up the parent tree.
	"""
	def initValue(self):
		return 0

"""
" Same as a Number, except values are combined using multiplication instead of addition
"""
class Ratio(Number):
	"""
	" CONSTRUCTOR
	" @param BaseObj parent: Object to which the new object should be parented.
	" 		Expected to be either a BaseObj, subclass of BaseObj, or None
	" @param string Name: Name for this object.
	" @param number value: Starting value for this object
	"""
	def __init__(self, parent = None, Name = "Number", value = 0):
		Number.__init__(self, parent = parent, Name = Name, value = value)

	"""
	" Multiplies similar values together
	" Used when this value walks up its parent tree to combine similar values
	"""
	def combine(self, v1, v2):
		return v1 * v2

	"""
	" Decides whether the value that belongs to this object should be included when
	" 		calculating the absolute value
	" @return: Value that represents the first value that should be used when walking
	" 		up the parent tree.
	"""
	def initValue(self):
		return 1

"""
" Tuple representing a 2D vector
"""
class Vector2d(Value):
	"""
	" CONSTRUCTOR
	" @param BaseObj parent: Object to which the new object should be parented.
	" 		Expected to be either a BaseObj, subclass of BaseObj, or None
	" @param string Name: Name for this object.
	" @param number value: Starting value for this object
	"""
	def __init__(self, parent = None, Name = "Number", value = 0):
		Value.__init__(self, parent = parent, Name = Name)
		self.__value__ = value # Container for the actual value owned by this object

	"""
	" Adds the two coordinates of the tuple together
	" Used when this value walks up its parent tree to combine similar values
	"""
	def combine(self, v1, v2):
		return (v1[0] + v2[0], v1[1] + v2[0])

	"""
	" Decides whether the value that belongs to this object should be included when
	" 		calculating the absolute value
	" @return: Value that represents the first value that should be used when walking
	" 		up the parent tree.
	"""
	def initValue(self):
		return (0, 0)