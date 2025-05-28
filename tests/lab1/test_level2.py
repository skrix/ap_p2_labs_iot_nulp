import unittest
from src.lab1.level2 import solution

class TestLevel2(unittest.TestCase):

    def test_solution_1(self):
        element, position = solution([15, 7, 22, 9, 36, 2, 42, 18], 1)
        self.assertEqual(element, 42)
        self.assertEqual(position, 6)

    def test_solution_2(self):
        element, position = solution([15, 7, 22, 9, 36, 2, 42, 18], 2)
        self.assertEqual(element, 36)
        self.assertEqual(position, 4)

    def test_solution_3(self):
        element, position = solution([15, 7, 22, 9, 36, 2, 42, 18], 3)
        self.assertEqual(element, 22)
        self.assertEqual(position, 2)

    def test_solution_4(self):
        element, position = solution([15, 7, 22, 9, 36, 2, 42, 18], 4)
        self.assertEqual(element, 18)
        self.assertEqual(position, 7)

    def test_solution_5(self):
        element, position = solution([15, 7, 22, 9, 36, 2, 42, 18], 5)
        self.assertEqual(element, 15)
        self.assertEqual(position, 0)

    def test_solution_6(self):
        element, position = solution([15, 7, 22, 9, 36, 2, 42, 18], 6)
        self.assertEqual(element, 9)
        self.assertEqual(position, 3)

    def test_solution_7(self):
        element, position = solution([15, 7, 22, 9, 36, 2, 42, 18], 7)
        self.assertEqual(element, 7)
        self.assertEqual(position, 1)

    def test_solution_8(self):
        element, position = solution([15, 7, 22, 9, 36, 2, 42, 18], 8)
        self.assertEqual(element, 2)
        self.assertEqual(position, 5)

if __name__ == "__main__":
    unittest.main()
