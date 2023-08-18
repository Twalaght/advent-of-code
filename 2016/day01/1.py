#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	instructions = [x.strip() for x in f.read().split(",")]

direction = 0
visited = set()
silver, gold = [0, 0], None

for move in instructions:
	direction = (direction + (1 if move[0] == "R" else -1)) % 4
	
	for step in range(int(move[1:])):
		mod = direction % 2
		silver[mod] += direction - 1 - mod

		if (location := tuple(silver)) in visited and not gold: gold = location
		visited.add(location)
		
abs_dist = lambda pos: abs(pos[0]) + abs(pos[1])
print(f"Silver: {abs_dist(silver)}\nGold: {abs_dist(gold)}")
