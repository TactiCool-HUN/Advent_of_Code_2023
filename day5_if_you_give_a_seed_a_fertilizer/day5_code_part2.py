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


class Range:
	def __init__(self, start: int, length: int):
		if length < 1:
			raise ValueError("Negative Length")
		elif start < 0:
			raise ValueError("Negative Start")
		self.start = start
		self.end = start + length - 1

	def __contains__(self, item: int):
		return self.start <= item <= self.end

	def __len__(self):
		return self.end - self.start + 1

	def __add__(self, other: int):
		start = self.start + other
		end = self.end + other
		return Range(start, end - start + 1)

	def split(self, point: int, point_to: str):  # point_to: "left"||"right"
		if self.start == point:
			if point_to == "right":
				return None, self
			else:
				return self, None
		elif self.end == point:
			if point_to == "right":
				return None, self
			else:
				return self, None
		elif point in self:
			if point_to == "right":
				return Range(self.start, point - self.start), Range(point, self.end - point + 1)
			else:
				return Range(self.start, point - self.start + 1), Range(point + 1, self.end - point + 1)
		else:
			if point_to == "right":
				return None, self
			else:
				return self, None


temp = almanach[0].split(": ")[1]
temp = [int(i) for i in temp.split(" ")]
seeds: list[Range] = [Range(temp[i], temp[i + 1]) for i in range(len(temp)) if i % 2 == 0]

instructions: list[list[dict]] = []
temp = []
for i, line in enumerate(almanach[2:]):
	print(i + 2)
	line = line.strip()
	if line == "":
		instructions.append(temp)
		temp = []
		continue
	elif not line[0].isdigit():
		continue

	temp.append({
		"in": Range(int(line.split(" ")[1]), int(line.split(" ")[2])),
		"out": Range(int(line.split(" ")[0]), int(line.split(" ")[2])),
		"move": int(line.split(" ")[0]) - int(line.split(" ")[1])
	})
instructions.append(temp)

for i, instruction_set in enumerate(instructions):
	print(f"- - - - - Instructions {i + 1}/{len(instructions)} - - - - -")
	new_seeds = []
	while seeds:
		print(f"Seed count: {len(seeds)}")
		seed_range = seeds.pop(0)
		print(f"Checking Seed {seed_range.start} - {seed_range.end}")
		for j, instruction_dict in enumerate(instruction_set):
			print(f"- Instruction dict {j + 1}/{len(instruction_set)}")
			print(f"- Against {instruction_dict['in'].start} - {instruction_dict['in'].end}, which moves {instruction_dict['move']}")
			if instruction_dict["in"].start in seed_range and instruction_dict["in"].end not in seed_range:
				# instruction range starts within seed range but ends outside
				print("- - Found at 1")
				unchanging, changing = seed_range.split(instruction_dict["in"].start, "right")

				if changing is None:
					raise ValueError
				else:
					changing += instruction_dict["move"]
					new_seeds.append(changing)
				if unchanging is not None:
					seeds.append(unchanging)
				break
			elif seed_range.start in instruction_dict["in"] and seed_range.end not in instruction_dict["in"]:
				# seed range starts within instruction range but ends outside
				print("- - Found at 2")
				changing, unchanging = seed_range.split(instruction_dict["in"].end, "left")

				if changing is None:
					raise ValueError
				else:
					changing += instruction_dict["move"]
					new_seeds.append(changing)
				if unchanging is not None:
					seeds.append(unchanging)
				break
			elif instruction_dict["in"].start in seed_range and instruction_dict["in"].end in seed_range:
				# instruction range completely within seed range
				print("- - Found at 3")
				unchanging1, temp = seed_range.split(instruction_dict["in"].start, "right")

				changing, unchanging2 = temp.split(instruction_dict["in"].end, "left")

				if changing is None:
					raise ValueError
				else:
					print(f"{changing.start} - {changing.end}")
					changing += instruction_dict["move"]
					new_seeds.append(changing)
				if unchanging1 is not None:
					seeds.append(unchanging1)
				if unchanging2 is not None:
					seeds.append(unchanging2)
				break
			elif seed_range.start in instruction_dict["in"] and seed_range.end in instruction_dict["in"]:
				# seed range completely within instruction range
				# everything changes
				print("- - Found at 4")
				changing = seed_range + instruction_dict["move"]

				new_seeds.append(changing)
				break
		else:
			print("- - Unchanged")
			new_seeds.append(seed_range)
	seeds = new_seeds

lowest = seeds[0].start
for seed in seeds:
	if seed.start < lowest:
		lowest = seed.start

print(lowest)
