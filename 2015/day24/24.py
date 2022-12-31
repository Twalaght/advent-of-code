#!/usr/bin/python3

import sys
from itertools import combinations
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [int(x) for x in f.read().splitlines()]

def solve(data, gold):
	seg_weight = sum(data) // (4 if gold else 3)
	opts = []
	fewest = len(data)

	for i in range(len(data)):
		if i > fewest: continue

		for x in combinations(data, i):
			if sum(x) == seg_weight:
				opts.append(x)
				fewest = i

	qe = []
	for opt in opts:
		mul = 1
		for x in opt: mul *= x
		qe.append(mul)

	return min(qe)

silver, gold = solve(data, False), solve(data, True)
print(f"Silver: {silver}\nGold: {gold}")
