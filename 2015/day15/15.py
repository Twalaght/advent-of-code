#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x.replace(",", "").split() for x in f.read().splitlines()]

data = [[int(line[i]) for i in [2, 4, 6, 8, 10]] for line in data]

silver, gold = 0, 0
for i in range(100 + 1):
	for j in range(100 + 1 - i):
		for k in range(100 + 1 - i - j):
			l = 100 - (i + j + k)

			prop = [[x * n for x in line] for n, line in zip([i, j, k, l], data)]
			prop = [sum([x[i] for x in prop]) for i in range(5)]
			if any([x for x in prop if x <= 0]): continue
			score = prop[0] * prop[1] * prop[2] * prop[3]

			if score > silver: silver = score
			if score > gold and prop[4] == 500: gold = score

print(f"Silver: {silver}\nGold: {gold}")
