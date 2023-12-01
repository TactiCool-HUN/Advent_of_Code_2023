def solve_line(line: str) -> int:
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
	
calibration_values = []
for calibration_line in calibration_document:
	calibration_number = solve_line(calibration_line)
	calibration_values.append(calibration_number)

print(sum(calibration_values))
