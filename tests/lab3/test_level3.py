import unittest
from src.lab3.node import Node
from src.lab3.level3 import binary_tree_diameter


class TestLevel3(unittest.TestCase):

    def setUp(self):
        self.node_9 = Node(9)
        self.node_8 = Node(8, left=self.node_9)
        self.node_7 = Node(7, left=self.node_8)
        self.node_6 = Node(6)
        self.node_5 = Node(5, right=self.node_6)
        self.node_4 = Node(4, right=self.node_5)
        self.node_3 = Node(3, left=self.node_7, right=self.node_4)
        self.node_2 = Node(2)
        self.node_1 = Node(1, left=self.node_3, right=self.node_2)

    def test_binary_tree_diameter(self):
        self.assertEqual(binary_tree_diameter(self.node_1), 6)


if __name__ == "__main__":
    unittest.main()
