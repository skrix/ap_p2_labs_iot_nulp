class Maze:
	def __init__(self):
		self.start = None
		self.finish = None
		self.dimensions = None
		self.matrix = None

	def setup(self, file = 'tests/lab5/fixtures/input.txt'):
		with open(file, 'r') as f:
			lines = f.readlines()

		self.start = self.__parse_line(lines[0])
		self.finish = self.__parse_line(lines[1])
		self.dimensions = self.__parse_line(lines[2])
		self.matrix = self.__build_matrix(lines[3:])
		return self

	def __parse_line(self, line):
		return list(map(int, line.strip().split(',')))

	def __parse_row(self, line):
		return list(map(int, line.strip().replace('[', '').replace(']', '').split()))

	def __build_matrix(self, matrix_lines):
		self.matrix = []
		for line in matrix_lines:
			self.matrix.append(self.__parse_row(line))
		return self.matrix
