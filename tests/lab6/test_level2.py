import unittest
from src.lab6.level2 import solution


class TestLevel2(unittest.TestCase):

    def test_case_1(self):
        # In:
        # 3
        # 1 2
        # 2 4
        # 3 5
        # Out: 4
        relations = [(1, 2), (2, 4), (3, 5)]
        self.assertEqual(solution(relations), 4)

    def test_case_2(self):
        # In:
        # 5
        # 1 2
        # 2 4
        # 1 3
        # 3 5
        # 8 10
        # Out: 6
        relations = [(1, 2), (2, 4), (1, 3), (3, 5), (8, 10)]
        self.assertEqual(solution(relations), 6)

    def test_all_in_one_tribe(self):
        # In:
        # 3
        # 1 2
        # 2 3
        # 3 4
        # Out: 0
        relations = [(1, 2), (2, 3), (3, 4)]
        self.assertEqual(solution(relations), 0)

    def test_all_boys_two_tribes(self):
        # In:
        # 2
        # 1 3
        # 5 7
        # Out: 0
        relations = [(1, 3), (5, 7)]
        self.assertEqual(solution(relations), 0)

    def test_all_girls_two_tribes(self):
        # In:
        # 2
        # 2 4
        # 6 8
        # Out: 0
        relations = [(2, 4), (6, 8)]
        self.assertEqual(solution(relations), 0)

    def test_one_boy_one_girl_different_tribes(self):
        # In:
        # 2
        # 1 1
        # 2 2
        # Out: 1
        relations = [(1,1), (2,2)]
        self.assertEqual(solution(relations), 1)

    def test_no_relations(self):
        # In:
        # 0
        # Out: 0
        self.assertEqual(solution([]), 0)

    def test_single_person_no_relations(self):
        # In:
        # 1
        # 1 1
        # Out: 0
        self.assertEqual(solution([(1,1)]), 0)

if __name__ == "__main__":
    unittest.main()
