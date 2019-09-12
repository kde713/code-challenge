import unittest

from .solution import solution


class P126TestCase(unittest.TestCase):
    def test_case1(self):
        input_list = [1, 2, 3, 4, 5, 6]
        solution(input_list, 2)
        self.assertEqual(input_list, [3, 4, 5, 6, 1, 2])
