#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-
import unittest
from LinkedList import LinkedList


class TestLinkedList(unittest.TestCase):
	"""docstring for TestLinkedList"""

	def test_GetByIndex_BorderOOPList(self):
		# `border` is the default policy, so I specify nothing
		ll = LinkedList()
		self.assertEqual(ll.getLength(), 0)

		self.assertRaises(IndexError, ll.getByIndex(0))
		self.assertRaises(IndexError, ll.getByIndex(1))
		self.assertRaises(IndexError, ll.getByIndex(-1))

		ll.insert(data="tres", index=-1)
		self.assertEqual(ll.getByIndex(0), "tres")
		self.assertEqual(ll.getByIndex(1), "tres")
		self.assertEqual(ll.getByIndex(-1), "tres")
		self.assertEqual(ll.getLength(), 1)

		ll.insert(data="uno")
		self.assertEqual(ll.getByIndex(0), "uno")
		self.assertEqual(ll.getByIndex(1), "tres")
		self.assertEqual(ll.getByIndex(-1), "uno")
		self.assertEqual(ll.getByIndex(-2), "uno")
		self.assertEqual(ll.getByIndex(2), "tres")
		self.assertEqual(ll.getByIndex(3), "tres")
		self.assertEqual(ll.getByIndex(4), "tres")
		self.assertEqual(ll.getLength(), 2)

		ll.insert(data="dos", index=1)
		self.assertEqual(ll.getByIndex(0), "uno")
		self.assertEqual(ll.getByIndex(2), "tres")
		self.assertEqual(ll.getByIndex(1), "dos")
		self.assertEqual(ll.getByIndex(-1), "uno")
		self.assertEqual(ll.getByIndex(-2), "uno")
		self.assertEqual(ll.getByIndex(-3), "uno")
		self.assertEqual(ll.getByIndex(-4), "uno")
		self.assertEqual(ll.getByIndex(3), "tres")
		self.assertEqual(ll.getByIndex(4), "tres")
		self.assertEqual(ll.getByIndex(5), "tres")
		self.assertEqual(ll.getLength(), 3)

		ll.insert(data="cuatro", index=5)
		self.assertEqual(ll.getByIndex(0), "uno")
		self.assertEqual(ll.getByIndex(2), "tres")
		self.assertEqual(ll.getByIndex(1), "dos")
		self.assertEqual(ll.getByIndex(3), "cuatro")
		self.assertEqual(ll.getByIndex(4), "cuatro")
		self.assertEqual(ll.getByIndex(5), "cuatro")
		self.assertEqual(ll.getByIndex(6), "cuatro")
		self.assertEqual(ll.getByIndex(7), "cuatro")
		self.assertEqual(ll.getByIndex(-1), "uno")
		self.assertEqual(ll.getByIndex(-2), "uno")
		self.assertEqual(ll.getByIndex(-3), "uno")
		self.assertEqual(ll.getByIndex(-4), "uno")
		self.assertEqual(ll.getByIndex(-5), "uno")
		self.assertEqual(ll.getLength(), 4)

		ll.insert(data="cero", index=0)
		self.assertEqual(ll.getByIndex(1), "uno")
		self.assertEqual(ll.getByIndex(3), "tres")
		self.assertEqual(ll.getByIndex(2), "dos")
		self.assertEqual(ll.getByIndex(4), "cuatro")
		self.assertEqual(ll.getByIndex(0), "cero")
		self.assertEqual(ll.getByIndex(-1), "cero")
		self.assertEqual(ll.getByIndex(-2), "cero")
		self.assertEqual(ll.getByIndex(-3), "cero")
		self.assertEqual(ll.getByIndex(-4), "cero")
		self.assertEqual(ll.getByIndex(-5), "cero")

		self.assertEqual(ll.getLength(), 5)

	def test_GetByIndex_RoundOOPList(self):
		ll = LinkedList(oor_policy="round")
		self.assertEqual(ll.getLength(), 0)

		self.assertRaises(IndexError, ll.getByIndex(0))
		self.assertRaises(IndexError, ll.getByIndex(1))
		self.assertRaises(IndexError, ll.getByIndex(-1))

		ll.insert("tres")
		self.assertEqual(ll.getByIndex(0), "tres")
		self.assertEqual(ll.getByIndex(1), "tres")
		self.assertEqual(ll.getByIndex(-1), "tres")
		self.assertEqual(ll.getLength(), 1)

		ll.insert(data="uno")
		self.assertEqual(ll.getByIndex(0), "uno")
		self.assertEqual(ll.getByIndex(1), "tres")
		self.assertEqual(ll.getByIndex(-1), "tres")
		self.assertEqual(ll.getByIndex(-2), "uno")
		self.assertEqual(ll.getByIndex(2), "uno")
		self.assertEqual(ll.getByIndex(3), "tres")
		self.assertEqual(ll.getByIndex(4), "uno")
		self.assertEqual(ll.getLength(), 2)

		ll.insert(data="dos", index=1)
		self.assertEqual(ll.getByIndex(0), "uno")
		self.assertEqual(ll.getByIndex(2), "tres")
		self.assertEqual(ll.getByIndex(1), "dos")
		self.assertEqual(ll.getByIndex(-1), "tres")
		self.assertEqual(ll.getByIndex(-2), "dos")
		self.assertEqual(ll.getByIndex(-3), "uno")
		self.assertEqual(ll.getByIndex(-4), "tres")
		self.assertEqual(ll.getByIndex(3), "uno")
		self.assertEqual(ll.getByIndex(4), "dos")
		self.assertEqual(ll.getByIndex(5), "tres")
		self.assertEqual(ll.getByIndex(6), "uno")

		self.assertEqual(ll.getLength(), 3)

		ll.insert(data="cuatro", index=3)
		self.assertEqual(ll.getByIndex(0), "uno")
		self.assertEqual(ll.getByIndex(2), "tres")
		self.assertEqual(ll.getByIndex(1), "dos")
		self.assertEqual(ll.getByIndex(3), "cuatro")
		self.assertEqual(ll.getByIndex(4), "uno")
		self.assertEqual(ll.getByIndex(5), "dos")
		self.assertEqual(ll.getByIndex(6), "tres")
		self.assertEqual(ll.getByIndex(7), "cuatro")
		self.assertEqual(ll.getByIndex(-1), "cuatro")
		self.assertEqual(ll.getByIndex(-2), "tres")
		self.assertEqual(ll.getByIndex(-3), "dos")
		self.assertEqual(ll.getByIndex(-4), "uno")
		self.assertEqual(ll.getByIndex(-5), "cuatro")
		self.assertEqual(ll.getLength(), 4)

		ll.insert(data="cero", index=0)
		self.assertEqual(ll.getByIndex(1), "uno")
		self.assertEqual(ll.getByIndex(3), "tres")
		self.assertEqual(ll.getByIndex(2), "dos")
		self.assertEqual(ll.getByIndex(4), "cuatro")
		self.assertEqual(ll.getByIndex(0), "cero")
		self.assertEqual(ll.getLength(), 5)

	def test_GetByIndex_ExceptOOPList(self):
		ll = LinkedList(oor_policy="except")
		self.assertEqual(ll.getLength(), 0)

		self.assertRaises(IndexError, ll.getByIndex(0))
		self.assertRaises(IndexError, ll.getByIndex(1))
		self.assertRaises(IndexError, ll.getByIndex(-1))

		ll.insert("tres")
		self.assertEqual(ll.getByIndex(0), "tres")
		self.assertEqual(ll.getLength(), 1)
		self.assertRaises(IndexError, ll.getByIndex(1))

		ll.insert(data="uno")
		self.assertEqual(ll.getByIndex(0), "uno")
		self.assertEqual(ll.getByIndex(1), "tres")
		self.assertEqual(ll.getLength(), 2)
		self.assertRaises(IndexError, ll.getByIndex(2))
		self.assertRaises(IndexError, ll.getByIndex(-1))

		ll.insert(data="dos", index=1)
		self.assertEqual(ll.getByIndex(0), "uno")
		self.assertEqual(ll.getByIndex(2), "tres")
		self.assertEqual(ll.getByIndex(1), "dos")
		self.assertEqual(ll.getLength(), 3)
		self.assertRaises(IndexError, ll.getByIndex(3))
		self.assertRaises(IndexError, ll.getByIndex(-1))

		ll.insert(data="cuatro", index=3)
		self.assertEqual(ll.getByIndex(0), "uno")
		self.assertEqual(ll.getByIndex(2), "tres")
		self.assertEqual(ll.getByIndex(1), "dos")
		self.assertEqual(ll.getByIndex(3), "cuatro")
		self.assertEqual(ll.getLength(), 4)

		ll.insert(data="cero", index=0)
		self.assertEqual(ll.getByIndex(1), "uno")
		self.assertEqual(ll.getByIndex(3), "tres")
		self.assertEqual(ll.getByIndex(2), "dos")
		self.assertEqual(ll.getByIndex(4), "cuatro")
		self.assertEqual(ll.getByIndex(0), "cero")
		self.assertEqual(ll.getLength(), 5)

if __name__ == '__main__':
	unittest.main()
