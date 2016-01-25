#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-
# TODO: method that returns a generator.
# TODO: delete, search, slicing
# TODO: More heads for faster accessing


class Node:
	"""docstring for Node"""

	def __init__(self, data=None, next_element=None):
		super(Node, self).__init__()
		self._data = data
		# Stores the reference to a next element
		self._next = next_element

	def setNext(self, node):
		self._next = node

	def getNext(self):
		return self._next

	def getData(self):
		return self._data


class LinkedList(object):
	"""docstring for LinkedList"""

	def __init__(self, oor_policy="border"):
		super(LinkedList, self).__init__()
		# TODO: Initialization from iterable
		# The first element (node) in list
		self._first = None
		# It is currently empty
		self._length = 0
		# Global out-of-range policy if none specified for a function
		self._global_oor_policy = oor_policy

	# def slice(self, start=0, end=None):
	# 	if end is None:
	# 		end = self._length

	def _oorPolicyHandler(self, index, oor_policy=None):
		"""
		Handles what to do with an index if it goes beyond the range of list
		:param index:
		:param oor_policy: Parameter that determines how to treat out-of-range indexes.
		If set to "border" (which is default),
		this method returns the last element in the list if `index` is equal or higher than list's length
		and the first element if `index` is below zero.
		If set to "round", then the out of range indicies are modulated by length of list.
		For example, if a list has 3 elements, then `index` of 3 returns the first element (just like `index` of 0),
		4 returns the second, 5 returns the third, 6 returns the first again, etc.
		Likewise, index of -1 returns the third element, -2 returns the second, -3 returns the first,
		-4 returns the third again, etc.
		If set to "except", any out-of-range indicies raise IndexError.
		Note: if the list is empty, IndexError is raised in any case.
		:return: the new index or None
		"""

		# If no policy is specified, import global one
		if not oor_policy:
			oor_policy = self._global_oor_policy

		# How to handle out-of-range indexes?
		if oor_policy == "except":
			# Throw exception
			try:
				if index < 0 or index >= self._length:
					raise IndexError("""No element with index %d!
						Note: you can change the oor_policy argument.
						See documentation for more details.""" % index)
			except IndexError as e:
				print(str(e))
				index = None
		elif oor_policy == "round":
			index %= self._length
		# In case of default "border" or anything else (Anti-fool protection).
		else:
			# Set to border value (first or last)
			if index < 0:
				index = 0
			elif index >= self._length:
				index = self._length - 1

		return index

	def append(self, data):
		self.insert(data, index=self._length)

	# TODO insert is not supposed to work for last element. use append instead for that.
	def insert(self, data, index=0):
		"""
		Inserts an element at the given index.
		:param data: data to put.
		:param index: index to put data to. 
		If index is equal or larger than the list length, element is put right before the last element.
		If index is negative, index is set to 0, and the element is put in the beginning of the list.
		:return: None
		"""

		if not self._first:
			# List is empty.
			self._first = Node(data=data)
		else:
			# List is not empty
			if index < 0:
				index = 0
			elif index > self._length:
				index = self._length

			# Inserting element to the beginning of the list
			if index == 0:
				# Create new node
				new_elem = Node(data=data)
				# Make the current first node the next one
				new_elem.setNext(self._first)
				# Make it the first
				self._first = new_elem
			# Inserting somewhere else
			else:
				# Get the element that will be the previous for the new one
				prev_elem = self._first
				for i in range(index - 1):
					prev_elem = prev_elem.getNext()
				# Get the element that will be the next for the new one
				next_elem = prev_elem.getNext()
				# Create new node
				new_elem = Node(data=data)
				# Set the new element as the next one for the previous one
				prev_elem.setNext(new_elem)
				# Set the next one
				new_elem.setNext(next_elem)

		# updating length
		self._length += 1

	def getLength(self):
		"""
		Returns the number of elements in the list
		:return: number of elements in the list
		:rtype: int
		"""
		return self._length

	def _updateLength(self):
		# TODO: test this one
		# Is list empty?
		if not self._first:
			# yes, because there is no first node.
			length = 0
		else:
			# nope!
			count = 0
			cur_node = self._first
			while cur_node:
				cur_node = cur_node.getNext()
				count += 1
			length = count
		self._length = length

	def getByIndex(self, index=0, oor_policy=None):
		"""
		Get the element data by index.
		:param index:
		:param oor_policy: Parameter that determines how to treat out-of-range indexes.
		If set to "border" (which is default),
		this method returns the last element in the list if `index` is equal or higher than list's length
		and the first element if `index` is below zero.
		If set to "round", then the out of range indicies are modulated by length of list.
		For example, if a list has 3 elements, then `index` of 3 returns the first element (just like `index` of 0),
		4 returns the second, 5 returns the third, 6 returns the first again, etc.
		Likewise, index of -1 returns the third element, -2 returns the second, -3 returns the first,
		-4 returns the third again, etc.
		If set to "except", any out-of-range indicies raise IndexError.
		Note: if the list is empty, IndexError is raised in any case.
		:raises: IndexError
		:return: data
		"""
		try:
			# Check for existence of the first element. If not, the list is empty.
			if not self._first:
				raise IndexError("List is empty. There's nothing to get.")
			# If we try to get the first element, everything's easy
			if index == 0:
				return self._first.getData()
			# not the first element
			else:
				index = self._oorPolicyHandler(index, oor_policy=oor_policy)

				if not (index is None):
					# Getting the element
					elem = self._first
					for i in range(index):
						elem = elem.getNext()
					return elem.getData()

		except IndexError as e:
			print(str(e))
