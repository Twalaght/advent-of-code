#!/usr/bin/python3

import json
import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x.splitlines() for x in f.read().split("\n\n")]

data = [[json.loads(x[0]), json.loads(x[1])] for x in data]

def compare(left, right):
	if isinstance(left, int) and isinstance(right, int):
		if left < right: return -1
		if left > right: return 1

	if isinstance(left, list) and isinstance(right, list):
		for l, r in zip(left, right):
			res = compare(l, r)
			if res != 0: return res

		if len(left) < len(right): return -1
		if len(left) > len(right): return 1

	if isinstance(left, list) and isinstance(right, int):
		return compare(left, [right])

	if isinstance(left, int) and isinstance(right, list):
		return compare([left], right)

	return 0

silver = 0
for i, x in enumerate(data):
	res = compare(x[0], x[1])
	if res == -1: silver += (i + 1)

new = [[[2]], [[6]]]
for x in data:
	new.append(x[0])
	new.append(x[1])

from functools import cmp_to_key
new = sorted(new, key=cmp_to_key(compare))
gold = (new.index([[2]]) + 1) * (new.index([[6]]) + 1)

print(f"Silver: {silver}\nGold: {gold}")
