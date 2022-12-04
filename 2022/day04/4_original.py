#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x.split(",") for x in f.read().splitlines()]

silver, gold = 0, 0
for line in data:
	left = list(map(int, line[0].split("-")))
	left = set(range(left[0], left[1] + 1))

	right = list(map(int, line[1].split("-")))
	right = set(range(right[0], right[1] + 1))

	if left.issubset(right) or right.issubset(left):
		silver += 1

	if left.intersection(right) or right.intersection(left):
		gold += 1

print(f"Silver: {silver}\nGold: {gold}")
