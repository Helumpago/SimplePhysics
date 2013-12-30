
import collections
import threading

## Exception definitions ##
class ParentError(Exception):
	def __init__(self, message):
		Exception.__init__(self, message)

"""
" Defines a dictionary object that can hold more than one object per key
"""
class NamedDictionary(collections.MutableMapping):
	"""
	" CONSTRUCTOR
	"""
	def __init__(self):
		self.children = dict()

	"""
	" Gets the requested set of children
	" @param string key: Name of children to look for
	" @return: Table of children with the requested name. Returns None 
	" 		if there are no children with that name
	"""
	def __getitem__(self, key):
		try:
			return self.children[key]
		except KeyError:
			return None

	"""
	" Adds a child to the dictionary
	" @param string key: Name of child that is being added
	" @param BaseObj value: Reference to the object that is being added
	"""
	def __setitem__(self, key, value):
		try:
			self.children[key].append(value)
		except KeyError:
			self.children[key] = [value]

	"""
	" Removes a specific child from this dictionary
	" @param BaseObj key: Reference to the object to remove.
	"		Note that the expected type is a BaseObj, not a string.
	" @remarks: Throws KeyError if key does not belong to this dictionary
	"""
	def __delitem__(self, key):
		name = key.Name
		i = 0 # Holds the index of the object that will be deleted
		for o in self.children[name]: # Loop through the list of children belonging to this dictionary that have the given name
			if o == key: # Delete the requested object from the children list
				del self.children[name][i]
			else:
				i += 1

	def __iter__(self):
		return iter(self.children)

	def __len__(self):
		return len(self.children)

"""
" Base class for all objects that can be placed in the scene graph
" Defines an object that can do something during the model stage.
"""
class BaseObj(object):
	"""
	" CONSTRUCTOR
	" @param BaseObj parent: Object to which the new object should be parented.
	" 		Expected to be either a BaseObj, subclass of BaseObj, or None
	" @param string Name: Name for this object.
	"""
	def __init__(self, parent = None, Name = "Object"):
		object.__setattr__(self, "lock", threading.Semaphore())
		self.children = NamedDictionary() # Set of children that belong to this object
		self.Name = Name
		object.__setattr__(self, "parent", None)
		self.setParent(parent = parent)

	"""
	" Changes the parent of this object
	" @param BaseObj parent: Object to which this object should be parented.
	" 		Expected to be either a BaseObj, subclass of BaseObj, or None
	"""
	def setParent(self, parent = None):
		## Ensure that this object is not being parented to itself ##
		if self == parent:
			raise ParentError("Can't set parent to self")

		## Remove this object from its original parent ##
		if self.parent != None:
			self.parent.__delChild__(self)

		## Add this object to the new parent ##
		if parent != None:
			parent.__addChild__(self)
		object.__setattr__(self, "parent", parent)

	"""
	" Adds a child to this object
	" @param BaseObj child: Reference to the object to add
	"""
	def __addChild__(self, child):
		self.children[child.Name] = child

	"""
	" Removes a given child from this object
	" @param BaseObj child: Reference to the object to remove
	" @remarks: Throws KeyError if child is not parented to ths object
	"""
	def __delChild__(self, child):
		del self.children[child]

	"""
	" Gets the first child with the given name
	" @param string Name: Name of the object to look for
	" @return: Reference to the first object with the given name.
	"		If no children with that name exist, returns None
	"""
	def getFirst(self, Name):
		try:
			return self.children[Name][0]
		except (KeyError, TypeError):
			return None

	"""
	" Get every child that has the given name
	" @param string Name: Name of objects to collect. If None, all
	" 		children will be collapsed into a single list and returned.
	" 		In other words, set Name to None to get all children
	" @return: List of child objects that have the requested name.
	"		If no children exist with the given name, returns None
	"""
	def getChildren(self, Name = None):
		## non-specific name ##
		if Name == None:
			l = []
			for nameSet in self.children.values(): # Loop through all keys
				for o in nameSet: # loop through all children with the given name
					l.append(o)

			return l

		## Specific name ##
		try:
			return self.children[Name]
		except KeyError:
			return None

	"""
	" Allow setParent to be called by directly setting the parent attribute
	"""
	def __setattr__(self, key, value):
		self.lock.acquire()
		if key != "parent":
			object.__setattr__(self, key, value)
		else:
			self.setParent(value)

		self.lock.release()

	"""
	" Allow automatic thread synchronization
	"""
	def __getitem__(self, key):
		self.lock.acquire()
		o = object.__getitem__(self, key)
		self.lock.release()
		return o

	"""
	" Decide which events should be fired
	"""
	def collectEvents(self):
		pass

	"""
	" Allow this object and its descendents to check whether they should run their events
	"""
	def __collectEvents__(self):
		self.collectEvents()
		for o in self.getChildren():
			o.__collectEvents__()

	"""
	" Prints the name of this object and all its children.
	" @param int depth: Number of tabs to place before he first line.
	" 		Recommended to leave this blank.
	"""
	def printChildren(self, depth = 1):
		for _ in range(1, depth):
			print('\t', end = "")

		print("%s" % self.Name)
		for o in self.getChildren():
			o.printChildren(depth + 1)