#!/usr/bin/python3

import json
import sys
from functools import cmp_to_key
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [[json.loads(p) for p in x.splitlines()] for x in f.read().split("\n\n")]

def compare(left, right):
	if isinstance(left, int) and isinstance(right, int): return left - right

	if isinstance(right, int): right = [right]
	if isinstance(left, int): left = [left]

	for l, r in zip(left, right):
		res = compare(l, r)
		if res != 0: return res

	return len(left) - len(right)

silver = 0
for i, x in enumerate(data):
	if compare(x[0], x[1]) < 0: silver += i + 1

gold = [[[2]], [[6]]]
for x in data: gold += x[0], x[1]
gold = sorted(gold, key=cmp_to_key(compare))
gold = (gold.index([[2]]) + 1) * (gold.index([[6]]) + 1)

print(f"Silver: {silver}\nGold: {gold}")
