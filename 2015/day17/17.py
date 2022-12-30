#!/usr/bin/python3

import sys
from itertools import combinations
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [int(x) for x in f.read().splitlines()]

silver, gold = 0, 0
for i in range(len(data)):
	smallest = False
	for opt in combinations(data, i + 1):
		if sum(opt) == 150:
			if silver == 0: smallest = True
			silver += 1

	if smallest: gold = silver

print(f"Silver: {silver}\nGold: {gold}")
