import unittest
from src.lab2.level3 import solution

class TestLevel3(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution(3, [1,2,8,4,9]), 3)

if __name__ == "__main__":
    unittest.main()
