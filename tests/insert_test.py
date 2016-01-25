from unittest import TestCase

from LinkedList import LinkedList


class TestLinkedList(TestCase):
	def test_insert(self):
		ll = LinkedList()
		ll.append("cero")
		ll.append("uno")
		ll.append("dos")
		ll.append("tres")
		ll.append("cuatro")

		self.assertEqual(ll.getByIndex(0),"cero")
		self.assertEqual(ll.getByIndex(1),"uno")
		self.assertEqual(ll.getByIndex(2),"dos")
		self.assertEqual(ll.getByIndex(3),"tres")
		self.assertEqual(ll.getByIndex(4),"cuatro")