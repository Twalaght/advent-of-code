#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = ",".join([x for x in f.read().splitlines()])

# Split on blank lines, and sum the resulting sub-lists
data = sorted([sum(map(int, x.split(","))) for x in data.split(",,")])

silver, gold = max(data), sum(data[-3:])
print(f"Silver: {silver}\nGold: {gold}")
