#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

height, width = len(data), len(data[0])

blizard = []
cycle = (height - 2) * (width - 2) + 1
for t in range(cycle):
	state = set()
	for y in range(height):
		for x in range(width):
			if data[y][x] == ">":
				tmp = (1 + ((x - 1 + t) % (width - 2)), y)
				state.add(tmp)

			if data[y][x] == "v":
				tmp = (x, 1 + ((y - 1 + t) % (height - 2)))
				state.add(tmp)

			if data[y][x] == "<":
				tmp = (1 + ((x - 1 - t) % (width - 2)), y)
				state.add(tmp)

			if data[y][x] == "^":
				tmp = (x, 1 + ((y - 1 - t) % (height - 2)))
				state.add(tmp)

	blizard.append(state)

silver, gold = 0, 0
mem = set()
queue = [(1, 0, 0, False, False)]

while queue:
	x, y, t, end, start = queue.pop(0)

	# If not in range, and not in a wall
	if not (0 <= y < height and 0 <= x < width and data[y][x] != "#"): continue

	if y == height - 1 and end and start:
		gold = t
		break

	if y == height - 1 and silver == 0:
		silver = t

	if y == height - 1:
		end = True

	if y == 0 and end:
		start = True

	if (x, y, t, end, start) in mem: continue

	mem.add((x, y, t, end, start))

	# Tick the blizard
	bliz = blizard[(t + 1) % cycle]

	if (x, y) not in bliz:
		queue.append((x, y, t + 1, end, start))

	if (x + 1, y) not in bliz:
		queue.append((x + 1, y, t + 1, end, start))

	if (x - 1, y) not in bliz:
		queue.append((x - 1, y, t + 1, end, start))

	if (x, y + 1) not in bliz:
		queue.append((x, y + 1, t + 1, end, start))

	if (x, y - 1) not in bliz:
		queue.append((x, y - 1, t + 1, end, start))

print(f"Silver: {silver}\nGold: {gold}")
