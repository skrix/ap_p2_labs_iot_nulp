import unittest
from lab1.level1 import solution

class TestLevel1(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([-4,-2,0,1,3]), [0,1,4,9,16])
        self.assertEqual(solution([1,2,3,4,5]), [1,4,9,16,25])

if __name__ == "__main__":
    unittest.main()
