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


def spacer(galaxy_cluster: list[list[str]]) -> list[list[str]]:
	temp = []
	empty_columns = [True] * len(galaxy_cluster[0])
	for line in galaxy_cluster:
		if "#" in line:
			for i in range(len(line)):
				if line[i] == "#":
					empty_columns[i] = False
		else:
			temp.append(line[:])
		temp.append(line)

	galaxy_cluster = temp

	for i, colum in enumerate(reversed(empty_columns)):
		if colum:
			for j in range(len(galaxy_cluster)):
				galaxy_cluster[j].insert(len(empty_columns) - i, ".")

	return galaxy_cluster


def solve(galaxy_cluster: list[str]) -> int:
	galaxy_cluster = [list(i) for i in galaxy_cluster]
	galaxy_cluster = spacer(galaxy_cluster)

	galaxy_positions = []
	for i in range(len(galaxy_cluster)):
		for j in range(len(galaxy_cluster[0])):
			if galaxy_cluster[i][j] == "#":
				galaxy_positions.append(Point(i, j))

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
