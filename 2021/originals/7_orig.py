#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
		data = [int(x) for x in f.read().split(",")]

best_pos = -1
best_cost = -1

for i in range(max(data)):
	cost = 0
	for crab in data:
		n = abs(crab - i)
		cost += n

	if i == 0:
		best_cost = cost
		best_pos = i

	if cost < best_cost:
		best_cost = cost
		best_pos = i

print(best_cost)

best_pos = -1
best_cost = -1

for i in range(max(data)):
	cost = 0
	for crab in data:
		n = abs(crab - i)
		cost += int((n * (n + 1)) / 2)

	if i == 0:
		best_cost = cost
		best_pos = i

	if cost < best_cost:
		best_cost = cost
		best_pos = i

print(best_cost)
