#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x.split() for x in f.read().splitlines()]

silver, gold = set(), set()
rope = [[0, 0] for _ in range(10)]

for move in data:
	for _ in range(int(move[1])):
		axis = 0 if move[0] in ["L", "R"] else 1
		val = 1 if move[0] in ["R", "U"] else -1
		rope[0][axis] += val

		for i in range(1, len(rope)):
			if abs(rope[i - 1][0] - rope[i][0]) > 1 or abs(rope[i - 1][1] - rope[i][1]) > 1:
				if rope[i - 1][0] > rope[i][0]: rope[i][0] += 1
				if rope[i - 1][0] < rope[i][0]: rope[i][0] -= 1
				if rope[i - 1][1] > rope[i][1]: rope[i][1] += 1
				if rope[i - 1][1] < rope[i][1]: rope[i][1] -= 1

		silver.add(tuple(rope[1]))
		gold.add(tuple(rope[-1]))

silver, gold = len(silver), len(gold)
print(f"Silver: {silver}\nGold: {gold}")
