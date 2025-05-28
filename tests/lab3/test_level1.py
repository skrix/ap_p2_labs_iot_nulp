import unittest
from src.lab3.node import Node
from src.lab3.level1 import in_order_traversal, pre_order_traversal, post_order_traversal


class TestLevel1(unittest.TestCase):

    def setUp(self):
        self.node_7 = Node(7)
        self.node_6 = Node(6)
        self.node_5 = Node(5)
        self.node_3 = Node(3, left=self.node_6, right=self.node_7)
        self.node_2 = Node(2, right=self.node_5)
        self.node_1 = Node(1, left=self.node_2, right=self.node_3)

    def test_in_order_traversal(self):
        self.assertEqual(in_order_traversal(self.node_1), [2, 5, 1, 6, 3, 7])

    def test_pre_order_traversal(self):
        self.assertEqual(pre_order_traversal(self.node_1), [1, 2, 5, 3, 6, 7])

    def test_post_order_traversal(self):
        self.assertEqual(post_order_traversal(self.node_1), [5, 2, 6, 7, 3, 1])


if __name__ == "__main__":
    unittest.main()
