from __future__ import annotations


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def get_left(self) -> Node or None:
        return self.left

    def set_left(self, node: Node):
        node.parent = self
        self.left = node

    def get_right(self) -> Node or None:
        return self.right

    def set_right(self, node: Node):
        node.parent = self
        self.right = node

    def get_value(self) -> int:
        return self.value

    def __repr__(self):
        return f"Node({repr(self.value)}, left={repr(self.left)}, right={repr(self.right)})"


def solution(root_node: Node) -> int:
    # TODO: solve
    return 0
