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
        self.assertRaises(AssertionError, base_node.set_left, big_node)
        self.assertRaises(AssertionError, base_node.set_right, small_node)
        base_node.set_left(small_node)
        base_node.set_right(big_node)
        self.assertEqual(base_node.get_left(), small_node)
        self.assertEqual(base_node.get_right(), big_node)

    def test_parent(self):
        root_node = Node(10)
        sub_root_node = Node(30)
        test_node = Node(22)
        root_node.set_left(Node(5))
        root_node.set_right(sub_root_node)
        sub_root_node.set_left(test_node)
        sub_root_node.set_right(Node(35))
        self.assertEqual(test_node.get_parent().get_value(), sub_root_node.get_value())
        self.assertEqual(test_node.get_parent().get_parent().get_value(), root_node.get_value())


class P133TestCase(unittest.TestCase):
    def test_case1(self):
        root_node = Node(5)
        root_node.set_right(Node(7))
        root_node.get_right().set_left(Node(6))
        next_bigger_node = solution(root_node)
        self.assertEqual(next_bigger_node.get_value(), 6)

    def test_case2(self):
        root_node = Node(5)
        root_node.set_left(Node(3))
        test_node = root_node.get_left()
        next_bigger_node = solution(test_node)
        self.assertEqual(next_bigger_node.get_value(), 5)

    def test_case3(self):
        root_node = Node(5)
        root_node.set_left(Node(3))
        root_node.get_left().set_left(Node(1))
        test_node = root_node.get_left().get_left()
        next_bigger_node = solution(test_node)
        self.assertEqual(next_bigger_node.get_value(), 3)

    def test_case4(self):
        root_node = Node(5)
        root_node.set_right(Node(8))
        root_node.get_right().set_left(Node(6))
        root_node.get_right().get_left().set_right(Node(7))
        test_node = root_node.get_right().get_left()
        next_bigger_node = solution(test_node)
        self.assertEqual(next_bigger_node.get_value(), 7)

    def test_case5(self):
        root_node = Node(10)
        root_node.set_left(Node(5))
        root_node.set_right(Node(30))
        root_node.get_right().set_left(Node(22))
        root_node.get_right().set_right(Node(35))
        test_node = root_node.get_right().get_left()
        next_bigger_node = solution(test_node)
        self.assertEqual(next_bigger_node.get_value(), 30)

    def test_case6(self):
        root_node = Node(10)
        test_node = Node(25)
        root_node.set_left(Node(5))
        root_node.set_right(Node(30))
        root_node.get_right().set_left(Node(22))
        root_node.get_right().get_left().set_right(test_node)
        root_node.get_right().set_right(Node(35))
        next_bigger_node = solution(test_node)
        self.assertEqual(next_bigger_node.get_value(), 30)
