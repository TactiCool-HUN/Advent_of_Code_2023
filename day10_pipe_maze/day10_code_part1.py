class Point:
	def __init__(self, x: int, y: int, character: str):
		self.x: int = x
		self.y: int = y
		self.char: str = character

	def __eq__(self, other):
		if isinstance(other, Point):
			return self.x == other.x and self.y == other.y
		else:
			raise TypeError

	def __str__(self):
		return f"Point: {self.char} ({self.x}, {self.y})"


dir_dict = {
	"down": (0, 1, ["|", "L", "J"]),
	"up": (0, -1, ["|", "F", "7"]),
	"right": (1, 0, ["-", "7", "J"]),
	"left": (-1, 0, ["-", "F", "L"])
}


def solver(maze: list[list[str]]) -> int:
	path: list[Point] = []
	height = len(maze)
	width = len(maze[0])

	start: Point = Point(-1, -1, "X")
	for y in range(height):
		for x in range(width):
			if maze[y][x] == "S":
				start = Point(x, y, "S")
				break
		else:
			continue
		break

	if start.char == "X":
		raise ValueError("Start not found")



	path.append(start)

	return len(path) // 2


"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F i
"""


def main():
	with open("day10_puzzle_input.txt", "r") as f:
		raw = f.readlines()

	main_input = []
	for line in raw:
		line = line.strip()
		main_input.append([i for i in line])

	easy_input_1 = [
		[".", ".", ".", ".", "."],
		[".", "S", "-", "7", "."],
		[".", "|", ".", "|", "."],
		[".", "L", "-", "J", "."],
		[".", ".", ".", ".", "."]
	]

	easy_input_2 = [
		["-", "L", "|", "F", "7"],
		["7", "S", "-", "7", "|"],
		["L", "|", "7", "|", "|"],
		["-", "L", "-", "J", "|"],
		["L", "|", "-", "J", "F"]
	]

	hard_input_1 = [
		[".", ".", "F", "7", "."],
		[".", "F", "J", "|", "."],
		["S", "J", ".", "L", "7"],
		["|", "F", "-", "-", "J"],
		["L", "J", ".", ".", "."]
	]

	hard_input_2 = [
		["7", "-", "F", "7", "-"],
		[".", "F", "J", "|", "7"],
		["S", "J", "L", "L", "7"],
		["|", "F", "-", "-", "J"],
		["L", "J", ".", "L", "J"]
	]

	result = solver(easy_input_1)
	if result == 4:
		print("Easy 1 Passed!")
	else:
		print(f"Easy 1 Failed! {result}")
	result = solver(easy_input_2)
	if result == 4:
		print("Easy 2 Passed!")
	else:
		print(f"Easy 2 Failed! {result}")
	result = solver(hard_input_1)
	if result == 8:
		print("Hard 1 Passed!")
	else:
		print(f"Hard 1 Failed! {result}")
	result = solver(hard_input_2)
	if result == 8:
		print("Hard 2 Passed!")
	else:
		print(f"Hard 2 Failed! {result}")

	print(solver(main_input))


main()
