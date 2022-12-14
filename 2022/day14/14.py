#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x.split(" -> ") for x in f.read().splitlines()]

data = [[(int(c.split(",")[0]), int(c.split(",")[1])) for c in x] for x in data]

cave = set()
for line in data:
	for i in range(len(line) - 1):
		side = 1 if line[i][0] == line[i + 1][0] else 0
		l, r = sorted([line[i][side], line[i + 1][side]])
		run = list(range(l, r + 1))
		for x in run: cave.add((line[i][0], x) if side == 1 else (x, line[i][1]))

def simulate(cave, gold):
	bottom = max([x[1] for x in list(cave)]) + 2

	if gold:
		for x in range(499 - bottom, 501 + bottom): cave.add((x, bottom))

	for sand in range(int(1e7)):
		x, y = 500, 0
		if (x, y) in cave and gold: return sand

		while True:
			if y > bottom and not gold: return sand

			for move in [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]:
				if move not in cave:
					x, y = move
					break
			else:
				cave.add((x, y))
				break

silver, gold = simulate(cave.copy(), False), simulate(cave.copy(), True)
print(f"Silver: {silver}\nGold: {gold}")
