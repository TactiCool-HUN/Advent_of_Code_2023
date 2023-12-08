from collections import deque

with open("day8_puzzle_input.txt", "r") as f:
    temp = f.readlines()
map_raw = [i.strip() for i in temp]

"""map_raw = [
    "LLR",
    "",
    "AAA = (BBB, BBB)",
    "BBB = (AAA, ZZZ)",
    "ZZZ = (ZZZ, ZZZ)"
]"""

directions = deque(map_raw[0])
waypoints = {}
for way in map_raw[2:]:
    current, temp = way.split(" = ")
    left = temp.split(", ")[0][1:]
    right = temp.split(", ")[1][:-1]
    waypoints[current] = (left, right)

current = "AAA"
steps = 0
while current != "ZZZ":
    current = waypoints[current][int(directions[0] == "R")]
    steps += 1
    directions.rotate(-1)

print(steps)
