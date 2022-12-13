#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

h, w = len(data), len(data[0])

# Generate height map
height = []
for y in range(h):
	tmp = []
	for x in range(w):
		tmp.append(ord(data[y][x]) - ord("a") + 1)
		if data[y][x] == "S":
			start = (y, x)
			tmp[-1] = 1
		if data[y][x] == "E":
			end = (y, x)
			tmp[-1] = 26

	height.append(tmp)

# Set the initial cost to arbitrarily high value, except the end
cost = [[int(1e7) for x in range(w)] for y in range(h)]

# Process an update message
def update(y, x, new_cost):
	updates = []
	if cost[y][x] > new_cost:
		cost[y][x] = new_cost
		for c in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
			if 0 <= c[0] < h and 0 <= c[1] < w:
				if height[y][x] - height[c[0]][c[1]] <= 1:
					updates.append((*c, cost[y][x] + 1))

	return updates

# Run Dijkstra and update all costs
msgs = update(end[0], end[1], 0)
while msgs: msgs += update(*msgs.pop(0))
silver = cost[start[0]][start[1]]

# Find the minimum cost value with a height of 1
gold = [[cost[y][x] for x in range(w) if height[y][x] == 1] for y in range(h)]
gold = min(min(gold))

print(f"Silver: {silver}\nGold: {gold}")
