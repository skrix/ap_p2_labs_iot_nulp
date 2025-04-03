import unittest
from src.lab2.level2 import solution

class TestLevel2(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([3,6,7,11], 8), 4)
        self.assertEqual(solution([30,11,23,4,20], 5), 30)
        self.assertEqual(solution([30,11,23,4,20], 6), 23)

if __name__ == "__main__":
    unittest.main()
