#!/usr/bin/python3

import sys
from copy import deepcopy
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()

data = [[char for char in line] for line in data]

mod = []
for i in range(len(data)): mod.append(["."] * len(data[0]))
blank = deepcopy(mod)

for loop in range(9999):
	moved = False

	for y in range(len(data)):
		for x in range(len(data[0])):
			if data[y][x] == ">":
				if data[y][(x + 1) % len(data[0])] == ".":
					mod[y][(x + 1) % len(data[0])] = ">"
					moved = True
				else:
					mod[y][x] = ">"

			if data[y][x] == "v": mod[y][x] = "v"

	data = deepcopy(mod)
	mod = deepcopy(blank)

	for y in range(len(data)):
		for x in range(len(data[0])):
			if data[y][x] == "v":
				if data[(y + 1) % len(data)][x] == ".":
					mod[(y + 1) % len(data)][x] = "v"
					moved = True
				else:
					mod[y][x] = "v"

			if data[y][x] == ">": mod[y][x] = ">"

	data = deepcopy(mod)
	mod = deepcopy(blank)

	if not moved:
		print(f"Gold: {loop + 1}")
		break
