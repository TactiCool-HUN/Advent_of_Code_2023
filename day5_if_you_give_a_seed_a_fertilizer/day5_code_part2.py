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

seeds = almanach[0].split(": ")[1]
seeds = [int(i) for i in seeds.split(" ")]
seeds = [[seeds[i], seeds[i] + seeds[i + 1]] for i in range(len(seeds)) if i % 2 == 0]

instructions: list[list[list[int]]] = []
temp = []
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

for instruction_map in instructions:
	new_seeds = []
	for seed_range in seeds:
		for instruction_range in instruction_map:
			if seed_range[0] <= instruction_range[1] <= seed_range[1] < (instruction_range[1] + instruction_range[2]):
				# instruction range starts within seed range but ends outside
				new_seeds.append([seed_range[0], instruction_range[1] - 1])  # unchanging range
				temp = [instruction_range[1], seed_range[1]]  # changing range

				temp = [i - instruction_range[1] + instruction_range[0] for i in temp]  # applying change
				new_seeds.append(temp)
				break
			elif instruction_range[1] < seed_range[0] <= (instruction_range[1] + instruction_range[2]) <= seed_range[1]:
				# seed range starts within instruction range but ends outside
				temp = [seed_range[0], instruction_range[1] + instruction_range[2]]  # changing range
				new_seeds.append([instruction_range[1] + instruction_range[2] + 1, seed_range[1]])  # unchanging range

				temp = [i - instruction_range[1] + instruction_range[0] for i in temp]  # applying change
				new_seeds.append(temp)
				break
			elif seed_range[0] <= instruction_range[1] and instruction_range[1] + instruction_range[2] <= seed_range[1]:
				# instruction range completely within seed range
				new_seeds.append([seed_range[0], instruction_range[1] - 1])  # unchanging range
				temp = [instruction_range[1], instruction_range[1] + instruction_range[2]]  # changing range
				new_seeds.append([instruction_range[1] + instruction_range[2] + 1, seed_range[1]])  # unchanging range

				temp = [i - instruction_range[1] + instruction_range[0] for i in temp]  # applying change
				new_seeds.append(temp)
				break
			elif instruction_range[1] < seed_range[0] and seed_range[1] < instruction_range[1] + instruction_range[2]:
				# seed range completely within instruction range
				# everything changes
				temp = [i - instruction_range[1] + instruction_range[0] for i in seed_range]  # applying change
				new_seeds.append(temp)
				break
		else:
			new_seeds.append(seed_range)
	seeds = new_seeds

lowest = seeds[0][0]
for seed_range in seeds:
	if seed_range[0] < lowest:
		lowest = seed_range[0]

print(lowest)
