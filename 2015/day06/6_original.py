#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

cmds = []
for line in data:
	tmp = {}
	test = line.split()

	if test[0] == "toggle":
		tmp["cmd"] = "swap"
	elif test[1] == "on":
		tmp["cmd"] = "on"
	else:
		tmp["cmd"] = "off"

	tmp["start"] = [int(x) for x in test[-3].split(",")]
	tmp["end"] = [int(x) for x in test[-1].split(",")]

	cmds.append(tmp)

grid = []
for _ in range(1000): grid.append([0] * 1000)

for cmd in cmds:
	for x in range(cmd["start"][0], cmd["end"][0] + 1):
		for y in range(cmd["start"][1], cmd["end"][1] + 1):
			if cmd["cmd"] == "swap":
				if grid[x][y] == 0:
					grid[x][y] = 1
				elif grid[x][y] == 1:
					grid[x][y] = 0

			if cmd["cmd"] == "on":
				grid[x][y] = 1

			if cmd["cmd"] == "off":
				grid[x][y] = 0

counter = 0
for line in grid:
	for light in line:
		if light == 1:
			counter += 1

print(f"Silver: {counter}")

grid = []
for _ in range(1000): grid.append([0] * 1000)
for cmd in cmds:
	for x in range(cmd["start"][0], cmd["end"][0] + 1):
		for y in range(cmd["start"][1], cmd["end"][1] + 1):
			if cmd["cmd"] == "swap":
				grid[x][y] += 2

			if cmd["cmd"] == "on":
				grid[x][y] += 1

			if cmd["cmd"] == "off":
				if grid[x][y] > 0:
					grid[x][y] -= 1

counter = 0
for line in grid:
	for light in line:
		counter += light

print(f"Gold: {counter}")
