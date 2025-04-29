import unittest
from src.lab4.level_1.queue import Queue

class TestLevel1(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        node_1 = self.queue.enqueue(value='node_1', priority=5)
        self.assertEqual(node_1.prev, None)
        self.assertEqual(node_1.next, None)

        node_2 = self.queue.enqueue(value='node_2', priority=1)
        self.assertEqual(node_1.prev, None)
        self.assertEqual(node_1.next, node_2)
        self.assertEqual(node_2.prev, node_1)
        self.assertEqual(node_2.next, None)

        node_3 = self.queue.enqueue(value='node_3', priority=1)
        self.assertEqual(node_1.prev, None)
        self.assertEqual(node_1.next, node_2)
        self.assertEqual(node_2.prev, node_1)
        self.assertEqual(node_2.next, node_3)
        self.assertEqual(node_3.prev, node_2)
        self.assertEqual(node_3.next, None)

        node_4 = self.queue.enqueue(value='node_4', priority=3)
        self.assertEqual(node_1.prev, None)
        self.assertEqual(node_1.next, node_4)
        self.assertEqual(node_4.prev, node_1)
        self.assertEqual(node_4.next, node_2)
        self.assertEqual(node_2.prev, node_4)
        self.assertEqual(node_2.next, node_3)
        self.assertEqual(node_3.prev, node_2)
        self.assertEqual(node_3.next, None)

    def test_dequeue(self):
        self.assertEqual(self.queue.dequeue(), None)

        node_1 = self.queue.enqueue(value='node_1', priority=5)
        node_2 = self.queue.enqueue(value='node_2', priority=1)
        node_3 = self.queue.enqueue(value='node_3', priority=1)
        node_4 = self.queue.enqueue(value='node_4', priority=3)

        head = self.queue.dequeue()
        self.assertEqual(head, node_1)
        self.assertEqual(node_4.prev, None)
        self.assertEqual(node_4.next, node_2)
        self.assertEqual(node_2.prev, node_4)
        self.assertEqual(node_2.next, node_3)
        self.assertEqual(node_3.prev, node_2)
        self.assertEqual(node_3.next, None)

        head = self.queue.dequeue()
        self.assertEqual(head, node_4)
        self.assertEqual(node_2.prev, None)
        self.assertEqual(node_2.next, node_3)
        self.assertEqual(node_3.prev, node_2)
        self.assertEqual(node_3.next, None)


    def test_status(self):
        node_1 = self.queue.enqueue(value='node_1', priority=5)
        node_2 = self.queue.enqueue(value='node_2', priority=1)
        node_3 = self.queue.enqueue(value='node_3', priority=1)
        node_4 = self.queue.enqueue(value='node_4', priority=3)

        expected_result = [
            [node_1.value, node_1.priority],
            [node_4.value, node_4.priority],
            [node_2.value, node_2.priority],
            [node_3.value, node_3.priority],
        ]

        self.assertEqual(self.queue.status(), expected_result)




if __name__ == "__main__":
    unittest.main()
