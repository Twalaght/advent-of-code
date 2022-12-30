#!/usr/bin/python3

import sys
from copy import deepcopy
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [[char for char in x] for x in f.read().splitlines()]

def count_adj(x, y, data):
	on = 0
	for dy in [i for i in [y - 1, y, y + 1] if 0 <= i < len(data)]:
		for dx in [i for i in [x - 1, x, x + 1] if 0 <= i < len(data[dy])]:
			if data[dy][dx] == "#" and not (dy == y and dx == x): on += 1

	return on

def simulate(state, rounds, gold):
	data = deepcopy(state)

	for _ in range(rounds):
		counts = [[count_adj(x, y, data) for x in range(len(data[y]))] for y in range(len(data))]

		for y in range(len(data)):
			for x in range(len(data[y])):
				if data[y][x] == "#" and counts[y][x] not in [2, 3]: data[y][x] = "."
				if data[y][x] == "." and counts[y][x] == 3: data[y][x] = "#"

				if gold:
					data[0][0] = "#"
					data[len(data) - 1][0] = "#"
					data[0][len(data[0]) - 1] = "#"
					data[len(data) - 1][len(data[0]) - 1] = "#"

	return sum([sum([1 for x in line if x == "#"]) for line in data])

silver, gold = simulate(data, 100, False), simulate(data, 100, True)
print(f"Silver: {silver}\nGold: {gold}")
