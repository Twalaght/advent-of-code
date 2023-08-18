#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	instructions = [x.strip() for x in f.read().split(",")]

direction = 0
x, y = 0, 0

locations = set()
gold = None

for move in instructions:
	if move[0] == "L":
		direction = (direction - 1) % 4
	if move[0] == "R":
		direction = (direction + 1) % 4
	
	for step in range(int(move[1:])):
		if direction == 0:
			y += 1
			if (x, y) in locations and not gold:
				gold = abs(x) + abs(y)
			else:
				locations.add((x, y))
		
		if direction == 1:
			x += 1
			if (x, y) in locations and not gold:
				gold = abs(x) + abs(y)
			else:
				locations.add((x, y))

		if direction == 2:
			y -= 1
			if (x, y) in locations and not gold:
				gold = abs(x) + abs(y)
			else:
				locations.add((x, y))

		if direction == 3:
			x -= 1
			if (x, y) in locations and not gold:
				gold = abs(x) + abs(y)
			else:
				locations.add((x, y))

silver = abs(x) + abs(y)
print(f"Silver: {silver}\nGold: {gold}")
