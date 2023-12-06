from math import sqrt, floor, ceil

with open("day6_puzzle_input.txt", "r") as f:
	data = f.readlines()

"""data = [
	"Time:      7  15   30",
	"Distance:  9  40  200"
]"""

time = int(data[0].split(":")[1].replace(" ", ""))
distance = int(data[1].split(":")[1].replace(" ", ""))

option_1 = (time - sqrt(time ** 2 - 4 * distance)) / 2
option_2 = (time + sqrt(time ** 2 - 4 * distance)) / 2

if option_1 % 1 == 0:
	option_1 += 1
if option_2 % 1 == 0:
	option_2 -= 1

options = floor(option_2) - ceil(option_1) + 1

print(options)
