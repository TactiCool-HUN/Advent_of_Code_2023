import re


def get_num_pus_around(star_pos: int, lines: list[str]) -> list[re.Match]:
	nearby_numbers = []

	for line in lines:
		number_positions = list(re.finditer("[0-9]+", line))
		for number in number_positions:
			start = number.regs[0][0]
			end = number.regs[0][1] - 1

			if (start - 1) <= star_pos <= (end + 1):
				nearby_numbers.append(number)

	return nearby_numbers


def main():
	with open("day3_puzzle_input.txt", "r") as f:
		schematic = f.readlines()

	"""schematic = [
		"467..114..",
		"...*......",
		"..35..633.",
		"......#...",
		"617*......",
		".....+.58.",
		"..592.....",
		"......755.",
		"...$.*....",
		".664.598.."
	]"""

	prev_line = ""
	main_line = ""
	next_line = ""
	gear_sum = 0

	for line in schematic + [""]:
		prev_line = main_line
		main_line = next_line
		next_line = line.strip()

		if main_line == "":
			continue

		star_positions = list(re.finditer("\*", main_line))
		for star in star_positions:
			star_pos = star.regs[0][0]

			number_positions = get_num_pus_around(star_pos, [prev_line, main_line, next_line])

			if len(number_positions) != 2:
				continue

			num1 = number_positions[0].string[number_positions[0].regs[0][0]:number_positions[0].regs[0][1]]
			num2 = number_positions[1].string[number_positions[1].regs[0][0]:number_positions[1].regs[0][1]]
			gear_sum += int(num1) * int(num2)

	print(gear_sum)


main()
