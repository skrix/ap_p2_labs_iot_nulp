import unittest
from src.lab9.word_game import WordGame

class TestWordChain(unittest.TestCase):
    def __run_test_case(self, input_data, expected_output):
        self.assertEqual(WordGame(input_data).result(), expected_output)

    def test_example_1(self):
        self.__run_test_case('tests/lab9/fixtures/test_case_1.txt', 6)

    def test_example_2(self):
        self.__run_test_case('tests/lab9/fixtures/test_case_2.txt', 4)

    def test_example_3(self):
        self.__run_test_case('tests/lab9/fixtures/test_case_3.txt', 1)

    def test_single_word(self):
        self.__run_test_case('tests/lab9/fixtures/test_case_4.txt', 1)

    def test_no_chain_possible(self):
        self.__run_test_case('tests/lab9/fixtures/test_case_5.txt', 1)

    def test_no_chain_possible(self):
        self.__run_test_case('tests/lab9/fixtures/test_case_6.txt', 0)

if __name__ == '__main__':
   unittest.main()
