class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def distance(self, other) -> int:
		if isinstance(other, Point):
			return abs(self.x - other.x) + abs(self.y - other.y)
		elif isinstance(other, list):
			total = 0
			for point in other:
				if isinstance(point, Point):
					total += abs(self.x - point.x) + abs(self.y - point.y)
				else:
					raise ValueError
			return total
		else:
			raise ValueError


def spacer(galaxy_cluster: list[list[str]]) -> tuple[tuple, tuple]:
	empty_columns = list(range(len(galaxy_cluster[0])))
	empty_rows = []
	for i, line in enumerate(galaxy_cluster):
		if "#" in line:
			for j, point in enumerate(line):
				if point == "#":
					try:
						empty_columns.remove(j)
					except ValueError:
						pass
		else:
			empty_rows.append(i)

	return tuple(empty_rows), tuple(empty_columns)


def solve(galaxy_cluster: list[str]) -> int:
	galaxy_cluster = [list(i) for i in galaxy_cluster]
	spaced_rows, spaced_columns = spacer(galaxy_cluster)

	factor = 10 ** 6 - 1

	galaxy_positions = []
	for i in range(len(galaxy_cluster)):
		for j in range(len(galaxy_cluster[0])):
			if galaxy_cluster[i][j] == "#":
				y = i
				x = j
				for row in spaced_rows:
					if i > row:
						y += factor
					else:
						break

				for column in spaced_columns:
					if j > column:
						x += factor
					else:
						break

				galaxy_positions.append(Point(x, y))

	total_distance = 0
	for i, position in enumerate(galaxy_positions):
		total_distance += position.distance(galaxy_positions[i + 1:])

	return total_distance


def main():
	example = [
		"...#......",
		".......#..",
		"#.........",
		"..........",
		"......#...",
		".#........",
		".........#",
		"..........",
		".......#..",
		"#...#....."
	]

	with open("day11_puzzle_input.txt", "r") as f:
		galaxy = f.readlines()
	galaxy = [i.strip() for i in galaxy]

	total = solve(galaxy)
	print(total)


main()
