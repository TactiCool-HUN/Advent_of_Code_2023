with open("day5_puzzle_input.txt", "r") as f:
	almanach = f.readlines()

"""almanach = [
	"seeds: 79 14 55 13",
	"",
	"seed-to-soil map:",
	"50 98 2",
	"52 50 48",
	"",
	"soil-to-fertilizer map:",
	"0 15 37",
	"37 52 2",
	"39 0 15",
	"",
	"fertilizer-to-water map:",
	"49 53 8",
	"0 11 42",
	"42 0 7",
	"57 7 4",
	"",
	"water-to-light map:",
	"88 18 7",
	"18 25 70",
	"",
	"light-to-temperature map:",
	"45 77 23",
	"81 45 19",
	"68 64 13",
	"",
	"temperature-to-humidity map:",
	"0 69 1",
	"1 0 69",
	"",
	"humidity-to-location map:",
	"60 56 37",
	"56 93 4"
]"""

seeds = almanach[0]
seeds = seeds.split(": ")[1]
seeds = [[int(i), True] for i in seeds.split(" ")]

instructions: list[list[list[int]]] = []
temp: list[list[int]] = []
for line in almanach[2:]:
	line = line.strip()
	if line == "":
		instructions.append(temp)
		temp = []
		continue
	elif not line[0].isdigit():
		continue

	temp.append([int(i) for i in line.split(" ")])
instructions.append(temp)

for connection in instructions:
	for con_range in connection:
		for i, seed in enumerate(seeds):
			if seed[1]:
				if con_range[1] <= seed[0] <= (con_range[1] + con_range[2]):
					seeds[i][0] = seed[0] - con_range[1] + con_range[0]
					seeds[i][1] = False

	seeds = [[seed[0], True] for seed in seeds]

lowest = seeds[0][0]
for seed in seeds:
	if lowest > seed[0]:
		lowest = seed[0]

print(lowest)

