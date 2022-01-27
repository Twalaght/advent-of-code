#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [[int(x) for x in line] for line in f.read().splitlines()]

def flow(update):
	x, y = update

	if x != 0 and data[x - 1][y] < data[x][y]: update = [x - 1, y]
	if y != 0 and data[x][y - 1] < data[x][y]: update = [x, y - 1]
	if x != len(data) - 1 and data[x + 1][y] < data[x][y]: update = [x + 1, y]
	if y != len(data[x]) - 1 and data[x][y + 1] < data[x][y]: update = [x, y + 1]

	return True if update[0] == x and update[1] == y else update

lows = {}
for x in range(len(data)):
	for y in range(len(data[x])):
		if data[x][y] == 9: continue

		point = [x, y]
		while flow(point) != True: point = flow(point)

		if tuple(point) not in lows: lows[tuple(point)] = 0
		lows[tuple(point)] += 1

silver = sum([data[key[0]][key[1]] + 1 for key in lows])
basins = sorted((lows.values()))[-3:]
gold = basins[0] * basins[1] * basins[2]

print(f"Silver: {silver}\nGold: {gold}")
