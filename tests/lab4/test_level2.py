import unittest
from src.lab4.level_2.queue import Queue


class TestLevel2(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_ordered_enqueue(self):
        node_1 = self.queue.enqueue(value='node_1', priority=5)
        self.assertEqual(node_1.left, None)
        self.assertEqual(node_1.right, None)
        self.assertEqual(self.queue.root, node_1)

        node_2 = self.queue.enqueue(value='node_2', priority=4)
        self.assertEqual(node_1.left, None)
        self.assertEqual(node_1.right, node_2)
        self.assertEqual(node_2.left, None)
        self.assertEqual(node_2.right, None)
        self.assertEqual(self.queue.root, node_1)

        node_3 = self.queue.enqueue(value='node_3', priority=3)
        self.assertEqual(node_1.left, None)
        self.assertEqual(node_1.right, node_2)
        self.assertEqual(node_2.left, None)
        self.assertEqual(node_2.right, node_3)
        self.assertEqual(node_3.left, None)
        self.assertEqual(node_3.right, None)
        self.assertEqual(self.queue.root, node_1)

        node_4 = self.queue.enqueue(value='node_4', priority=2)
        self.assertEqual(node_1.left, None)
        self.assertEqual(node_1.right, node_2)
        self.assertEqual(node_2.left, None)
        self.assertEqual(node_2.right, node_3)
        self.assertEqual(node_3.left, None)
        self.assertEqual(node_3.right, node_4)
        self.assertEqual(node_4.left, None)
        self.assertEqual(node_4.right, None)
        self.assertEqual(self.queue.root, node_1)

        node_5 = self.queue.enqueue(value='node_5', priority=1)
        self.assertEqual(node_1.left, None)
        self.assertEqual(node_1.right, node_2)
        self.assertEqual(node_2.left, None)
        self.assertEqual(node_2.right, node_3)
        self.assertEqual(node_3.left, None)
        self.assertEqual(node_3.right, node_4)
        self.assertEqual(node_4.left, None)
        self.assertEqual(node_4.right, node_5)
        self.assertEqual(node_5.left, None)
        self.assertEqual(node_5.right, None)
        self.assertEqual(self.queue.root, node_1)

    def test_unordered_enqueue(self):
        node_1 = self.queue.enqueue(value='node_1', priority=5)
        self.assertEqual(node_1.left, None)
        self.assertEqual(node_1.right, None)
        self.assertEqual(self.queue.root, node_1)

        node_2 = self.queue.enqueue(value='node_2', priority=2)
        self.assertEqual(node_1.left, None)
        self.assertEqual(node_1.right, node_2)
        self.assertEqual(node_2.left, None)
        self.assertEqual(node_2.right, None)
        self.assertEqual(self.queue.root, node_1)

        node_3 = self.queue.enqueue(value='node_3', priority=1)
        self.assertEqual(node_1.left, None)
        self.assertEqual(node_1.right, node_2)
        self.assertEqual(node_2.left, None)
        self.assertEqual(node_2.right, node_3)
        self.assertEqual(node_3.left, None)
        self.assertEqual(node_3.right, None)
        self.assertEqual(self.queue.root, node_1)

        node_4 = self.queue.enqueue(value='node_4', priority=3)
        self.assertEqual(node_1.left, None)
        self.assertEqual(node_1.right, node_2)
        self.assertEqual(node_2.left, node_4)
        self.assertEqual(node_2.right, node_3)
        self.assertEqual(node_3.left, None)
        self.assertEqual(node_3.right, None)
        self.assertEqual(node_4.left, None)
        self.assertEqual(node_4.right, None)
        self.assertEqual(self.queue.root, node_1)

        node_5 = self.queue.enqueue(value='node_5', priority=1)
        self.assertEqual(node_1.left, None)
        self.assertEqual(node_1.right, node_2)
        self.assertEqual(node_2.left, node_4)
        self.assertEqual(node_2.right, node_3)
        self.assertEqual(node_3.left, node_5)
        self.assertEqual(node_3.right, None)
        self.assertEqual(node_4.left, None)
        self.assertEqual(node_4.right, None)
        self.assertEqual(node_5.left, None)
        self.assertEqual(node_5.right, None)
        self.assertEqual(self.queue.root, node_1)

    def test_dequeue(self):
        self.assertEqual(self.queue.dequeue(), None)

        node_1 = self.queue.enqueue(value='node_1', priority=5)
        node_2 = self.queue.enqueue(value='node_2', priority=1)
        node_3 = self.queue.enqueue(value='node_3', priority=1)
        node_4 = self.queue.enqueue(value='node_4', priority=3)
        self.assertEqual(node_1.left, None)
        self.assertEqual(node_1.right, node_2)
        self.assertEqual(node_2.left, node_3)
        self.assertEqual(node_2.right, None)
        self.assertEqual(node_3.left, node_4)
        self.assertEqual(node_3.right, None)
        self.assertEqual(node_4.left, None)
        self.assertEqual(node_4.right, None)
        self.assertEqual(self.queue.root, node_1)

        head = self.queue.dequeue()
        self.assertEqual(head, node_1)
        self.assertEqual(node_1.left, None)
        self.assertEqual(node_1.right, None)
        self.assertEqual(node_2.left, node_3)
        self.assertEqual(node_2.right, None)
        self.assertEqual(node_3.left, node_4)
        self.assertEqual(node_3.right, None)
        self.assertEqual(node_4.left, None)
        self.assertEqual(node_4.right, None)
        self.assertEqual(self.queue.root, node_2)

        head = self.queue.dequeue()
        self.assertEqual(head, node_4)
        self.assertEqual(node_2.left, node_3)
        self.assertEqual(node_2.right, None)
        self.assertEqual(node_3.left, None)
        self.assertEqual(node_3.right, None)
        self.assertEqual(self.queue.root, node_2)

    def test_status_for_ordered_enqueue(self):
        node_1 = self.queue.enqueue(value='node_1', priority=5)
        node_2 = self.queue.enqueue(value='node_2', priority=4)
        node_3 = self.queue.enqueue(value='node_3', priority=3)
        node_4 = self.queue.enqueue(value='node_4', priority=2)
        node_5 = self.queue.enqueue(value='node_5', priority=1)

        expected_result = [
            [node_1.value, node_1.priority],
            [node_2.value, node_2.priority],
            [node_3.value, node_3.priority],
            [node_4.value, node_4.priority],
            [node_5.value, node_5.priority]
        ]

        self.assertEqual(self.queue.status(), expected_result)

    def test_status_for_inverse_ordered_enqueue(self):
        node_5 = self.queue.enqueue(value='node_5', priority=1)
        node_4 = self.queue.enqueue(value='node_4', priority=2)
        node_3 = self.queue.enqueue(value='node_3', priority=3)
        node_2 = self.queue.enqueue(value='node_2', priority=4)
        node_1 = self.queue.enqueue(value='node_1', priority=5)

        expected_result = [
            [node_1.value, node_1.priority],
            [node_2.value, node_2.priority],
            [node_3.value, node_3.priority],
            [node_4.value, node_4.priority],
            [node_5.value, node_5.priority]
        ]

        self.assertEqual(self.queue.status(), expected_result)

    def test_status_for_unordered_enqueue(self):
        node_1 = self.queue.enqueue(value='node_1', priority=5)
        node_2 = self.queue.enqueue(value='node_2', priority=2)
        node_3 = self.queue.enqueue(value='node_3', priority=1)
        node_4 = self.queue.enqueue(value='node_4', priority=3)
        node_5 = self.queue.enqueue(value='node_5', priority=1)

        expected_result = [
            [node_1.value, node_1.priority],
            [node_4.value, node_4.priority],
            [node_2.value, node_2.priority],
            [node_5.value, node_5.priority],
            [node_3.value, node_3.priority]
        ]

        self.assertEqual(self.queue.status(), expected_result)


if __name__ == "__main__":
    unittest.main()
