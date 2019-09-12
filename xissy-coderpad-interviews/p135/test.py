import unittest

from .solution import Node, solution


class NodeTestCase(unittest.TestCase):
    def test_initialize(self):
        test_value = 5
        test_node = Node(test_value)
        self.assertEqual(test_node.value, test_value)

    def test_left_right_assert(self):
        base_node = Node(5)
        small_node = Node(3)
        big_node = Node(7)
        base_node.set_left(big_node)
        base_node.set_right(small_node)
        self.assertEqual(base_node.get_left(), big_node)
        self.assertEqual(base_node.get_right(), small_node)


class P135TestCase(unittest.TestCase):
    def test_case1(self):
        root_node = Node(10)
        min_path_sum = solution(root_node)
        self.assertEqual(min_path_sum, 10)

    def test_case2(self):
        root_node = Node(10)
        root_node.set_left(Node(5))
        root_node.set_right(Node(5))
        min_path_sum = solution(root_node)
        self.assertEqual(min_path_sum, 15)

    def test_case3(self):
        root_node = Node(10)
        root_node.set_left(Node(5))
        root_node.get_left().set_right(Node(2))
        root_node.set_right(Node(5))
        min_path_sum = solution(root_node)
        self.assertEqual(min_path_sum, 15)

    def test_case4(self):
        root_node = Node(10)
        root_node.set_left(Node(5))
        root_node.get_left().set_right(Node(2))
        root_node.set_right(Node(5))
        root_node.get_right().set_right(Node(1))
        min_path_sum = solution(root_node)
        self.assertEqual(min_path_sum, 16)

    def test_case5(self):
        root_node = Node(10)
        root_node.set_left(Node(5))
        root_node.get_left().set_right(Node(2))
        root_node.set_right(Node(5))
        root_node.get_right().set_right(Node(1))
        root_node.get_right().get_right().set_left(Node(-1))
        min_path_sum = solution(root_node)
        self.assertEqual(min_path_sum, 15)
