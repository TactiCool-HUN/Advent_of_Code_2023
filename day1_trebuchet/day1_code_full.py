import re

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def solve_line(line: str) -> int:
	positions = []
	for i, digit in enumerate(digits):
		if digit in line:
			pos_s = list(re.finditer(digit, line))
			for pos in pos_s:
				positions.append([pos.regs[0][0], str(i + 1)])

	positions.sort(key = lambda x: x[0])
	for i, pos in enumerate(positions):
		line = line[:pos[0] + i] + pos[1] + line[pos[0] + i:]

	left = -1
	right = -1
	for letter in line:
		if letter.isnumeric():
			left = letter
			break

	for letter in reversed(line):
		if letter.isnumeric():
			right = letter
			break

	return int(f"{left}{right}")


with open("day1_puzzle_input.txt") as r:
	calibration_document = r.readlines()

"""calibration_document = [
	"two1nine",
	"eightwothree",
	"abcone2threexyz",
	"xtwone3four",
	"4nineeightseven2",
	"zoneight234",
	"7pqrstsixteen"
]"""

calibration_values = []
for calibration_line in calibration_document:
	calibration_number = solve_line(calibration_line)
	calibration_values.append(calibration_number)
	print(calibration_number)

print(sum(calibration_values))
