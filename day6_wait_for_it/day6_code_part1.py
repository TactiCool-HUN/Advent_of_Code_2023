from math import sqrt, floor, ceil

with open("day6_puzzle_input.txt", "r") as f:
	data = f.readlines()

"""data = [
	"Time:      7  15   30",
	"Distance:  9  40  200"
]"""

time = data[0].split(":")[1].split(" ")
time = [int(i) for i in time if i != ""]
distance = data[1].split(":")[1].split(" ")
distance = [int(i) for i in distance if i != ""]
races = []
for i in range(len(time)):
	races.append([time[i], distance[i]])

option_amount = 1
for race in races:
	option_1 = (race[0] - sqrt(race[0] ** 2 - 4 * race[1])) / 2
	option_2 = (race[0] + sqrt(race[0] ** 2 - 4 * race[1])) / 2

	if option_1 % 1 == 0:
		option_1 += 1
	if option_2 % 1 == 0:
		option_2 -= 1

	options = floor(option_2) - ceil(option_1) + 1
	option_amount *= options

print(option_amount)
