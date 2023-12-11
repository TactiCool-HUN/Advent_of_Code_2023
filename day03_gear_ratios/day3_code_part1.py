import re

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

previous_line = ""
main_line = ""
next_line = ""
part_sum = 0

for line in schematic + [""]:
	previous_line = main_line
	main_line = next_line
	next_line = line.strip()

	if main_line == "":
		continue

	number_positions = list(re.finditer("[0-9]+", main_line))
	for number in number_positions:
		start_pos = max(number.regs[0][0] - 1, 0)
		end_pos = number.regs[0][1] + 1

		prev_temp = previous_line[start_pos:end_pos]
		main_temp = main_line[start_pos:end_pos]
		next_temp = next_line[start_pos:end_pos]

		prev_temp = prev_temp.replace(".", "")
		main_temp = main_temp.replace(".", "")
		next_temp = next_temp.replace(".", "")

		prev_temp = ''.join([i for i in prev_temp if not i.isdigit()])
		main_temp = ''.join([i for i in main_temp if not i.isdigit()])
		next_temp = ''.join([i for i in next_temp if not i.isdigit()])

		if prev_temp != "" or next_temp != "" or main_temp != "":
			part_sum += int(main_line[number.regs[0][0]:number.regs[0][1]])

print(part_sum)
