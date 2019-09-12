import unittest

from .solution import solution


class P77TestCase(unittest.TestCase):
    def test_case1(self):
        result = solution([(1, 3), (5, 8), (4, 10), (20, 25)])
        self.assertEqual(result, [(1, 3), (4, 10), (20, 25)])

    def test_case2(self):
        result = solution([(1, 3), (5, 8), (4, 10), (20, 25), (22, 27)])
        self.assertEqual(result, [(1, 3), (4, 10), (20, 27)])
