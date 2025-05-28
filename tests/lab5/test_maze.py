import unittest
from src.lab5.level_2.maze import Maze

class TestMaze(unittest.TestCase):
    def setUp(self):
        self.maze = Maze()

    def test_parse_line(self):
        result = self.maze._Maze__parse_line("1, 2")
        expected = [1, 2]
        self.assertEqual(result, expected)

    def test_parse_row(self):
        result = self.maze._Maze__parse_row("[1 0 1]\n")
        expected = [1, 0, 1]
        self.assertEqual(result, expected)

    def test_build_matrix(self):
        lines = [
            "[1 0 1]\n",
            "[0 1 0]\n",
            "[1 0 1]\n"
        ]
        expected = [
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]
        ]
        matrix = self.maze._Maze__build_matrix(lines)
        self.assertEqual(matrix, expected)
        self.assertEqual(self.maze.matrix, matrix)

    def test_setup(self):
        self.maze._Maze__setup(file='tests/lab5/fixtures/input.txt')
        expected_matrix = [
            [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
            [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
            [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
        ]

        self.assertEqual(self.maze.start, [0, 0])
        self.assertEqual(self.maze.finish, [7, 5])
        self.assertEqual(self.maze.dimensions, [10, 10])
        self.assertEqual(self.maze.matrix, expected_matrix)


    def test_solve(self):
        result = self.maze.solve(file='tests/lab5/fixtures/input.txt')
        self.assertEqual(self.maze.start, [0, 0])
        self.assertEqual(self.maze.finish, [7, 5])
        self.assertEqual(result, 12)

if __name__ == '__main__':
    unittest.main()
