import unittest
from src.lab3.node import Node
from src.lab3.level2 import invert_binary_tree


class TestLevel2(unittest.TestCase):

    def setUp(self):
        self.node_7 = Node(7)
        self.node_6 = Node(6)
        self.node_5 = Node(5)
        self.node_4 = Node(4)
        self.node_3 = Node(3, left=self.node_6, right=self.node_7)
        self.node_2 = Node(2, left=self.node_4, right=self.node_5)
        self.node_1 = Node(1, left=self.node_2, right=self.node_3)

    def test_invert_binary_tree(self):
        invered_tree = invert_binary_tree(self.node_1)

        self.assertEqual(invered_tree.value, self.node_1.value)
        self.assertEqual(invered_tree.left.value, self.node_3.value)
        self.assertEqual(invered_tree.left.left.value, self.node_3.right.value)
        self.assertEqual(invered_tree.left.right.value, self.node_3.left.value)
        self.assertEqual(invered_tree.right.value, self.node_2.value)
        self.assertEqual(invered_tree.right.left.value, self.node_2.right.value)
        self.assertEqual(invered_tree.right.right.value, self.node_2.left.value)


if __name__ == "__main__":
    unittest.main()
