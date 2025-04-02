import unittest
from lab2.level1 import solution

class TestLevel1(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(solution([0,10,15,50,0,14,9,12,40]), 7)

    def test_case_2(self):
        self.assertEqual(solution([1,1,1,2,1,1,3]), 3)

    def test_case_3(self):
        self.assertEqual(solution([5,6,5,6,5,6,5,6,5,6,5,0,0]), 4)

if __name__ == "__main__":
    unittest.main()
