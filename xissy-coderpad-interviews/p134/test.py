import unittest

from .solution import SparseArray


class P134TestCase(unittest.TestCase):
    def setUp(self):
        self.array = SparseArray()
        self.array.init([0, 0, 0], 5)

    def test_get_blank(self):
        self.assertEqual(self.array.get(0), 0)
        self.assertEqual(self.array.get(3), 0)

    def test_out_of_index(self):
        self.assertRaises(IndexError, self.array.get, -1)
        self.assertRaises(IndexError, self.array.get, 5)

    def test_set_and_get(self):
        self.array.set(0, 1)
        self.assertEqual(self.array.get(0), 1)
        self.array.set(4, 1)
        self.assertEqual(self.array.get(4), 1)
