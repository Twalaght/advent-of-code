#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x.split(" -> ") for x in f.read().splitlines()]

data = [[(int(c.split(",")[0]), int(c.split(",")[1])) for c in x] for x in data]

cave = set()
for line in data:
	for i in range(len(line) - 1):
		if line[i][0] == line[i + 1][0]:
			l = min(line[i][1], line[i + 1][1])
			r = max(line[i][1], line[i + 1][1])
			rng = list(range(l, r + 1))

			for run in rng:
				tmp = (line[i][0], run)
				cave.add(tmp)

		if line[i][1] == line[i + 1][1]:
			l = min(line[i][0], line[i + 1][0])
			r = max(line[i][0], line[i + 1][0])
			rng = list(range(l, r + 1))

			for run in rng:
				tmp = (run, line[i][1])
				cave.add(tmp)

cave_gold = cave.copy()
bottom = max([x[1] for x in list(cave)]) + 2
for x in range(500 - bottom * 2, 500 + bottom * 2):
	tmp = (x, bottom)
	cave_gold.add(tmp)

finished = False
sand = 0
while not finished:
	x, y = 500, 0

	while True:
		if y > bottom:
			finished = True
			break

		# Check if we can go down
		tmp = (x, y + 1)
		if tmp not in cave:
			y += 1
			continue

		# Check if we can go left
		tmp = (x - 1, y + 1)
		if tmp not in cave:
			x -= 1
			y += 1
			continue

		# Check if we can go right
		tmp = (x + 1, y + 1)
		if tmp not in cave:
			x += 1
			y += 1
			continue

		tmp = (x, y)
		cave.add(tmp)
		break

	sand += 1

silver = sand - 1

finished = False
sand = 0
while not finished:
	x, y = 500, 0

	if (x, y) in cave_gold:
		break

	while True:
		# Check if we can go down
		tmp = (x, y + 1)
		if tmp not in cave_gold:
			y += 1
			continue

		# Check if we can go left
		tmp = (x - 1, y + 1)
		if tmp not in cave_gold:
			x -= 1
			y += 1
			continue

		# Check if we can go right
		tmp = (x + 1, y + 1)
		if tmp not in cave_gold:
			x += 1
			y += 1
			continue

		tmp = (x, y)
		cave_gold.add(tmp)
		break

	sand += 1

gold = sand
print(f"Silver: {silver}\nGold: {gold}")
