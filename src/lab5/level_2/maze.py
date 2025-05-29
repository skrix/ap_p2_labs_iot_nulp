from collections import deque

class Maze:
	def __init__(self):
		self.start = None
		self.finish = None
		self.dimensions = None
		self.matrix = None

	def solve(self, file):
		self.__setup(file=file)

		if self.__is_impossible_to_solve():
			return None

		start_x, start_y = self.start

		queue = deque([(start_x, start_y, 0)])  # (x, y, distance)
		visited = set() # set of sets
		visited.add((start_x, start_y))

		while queue:
			x, y, distance = queue.popleft()

			if self.__is_finish(x, y):
				return distance

			for dx, dy in self.__directions():
				new_x = x + dx
				new_y = y + dy

				if (self.__is_valid_step(new_x, new_y) and (new_x, new_y) not in visited):
					visited.add((new_x, new_y))
					queue.append((new_x, new_y, distance + 1))

		return	None

	def __setup(self, file):
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

	def __is_impossible_to_solve(self):
		start_x, start_y = self.start
		end_x, end_y = self.finish

		if (not self.__is_possible_to_pass(start_x, start_y) or not self.__is_possible_to_pass(end_x, end_y)):
			return True
		else:
			return False

	def __is_finish(self, x, y):
		end_x, end_y = self.finish
		return x == end_x and y == end_y

	def __is_possible_to_pass(self, x, y):
		return self.matrix[x][y] == 1

	def __is_valid_step(self, x, y):
		return self.__is_in_scope(x, y) and self.__is_possible_to_pass(x, y)

	def __is_in_scope(self, x, y):
		max_x, max_y = self.dimensions
		return 0 <= x < max_x and 0 <= y < max_y

	def __directions(self):
		return [
			(-1, 0), # Go Top: (x, y) ——> (x – 1, y)
			(0, -1), # Go Left: (x, y) ——> (x, y – 1)
			(1, 0),  # Go Down: (x, y) ——> (x + 1, y)
			(0, 1)   # Go Right: (x, y) ——> (x, y + 1)
		]
