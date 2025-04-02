import unittest
from src.lab1.level3 import solution

class TestLevel3(unittest.TestCase):

    def test_with_peak_subsequence(self):
        input_sequence = [1, 3, 5, 4, 2, 8, 3, 7]
        expected_subsequence_lenght = 5 # [1, 3, 5, 4, 2]
        self.assertEqual(solution(input_sequence), expected_subsequence_lenght)

    def test_with_asc_sorted_sequence(self):
        input_sequence = [1, 2, 3, 4, 5, 6, 7, 8]
        expected_subsequence_lenght = 0
        self.assertEqual(solution(input_sequence), expected_subsequence_lenght)

    def test_with_desc_sorted_sequence(self):
        input_sequence = [8, 7, 6, 5, 4, 3, 2, 1]
        expected_subsequence_lenght = 0
        self.assertEqual(solution(input_sequence), expected_subsequence_lenght)

    def test_with_two_elements_sequence(self):
        input_sequence = [1, 2]
        expected_subsequence_lenght = 0
        self.assertEqual(solution(input_sequence), expected_subsequence_lenght)

    def test_with_no_peak_subsequence(self):
        input_sequence =  [1, 3, 5, 5, 2, 3, 3, 7]
        expected_subsequence_lenght = 0
        self.assertEqual(solution(input_sequence), expected_subsequence_lenght)

    def test_with_negative_peak_subsequence(self):
        input_sequence =  [-1, -3, -5, -4, -2, 0]
        expected_subsequence_lenght = 0
        self.assertEqual(solution(input_sequence), expected_subsequence_lenght)

    def test_with_three_peak_subsequences_return_longest(self):
        input_sequence =  [1, 8, 3, 7, 2, 4, 5, 9, 7, 6, 4, 9]
        expected_subsequence_lenght = 7
        self.assertEqual(solution(input_sequence), expected_subsequence_lenght)

if __name__ == "__main__":
    unittest.main()
