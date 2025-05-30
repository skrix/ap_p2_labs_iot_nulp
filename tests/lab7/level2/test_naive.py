import unittest
from lab7.level2.naive import solution


class TestFindLastOccurrenceNaive(unittest.TestCase):

    def test_simple_match_last(self):
        self.assertEqual(solution("ababab", "aba"), (5, 8))

    def test_single_char_needle(self):
        self.assertEqual(solution("hello world", "o"), (8, 11))

    def test_no_match(self):
        self.assertEqual(solution("aaaaaa", "aab"), (None, 12))
        self.assertEqual(solution("abcdef", "xyz"), (None, 4))

    def test_empty_needle(self):
        self.assertEqual(solution("abc", ""), (None, 0))
        self.assertEqual(solution("", ""), (None, 0))

    def test_empty_haystack(self):
        self.assertEqual(solution("", "a"), (None, 0))

    def test_needle_longer_than_haystack(self):
        self.assertEqual(solution("abc", "abcdef"), (None, 0))

    def test_identical_strings(self):
        self.assertEqual(solution("abc", "abc"), (3, 3))

    def test_needle_at_beginning_only(self):
        self.assertEqual(solution("abcde", "ab"), (2, 5))

    def test_needle_at_end_only(self):
        self.assertEqual(solution("deabc", "abc"), (5, 5))

    def test_overlapping_occurrences(self):
        self.assertEqual(solution("aaaaa", "aa"), (5, 8))
        self.assertEqual(solution("abababa", "aba"), (7, 11))
        self.assertEqual(solution("aaaa", "aa"), (4, 6))


if __name__ == "__main__":
    unittest.main()
