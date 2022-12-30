#!/usr/bin/python3

import sys
from copy import deepcopy
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [[char for char in x] for x in f.read().splitlines()]

def count_adj(x, y, data):
	on = 0
	for dy in [y - 1, y, y + 1]:
		for dx in [x - 1, x, x + 1]:
			if dy == y and dx == x: continue

			if 0 <= dy < len(data) and 0 <= dx < len(data[dy]):
				if data[dy][dx] == "#":
					on += 1

	return on

backup = deepcopy(data)

for _ in range(100):
	counts = []
	for y in range(len(data)):
		tmp = []
		for x in range(len(data[y])):
			tmp.append(count_adj(x, y, data))

		counts.append(tmp)

	for y in range(len(data)):
		for x in range(len(data[y])):
			tmp = counts[y][x]

			if data[y][x] == "#":
				if tmp != 2 and tmp != 3:
					data[y][x] = "."
			else:
				if tmp == 3:
					data[y][x] = "#"

silver = sum([sum([1 for x in line if x == "#"]) for line in data])

data = backup
for _ in range(100):
	counts = []
	for y in range(len(data)):
		tmp = []
		for x in range(len(data[y])):
			tmp.append(count_adj(x, y, data))

		counts.append(tmp)

	for y in range(len(data)):
		for x in range(len(data[y])):
			tmp = counts[y][x]

			if data[y][x] == "#":
				if tmp != 2 and tmp != 3:
					data[y][x] = "."
			else:
				if tmp == 3:
					data[y][x] = "#"


	data[0][0] = "#"
	data[len(data) - 1][0] = "#"
	data[0][len(data[0]) - 1] = "#"
	data[len(data) - 1][len(data[0]) - 1] = "#"

gold = sum([sum([1 for x in line if x == "#"]) for line in data])
print(f"Silver: {silver}\nGold: {gold}")
