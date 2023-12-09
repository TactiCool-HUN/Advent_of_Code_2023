def create_history(reading: list[list[int]]) -> list[list[int]]:
	while any(i != 0 for i in reading[-1]):
		last_reading: list[int] = reading[-1]
		new_history = []

		for j in range(len(last_reading) - 1):
			new_history.append(last_reading[j + 1] - last_reading[j])

		reading.append(new_history)

	return reading


def create_next_step(reading: list[list[int]]) -> list[list[int]]:
	for i, step in enumerate(reversed(reading)):
		step = list(reversed(step))
		if all(j == 0 for j in step):
			step.append(0)
		else:
			temp: int = step[-1] - reading[-i][0]
			step.append(temp)

		reading[-i - 1] = list(reversed(step))
	return reading


def main():
	with open("day9_puzzle_input.txt", "r") as f:
		raw_reading = f.readlines()

	"""raw_reading = [
		"0 3 6 9 12 15",
		"1 3 6 10 15 21",
		"10 13 16 21 30 45"
	]"""

	raw_reading = [i.strip().split(" ") for i in raw_reading]
	oasis_reading: list[list[list[int]]] = []  # list of readings which are a list of history, each history is a list of values at that point
	for reading in raw_reading:
		oasis_reading.append([[int(i) for i in reading]])

	total = 0
	for i, reading in enumerate(oasis_reading):
		reading = create_history(reading)
		reading = create_next_step(reading)
		oasis_reading[i] = reading
		total += reading[0][0]

	print(total)


main()
