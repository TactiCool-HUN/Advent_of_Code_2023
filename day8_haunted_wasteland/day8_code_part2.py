from collections import deque
from math import lcm

with open("day8_puzzle_input.txt", "r") as f:
    temp = f.readlines()
map_raw = [i.strip() for i in temp]

"""map_raw = [
    "LR",
    "",
    "11A = (11B, XXX)",
    "11B = (XXX, 11Z)",
    "11Z = (11B, XXX)",
    "22A = (22B, XXX)",
    "22B = (22C, 22C)",
    "22C = (22Z, 22Z)",
    "22Z = (22B, 22B)",
    "XXX = (XXX, XXX)"
]"""

directions = deque(map_raw[0])
waypoints = {}
currents = []
for way in map_raw[2:]:
    current, temp = way.split(" = ")
    if "A" in current:
        currents.append(current)
    left = temp.split(", ")[0][1:]
    right = temp.split(", ")[1][:-1]
    waypoints[current] = (left, right)

steps = []
for current in currents:
    step = 0
    while "Z" not in current:
        current = waypoints[current][int(directions[0] == "R")]
        step += 1
        directions.rotate(-1)
    steps.append(step)

outcome = lcm(*steps)

print(outcome)
