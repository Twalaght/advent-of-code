#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

silver, gold = 0, 0
for line in data:
	tmp = sorted([int(x) for x in line.split("x")])
	sides = [tmp[0] * tmp[1], tmp[0] * tmp[2], tmp[1] * tmp[2]]
	silver += min(sides)
	for s in sides: silver += 2 * s
	gold += tmp[0] * tmp[1] * tmp[2] + 2 * (tmp[0] + tmp[1])

print(f"Silver: {silver}\nGold: {gold}")
