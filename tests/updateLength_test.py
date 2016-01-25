#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-
from unittest import TestCase

from LinkedList import LinkedList


class TestLinkedList(TestCase):
	def test__updateLength(self):
		ll = LinkedList()

		ll._updateLength()
		self.assertEqual(ll.getLength(), 0)

		ll.insert("cero")
		self.assertEqual(ll.getLength(), 1)

		ll._updateLength()
		self.assertEqual(ll.getLength(), 1)

		ll.insert("uno")
		ll.insert("dos")
		ll.insert("tres")
		ll.insert("cuatro")
		ll.insert("cinco")
		self.assertEqual(ll.getLength(), 6)

		ll._updateLength()
		self.assertEqual(ll.getLength(), 6)
