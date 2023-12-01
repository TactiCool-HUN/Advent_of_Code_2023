import re

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def solve_line(line: str) -> int:
	# so... ehm magic? :D
	positions = []

	# alright my main idea:
	# I'll get their positions first, with a list[int, str]
	# which will basically be list[position, number as str]
	# this way I won't mess up things like "eightwo"
	# where two numbers intersect
	for i, digit in enumerate(digits):
		if digit in line:
			# this will get me an iterator
			# full of re.Match() objects
			pos_s = re.finditer(digit, line)
			# pos_s now has all the indexes of the digits
			# I needed to use this because index() only returns the 1st
			# and there could be several of each digit
			for pos in pos_s:
				# from which I somehow pry out the actual start points
				positions.append([pos.regs[0][0], str(i + 1)])

	positions.sort(key = lambda x: x[0])
	for i, pos in enumerate(positions):
		# here i basically just place in numbers
		# right at the start of their written out counterparts
		# so their order doesn't change
		line = line[:pos[0] + i] + pos[1] + line[pos[0] + i:]
		# the +i is needed
		# because I'm pushing the line forward with each addition
		# this could be avoided if I go in reverse
		# however it makes more sense this way

	# from here it's same as part 1
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

calibration_sum = 0
for calibration_line in calibration_document:
	line_number = solve_line(calibration_line)
	calibration_sum += line_number

print(calibration_sum)
